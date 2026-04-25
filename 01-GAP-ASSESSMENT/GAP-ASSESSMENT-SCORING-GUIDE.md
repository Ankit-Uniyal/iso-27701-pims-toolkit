# Gap Assessment Scoring Guide

**Document ID:** PIMS-SCR-001  
**Version:** 1.0  
**Date:** 2025-01-01  
**Owner:** Data Protection Officer  
**Classification:** Internal  
**Review Date:** 2026-01-01

---

## 1. Purpose

This Scoring Guide provides interpretive guidance for completing the ISO/IEC 27701:2025 PIMS Gap Assessment Checklist (PIMS-GAP-001). It defines scoring criteria, rating bands, prioritisation logic, and roadmap-building instructions to enable organisations to translate raw gap scores into an actionable remediation plan.

---

## 2. Scope

This guide applies to all personnel conducting or reviewing a PIMS gap assessment against ISO/IEC 27701:2025, including internal audit teams, external consultants, and implementation leads.

---

## 3. Scoring Scale

Rate each ISO/IEC 27701:2025 requirement using the following five-point scale:

| Score | Rating | Description |
|-------|--------|-------------|
| 0 | Not Implemented | No evidence of the requirement being addressed. Policy, process, and records are absent. |
| 1 | Initial | Ad hoc or informal approach; not documented or consistently applied. |
| 2 | Partial | Partially implemented; documented in some areas but significant gaps remain. |
| 3 | Largely Conformant | Mostly implemented and documented; minor gaps or inconsistencies exist. |
| 4 | Full Conformant | Fully implemented, documented, reviewed, and evidenced. Meets the requirement completely. |

---

## 4. Scoring Guidance by Rating

### Score 0 — Not Implemented
- No policy, procedure, record, or activity exists to address the requirement.
- Evidence: No documents found; staff unaware of the requirement.
- **Action required:** Treat as critical gap; prioritise implementation immediately.

### Score 1 — Initial
- Some awareness or informal activity exists but it is undocumented and inconsistent.
- Evidence: Verbal confirmation only; no written procedure or log.
- **Action required:** Formalise and document the approach; assign owner and target date.

### Score 2 — Partial
- A documented approach exists but is incomplete, not fully deployed, or not regularly reviewed.
- Evidence: Draft policies; partial records; inconsistent application across departments.
- **Action required:** Complete documentation, extend coverage, and schedule review.

### Score 3 — Largely Conformant
- The requirement is substantially addressed. Minor gaps may exist in evidence, coverage, or review frequency.
- Evidence: Documented procedures; most records present; recent review on file.
- **Action required:** Close minor gaps; ensure full evidence trail before audit.

### Score 4 — Full Conformant
- The requirement is fully met. Robust evidence, consistent application, regular review, and management oversight are demonstrated.
- Evidence: Complete, current documentation; audit trail; management sign-off.
- **Action required:** Maintain; schedule next review per document control cycle.

---

## 5. Calculating Clause and Overall Scores

### 5.1 Clause Score

For each ISO/IEC 27701:2025 clause or Annex section:

```
Clause Score (%) = (Sum of actual scores / (Number of requirements x 4)) x 100
```

**Example:** Clause 6 has 8 requirements. Scores are: 4, 3, 2, 4, 3, 1, 4, 3.
- Sum = 24
- Maximum = 8 x 4 = 32
- Clause Score = (24 / 32) x 100 = **75%**

### 5.2 Overall PIMS Maturity Score

```
Overall Score (%) = (Total actual scores across all requirements / (Total requirements x 4)) x 100
```

### 5.3 Maturity Band

| Score Range | Band | Interpretation |
|-------------|------|----------------|
| 0-24% | Level 1 - Absent | PIMS does not exist. Significant remediation required before certification. |
| 25-49% | Level 2 - Developing | Foundational elements in place but major gaps across multiple clauses. |
| 50-74% | Level 3 - Defined | Core PIMS implemented; gaps in Annex A/B controls or operational procedures. |
| 75-89% | Level 4 - Managed | Well-established PIMS; minor gaps; ready for internal audit and pre-assessment. |
| 90-100% | Level 5 - Optimising | Fully mature PIMS; continuous improvement cycle operating; certification-ready. |

---

## 6. Gap Priority Classification

Assign each identified gap a priority based on the combination of clause criticality and score:

| Priority | Criteria | Target Completion |
|----------|----------|-------------------|
| P1 - Critical | Score 0 on a mandatory clause (4-10, Annex A/B); or a clause required for GDPR/data protection compliance | Within 30 days |
| P2 - High | Score 1 on mandatory clauses; or score 0-1 on significant Annex controls | Within 60 days |
| P3 - Medium | Score 2 on any clause; or score 0-1 on advisory Annex controls | Within 90 days |
| P4 - Low | Score 3 with minor documentation gaps; style or formatting improvements | Within 180 days |

---

## 7. Building the Remediation Roadmap

### Step 1: Export Gap Data
Transfer all scores from the PIMS-GAP-ASSESSMENT-CHECKLIST.md into a spreadsheet. Add columns for: Owner, Priority, Target Date, and Status.

### Step 2: Identify P1 Critical Gaps
Filter for score 0 or 1 on Clauses 4-10 and Annex A/B. These represent items that must be resolved before any certification attempt.

### Step 3: Group by Theme
Cluster gaps into themes (e.g., Policy documentation, DPIA process, Third-party controls) to enable efficient batch remediation.

### Step 4: Assign Owners
Allocate each gap to a named owner with a realistic completion date. The DPO should hold overall accountability.

### Step 5: Track Progress
Review the remediation tracker monthly. Re-score completed items against the checklist and recalculate clause and overall scores.

### Step 6: Pre-Audit Self-Check
When the overall score reaches Level 4 (>=75%), conduct an internal audit using Section 8 of this toolkit before engaging an external certification body.

---

## 8. Evidence Requirements by Clause

| Clause | Minimum Evidence Required |
|--------|---------------------------|
| 4 - Context | Scope statement; interested parties register; legal/regulatory requirements register |
| 5 - Leadership | Signed leadership commitment; DPO ToR; RACI matrix; Privacy Policy |
| 6 - Planning | Risk assessment methodology; risk register; risk treatment plan; SoA |
| 7 - Support | Document master list; training register; competence records; communications plan |
| 8 - Operation | DPIA records; DSR logs; consent records; breach register; third-party assessments; ROPA |
| 9 - Performance | Internal audit report; management review minutes; KPI dashboard |
| 10 - Improvement | NCR/CAR register; continual improvement log |
| Annex A | Completed Annex A controls with applicability statements and evidence references |
| Annex B | Completed Annex B controls with applicability statements and evidence references |

---

## 9. Interpreting Annex A and B Controls

### Annex A - PII Controller Controls
These controls apply when the organisation acts as a **PII Controller** (i.e., it determines the purposes and means of processing personal data). Mark each control as:
- **Applicable:** Organisation acts as controller and the control is relevant.
- **Not Applicable:** Organisation does not act as controller for the processing in scope (provide justification).

### Annex B - PII Processor Controls
These controls apply when the organisation acts as a **PII Processor** (i.e., it processes personal data on behalf of another organisation). Mark each control as:
- **Applicable:** Organisation acts as processor and the control is relevant.
- **Not Applicable:** Organisation does not act as processor (provide justification).

### Dual Role
If the organisation acts as both controller and processor, both Annex A and Annex B apply. Score each set independently.

---

## 10. Linking Gaps to the Statement of Applicability (SoA)

Each Annex A/B control in the SoA (PIMS-PLN-003) should reference its gap assessment score. Where a control is marked Not Applicable, the justification must be documented in both the SoA and the gap assessment.

---

## 11. Common Scoring Errors to Avoid

1. **Over-scoring based on intent:** Score what is implemented, not what is planned.
2. **Ignoring evidence:** A policy exists but is not signed off or communicated -- score 2, not 4.
3. **Clause conflation:** Score each requirement independently even if they share a common owner.
4. **Ignoring Annex B if processor:** Many organisations underestimate processor obligations. Apply Annex B rigorously.
5. **Static scoring:** Re-score after each remediation cycle; the checklist is a living document.

---

## 12. Integration with Python GRC Scripts

The repository includes automated scoring tools in `13-SCRIPTS/`:

- **`pims_gap_checker.py`** -- Parses checklist CSV exports and calculates clause scores, overall maturity score, and gap distribution. Outputs a prioritised remediation summary.
- **`dpia_risk_scorer.py`** -- Scores individual DPIA entries and flags high-risk processing activities requiring escalation.
- **`pims_soa_tracker.py`** -- Tracks SoA control applicability and implementation status across Annex A and B.

To use the gap checker:
```bash
python 13-SCRIPTS/pims_gap_checker.py --input gap_assessment_export.csv --output remediation_report.txt
```

---

## 13. Version History

| Version | Date | Author | Change Description |
|---------|------|--------|--------------------|
| 1.0 | 2025-01-01 | DPO | Initial release -- ISO/IEC 27701:2025 |

---

*ISO/IEC 27701:2025 PIMS Toolkit | Gap Assessment Scoring Guide | PIMS-SCR-001*
