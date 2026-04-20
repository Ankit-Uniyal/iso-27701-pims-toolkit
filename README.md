# ISO/IEC 27701:2019 PIMS Toolkit

> A practical, audit-ready implementation toolkit for ISO/IEC 27701:2019 Privacy Information Management Systems — extending ISO 27001 and ISO 27002 with privacy-specific controls for PII controllers and PII processors. Covers all 10 PIMS clauses, all 49 Annex A/B controls, DPIA templates, privacy risk register, and implementation roadmap for GRC professionals, Data Protection Officers, and privacy practitioners.
>
> ---
>
> ## What This Toolkit Contains
>
> - All 10 ISO 27701 clauses with implementation templates (extending ISO 27001 Clauses 4–10)
> - - Full PIMS Gap Assessment covering all 49 controls (31 controller + 18 processor)
>   - - Privacy Risk Register with PII-specific risk methodology
>     - - Data Protection Impact Assessment (DPIA) template
>       - - Statement of Applicability (SoA) for all Annex A and Annex B controls
>         - - PII Controller controls — Annex A (ISO 27701:2019)
>           - - PII Processor controls — Annex B (ISO 27701:2019)
>             - - Privacy Notice, Consent Management, and Data Subject Rights procedures
>               - - Legal & Regulatory Requirements Register (GDPR, UAE PDPL, UK GDPR, CCPA, HIPAA)
>                 - - Worked examples for a fictional organisation (Nexus Financial Services Ltd)
>                   - - GRC automation scripts (Python)
>                     - - Cross-mapping to GDPR Articles, NIST Privacy Framework, and ISO 29100
>                      
>                       - ---
>
> ## Repository Structure
>
> | # | Folder / File | Contents |
> |---|---|---|
> | — | README.md | This file — full index and navigation guide |
> | — | 00-IMPLEMENTATION-GUIDE.md | How to use this toolkit; PIMS implementation roadmap |
> | 1 | 01-GAP-ASSESSMENT/ | 49-control PIMS gap assessment checklist |
> | 2 | 02-PIMS-POLICY/ | Privacy Policy, PIMS Objectives, Privacy Notice |
> | 3 | 03-CLAUSE4-CONTEXT/ | Context, interested parties, PIMS scope, legal register |
> | 4 | 04-CLAUSE5-LEADERSHIP/ | Leadership, DPO role, privacy roles and RACI |
> | 5 | 05-CLAUSE6-PLANNING/ | Privacy risk assessment, treatment, SoA (49 controls) |
> | 6 | 06-CLAUSE7-SUPPORT/ | Competence, awareness, communications, documented info |
> | 7 | 07-CLAUSE8-OPERATION/ | PII processing, DPIA, consent, data subject rights, breach response |
> | 8 | 08-CLAUSE9-PERFORMANCE/ | Internal audit, KPIs, management review |
> | 9 | 09-CLAUSE10-IMPROVEMENT/ | Nonconformities, corrective actions, continual improvement |
> | 10 | 10-ANNEX-A-CONTROLS/ | All 31 PII Controller controls reference guide |
> | 11 | 11-ANNEX-B-CONTROLS/ | All 18 PII Processor controls reference guide |
> | 12 | 12-WORKED-EXAMPLE/ | Fictional NFS PIMS implementation examples |
> | 13 | 13-SCRIPTS/ | Python GRC automation scripts |
>
> ---
>
> ## Clause-by-Clause File Index
>
> ### Implementation Guide (Root)
>
> | File | Purpose |
> |---|---|
> | 00-IMPLEMENTATION-GUIDE.md | Step-by-step PIMS implementation roadmap |
>
> ### Gap Assessment — `01-GAP-ASSESSMENT/`
>
> | # | File | Purpose |
> |---|---|---|
> | 1 | PIMS-GAP-ASSESSMENT-CHECKLIST.md | Full 49-control + clause-by-clause gap assessment |
> | 2 | GAP-ASSESSMENT-SCORING-GUIDE.md | Scoring methodology and rating guidance |
>
> ### PIMS Policy — `02-PIMS-POLICY/`
>
> | # | File | Purpose |
> |---|---|---|
> | 1 | PRIVACY-POLICY.md | Top-level Privacy Policy (Clause 5.2 extension) |
> | 2 | PIMS-OBJECTIVES.md | Measurable Privacy Objectives (Clause 6.2 extension) |
> | 3 | PRIVACY-NOTICE-TEMPLATE.md | External-facing Privacy Notice for data subjects |
>
> ### Clause 4 — Context of the Organisation — `03-CLAUSE4-CONTEXT/`
>
> | # | File | Purpose |
> |---|---|---|
> | 1 | CONTEXT-AND-ISSUES-REGISTER.md | Internal and external issues register (privacy lens) |
> | 2 | INTERESTED-PARTIES-REGISTER.md | Stakeholders, data subjects, regulators and requirements |
> | 3 | PIMS-SCOPE-STATEMENT.md | PIMS scope definition — PII processing activities |
> | 4 | LEGAL-REGULATORY-REQUIREMENTS-REGISTER.md | Privacy laws and regulatory obligations (GDPR, UAE PDPL, etc.) |
> | 5 | PII-PROCESSING-INVENTORY.md | Register of all PII processing activities (ROPA) |
>
> ### Clause 5 — Leadership — `04-CLAUSE5-LEADERSHIP/`
>
> | # | File | Purpose |
> |---|---|---|
> | 1 | LEADERSHIP-COMMITMENT-STATEMENT.md | Top management commitment to privacy (Clause 5.1 extension) |
> | 2 | DPO-TERMS-OF-REFERENCE.md | Data Protection Officer role, responsibilities and authority |
> | 3 | PRIVACY-ROLES-RESPONSIBILITIES-RACI.md | PIMS roles, RACI matrix and accountabilities |
> | 4 | PRIVACY-ACCEPTABLE-USE-POLICY.md | Acceptable use of PII by staff |
>
> ### Clause 6 — Planning — `05-CLAUSE6-PLANNING/`
>
> | # | File | Purpose |
> |---|---|---|
> | 1 | PRIVACY-RISK-ASSESSMENT-METHODOLOGY.md | Privacy risk assessment approach and criteria |
> | 2 | PRIVACY-RISK-REGISTER.md | Privacy risk register template |
> | 3 | PRIVACY-RISK-TREATMENT-PLAN.md | Privacy risk treatment decisions and actions |
> | 4 | STATEMENT-OF-APPLICABILITY.md | SoA with all 49 Annex A and Annex B controls |
>
> ### Clause 7 — Support — `06-CLAUSE7-SUPPORT/`
>
> | # | File | Purpose |
> |---|---|---|
> | 1 | COMPETENCE-AND-TRAINING-REGISTER.md | Staff privacy competence and training records |
> | 2 | PRIVACY-AWARENESS-PROGRAMME.md | Privacy awareness training plan |
> | 3 | PRIVACY-COMMUNICATIONS-PLAN.md | Internal and external privacy communications |
> | 4 | DOCUMENT-CONTROL-PROCEDURE.md | Documented information management (PIMS) |
> | 5 | PIMS-DOCUMENT-MASTER-LIST.md | Master list of all PIMS documents |
>
> ### Clause 8 — Operation — `07-CLAUSE8-OPERATION/`
>
> | # | File | Purpose |
> |---|---|---|
> | 1 | PII-PROCESSING-ACTIVITY-PROCEDURE.md | Procedures for lawful PII processing |
> | 2 | DATA-PROTECTION-IMPACT-ASSESSMENT.md | DPIA template and methodology |
> | 3 | CONSENT-MANAGEMENT-PROCEDURE.md | Obtaining, recording and withdrawing consent |
> | 4 | DATA-SUBJECT-RIGHTS-PROCEDURE.md | Handling DSARs, erasure, portability, objection |
> | 5 | PRIVACY-BREACH-RESPONSE-PROCEDURE.md | PII breach detection, notification and recovery |
> | 6 | DATA-RETENTION-AND-DISPOSAL-POLICY.md | Retention schedules and secure disposal of PII |
> | 7 | THIRD-PARTY-PRIVACY-ASSESSMENT.md | Processor due diligence and contract requirements |
> | 8 | CROSS-BORDER-TRANSFER-PROCEDURE.md | International PII transfer mechanisms and controls |
> | 9 | PRIVACY-BY-DESIGN-PROCEDURE.md | Privacy by design and default integration process |
>
> ### Clause 9 — Performance Evaluation — `08-CLAUSE9-PERFORMANCE/`
>
> | # | File | Purpose |
> |---|---|---|
> | 1 | PRIVACY-KPI-METRICS-DASHBOARD.md | Privacy performance metrics and KPIs |
> | 2 | PIMS-INTERNAL-AUDIT-PROGRAMME.md | Annual PIMS internal audit schedule and scope |
> | 3 | PIMS-INTERNAL-AUDIT-REPORT-TEMPLATE.md | Internal audit findings report template |
> | 4 | PIMS-MANAGEMENT-REVIEW-TEMPLATE.md | Management review agenda and minutes |
>
> ### Clause 10 — Improvement — `09-CLAUSE10-IMPROVEMENT/`
>
> | # | File | Purpose |
> |---|---|---|
> | 1 | NCR-CORRECTIVE-ACTION-REGISTER.md | Nonconformity and corrective action log |
> | 2 | CONTINUAL-IMPROVEMENT-LOG.md | Privacy improvement initiatives tracker |
>
> ### Annex A — PII Controller Controls — `10-ANNEX-A-CONTROLS/`
>
> | # | File | Purpose |
> |---|---|---|
> | 1 | README.md | Annex A overview — 31 controller controls |
> | 2 | A7-CONDITIONS-FOR-COLLECTION-USE.md | Controls A.7.2–A.7.4 (Lawfulness, purpose, minimisation) |
> | 3 | A8-OBLIGATIONS-TO-PII-PRINCIPALS.md | Controls A.8.1–A.8.5 (DSARs, consent, correction, erasure) |
>
> ### Annex B — PII Processor Controls — `11-ANNEX-B-CONTROLS/`
>
> | # | File | Purpose |
> |---|---|---|
> | 1 | README.md | Annex B overview — 18 processor controls |
> | 2 | B8-PROCESSOR-OBLIGATIONS.md | Controls B.8.1–B.8.5 (Processor-specific obligations) |
>
> ### Worked Example — Nexus Financial Services — `12-WORKED-EXAMPLE/`
>
> Fictional implementation reference — completed templates for educational use only.
>
> | # | File | What It Shows |
> |---|---|---|
> | 1 | README.md | NFS org profile and PIMS file index |
> | 2 | NFS-PIMS-SCOPE-STATEMENT.md | Completed PIMS Scope Statement |
> | 3 | NFS-PRIVACY-RISK-REGISTER-ENTRY.md | Three populated privacy risk register entries |
> | 4 | NFS-SOA-EXCERPT.md | Completed SoA excerpt (Annex A controller controls) |
> | 5 | NFS-DPIA-ENTRY.md | Completed DPIA for a sample PII processing activity |
> | 6 | NFS-BREACH-LOG-ENTRY.md | Completed privacy breach log entry |
>
> ### Scripts and Automation — `13-SCRIPTS/`
>
> | File | Purpose |
> |---|---|
> | pims_soa_tracker.py | SoA tracker — all 49 controls with progress reporting |
> | pims_gap_checker.py | Automated PIMS gap assessment checker |
> | dpia_risk_scorer.py | DPIA risk scoring and threshold alert tool |
>
> ---
>
> ## ISO 27701:2019 Quick Reference
>
> | Clause | Extension Title | Key Requirement |
> |---|---|---|
> | 4 | Context | Understand privacy context, PII processing inventory, privacy-specific interested parties |
> | 5 | Leadership | Top management privacy commitment, DPO appointment, privacy policy |
> | 6 | Planning | Privacy risk assessment, SoA for Annex A/B controls, privacy objectives |
> | 7 | Support | Privacy competence, awareness training, privacy communications |
> | 8 | Operation | DPIA, consent management, data subject rights, breach response, privacy by design |
> | 9 | Performance | Privacy KPIs, PIMS internal audit, management review |
> | 10 | Improvement | Nonconformities, corrective actions, continual improvement |
>
> ---
>
> ## Annex A/B Control Summary
>
> | Annex | Applies To | Control Count | Description |
> |---|---|---|---|
> | A — Clauses A.7–A.8 | PII Controllers | 31 | Conditions for collection, obligations to data subjects, privacy notices, consent, DSARs |
> | B — Clauses B.8 | PII Processors | 18 | Processor-specific obligations, sub-processor management, PII return and deletion |
> | **Total** | | **49** | |
>
> ---
>
> ## Cross-Mapping
>
> This toolkit cross-maps ISO 27701:2019 controls to:
>
> - **GDPR Articles** — EU General Data Protection Regulation article-level mapping
> - - **UAE PDPL** — UAE Personal Data Protection Law alignment
>   - - **NIST Privacy Framework 1.0** — Identify-P / Govern-P / Control-P / Communicate-P / Protect-P functions
>     - - **ISO/IEC 29100:2011** — Privacy framework and privacy principles alignment
>       - - **UK GDPR / DPA 2018** — Post-Brexit UK data protection alignment
>         - - **CCPA / CPRA** — California Consumer Privacy Act alignment
>          
>           - ---
>
> *Maintained by Ankit Uniyal — ISO 27001 Lead Auditor | GRC Lead*
> *See 00-IMPLEMENTATION-GUIDE.md for the full implementation roadmap.*
