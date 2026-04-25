# ISO/IEC 27701:2025 PIMS Toolkit

> A practical, audit-ready implementation toolkit for **ISO/IEC 27701:2025** Privacy Information Management Systems — extending **ISO 27001:2022** and ISO 27002:2022 with privacy-specific controls for PII controllers and PII processors. Updated for the 2025 edition with expanded Annex A/B controls, enhanced DPIA requirements, joint-controller provisions, and full alignment to ISO 27001:2022 (HLS/Annex SL).

> **Updated:** April 2025 | **Standard Version:** ISO/IEC 27701:2025 | **Replaces:** ISO/IEC 27701:2019

> ---

## What This Toolkit Contains

- All 10 PIMS clauses with implementation templates (extending ISO 27001:2022 Clauses 4–10)
- Full PIMS Gap Assessment covering all updated Annex A/B controls (aligned to ISO 27002:2022 structure)
- Privacy Risk Register with PII-specific risk methodology (aligned to ISO 27005:2022)
- Data Protection Impact Assessment (DPIA) template — enhanced per 27701:2025 requirements
- Statement of Applicability (SoA) for all updated Annex A and Annex B controls
- PII Controller controls — Annex A (ISO 27701:2025, aligned to ISO 27002:2022)
- PII Processor controls — Annex B (ISO 27701:2025, aligned to ISO 27002:2022)
- Privacy Notice, Consent Management, and Data Subject Rights procedures
- Legal & Regulatory Requirements Register (GDPR, UAE PDPL, UK GDPR, CCPA, HIPAA, India DPDPA)
- Worked examples for a fictional organisation (Nexus Financial Services Ltd)
- GRC automation scripts (Python)
- Cross-mapping to GDPR Articles, NIST Privacy Framework 1.0, ISO 29100:2011, and ISO 31700

## Key Changes: ISO/IEC 27701:2025 vs. 2019

| Area | 2019 Edition | 2025 Edition |
|------|-------------|-------------|
| **Base standard** | ISO 27001:2013 | ISO 27001:2022 (HLS/Annex SL) |
| **Control structure** | Annex A (31) + Annex B (18) = 49 | Expanded, aligned to ISO 27002:2022 (93-control structure) |
| **Privacy by Default** | Embedded in Annex A | Standalone control — explicit requirement |
| **Joint Controllers** | Limited guidance | Dedicated provisions and responsibilities |
| **DPIA triggers** | General guidance | Prescriptive threshold criteria |
| **Consent management** | Basic provisions | Granular consent lifecycle controls |
| **Cross-border transfers** | Reference to safeguards | Explicit transfer impact assessment (TIA) requirements |
| **Terminology** | "PII" primary | "Personal data" and "PII" harmonised |
| **ISO 29100 alignment** | Referenced | Deeper integration of 11 privacy principles |
| **ISO 31700 (PbD)** | Not referenced | Explicitly cross-referenced for Privacy by Design |
| **Audit requirements** | General PIMS audit | Specific privacy audit criteria and competence |

## Repository Structure

| # | Folder / File | Contents |
|---|--------------|----------|
| — | README.md | This file — full index and navigation guide |
| — | 00-IMPLEMENTATION-GUIDE.md | How to use this toolkit; PIMS implementation roadmap (2025 edition) |
| — | TRANSITION-GUIDE-2019-TO-2025.md | Transition guide: ISO 27701:2019 → 2025 — new controls, changes, gap analysis |
| 1 | 01-GAP-ASSESSMENT/ | Updated PIMS gap assessment checklist (2025 controls) |
| 2 | 02-PIMS-POLICY/ | Privacy Policy, PIMS Objectives, Privacy Notice |
| 3 | 03-CLAUSE4-CONTEXT/ | Context, interested parties, PIMS scope, legal register |
| 4 | 04-CLAUSE5-LEADERSHIP/ | Leadership, DPO role, privacy roles and RACI |
| 5 | 05-CLAUSE6-PLANNING/ | Privacy risk assessment, treatment, SoA (updated controls) |
| 6 | 06-CLAUSE7-SUPPORT/ | Competence, awareness, communications, documented info |
| 7 | 07-CLAUSE8-OPERATION/ | PII processing, DPIA, consent, data subject rights, breach response |
| 8 | 08-CLAUSE9-PERFORMANCE/ | Internal audit, KPIs, management review |
| 9 | 09-CLAUSE10-IMPROVEMENT/ | Nonconformities, corrective actions, continual improvement |
| 10 | 10-ANNEX-A-CONTROLS/ | PII Controller controls reference guide (2025 edition) |
| 11 | 11-ANNEX-B-CONTROLS/ | PII Processor controls reference guide (2025 edition) |
| 12 | 12-WORKED-EXAMPLE/ | Fictional NFS PIMS implementation examples |
| 13 | 13-SCRIPTS/ | Python GRC automation scripts |

## Clause-by-Clause File Index

### Implementation Guide (Root)

| File | Purpose |
|------|---------|
| 00-IMPLEMENTATION-GUIDE.md | Step-by-step PIMS implementation roadmap (2025 edition) |
| TRANSITION-GUIDE-2019-TO-2025.md | Guide for transitioning from ISO 27701:2019 to 2025 |

### Gap Assessment — 01-GAP-ASSESSMENT/

| # | File | Purpose |
|---|------|---------|
| 1 | PIMS-GAP-ASSESSMENT-CHECKLIST.md | Full PIMS gap assessment (2025 updated controls) |
| 2 | GAP-ASSESSMENT-SCORING-GUIDE.md | Scoring methodology and rating guidance |

### PIMS Policy — 02-PIMS-POLICY/

| # | File | Purpose |
|---|------|---------|
| 1 | PRIVACY-POLICY.md | Top-level Privacy Policy (Clause 5.2 extension) |
| 2 | PIMS-OBJECTIVES.md | Measurable Privacy Objectives (Clause 6.2 extension) |
| 3 | PRIVACY-NOTICE-TEMPLATE.md | External-facing Privacy Notice for data subjects |

### Clause 4 — Context of the Organisation — 03-CLAUSE4-CONTEXT/

| # | File | Purpose |
|---|------|---------|
| 1 | CONTEXT-AND-ISSUES-REGISTER.md | Internal and external issues register (privacy lens) |
| 2 | INTERESTED-PARTIES-REGISTER.md | Stakeholders, data subjects, regulators and requirements |
| 3 | PIMS-SCOPE-STATEMENT.md | PIMS scope definition — PII processing activities |
| 4 | LEGAL-REGULATORY-REQUIREMENTS-REGISTER.md | Privacy laws and regulatory obligations (GDPR, UAE PDPL, India DPDPA, etc.) |
| 5 | PII-PROCESSING-INVENTORY.md | Register of all PII processing activities (ROPA) |

### Clause 5 — Leadership — 04-CLAUSE5-LEADERSHIP/

| # | File | Purpose |
|---|------|---------|
| 1 | LEADERSHIP-COMMITMENT-STATEMENT.md | Top management commitment to privacy (Clause 5.1 extension) |
| 2 | DPO-TERMS-OF-REFERENCE.md | Data Protection Officer role, responsibilities and authority |
| 3 | PRIVACY-ROLES-RESPONSIBILITIES-RACI.md | PIMS roles, RACI matrix and accountabilities |
| 4 | PRIVACY-ACCEPTABLE-USE-POLICY.md | Acceptable use of PII by staff |

### Clause 6 — Planning — 05-CLAUSE6-PLANNING/

| # | File | Purpose |
|---|------|---------|
| 1 | PRIVACY-RISK-ASSESSMENT-METHODOLOGY.md | Privacy risk assessment approach and criteria (ISO 27005:2022 aligned) |
| 2 | PRIVACY-RISK-REGISTER.md | Privacy risk register template |
| 3 | PRIVACY-RISK-TREATMENT-PLAN.md | Privacy risk treatment decisions and actions |
| 4 | STATEMENT-OF-APPLICABILITY.md | SoA with all updated Annex A and Annex B controls |

### Clause 7 — Support — 06-CLAUSE7-SUPPORT/

| # | File | Purpose |
|---|------|---------|
| 1 | COMPETENCE-AND-TRAINING-REGISTER.md | Staff privacy competence and training records |
| 2 | PRIVACY-AWARENESS-PROGRAMME.md | Privacy awareness training plan |
| 3 | PRIVACY-COMMUNICATIONS-PLAN.md | Internal and external privacy communications |
| 4 | DOCUMENT-CONTROL-PROCEDURE.md | Documented information management (PIMS) |
| 5 | PIMS-DOCUMENT-MASTER-LIST.md | Master list of all PIMS documents |

### Clause 8 — Operation — 07-CLAUSE8-OPERATION/

| # | File | Purpose |
|---|------|---------|
| 1 | PII-PROCESSING-ACTIVITY-PROCEDURE.md | Procedures for lawful PII processing |
| 2 | DATA-PROTECTION-IMPACT-ASSESSMENT.md | DPIA template and methodology (2025 enhanced) |
| 3 | CONSENT-MANAGEMENT-PROCEDURE.md | Obtaining, recording and withdrawing consent |
| 4 | DATA-SUBJECT-RIGHTS-PROCEDURE.md | Handling DSARs, erasure, portability, objection |
| 5 | PRIVACY-BREACH-RESPONSE-PROCEDURE.md | PII breach detection, notification and recovery |
| 6 | DATA-RETENTION-AND-DISPOSAL-POLICY.md | Retention schedules and secure disposal of PII |
| 7 | THIRD-PARTY-PRIVACY-ASSESSMENT.md | Processor due diligence and contract requirements |
| 8 | CROSS-BORDER-TRANSFER-PROCEDURE.md | International PII transfer mechanisms and Transfer Impact Assessment (TIA) |
| 9 | PRIVACY-BY-DESIGN-PROCEDURE.md | Privacy by Design and Default (ISO 31700 aligned) |

### Clause 9 — Performance Evaluation — 08-CLAUSE9-PERFORMANCE/

| # | File | Purpose |
|---|------|---------|
| 1 | PRIVACY-KPI-METRICS-DASHBOARD.md | Privacy performance metrics and KPIs |
| 2 | PIMS-INTERNAL-AUDIT-PROGRAMME.md | Annual PIMS internal audit schedule and scope |
| 3 | PIMS-INTERNAL-AUDIT-REPORT-TEMPLATE.md | Internal audit findings report template |
| 4 | PIMS-MANAGEMENT-REVIEW-TEMPLATE.md | Management review agenda and minutes |

### Clause 10 — Improvement — 09-CLAUSE10-IMPROVEMENT/

| # | File | Purpose |
|---|------|---------|
| 1 | NCR-CORRECTIVE-ACTION-REGISTER.md | Nonconformity and corrective action log |
| 2 | CONTINUAL-IMPROVEMENT-LOG.md | Privacy improvement initiatives tracker |

### Annex A — PII Controller Controls — 10-ANNEX-A-CONTROLS/

| # | File | Purpose |
|---|------|---------|
| 1 | README.md | Annex A overview — PII Controller control index (2025 edition) |
| 2 | ANNEX-A-PII-CONTROLLER-CONTROLS.md | Full A.7–A.8 implementation reference with guidance and evidence |

### Annex B — PII Processor Controls — 11-ANNEX-B-CONTROLS/

| # | File | Purpose |
|---|------|---------|
| 1 | README.md | Annex B overview — PII Processor control index (2025 edition) |
| 2 | ANNEX-B-PII-PROCESSOR-CONTROLS.md | Full B.8 implementation reference with guidance and evidence |

### Worked Example — Nexus Financial Services — 12-WORKED-EXAMPLE/
Fictional implementation reference — completed templates for educational use only.

| # | File | What It Shows |
|---|------|--------------|
| 1 | README.md | NFS org profile, gap scores, risk summary and file index |
| 2 | NFS-PIMS-SCOPE-STATEMENT.md | Completed PIMS Scope Statement |
| 3 | NFS-PRIVACY-RISK-REGISTER-ENTRY.md | Three populated privacy risk register entries |
| 4 | NFS-SOA-EXCERPT.md | Completed SoA excerpt (Annex A + B controls, 2025 edition) |
| 5 | NFS-DPIA-ENTRY.md | Completed DPIA for a sample PII processing activity |
| 6 | NFS-BREACH-LOG-ENTRY.md | Completed privacy breach log entry |

### Scripts and Automation — 13-SCRIPTS/

| File | Purpose |
|------|---------|
| pims_soa_tracker.py | SoA tracker — all 2025 controls with progress reporting, CSV export |
| pims_gap_checker.py | Automated PIMS gap assessment checker with demo mode and priority ranking |
| dpia_risk_scorer.py | DPIA risk scoring and threshold alert tool |

---

## ISO 27701:2025 Quick Reference

### PIMS Clause Extension Overview

| Clause | Extension Title | Key Requirement |
|--------|----------------|----------------|
| 4 | Context | Understand privacy context, PII processing inventory, privacy-specific interested parties, joint controller identification |
| 5 | Leadership | Top management privacy commitment, DPO appointment, privacy policy, roles for joint controllers |
| 6 | Planning | Privacy risk assessment (ISO 27005:2022), SoA for updated Annex A/B controls, privacy objectives |
| 7 | Support | Privacy competence, awareness training, communications, documented PIMS information |
| 8 | Operation | DPIA (enhanced triggers), consent lifecycle management, data subject rights, breach response, privacy by design (ISO 31700), TIA for transfers |
| 9 | Performance | Privacy KPIs, PIMS internal audit (updated criteria), management review |
| 10 | Improvement | Nonconformities, corrective actions, continual improvement |

### Annex A/B Control Summary (2025 Edition)

| Annex | Applies To | Description |
|-------|-----------|-------------|
| A — Clauses A.7–A.8 | PII Controllers | Conditions for collection/use, obligations to data subjects, privacy notices, consent lifecycle, DSARs, Privacy by Default, joint controller provisions |
| B — Clauses B.8 | PII Processors | Processor-specific obligations, sub-processor management, PII return/deletion, transfer safeguards, audit rights |

---

## Supplementary Resources (Root Level)

| File | Purpose |
|------|---------|
| GDPR-MAPPING-CROSS-REFERENCE.md | ISO 27701:2025 ↔ GDPR Articles cross-reference |
| UAE-PDPL-ALIGNMENT-GUIDE.md | UAE Personal Data Protection Law alignment guide |
| DPA-TEMPLATE.md | Data Processing Agreement template (controller–processor) |
| DATA-SUBJECT-REQUEST-FORM-TEMPLATE.md | Data Subject Access Request (DSAR) form |
| SUPPLIER-PRIVACY-QUESTIONNAIRE.md | Third-party supplier privacy due diligence questionnaire |
| COOKIE-CONSENT-MANAGEMENT-GUIDE.md | Cookie consent and Consent Management Platform (CMP) guide |
| TRANSITION-GUIDE-2019-TO-2025.md | Complete transition guide from 2019 to 2025 edition |

---

## Cross-Mapping

This toolkit cross-maps ISO 27701:2025 controls to:

- **GDPR Articles** — EU General Data Protection Regulation article-level mapping
- **UAE PDPL** — UAE Personal Data Protection Law alignment
- **India DPDPA 2023** — Digital Personal Data Protection Act alignment
- **NIST Privacy Framework 1.0** — Identify-P / Govern-P / Control-P / Communicate-P / Protect-P functions
- **ISO/IEC 29100:2011** — Privacy framework and 11 privacy principles alignment
- **ISO/IEC 31700:2023** — Privacy by Design standard cross-reference
- **UK GDPR / DPA 2018** — Post-Brexit UK data protection alignment
- **CCPA / CPRA** — California Consumer Privacy Act alignment

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.2 | April 2025 | Comprehensive audit and fix — replaced incorrect placeholder content in 11 files with correct docs; completed THIRD-PARTY-PRIVACY-ASSESSMENT.md; fixed all ISO/IEC 27701:2019 body/footer refs to 2025; fixed dpia_risk_scorer.py version refs |
| 2.3 | April 2025 | Final deep audit — fixed wrong content in GAP-ASSESSMENT-SCORING-GUIDE (was showing checklist, now proper scoring guide PIMS-SCR-001); updated ISO/IEC 27701:2019 → 2025 in 17 additional files (body text, footer citations, document titles, contributing guidelines) — all 63 files now fully consistent with 2025 edition |
| 2.1 | April 2025 | Fixed file reference errors — Annex A/B now correctly reference ANNEX-A-PII-CONTROLLER-CONTROLS.md and ANNEX-B-PII-PROCESSOR-CONTROLS.md |
| 2.0 | April 2025 | Updated to ISO/IEC 27701:2025 — HLS alignment, expanded controls, DPIA enhancements, TIA, joint controller provisions, ISO 31700 cross-reference |
| 1.0 | 2024 | Initial release — ISO/IEC 27701:2019 edition |

---

*Maintained by Ankit Uniyal — ISO 27001 Lead Auditor | GRC Lead*

*See [00-IMPLEMENTATION-GUIDE.md](00-IMPLEMENTATION-GUIDE.md) for the full implementation roadmap.*

*ISO/IEC 27701:2025 PIMS Toolkit | README | PIMS-README-001 | v2.1 | Classification: Public*
