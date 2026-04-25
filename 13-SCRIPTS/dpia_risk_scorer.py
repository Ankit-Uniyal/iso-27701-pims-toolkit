#!/usr/bin/env python3
"""
dpia_risk_scorer.py
===================
DPIA Risk Scorer for ISO/IEC 27701:2025 PIMS Toolkit
h
Calculates privacy risk scores for DPIA entries based on likelihood
and impact ratings, determines risk level, and provides treatment
recommendations aligned to the Privacy Risk Assessment Methodology
(PIMS-PLN-003).

Usage:
    python dpia_risk_scorer.py
    python dpia_risk_scorer.py --interactive
    python dpia_risk_scorer.py --batch risks.csv --output report.csv

Requirements:
    Python 3.8+
    No external dependencies required (uses only stdlib)

ISO/IEC 27701:2025 PIMS Toolkit
Author: PIMS Toolkit Project
License: MIT
"""

import argparse
import csv
import json
import sys
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional, Tuple


# ============================================================
# Risk Level Definitions
# ============================================================

RISK_LEVELS = {
    (20, 25): ("Critical", "🔴", "Immediate escalation to DPO and senior management required. "
               "Processing must be suspended or immediate controls implemented. DPIA mandatory. "
               "ICO prior consultation may be required."),
    (12, 19): ("High", "🟠", "DPO must be informed immediately. Documented treatment plan with "
               "target date required within 30 days. Processing may continue only with DPO approval."),
    (6, 11):  ("Medium", "🟡", "Treatment plan required. Review at next management meeting. "
               "Increased monitoring. Processing may continue with controls."),
    (2, 5):   ("Low", "🟢", "Accept with monitoring. Document in risk register. Annual review. "
               "Processing may continue."),
    (1, 1):   ("Minimal", "⚪", "Accept. Note in risk register. No further action required."),
}

LIKELIHOOD_DESCRIPTIONS = {
    1: "Very Low — Unlikely; no precedent; strong controls",
    2: "Low — Could occur occasionally; partial controls",
    3: "Medium — Might occur periodically; moderate controls",
    4: "High — Likely to occur; recurring issues; weak controls",
    5: "Very High — Almost certain; active threat; minimal controls",
}

IMPACT_DESCRIPTIONS = {
    1: "Negligible — Minimal or no actual harm to individuals",
    2: "Minor — Temporary embarrassment; minor data quality issue",
    3: "Moderate — Significant harm: discrimination, financial loss",
    4: "Major — Serious harm: identity theft, employment consequences",
    5: "Severe — Life-altering: physical danger, severe discrimination",
}

DPIA_MANDATORY_TRIGGERS = [
    "Systematic and extensive profiling with significant effects",
    "Processing of special category data at scale",
    "Systematic monitoring of publicly accessible areas",
    "Processing of children's data in online services",
    "Cross-border transfer to non-adequate country",
    "Novel technology or high uncertainty",
    "Large-scale processing (>100,000 records)",
    "Risk score >= 20 (Critical)",
]


# ============================================================
# Data Classes
# ============================================================

@dataclass
class DPIARisk:
    """Represents a single privacy risk in a DPIA."""
    risk_id: str
    description: str
    likelihood: int
    impact: int
    pii_categories: str = ""
    current_controls: str = ""
    treatment_option: str = ""
    treatment_actions: str = ""
    risk_owner: str = ""
    target_date: str = ""
    
    # Computed fields
    risk_score: int = field(init=False)
    risk_level: str = field(init=False)
    risk_emoji: str = field(init=False)
    recommendation: str = field(init=False)
    
    def __post_init__(self):
        self.risk_score, self.risk_level, self.risk_emoji, self.recommendation =             calculate_risk(self.likelihood, self.impact)


@dataclass
class DPIAAssessment:
    """Represents a complete DPIA assessment."""
    reference: str
    project_name: str
    assessor: str
    date: str
    risks: List[DPIARisk] = field(default_factory=list)
    dpia_required_triggers: List[str] = field(default_factory=list)
    
    @property
    def total_risks(self) -> int:
        return len(self.risks)
    
    @property
    def critical_count(self) -> int:
        return sum(1 for r in self.risks if r.risk_level == "Critical")
    
    @property
    def high_count(self) -> int:
        return sum(1 for r in self.risks if r.risk_level == "High")
    
    @property
    def medium_count(self) -> int:
        return sum(1 for r in self.risks if r.risk_level == "Medium")
    
    @property
    def low_count(self) -> int:
        return sum(1 for r in self.risks if r.risk_level in ("Low", "Minimal"))
    
    @property
    def highest_risk_score(self) -> int:
        return max((r.risk_score for r in self.risks), default=0)
    
    @property
    def dpia_proceed_recommendation(self) -> str:
        if self.critical_count > 0:
            return "DO NOT PROCEED — Critical risk(s) require immediate resolution before processing commences"
        elif self.high_count > 0:
            return "CONDITIONAL PROCEED — High risk(s) require documented treatment plan and DPO approval before go-live"
        elif self.medium_count > 0:
            return "PROCEED WITH CONTROLS — Medium risk(s) require treatment plan and increased monitoring"
        else:
            return "PROCEED — All risks are Low/Minimal. Document in risk register and review annually"
    
    @property
    def prior_ico_consultation_required(self) -> bool:
        return self.critical_count > 0


# ============================================================
# Core Functions
# ============================================================

def calculate_risk(likelihood: int, impact: int) -> Tuple[int, str, str, str]:
    """
    Calculate the risk score and determine risk level.
    
    Args:
        likelihood: 1-5 scale
        impact: 1-5 scale
        
    Returns:
        Tuple of (score, level_name, emoji, recommendation)
    
    Raises:
        ValueError: If likelihood or impact are out of range
    """
    if not (1 <= likelihood <= 5):
        raise ValueError(f"Likelihood must be 1-5, got {likelihood}")
    if not (1 <= impact <= 5):
        raise ValueError(f"Impact must be 1-5, got {impact}")
    
    score = likelihood * impact
    
    for (low, high), (level, emoji, rec) in RISK_LEVELS.items():
        if low <= score <= high:
            return score, level, emoji, rec
    
    # Should never reach here
    return score, "Unknown", "❓", "Unable to determine risk level"


def validate_rating(value: int, field_name: str) -> int:
    """Validate a 1-5 rating value."""
    if not isinstance(value, int) or not (1 <= value <= 5):
        raise ValueError(f"{field_name} must be an integer between 1 and 5, got: {value}")
    return value


def display_risk_matrix():
    """Display the 5x5 risk heat map."""
    print("\n📊 PRIVACY RISK HEAT MAP (Likelihood × Impact)\n")
    print("         " + "  ".join([f"I={i}" for i in range(1, 6)]))
    print("         " + "-" * 35)
    
    for likelihood in range(5, 0, -1):
        row = f"L={likelihood}  |  "
        for impact in range(1, 6):
            score = likelihood * impact
            _, level, emoji, _ = calculate_risk(likelihood, impact)
            row += f"{score:2d}{emoji} "
        print(row)
    
    print("\nLegend: 🔴 Critical(20-25) 🟠 High(12-19) 🟡 Medium(6-11) 🟢 Low(2-5) ⚪ Minimal(1)")


def print_risk_detail(risk: DPIARisk, index: int = 1):
    """Print detailed information about a single risk."""
    print(f"\n{'='*60}")
    print(f"  RISK {index}: {risk.risk_id}")
    print(f"{'='*60}")
    print(f"  Description   : {risk.description}")
    if risk.pii_categories:
        print(f"  PII Categories: {risk.pii_categories}")
    print(f"  Likelihood    : {risk.likelihood} — {LIKELIHOOD_DESCRIPTIONS[risk.likelihood]}")
    print(f"  Impact        : {risk.impact} — {IMPACT_DESCRIPTIONS[risk.impact]}")
    print(f"  ─────────────────────────────────────────────────────")
    print(f"  RISK SCORE    : {risk.risk_score}")
    print(f"  RISK LEVEL    : {risk.risk_emoji} {risk.risk_level.upper()}")
    print(f"  ─────────────────────────────────────────────────────")
    print(f"  Recommendation: {risk.recommendation}")
    if risk.current_controls:
        print(f"  Current Controls: {risk.current_controls}")
    if risk.treatment_option:
        print(f"  Treatment Option: {risk.treatment_option}")
    if risk.treatment_actions:
        print(f"  Treatment Actions: {risk.treatment_actions}")
    if risk.risk_owner:
        print(f"  Risk Owner: {risk.risk_owner}")
    if risk.target_date:
        print(f"  Target Date: {risk.target_date}")


def print_assessment_summary(assessment: DPIAAssessment):
    """Print summary of a complete DPIA assessment."""
    print(f"\n{'#'*60}")
    print(f"  DPIA RISK ASSESSMENT SUMMARY")
    print(f"{'#'*60}")
    print(f"  Reference    : {assessment.reference}")
    print(f"  Project      : {assessment.project_name}")
    print(f"  Assessor     : {assessment.assessor}")
    print(f"  Date         : {assessment.date}")
    print(f"  Total Risks  : {assessment.total_risks}")
    print(f"{'─'*60}")
    print(f"  Risk Summary :")
    print(f"    🔴 Critical : {assessment.critical_count}")
    print(f"    🟠 High     : {assessment.high_count}")
    print(f"    🟡 Medium   : {assessment.medium_count}")
    print(f"    🟢 Low/Min  : {assessment.low_count}")
    print(f"    Highest Score: {assessment.highest_risk_score}")
    print(f"{'─'*60}")
    print(f"  DPO RECOMMENDATION:")
    print(f"  {assessment.dpia_proceed_recommendation}")
    if assessment.prior_ico_consultation_required:
        print(f"\n  ⚠️  PRIOR ICO CONSULTATION MAY BE REQUIRED")
        print(f"     (Critical risk identified — GDPR Art. 36)")
    if assessment.dpia_required_triggers:
        print(f"\n  DPIA Mandatory Triggers Identified:")
        for trigger in assessment.dpia_required_triggers:
            print(f"    ✓ {trigger}")
    print(f"{'#'*60}\n")


def interactive_dpia_scorer():
    """Run interactive DPIA risk scoring session."""
    print("\n" + "="*60)
    print("  ISO/IEC 27701:2025 DPIA Risk Scorer — Interactive Mode")
    print("="*60)
    
    # DPIA metadata
    reference = input("\nDPIA Reference (e.g., DPIA-2025-001): ").strip() or "DPIA-2025-001"
    project = input("Project Name: ").strip() or "Unnamed Project"
    assessor = input("Assessor Name: ").strip() or "DPO"
    date = input(f"Date [{datetime.today().strftime('%Y-%m-%d')}]: ").strip() or datetime.today().strftime('%Y-%m-%d')
    
    assessment = DPIAAssessment(
        reference=reference,
        project_name=project,
        assessor=assessor,
        date=date
    )
    
    # Check DPIA triggers
    print("\n--- DPIA MANDATORY TRIGGERS ---")
    print("Select any applicable triggers (enter numbers separated by commas, or press Enter to skip):")
    for i, trigger in enumerate(DPIA_MANDATORY_TRIGGERS, 1):
        print(f"  {i}. {trigger}")
    
    trigger_input = input("\nTrigger numbers: ").strip()
    if trigger_input:
        for num in trigger_input.split(","):
            try:
                idx = int(num.strip()) - 1
                if 0 <= idx < len(DPIA_MANDATORY_TRIGGERS):
                    assessment.dpia_required_triggers.append(DPIA_MANDATORY_TRIGGERS[idx])
            except ValueError:
                pass
    
    # Risk entry
    print("\n--- RISK ENTRY ---")
    print("Enter privacy risks for this DPIA. Type 'done' when finished.\n")
    
    display_risk_matrix()
    
    risk_count = 0
    while True:
        risk_count += 1
        print(f"\n--- Risk {risk_count} ---")
        
        risk_id = input(f"Risk ID [RISK-{risk_count:03d}]: ").strip() or f"RISK-{risk_count:03d}"
        description = input("Risk Description: ").strip()
        
        if description.lower() == "done" or not description:
            risk_count -= 1
            break
        
        pii_categories = input("PII Categories (optional): ").strip()
        
        # Likelihood
        print("\nLikelihood scale:")
        for k, v in LIKELIHOOD_DESCRIPTIONS.items():
            print(f"  {k} = {v}")
        while True:
            try:
                likelihood = int(input("Likelihood (1-5): "))
                validate_rating(likelihood, "Likelihood")
                break
            except (ValueError, TypeError) as e:
                print(f"  Invalid: {e}. Please enter 1-5.")
        
        # Impact
        print("\nImpact scale:")
        for k, v in IMPACT_DESCRIPTIONS.items():
            print(f"  {k} = {v}")
        while True:
            try:
                impact = int(input("Impact (1-5): "))
                validate_rating(impact, "Impact")
                break
            except (ValueError, TypeError) as e:
                print(f"  Invalid: {e}. Please enter 1-5.")
        
        current_controls = input("Current controls (optional): ").strip()
        treatment_option = input("Treatment option (Mitigate/Avoid/Transfer/Accept): ").strip()
        treatment_actions = input("Treatment actions (optional): ").strip()
        risk_owner = input("Risk owner (optional): ").strip()
        target_date = input("Target date (YYYY-MM-DD, optional): ").strip()
        
        risk = DPIARisk(
            risk_id=risk_id,
            description=description,
            likelihood=likelihood,
            impact=impact,
            pii_categories=pii_categories,
            current_controls=current_controls,
            treatment_option=treatment_option,
            treatment_actions=treatment_actions,
            risk_owner=risk_owner,
            target_date=target_date,
        )
        assessment.risks.append(risk)
        print_risk_detail(risk, risk_count)
        
        if input("\nAdd another risk? (y/n) [y]: ").strip().lower() == "n":
            break
    
    # Summary
    if assessment.risks:
        print_assessment_summary(assessment)
    else:
        print("\nNo risks entered. Exiting.")


def process_batch_csv(input_file: str, output_file: Optional[str] = None):
    """
    Process risks from a CSV file.
    
    CSV format: risk_id,description,likelihood,impact,pii_categories,current_controls,treatment_option,risk_owner
    """
    risks = []
    
    try:
        with open(input_file, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    risk = DPIARisk(
                        risk_id=row.get("risk_id", "UNKNOWN"),
                        description=row.get("description", ""),
                        likelihood=int(row.get("likelihood", 3)),
                        impact=int(row.get("impact", 3)),
                        pii_categories=row.get("pii_categories", ""),
                        current_controls=row.get("current_controls", ""),
                        treatment_option=row.get("treatment_option", ""),
                        risk_owner=row.get("risk_owner", ""),
                        target_date=row.get("target_date", ""),
                    )
                    risks.append(risk)
                except (ValueError, KeyError) as e:
                    print(f"Warning: Skipping row {row} — {e}", file=sys.stderr)
    except FileNotFoundError:
        print(f"Error: File not found: {input_file}", file=sys.stderr)
        sys.exit(1)
    
    if not risks:
        print("No valid risks found in file.")
        return
    
    # Print results
    print(f"\n📋 BATCH DPIA RISK SCORING — {input_file}")
    print(f"{'='*60}")
    
    for i, risk in enumerate(risks, 1):
        print_risk_detail(risk, i)
    
    # Summary
    critical = sum(1 for r in risks if r.risk_level == "Critical")
    high = sum(1 for r in risks if r.risk_level == "High")
    medium = sum(1 for r in risks if r.risk_level == "Medium")
    low = sum(1 for r in risks if r.risk_level in ("Low", "Minimal"))
    
    print(f"\n{'='*60}")
    print(f"SUMMARY: {len(risks)} risks | 🔴 {critical} Critical | 🟠 {high} High | 🟡 {medium} Medium | 🟢 {low} Low")
    print(f"{'='*60}")
    
    # Write output CSV if specified
    if output_file:
        fieldnames = ["risk_id", "description", "likelihood", "impact", "risk_score",
                      "risk_level", "pii_categories", "current_controls",
                      "treatment_option", "risk_owner", "target_date", "recommendation"]
        with open(output_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for risk in risks:
                writer.writerow({
                    "risk_id": risk.risk_id,
                    "description": risk.description,
                    "likelihood": risk.likelihood,
                    "impact": risk.impact,
                    "risk_score": risk.risk_score,
                    "risk_level": risk.risk_level,
                    "pii_categories": risk.pii_categories,
                    "current_controls": risk.current_controls,
                    "treatment_option": risk.treatment_option,
                    "risk_owner": risk.risk_owner,
                    "target_date": risk.target_date,
                    "recommendation": risk.recommendation,
                })
        print(f"\nResults written to: {output_file}")


def demo_mode():
    """Run a demonstration with sample DPIA risks."""
    print("\n" + "="*60)
    print("  ISO/IEC 27701:2025 DPIA Risk Scorer — Demo Mode")
    print("="*60)
    print("  Fictional Organisation: Nexus Financial Services Ltd")
    print("  Project: Salesforce CRM Migration")
    print("="*60)
    
    sample_risks = [
        DPIARisk("DPIA-R01", "Data loss during migration", 3, 4,
                 "Customer name, contact, loan history", "Manual backups",
                 "Mitigate", "Full backup + validation + rollback plan", "IT Director", "2025-04-01"),
        DPIARisk("DPIA-R02", "Unauthorised access during migration window", 3, 4,
                 "All customer PII", "Access controls exist", "Mitigate",
                 "Encryption + restricted access + audit logging", "CISO", "2025-04-01"),
        DPIARisk("DPIA-R03", "Cross-border transfer to Salesforce US without SCCs", 4, 3,
                 "Customer contact + marketing data", "Old DPA in place", "Mitigate",
                 "Execute updated SCCs with Salesforce EU module", "Legal/DPO", "2025-03-31"),
        DPIARisk("DPIA-R04", "Privacy notice does not disclose Salesforce as processor", 4, 3,
                 "All processing activities", "None", "Mitigate",
                 "Update privacy notice before migration", "DPO", "2025-02-28"),
        DPIARisk("DPIA-R05", "Consent records not migrated accurately", 4, 3,
                 "Marketing preferences, consent timestamps", "No consent audit done",
                 "Mitigate", "Migrate with metadata; post-migration consent audit", "Marketing/IT", "2025-05-31"),
    ]
    
    display_risk_matrix()
    
    assessment = DPIAAssessment(
        reference="NFS-DPIA-2025-003",
        project_name="Salesforce CRM Migration",
        assessor="Sarah Chen, DPO",
        date="2025-01-15",
        risks=sample_risks,
        dpia_required_triggers=["Large-scale processing (>100,000 records)", "Novel technology or high uncertainty"]
    )
    
    for i, risk in enumerate(sample_risks, 1):
        print_risk_detail(risk, i)
    
    print_assessment_summary(assessment)


def main():
    """Main entry point with argument parsing."""
    parser = argparse.ArgumentParser(
        description="ISO/IEC 27701:2025 DPIA Risk Scorer",
        epilog="Part of the PIMS Toolkit — github.com/Ankit-Uniyal/iso-27701-pims-toolkit"
    )
    
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--interactive", "-i", action="store_true",
                       help="Run in interactive mode to enter risks manually")
    group.add_argument("--batch", "-b", metavar="INPUT_CSV",
                       help="Process risks from a CSV file")
    group.add_argument("--demo", "-d", action="store_true",
                       help="Run demo with sample NFS DPIA risks")
    group.add_argument("--matrix", "-m", action="store_true",
                       help="Display the risk heat map and exit")
    
    parser.add_argument("--output", "-o", metavar="OUTPUT_CSV",
                        help="Output CSV file for batch mode results")
    
    parser.add_argument("--score", "-s", nargs=2, type=int, metavar=("LIKELIHOOD", "IMPACT"),
                        help="Score a single risk: --score LIKELIHOOD IMPACT")
    
    args = parser.parse_args()
    
    if args.score:
        l, i = args.score
        try:
            score, level, emoji, rec = calculate_risk(l, i)
            print(f"\nRisk Score: {score} | Level: {emoji} {level}")
            print(f"Recommendation: {rec}\n")
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
    elif args.matrix:
        display_risk_matrix()
    elif args.interactive:
        interactive_dpia_scorer()
    elif args.batch:
        process_batch_csv(args.batch, args.output)
    elif args.demo:
        demo_mode()
    else:
        # Default: run demo
        print("No mode specified. Running demo. Use --help for options.")
        demo_mode()


if __name__ == "__main__":
    main()
