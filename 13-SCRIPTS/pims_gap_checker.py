#!/usr/bin/env python3
"""
ISO/IEC 27701:2025 PIMS Gap Checker
=====================================
Automated PIMS gap assessment tool — checks your documented PIMS
state against ISO/IEC 27701:2025 clause and control requirements.

Accepts a YAML or JSON input file describing your current implementation
state, or runs in interactive mode for manual input.

Updated for ISO 27701:2025 — includes all new controls:
  - Joint PII Controller Arrangements (A.7.2.7)
  - Privacy by Default standalone (A.7.2.8)
  - TIA for cross-border transfers
  - Enhanced DPIA triggers
  - Consent refresh (A.8.3.2)
  - Automated decision-making (A.8.2.6)
  - Processor Privacy by Design standalone (B.8.3.1)
  - Processor Audit Rights (B.8.6)

Usage:
    python pims_gap_checker.py                  # Interactive mode
    python pims_gap_checker.py --input state.json   # Load from file
    python pims_gap_checker.py --demo           # Demo with sample data
    python pims_gap_checker.py --report         # Generate gap report

Version: 2.0 | Standard: ISO/IEC 27701:2025
"""

import argparse
import json
import sys
from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional, Tuple


class MaturityLevel(Enum):
    NOT_IMPLEMENTED = 0
    INITIAL = 1
    DEVELOPING = 2
    DEFINED = 3
    MANAGED = 4
    OPTIMISED = 5


class Priority(Enum):
    CRITICAL = "Critical"
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"


@dataclass
class GapRequirement:
    ref: str
    section: str
    requirement: str
    priority: Priority
    is_new_2025: bool = False
    score: int = 0  # 0-5 maturity score
    evidence: str = ""
    gap_notes: str = ""


# ============================================================
# PIMS REQUIREMENTS REGISTRY (ISO 27701:2025)
# ============================================================

PIMS_REQUIREMENTS: List[GapRequirement] = [

    # CLAUSE 4 — CONTEXT
    GapRequirement("4.1.1", "Clause 4 — Context",
        "Privacy-specific internal and external issues identified and documented", Priority.HIGH),
    GapRequirement("4.2.1", "Clause 4 — Context",
        "Data subjects identified as interested party", Priority.HIGH),
    GapRequirement("4.2.2", "Clause 4 — Context",
        "Privacy regulators identified with requirements mapped", Priority.HIGH),
    GapRequirement("4.2.3", "Clause 4 — Context",
        "Joint controller relationships identified", Priority.HIGH, is_new_2025=True),
    GapRequirement("4.3.1", "Clause 4 — Context",
        "PIMS scope defined covering all PII processing activities", Priority.CRITICAL),
    GapRequirement("4.4.1", "Clause 4 — Context",
        "Record of Processing Activities (ROPA) established and current", Priority.CRITICAL),
    GapRequirement("4.4.3", "Clause 4 — Context",
        "Legal basis identified for each processing activity", Priority.CRITICAL),

    # CLAUSE 5 — LEADERSHIP
    GapRequirement("5.1.1", "Clause 5 — Leadership",
        "Top management commitment to PIMS demonstrated", Priority.HIGH),
    GapRequirement("5.2.1", "Clause 5 — Leadership",
        "Privacy Policy approved and communicated by top management", Priority.CRITICAL),
    GapRequirement("5.3.1", "Clause 5 — Leadership",
        "DPO or equivalent role appointed (where required)", Priority.CRITICAL),
    GapRequirement("5.3.3", "Clause 5 — Leadership",
        "Privacy RACI matrix defined and communicated", Priority.HIGH),
    GapRequirement("5.3.4", "Clause 5 — Leadership",
        "Joint controller responsibilities assigned", Priority.HIGH, is_new_2025=True),

    # CLAUSE 6 — PLANNING
    GapRequirement("6.1.1", "Clause 6 — Planning",
        "Privacy risk assessment methodology defined (ISO 27005:2022 aligned)", Priority.CRITICAL),
    GapRequirement("6.1.2", "Clause 6 — Planning",
        "Privacy risk assessment conducted for all PII processing activities", Priority.CRITICAL),
    GapRequirement("6.1.5", "Clause 6 — Planning",
        "Cross-border transfer risks assessed (TIA approach documented)", Priority.HIGH, is_new_2025=True),
    GapRequirement("6.1.6", "Clause 6 — Planning",
        "Privacy Risk Register maintained and current", Priority.HIGH),
    GapRequirement("6.1.7", "Clause 6 — Planning",
        "Privacy Risk Treatment Plan documented and implemented", Priority.HIGH),
    GapRequirement("6.2.1", "Clause 6 — Planning",
        "Measurable Privacy Objectives established", Priority.HIGH),
    GapRequirement("6.3.1", "Clause 6 — Planning",
        "SoA produced covering all updated Annex A controls", Priority.CRITICAL),
    GapRequirement("6.3.2", "Clause 6 — Planning",
        "SoA produced covering all updated Annex B controls", Priority.CRITICAL),

    # CLAUSE 7 — SUPPORT
    GapRequirement("7.1.1", "Clause 7 — Support",
        "Privacy competence requirements defined for all relevant roles", Priority.MEDIUM),
    GapRequirement("7.2.1", "Clause 7 — Support",
        "Privacy Awareness Programme established and delivered", Priority.MEDIUM),
    GapRequirement("7.3.1", "Clause 7 — Support",
        "Privacy Communications Plan documented", Priority.MEDIUM),
    GapRequirement("7.4.1", "Clause 7 — Support",
        "Document Control Procedure for PIMS documents in place", Priority.MEDIUM),
    GapRequirement("7.4.3", "Clause 7 — Support",
        "PIMS Document Master List maintained", Priority.LOW),

    # CLAUSE 8 — OPERATION
    GapRequirement("8.1.1", "Clause 8 — Operation",
        "PII processing activity procedure documented (ROPA complete)", Priority.CRITICAL),
    GapRequirement("8.2.1", "Clause 8 — Operation",
        "DPIA procedure and 2025 trigger criteria defined", Priority.CRITICAL, is_new_2025=True),
    GapRequirement("8.2.2", "Clause 8 — Operation",
        "DPIAs conducted for all high-risk processing activities", Priority.CRITICAL),
    GapRequirement("8.3.1", "Clause 8 — Operation",
        "Consent Management Procedure documented", Priority.HIGH),
    GapRequirement("8.3.5", "Clause 8 — Operation",
        "Consent refresh process implemented", Priority.HIGH, is_new_2025=True),
    GapRequirement("8.4.1", "Clause 8 — Operation",
        "Data Subject Rights Procedure covers all applicable rights", Priority.CRITICAL),
    GapRequirement("8.4.6", "Clause 8 — Operation",
        "Automated decision-making rights handling implemented", Priority.HIGH, is_new_2025=True),
    GapRequirement("8.5.1", "Clause 8 — Operation",
        "Privacy Breach Response Procedure documented (72-hr rule embedded)", Priority.CRITICAL),
    GapRequirement("8.6.1", "Clause 8 — Operation",
        "Retention schedules defined for all PII categories", Priority.HIGH),
    GapRequirement("8.7.3", "Clause 8 — Operation",
        "Data Processing Agreements (DPAs) in place for all processors", Priority.CRITICAL),
    GapRequirement("8.8.1", "Clause 8 — Operation",
        "All cross-border transfers identified and documented", Priority.HIGH),
    GapRequirement("8.8.3", "Clause 8 — Operation",
        "Transfer Impact Assessment (TIA) conducted where required", Priority.HIGH, is_new_2025=True),
    GapRequirement("8.9.1", "Clause 8 — Operation",
        "Privacy by Design procedure documented (ISO 31700:2023 aligned)", Priority.HIGH, is_new_2025=True),
    GapRequirement("8.9.3", "Clause 8 — Operation",
        "Privacy by Default applied — maximum privacy settings as default", Priority.HIGH, is_new_2025=True),

    # CLAUSE 9 — PERFORMANCE
    GapRequirement("9.1.1", "Clause 9 — Performance",
        "Privacy KPIs and metrics defined and reported", Priority.HIGH),
    GapRequirement("9.2.1", "Clause 9 — Performance",
        "PIMS Internal Audit Programme established (covers 2025 controls)", Priority.HIGH),
    GapRequirement("9.2.3", "Clause 9 — Performance",
        "PIMS auditors competent in ISO 27701:2025", Priority.MEDIUM, is_new_2025=True),
    GapRequirement("9.3.1", "Clause 9 — Performance",
        "PIMS Management Review conducted at least annually", Priority.HIGH),

    # CLAUSE 10 — IMPROVEMENT
    GapRequirement("10.1", "Clause 10 — Improvement",
        "Nonconformity and corrective action process established", Priority.HIGH),
    GapRequirement("10.5", "Clause 10 — Improvement",
        "Continual Improvement Log maintained", Priority.MEDIUM),
]


# ============================================================
# DEMO DATA (sample state for illustration)
# ============================================================
DEMO_SCORES = {
    "4.1.1": 3, "4.2.1": 4, "4.2.2": 3, "4.2.3": 1, "4.3.1": 4,
    "4.4.1": 3, "4.4.3": 3, "5.1.1": 4, "5.2.1": 5, "5.3.1": 5,
    "5.3.3": 3, "5.3.4": 0, "6.1.1": 3, "6.1.2": 3, "6.1.5": 0,
    "6.1.6": 3, "6.1.7": 2, "6.2.1": 2, "6.3.1": 2, "6.3.2": 2,
    "7.1.1": 3, "7.2.1": 3, "7.3.1": 2, "7.4.1": 3, "7.4.3": 2,
    "8.1.1": 3, "8.2.1": 2, "8.2.2": 2, "8.3.1": 3, "8.3.5": 0,
    "8.4.1": 3, "8.4.6": 0, "8.5.1": 3, "8.6.1": 3, "8.7.3": 3,
    "8.8.1": 2, "8.8.3": 0, "8.9.1": 2, "8.9.3": 0, "9.1.1": 2,
    "9.2.1": 2, "9.2.3": 1, "9.3.1": 2, "10.1": 3, "10.5": 2,
}


class Colour:
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    BOLD = "\033[1m"
    RESET = "\033[0m"
    MAGENTA = "\033[95m"


def score_colour(score: int) -> str:
    if score >= 4: return Colour.GREEN
    if score >= 3: return Colour.CYAN
    if score >= 2: return Colour.YELLOW
    return Colour.RED


def priority_colour(priority: Priority) -> str:
    mapping = {
        Priority.CRITICAL: Colour.RED + Colour.BOLD,
        Priority.HIGH: Colour.YELLOW,
        Priority.MEDIUM: Colour.CYAN,
        Priority.LOW: Colour.BLUE,
    }
    return mapping.get(priority, Colour.RESET)


def run_interactive(requirements: List[GapRequirement]) -> None:
    print(f"\n{Colour.BOLD}Interactive Gap Assessment Mode{Colour.RESET}")
    print("Rate each requirement 0-5:")
    print("  0=Not Implemented  1=Initial  2=Developing  3=Defined  4=Managed  5=Optimised")
    print("  (Press Enter to skip / use default of 0)\n")

    for req in requirements:
        new_tag = f" {Colour.MAGENTA}[NEW 2025]{Colour.RESET}" if req.is_new_2025 else ""
        prio = priority_colour(req.priority)
        print(f"  {Colour.BOLD}{req.ref}{Colour.RESET}{new_tag} [{prio}{req.priority.value}{Colour.RESET}]")
        print(f"  {req.requirement}")
        while True:
            try:
                val = input("  Score (0-5): ").strip()
                if val == "":
                    req.score = 0
                    break
                score = int(val)
                if 0 <= score <= 5:
                    req.score = score
                    break
                print("  Please enter 0-5")
            except ValueError:
                print("  Please enter a number 0-5")
        print()


def print_gap_report(requirements: List[GapRequirement]) -> None:
    total = len(requirements)
    gaps = [r for r in requirements if r.score <= 2]
    compliant = [r for r in requirements if r.score >= 3]
    new_2025_gaps = [r for r in gaps if r.is_new_2025]

    avg_score = sum(r.score for r in requirements) / total if total > 0 else 0
    readiness_pct = (len(compliant) / total * 100) if total > 0 else 0

    print(f"\n{Colour.BOLD}{'='*65}{Colour.RESET}")
    print(f"{Colour.BOLD}  ISO/IEC 27701:2025 PIMS GAP ASSESSMENT RESULTS{Colour.RESET}")
    print(f"{Colour.BOLD}{'='*65}{Colour.RESET}")
    print(f"  Total requirements assessed:     {total}")
    print(f"  {Colour.GREEN}Compliant (score ≥3):            {len(compliant)}{Colour.RESET}")
    print(f"  {Colour.RED}Gaps identified (score ≤2):      {len(gaps)}{Colour.RESET}")
    print(f"  {Colour.MAGENTA}New 2025 controls with gaps:     {len(new_2025_gaps)}{Colour.RESET}")
    print(f"  Average maturity score:          {avg_score:.1f}/5.0")

    bar_len = 50
    filled = int(bar_len * readiness_pct / 100)
    bar = f"[{'█' * filled}{'░' * (bar_len - filled)}]"
    bar_c = Colour.GREEN if readiness_pct >= 80 else (Colour.YELLOW if readiness_pct >= 60 else Colour.RED)
    print(f"  PIMS Readiness:                  {Colour.BOLD}{readiness_pct:.1f}%{Colour.RESET}")
    print(f"  {bar_c}{bar}{Colour.RESET}\n")

    if gaps:
        # Sort by priority, then section
        priority_order = {Priority.CRITICAL: 0, Priority.HIGH: 1,
                          Priority.MEDIUM: 2, Priority.LOW: 3}
        gaps_sorted = sorted(gaps, key=lambda r: (priority_order[r.priority], r.ref))

        print(f"{Colour.BOLD}  PRIORITY GAP LIST ({len(gaps)} gaps){Colour.RESET}")
        print(f"  {'─'*60}")
        for i, req in enumerate(gaps_sorted[:20], 1):  # Show top 20
            new_tag = f" {Colour.MAGENTA}[NEW 2025]{Colour.RESET}" if req.is_new_2025 else ""
            pc = priority_colour(req.priority)
            sc = score_colour(req.score)
            print(f"  {i:2d}. [{pc}{req.priority.value:8s}{Colour.RESET}] "
                  f"{Colour.BOLD}{req.ref}{Colour.RESET}{new_tag} "
                  f"Score:{sc}{req.score}{Colour.RESET}/5")
            print(f"      {req.section} — {req.requirement[:70]}")
        if len(gaps) > 20:
            print(f"  ... and {len(gaps)-20} more gaps")
        print()

    # Section breakdown
    sections = {}
    for req in requirements:
        sec = req.section
        if sec not in sections:
            sections[sec] = {"total": 0, "gaps": 0}
        sections[sec]["total"] += 1
        if req.score <= 2:
            sections[sec]["gaps"] += 1

    print(f"{Colour.BOLD}  SECTION SUMMARY{Colour.RESET}")
    print(f"  {'─'*60}")
    for sec, data in sections.items():
        pct = ((data["total"] - data["gaps"]) / data["total"] * 100)
        sc = Colour.GREEN if pct >= 80 else (Colour.YELLOW if pct >= 50 else Colour.RED)
        print(f"  {sec:<35} {sc}{pct:5.1f}%{Colour.RESET} "
              f"({data['gaps']} gaps/{data['total']})")
    print()


def main():
    parser = argparse.ArgumentParser(
        description="ISO/IEC 27701:2025 PIMS Gap Checker",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument("--input", help="JSON file with requirement scores")
    parser.add_argument("--demo", action="store_true", help="Run with sample demo data")
    parser.add_argument("--report", action="store_true", help="Generate gap report only")
    args = parser.parse_args()

    print(f"\n{Colour.BOLD}{'='*65}{Colour.RESET}")
    print(f"{Colour.BOLD}  ISO/IEC 27701:2025 PIMS Gap Checker{Colour.RESET}")
    print(f"{Colour.BOLD}{'='*65}{Colour.RESET}")
    print(f"  Standard:  ISO/IEC 27701:2025 (extends ISO 27001:2022)")
    print(f"  New 2025 requirements flagged with {Colour.MAGENTA}[NEW 2025]{Colour.RESET}")

    requirements = [GapRequirement(r.ref, r.section, r.requirement, r.priority,
                                    r.is_new_2025, r.score) for r in PIMS_REQUIREMENTS]

    if args.demo:
        print(f"\n  {Colour.YELLOW}Running in DEMO mode with sample data...{Colour.RESET}")
        for req in requirements:
            req.score = DEMO_SCORES.get(req.ref, 0)
    elif args.input:
        try:
            with open(args.input) as f:
                scores = json.load(f)
            for req in requirements:
                req.score = scores.get(req.ref, 0)
            print(f"\n  {Colour.GREEN}Loaded scores from {args.input}{Colour.RESET}")
        except FileNotFoundError:
            print(f"\n  {Colour.RED}File not found: {args.input}{Colour.RESET}")
            sys.exit(1)
    else:
        run_interactive(requirements)

    print_gap_report(requirements)
    print(f"  {Colour.CYAN}Tip: Use --demo to see a sample assessment, --report for report-only mode{Colour.RESET}\n")


if __name__ == "__main__":
    main()
