# GRC Automation Scripts — ISO/IEC 27701:2025 PIMS Toolkit

**Directory:** `13-SCRIPTS/`
**Python Version:** 3.8+
**Classification:** Public — Open Source

---

## Overview

This directory contains three production-quality Python GRC automation scripts for ISO/IEC 27701:2025 PIMS implementation. All scripts run standalone with no external dependencies beyond the Python standard library.

| Script | Purpose | ISO 27701:2025 Clause |
|--------|---------|----------------------|
| `pims_gap_checker.py` | Gap assessment scorer and maturity dashboard | Cl. 9.1, Annex A/B |
| `dpia_risk_scorer.py` | DPIA risk calculator (interactive + batch) | A.7.2.5 |
| `pims_soa_tracker.py` | Statement of Applicability tracker | Cl. 6.1, Annex A/B |

---

## Prerequisites

- Python 3.8 or higher
- No additional packages required (standard library only)

Verify your Python version:
```bash
python3 --version
```

---

## Quick Start

Clone the repository and navigate to the scripts directory:
```bash
git clone https://github.com/Ankit-Uniyal/iso-27701-pims-toolkit.git
cd iso-27701-pims-toolkit/13-SCRIPTS
```

Run any script in demo mode to see it in action immediately:
```bash
python3 pims_gap_checker.py --demo
python3 dpia_risk_scorer.py --demo
python3 pims_soa_tracker.py --demo
```

---

## Script 1: pims_gap_checker.py

### Purpose
Parses a gap assessment CSV export, calculates per-clause maturity scores, produces an overall PIMS maturity band, and outputs a colour-coded prioritised remediation report.

### Usage

**Demo mode (no input file needed):**
```bash
python3 pims_gap_checker.py --demo
```

**Interactive mode (enter scores manually):**
```bash
python3 pims_gap_checker.py --interactive
```

**Batch mode from CSV:**
```bash
python3 pims_gap_checker.py --input gap_scores.csv
python3 pims_gap_checker.py --input gap_scores.csv --output report.txt
```

### Input CSV Format (gap_scores.csv)

Create a CSV file with the following columns:

```
clause,requirement,score,owner,notes
4.1,Understanding the organisation and its context,2,DPO,Scope statement drafted but not approved
4.2,Understanding the needs of interested parties,3,DPO,Register complete
4.3,Determining the scope of the PIMS,2,DPO,Needs senior sign-off
5.1,Leadership and commitment,1,CEO,No formal commitment statement yet
5.2,Privacy policy,3,DPO,Policy exists but not communicated
6.1,Actions to address privacy risks,2,DPO,Risk register in draft
6.2,Privacy objectives,2,DPO,Objectives not formally documented
7.1,Resources,3,HR,DPO appointed
7.2,Competence,1,HR,No training records
7.3,Awareness,1,HR,No awareness programme
7.4,Communication,2,DPO,Ad hoc communications only
7.5,Documented information,2,DPO,Document control informal
8.1,Operational planning and control,2,DPO,Some procedures exist
8.2,Privacy risk assessment,1,DPO,No formal DPIA conducted
8.3,Privacy risk treatment,1,DPO,No treatment plan
9.1,Monitoring, measurement and analysis,1,DPO,No KPI tracking
9.2,Internal audit,0,DPO,No audit conducted
9.3,Management review,0,DPO,No review conducted
10.1,Nonconformity and corrective action,0,DPO,No NCR process
10.2,Continual improvement,1,DPO,Ad hoc improvements only
```

Scores: 0 = Not Implemented, 1 = Initial, 2 = Partial, 3 = Largely Conformant, 4 = Full Conformant

### Output
- Clause-by-clause score table with percentage and RAG status
- Overall PIMS maturity band (Level 1–5)
- Prioritised remediation list (P1 Critical → P4 Low)
- Estimated effort summary

---

## Script 2: dpia_risk_scorer.py

### Purpose
Calculates inherent and residual risk scores for DPIA entries using the ISO/IEC 27701:2025 risk matrix (A.7.2.5). Supports both interactive single-entry mode and batch CSV processing.

### Usage

**Demo mode:**
```bash
python3 dpia_risk_scorer.py --demo
```

**Interactive mode (guided prompts):**
```bash
python3 dpia_risk_scorer.py --interactive
```

**Batch mode from CSV:**
```bash
python3 dpia_risk_scorer.py --input dpia_entries.csv
python3 dpia_risk_scorer.py --input dpia_entries.csv --output dpia_report.txt
```

**Show risk matrix:**
```bash
python3 dpia_risk_scorer.py --matrix
```

### Input CSV Format (dpia_entries.csv)

```
processing_activity,data_categories,data_subjects,likelihood,impact,controls_in_place,residual_likelihood,residual_impact
Customer onboarding KYC,Special category (financial history),Retail customers,3,4,Identity verification controls,2,3
Employee HR records processing,Employee PII,All employees,2,3,HR access controls RBAC,1,2
Marketing analytics profiling,Behavioural and preference data,Website visitors,3,3,Consent management platform,2,2
Loan decisioning automated,Financial and credit data,Loan applicants,4,4,Explainability framework human review,2,3
Third-party payroll processing,Payroll and bank details,All employees,2,4,DPA in place processor audit,1,3
```

Likelihood/Impact scale: 1 = Very Low, 2 = Low, 3 = Medium, 4 = High, 5 = Very High

### Output
- Risk score table (inherent and residual)
- Risk level: Low / Medium / High / Critical
- Flag for activities requiring DPO escalation (residual risk >= High)
- Recommended actions per entry

---

## Script 3: pims_soa_tracker.py

### Purpose
Tracks ISO/IEC 27701:2025 Annex A (PII Controller) and Annex B (PII Processor) control applicability and implementation status. Produces a complete SoA status dashboard and identifies controls requiring attention.

### Usage

**Demo mode:**
```bash
python3 pims_soa_tracker.py --demo
```

**Interactive mode:**
```bash
python3 pims_soa_tracker.py --interactive
```

**Batch mode from CSV:**
```bash
python3 pims_soa_tracker.py --input soa_controls.csv
python3 pims_soa_tracker.py --input soa_controls.csv --output soa_report.txt
```

**Show Annex A controls list:**
```bash
python3 pims_soa_tracker.py --list-controls --annex A
```

### Input CSV Format (soa_controls.csv)

```
control_id,control_name,annex,applicable,justification,implementation_status,owner,evidence_ref,review_date
A.7.2.1,Identify and document the purposes of PII processing,A,Yes,,Implemented,DPO,PIMS-OPS-004,2026-04-01
A.7.2.2,Identify the lawful basis for processing,A,Yes,,Implemented,DPO/Legal,ROPA,2026-04-01
A.7.2.3,Determine when and how consent is to be obtained,A,Yes,,Partially Implemented,DPO,PIMS-OPS-003,2025-09-01
A.7.2.4,Obtain and record consent,A,Yes,,Partially Implemented,DPO,PIMS-OPS-003,2025-09-01
A.7.2.5,Privacy impact assessment (DPIA),A,Yes,,Implemented,DPO,PIMS-OPS-002,2026-04-01
A.7.2.6,Contracts with PII processors,A,Yes,,Implemented,Legal,DPA-TEMPLATE,2026-04-01
A.7.2.7,Joint PII controller arrangements,A,Yes,,Not Started,DPO,,2025-07-01
A.7.2.8,Privacy by default,A,Yes,,Partially Implemented,CISO/DPO,PIMS-OPS-009,2025-09-01
B.8.1.1,Identify and document the purposes of PII processing,B,No,Organisation acts as controller only,,,,
B.8.2.1,Org roles responsibilities and obligations,B,No,Organisation acts as controller only,,,,
```

Implementation Status values: `Implemented`, `Partially Implemented`, `Not Started`, `Not Applicable`

### Output
- Annex A and B implementation status dashboard
- Percentage implemented per annex
- Controls requiring immediate attention (Not Started / overdue reviews)
- SoA completeness score

---

## Sample Data Files

The sample CSV formats above can be saved directly and used as starting points:

| File | Use With |
|------|----------|
| `gap_scores.csv` (create from template above) | `pims_gap_checker.py` |
| `dpia_entries.csv` (create from template above) | `dpia_risk_scorer.py` |
| `soa_controls.csv` (create from template above) | `pims_soa_tracker.py` |

---

## Troubleshooting

**`ModuleNotFoundError`** — All scripts use only the Python standard library. If you see this error, check your Python version: `python3 --version` (requires 3.8+).

**`FileNotFoundError`** — Ensure you run scripts from the `13-SCRIPTS/` directory, or use the full path to the input CSV file.

**Encoding errors on Windows** — If your CSV contains special characters, save it as UTF-8: in Excel, use "Save As → CSV UTF-8 (Comma delimited)".

**Script exits immediately** — Run with `--demo` first to confirm the script works, then switch to `--interactive` or `--input`.

---

## Integration with the Toolkit

| Script Output | Maps To |
|---------------|---------|
| Gap checker maturity score | `01-GAP-ASSESSMENT/GAP-ASSESSMENT-SCORING-GUIDE.md` maturity bands |
| Gap checker remediation list | `05-CLAUSE6-PLANNING/PRIVACY-RISK-TREATMENT-PLAN.md` |
| DPIA scorer output | `07-CLAUSE8-OPERATION/DATA-PROTECTION-IMPACT-ASSESSMENT.md` |
| SoA tracker output | `05-CLAUSE6-PLANNING/STATEMENT-OF-APPLICABILITY.md` |

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2025-01-01 | Initial release — three GRC automation scripts |
| 2.0 | April 2025 | Updated for ISO/IEC 27701:2025; added demo modes, batch CSV support, and this README |

---

*ISO/IEC 27701:2025 PIMS Toolkit | GRC Scripts README | 13-SCRIPTS*
