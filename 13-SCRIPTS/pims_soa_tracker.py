#!/usr/bin/env python3
"""
ISO/IEC 27701:2025 PIMS SoA Tracker
====================================
Tracks Statement of Applicability (SoA) control completion status
across all Annex A (PII Controller) and Annex B (PII Processor) controls.

Updated for ISO/IEC 27701:2025 — includes new controls:
  - A.7.2.7 Joint PII Controller Arrangements
  - A.7.2.8 Privacy by Default (standalone)
  - A.7.4.x PII De-identification and Deletion
  - A.7.5.x PII Disclosure Controls
  - A.8.2.6 Automated Decision-Making and Profiling
  - A.8.3.2 Consent Refresh
  - B.8.3.1 Privacy by Design (Processor standalone)
  - B.8.3.2 Temporary Files (Processor)
  - B.8.6.x Audit Rights (Processor)

Usage:
    python pims_soa_tracker.py                  # Show full SoA status
    python pims_soa_tracker.py --summary        # Show summary only
    python pims_soa_tracker.py --annex A        # Show Annex A controls only
    python pims_soa_tracker.py --annex B        # Show Annex B controls only
    python pims_soa_tracker.py --incomplete     # Show incomplete/excluded controls only
    python pims_soa_tracker.py --export         # Export to CSV

Version: 2.0 | Standard: ISO/IEC 27701:2025
"""

import argparse
import csv
import sys
from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


class ControlStatus(Enum):
    INCLUDED_FULL = "Included - Fully Implemented"
    INCLUDED_PARTIAL = "Included - Partially Implemented"
    INCLUDED_NOT_STARTED = "Included - Not Yet Implemented"
    EXCLUDED_JUSTIFIED = "Excluded - Justified"
    NOT_APPLICABLE = "Not Applicable"


class Annex(Enum):
    A = "Annex A (PII Controller)"
    B = "Annex B (PII Processor)"


@dataclass
class SoAControl:
    ref: str
    title: str
    annex: Annex
    gdpr_ref: str
    status: ControlStatus
    justification: str = ""
    owner: str = ""
    is_new_2025: bool = False
    notes: str = ""


# ============================================================
# ANNEX A — PII CONTROLLER CONTROLS (ISO 27701:2025)
# ============================================================
ANNEX_A_CONTROLS: List[SoAControl] = [

    # A.7.2 — Identify and Document Purpose
    SoAControl("A.7.2.1", "Identify and document the purposes of PII processing",
               Annex.A, "Art. 5(1)(b)", ControlStatus.INCLUDED_NOT_STARTED,
               "All processing activities must have documented purposes", "DPO"),
    SoAControl("A.7.2.2", "Identify the lawful basis for processing",
               Annex.A, "Art. 6", ControlStatus.INCLUDED_NOT_STARTED,
               "Legal basis required for each processing activity", "DPO"),
    SoAControl("A.7.2.3", "Determine when and how consent is to be obtained",
               Annex.A, "Art. 7", ControlStatus.INCLUDED_NOT_STARTED,
               "Consent used as legal basis for marketing", "Privacy Lead"),
    SoAControl("A.7.2.4", "Obtain and record consent",
               Annex.A, "Art. 7", ControlStatus.INCLUDED_NOT_STARTED,
               "Consent records maintained in CMP", "Privacy Lead"),
    SoAControl("A.7.2.5", "Privacy impact assessment (DPIA)",
               Annex.A, "Art. 35", ControlStatus.INCLUDED_NOT_STARTED,
               "DPIA mandatory for high-risk processing per 2025 trigger criteria", "DPO"),
    SoAControl("A.7.2.6", "Contracts with PII processors",
               Annex.A, "Art. 28", ControlStatus.INCLUDED_NOT_STARTED,
               "All processors require DPAs", "Legal/DPO"),
    SoAControl("A.7.2.7", "Joint PII controller arrangements",
               Annex.A, "Art. 26", ControlStatus.INCLUDED_NOT_STARTED,
               "Joint controller agreements required where applicable", "DPO",
               is_new_2025=True),
    SoAControl("A.7.2.8", "Privacy by default",
               Annex.A, "Art. 25", ControlStatus.INCLUDED_NOT_STARTED,
               "Maximum privacy settings applied by default — ISO 31700:2023 aligned", "CISO/DPO",
               is_new_2025=True),

    # A.7.3 — PII Minimisation
    SoAControl("A.7.3.1", "Limit collection to what is necessary",
               Annex.A, "Art. 5(1)(c)", ControlStatus.INCLUDED_NOT_STARTED,
               "Data minimisation enforced", "DPO"),
    SoAControl("A.7.3.2", "Limit processing to identified purposes",
               Annex.A, "Art. 5(1)(b)", ControlStatus.INCLUDED_NOT_STARTED,
               "Purpose limitation controls", "DPO"),
    SoAControl("A.7.3.3", "Accuracy of PII",
               Annex.A, "Art. 5(1)(d)", ControlStatus.INCLUDED_NOT_STARTED,
               "Data quality controls", "Data Owners"),
    SoAControl("A.7.3.4", "Retention and disposal",
               Annex.A, "Art. 5(1)(e)", ControlStatus.INCLUDED_NOT_STARTED,
               "Retention schedule and secure disposal", "Data Owners"),

    # A.7.4 — PII De-identification and Deletion (NEW/EXPANDED 2025)
    SoAControl("A.7.4.1", "De-identification and anonymisation",
               Annex.A, "Art. 25, 32", ControlStatus.INCLUDED_NOT_STARTED,
               "Pseudonymisation/anonymisation applied where appropriate", "IT/DPO",
               is_new_2025=True),
    SoAControl("A.7.4.2", "Temporary files",
               Annex.A, "Art. 32", ControlStatus.INCLUDED_NOT_STARTED,
               "Temporary PII files managed and deleted per policy", "IT",
               is_new_2025=True),
    SoAControl("A.7.4.3", "Return, transfer or disposal of PII",
               Annex.A, "Art. 28(3)(g)", ControlStatus.INCLUDED_NOT_STARTED,
               "End-of-contract PII return/disposal procedure", "DPO/Procurement",
               is_new_2025=True),

    # A.7.5 — PII Disclosure Controls (NEW 2025)
    SoAControl("A.7.5.1", "Basis for PII transfer to third parties",
               Annex.A, "Art. 44", ControlStatus.INCLUDED_NOT_STARTED,
               "Transfers only with documented lawful basis and TIA where required", "DPO/Legal",
               is_new_2025=True),
    SoAControl("A.7.5.2", "Records of PII disclosure to third parties",
               Annex.A, "Art. 30", ControlStatus.INCLUDED_NOT_STARTED,
               "Third-party disclosure register maintained", "DPO",
               is_new_2025=True),
    SoAControl("A.7.5.3", "Notification of legally-binding disclosure requests",
               Annex.A, "Art. 23", ControlStatus.INCLUDED_NOT_STARTED,
               "Law enforcement request handling with legal review", "Legal/DPO",
               is_new_2025=True),

    # A.7.6 — Privacy Notices
    SoAControl("A.7.6.1", "Provide privacy notice to PII principals",
               Annex.A, "Art. 13-14", ControlStatus.INCLUDED_NOT_STARTED,
               "Privacy notice published and accessible", "DPO"),

    # A.8.1 — Obligations
    SoAControl("A.8.1.1", "Determine and document obligations to PII principals",
               Annex.A, "Art. 12-22", ControlStatus.INCLUDED_NOT_STARTED,
               "All data subject rights procedurally supported", "DPO"),

    # A.8.2 — Access, Correction, Erasure
    SoAControl("A.8.2.1", "Right of access",
               Annex.A, "Art. 15", ControlStatus.INCLUDED_NOT_STARTED,
               "DSAR procedure implemented", "DPO"),
    SoAControl("A.8.2.2", "Right to rectification",
               Annex.A, "Art. 16", ControlStatus.INCLUDED_NOT_STARTED,
               "Correction procedure implemented", "DPO"),
    SoAControl("A.8.2.3", "Right to erasure",
               Annex.A, "Art. 17", ControlStatus.INCLUDED_NOT_STARTED,
               "Right to be forgotten procedure with audit trail", "DPO/IT"),
    SoAControl("A.8.2.4", "Right to data portability",
               Annex.A, "Art. 20", ControlStatus.INCLUDED_NOT_STARTED,
               "Data portability capability implemented", "IT/DPO"),
    SoAControl("A.8.2.5", "Right to object",
               Annex.A, "Art. 21", ControlStatus.INCLUDED_NOT_STARTED,
               "Objection handling procedure in place", "DPO"),
    SoAControl("A.8.2.6", "Automated decision-making and profiling",
               Annex.A, "Art. 22", ControlStatus.INCLUDED_NOT_STARTED,
               "Rights re: automated decisions supported", "DPO/IT",
               is_new_2025=True),

    # A.8.3 — Consent Management
    SoAControl("A.8.3.1", "Withdraw consent",
               Annex.A, "Art. 7(3)", ControlStatus.INCLUDED_NOT_STARTED,
               "Consent withdrawal as easy as giving consent", "Privacy Lead"),
    SoAControl("A.8.3.2", "Consent refresh",
               Annex.A, "Art. 7", ControlStatus.INCLUDED_NOT_STARTED,
               "Consent refreshed on material processing changes", "Privacy Lead",
               is_new_2025=True),

    # A.8.4 — Privacy Complaints
    SoAControl("A.8.4.1", "Privacy complaints and appeals",
               Annex.A, "Art. 77", ControlStatus.INCLUDED_NOT_STARTED,
               "Privacy complaints procedure implemented", "DPO"),

    # A.8.5 — Processors
    SoAControl("A.8.5.1", "Contracts with PII processors",
               Annex.A, "Art. 28", ControlStatus.INCLUDED_NOT_STARTED,
               "DPAs in place covering all A.7.2.6 requirements", "Legal/DPO"),
]


# ============================================================
# ANNEX B — PII PROCESSOR CONTROLS (ISO 27701:2025)
# ============================================================
ANNEX_B_CONTROLS: List[SoAControl] = [

    # B.8.1 — Conditions for Collection and Processing
    SoAControl("B.8.1.1", "Processing only on controller instructions",
               Annex.B, "Art. 28(3)(a)", ControlStatus.INCLUDED_NOT_STARTED,
               "Processing only on documented controller instructions", "Operations/DPO"),
    SoAControl("B.8.1.2", "Purposes limited to controller instructions",
               Annex.B, "Art. 28(3)", ControlStatus.INCLUDED_NOT_STARTED,
               "No processing beyond contracted purposes", "DPO"),
    SoAControl("B.8.1.3", "Marketing and advertising restrictions",
               Annex.B, "Art. 28", ControlStatus.NOT_APPLICABLE,
               "Processor does not use PII for own marketing", "DPO"),
    SoAControl("B.8.1.4", "Sub-processor engagement",
               Annex.B, "Art. 28(4)", ControlStatus.INCLUDED_NOT_STARTED,
               "Sub-processors require controller authorisation and equivalent DPAs", "Procurement/DPO"),

    # B.8.2 — Privacy Obligations
    SoAControl("B.8.2.1", "Obligations to PII principals (processor)",
               Annex.B, "Art. 28(3)(e)", ControlStatus.INCLUDED_NOT_STARTED,
               "Assistance to controller for DSARs and rights", "DPO"),
    SoAControl("B.8.2.2", "Legitimate purpose only",
               Annex.B, "Art. 28", ControlStatus.INCLUDED_NOT_STARTED,
               "Processing limited to legitimate controller purposes", "DPO"),

    # B.8.3 — Privacy by Design (ENHANCED 2025)
    SoAControl("B.8.3.1", "Privacy by design (processor standalone)",
               Annex.B, "Art. 25, 32", ControlStatus.INCLUDED_NOT_STARTED,
               "Privacy by design applied per ISO 31700:2023", "CISO/DPO",
               is_new_2025=True),
    SoAControl("B.8.3.2", "Temporary files (processor)",
               Annex.B, "Art. 32", ControlStatus.INCLUDED_NOT_STARTED,
               "Temporary PII files managed and deleted", "IT",
               is_new_2025=True),
    SoAControl("B.8.3.3", "Return, transfer or disposal of PII (processor)",
               Annex.B, "Art. 28(3)(g)", ControlStatus.INCLUDED_NOT_STARTED,
               "PII returned or securely deleted at contract end", "IT/DPO"),

    # B.8.4 — Processor Obligations to Controller
    SoAControl("B.8.4.1", "Assistance for data subject rights",
               Annex.B, "Art. 28(3)(e)", ControlStatus.INCLUDED_NOT_STARTED,
               "Technical measures to assist controller with DSARs", "Operations/DPO"),
    SoAControl("B.8.4.2", "Notification of data subject requests",
               Annex.B, "Art. 28", ControlStatus.INCLUDED_NOT_STARTED,
               "Requests forwarded to controller promptly", "Operations/DPO"),
    SoAControl("B.8.4.3", "Privacy breach notification (processor)",
               Annex.B, "Art. 33", ControlStatus.INCLUDED_NOT_STARTED,
               "Breach notification to controller without undue delay per DPA timeline", "CISO/DPO"),

    # B.8.5 — Cross-Border Transfers
    SoAControl("B.8.5.1", "Basis for cross-border transfer (processor)",
               Annex.B, "Art. 44", ControlStatus.INCLUDED_NOT_STARTED,
               "Transfers only per controller instructions and approved mechanisms", "DPO/Legal"),
    SoAControl("B.8.5.2", "Countries and international organisations",
               Annex.B, "Art. 44-49", ControlStatus.INCLUDED_NOT_STARTED,
               "Transfer destinations documented; restrictions enforced", "DPO"),
    SoAControl("B.8.5.3", "Records of cross-border PII transfers (processor)",
               Annex.B, "Art. 30(2)", ControlStatus.INCLUDED_NOT_STARTED,
               "Transfer register maintained for controller and regulator", "DPO"),

    # B.8.6 — Audit and Compliance (NEW/ENHANCED 2025)
    SoAControl("B.8.6.1", "Audit rights",
               Annex.B, "Art. 28(3)(h)", ControlStatus.INCLUDED_NOT_STARTED,
               "Controller audit rights explicitly supported; third-party audit reports provided", "DPO",
               is_new_2025=True),
    SoAControl("B.8.6.2", "Assistance for regulatory audits",
               Annex.B, "Art. 31", ControlStatus.INCLUDED_NOT_STARTED,
               "Assistance to controller for supervisory authority inspections", "DPO",
               is_new_2025=True),
]

ALL_CONTROLS = ANNEX_A_CONTROLS + ANNEX_B_CONTROLS


# ============================================================
# STATUS COLOURS (ANSI)
# ============================================================
class Colour:
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    BOLD = "\033[1m"
    RESET = "\033[0m"
    MAGENTA = "\033[95m"


def status_colour(status: ControlStatus) -> str:
    mapping = {
        ControlStatus.INCLUDED_FULL: Colour.GREEN,
        ControlStatus.INCLUDED_PARTIAL: Colour.YELLOW,
        ControlStatus.INCLUDED_NOT_STARTED: Colour.RED,
        ControlStatus.EXCLUDED_JUSTIFIED: Colour.BLUE,
        ControlStatus.NOT_APPLICABLE: Colour.CYAN,
    }
    return mapping.get(status, Colour.RESET)


def print_control(ctrl: SoAControl, show_details: bool = True) -> None:
    sc = status_colour(ctrl.status)
    new_tag = f" {Colour.MAGENTA}[NEW 2025]{Colour.RESET}" if ctrl.is_new_2025 else ""
    print(f"  {Colour.BOLD}{ctrl.ref}{Colour.RESET}{new_tag}")
    print(f"  Title:   {ctrl.title}")
    print(f"  GDPR:    {ctrl.gdpr_ref}")
    print(f"  Status:  {sc}{ctrl.status.value}{Colour.RESET}")
    if show_details and ctrl.owner:
        print(f"  Owner:   {ctrl.owner}")
    if show_details and ctrl.justification:
        print(f"  Note:    {ctrl.justification}")
    print()


def print_summary(controls: List[SoAControl], title: str) -> dict:
    total = len(controls)
    counts = {s: sum(1 for c in controls if c.status == s) for s in ControlStatus}
    new_2025 = sum(1 for c in controls if c.is_new_2025)

    implemented = counts[ControlStatus.INCLUDED_FULL]
    partial = counts[ControlStatus.INCLUDED_PARTIAL]
    not_started = counts[ControlStatus.INCLUDED_NOT_STARTED]
    excluded = counts[ControlStatus.EXCLUDED_JUSTIFIED]
    na = counts[ControlStatus.NOT_APPLICABLE]

    applicable = total - excluded - na
    completion_pct = (implemented / applicable * 100) if applicable > 0 else 0

    print(f"\n{Colour.BOLD}{'='*60}{Colour.RESET}")
    print(f"{Colour.BOLD}{title}{Colour.RESET}")
    print(f"{'='*60}")
    print(f"  Total controls:          {total}")
    print(f"  New in 2025:             {Colour.MAGENTA}{new_2025}{Colour.RESET}")
    print(f"  Applicable:              {applicable}")
    print(f"  {Colour.GREEN}Fully Implemented:       {implemented}{Colour.RESET}")
    print(f"  {Colour.YELLOW}Partially Implemented:   {partial}{Colour.RESET}")
    print(f"  {Colour.RED}Not Yet Implemented:     {not_started}{Colour.RESET}")
    print(f"  {Colour.BLUE}Excluded (Justified):    {excluded}{Colour.RESET}")
    print(f"  {Colour.CYAN}Not Applicable:          {na}{Colour.RESET}")
    print(f"  {'─'*40}")
    print(f"  Completion:              {Colour.BOLD}{completion_pct:.1f}%{Colour.RESET}")

    bar_length = 40
    filled = int(bar_length * completion_pct / 100)
    bar = f"[{'█' * filled}{'░' * (bar_length - filled)}]"
    bar_colour = Colour.GREEN if completion_pct >= 80 else (Colour.YELLOW if completion_pct >= 50 else Colour.RED)
    print(f"  {bar_colour}{bar}{Colour.RESET}\n")

    return {"total": total, "applicable": applicable, "implemented": implemented,
            "partial": partial, "not_started": not_started, "completion_pct": completion_pct}


def export_csv(controls: List[SoAControl], filename: str = "soa_export.csv") -> None:
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Reference", "Annex", "Title", "GDPR Reference",
                         "Status", "New in 2025", "Owner", "Justification", "Notes"])
        for ctrl in controls:
            writer.writerow([
                ctrl.ref, ctrl.annex.value, ctrl.title, ctrl.gdpr_ref,
                ctrl.status.value, "Yes" if ctrl.is_new_2025 else "No",
                ctrl.owner, ctrl.justification, ctrl.notes
            ])
    print(f"{Colour.GREEN}  Exported {len(controls)} controls to {filename}{Colour.RESET}\n")


def main():
    parser = argparse.ArgumentParser(
        description="ISO/IEC 27701:2025 PIMS SoA Tracker",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument("--summary", action="store_true", help="Show summary only")
    parser.add_argument("--annex", choices=["A", "B"], help="Filter by annex")
    parser.add_argument("--incomplete", action="store_true",
                        help="Show incomplete/not-yet-implemented controls only")
    parser.add_argument("--export", action="store_true", help="Export to CSV")
    args = parser.parse_args()

    print(f"\n{Colour.BOLD}{'='*60}{Colour.RESET}")
    print(f"{Colour.BOLD}  ISO/IEC 27701:2025 PIMS — Statement of Applicability Tracker{Colour.RESET}")
    print(f"{Colour.BOLD}{'='*60}{Colour.RESET}")
    print(f"  Standard:  ISO/IEC 27701:2025 (extends ISO 27001:2022)")
    print(f"  Generated: April 2025")
    print(f"  New 2025 controls shown with {Colour.MAGENTA}[NEW 2025]{Colour.RESET} tag")

    # Filter controls
    controls = ALL_CONTROLS
    if args.annex == "A":
        controls = ANNEX_A_CONTROLS
    elif args.annex == "B":
        controls = ANNEX_B_CONTROLS

    if args.incomplete:
        controls = [c for c in controls
                    if c.status in (ControlStatus.INCLUDED_NOT_STARTED, ControlStatus.INCLUDED_PARTIAL)]

    if args.export:
        export_csv(controls)
        return

    if not args.summary:
        # Print full control listing
        current_annex = None
        for ctrl in controls:
            if ctrl.annex != current_annex:
                current_annex = ctrl.annex
                print(f"\n{Colour.BOLD}{'─'*60}{Colour.RESET}")
                print(f"{Colour.BOLD}  {ctrl.annex.value}{Colour.RESET}")
                print(f"{Colour.BOLD}{'─'*60}{Colour.RESET}")
            print_control(ctrl)

    # Summary
    a_controls = [c for c in controls if c.annex == Annex.A]
    b_controls = [c for c in controls if c.annex == Annex.B]

    if a_controls:
        print_summary(a_controls, "ANNEX A — PII CONTROLLER CONTROLS SUMMARY")
    if b_controls:
        print_summary(b_controls, "ANNEX B — PII PROCESSOR CONTROLS SUMMARY")
    if a_controls and b_controls:
        print_summary(controls, "COMBINED SoA SUMMARY")

    # New 2025 controls highlight
    new_controls = [c for c in controls if c.is_new_2025]
    if new_controls:
        print(f"\n{Colour.MAGENTA}{Colour.BOLD}NEW CONTROLS IN ISO 27701:2025 ({len(new_controls)} controls){Colour.RESET}")
        print(f"{'─'*60}")
        for ctrl in new_controls:
            print(f"  {Colour.BOLD}{ctrl.ref}{Colour.RESET} — {ctrl.title}")
        print()


if __name__ == "__main__":
    main()
