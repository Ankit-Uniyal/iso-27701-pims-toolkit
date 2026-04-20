# ISO/IEC 27701:2019 PIMS Implementation Guide

**Document ID:** PIMS-GUIDE-001
**Version:** 1.0 | **Date:** 2025 | **Audience:** PIMS implementers, DPOs, GRC professionals, Privacy practitioners

---

## What is ISO/IEC 27701:2019?

ISO/IEC 27701:2019 is an extension to ISO/IEC 27001 and ISO/IEC 27002 for privacy information management. It specifies requirements for establishing, implementing, maintaining, and continually improving a **Privacy Information Management System (PIMS)** as an extension to an existing ISMS.

The standard addresses the processing of **Personally Identifiable Information (PII)** and provides guidance for both:
- **PII Controllers** — organisations that determine the purpose and means of PII processing
- **PII Processors** — organisations that process PII on behalf of a controller

**Key facts:**
- ISO 27701 cannot be implemented standalone — it extends an existing ISO 27001 ISMS
- Organisations must be certified to ISO 27001 (or working towards it) before certifying to ISO 27701
- Annex A covers 31 controls specific to PII Controllers
- Annex B covers 18 controls specific to PII Processors
- ISO 27701 maps directly to GDPR requirements, making it a recognised compliance tool

---

## Implementation Roadmap

### Phase 1 — Foundation (Months 1–2)

| Step | Activity | Folder / File |
|---|---|---|
| 1.1 | Conduct PIMS gap assessment against all 49 controls and clauses | 01-GAP-ASSESSMENT/ |
| 1.2 | Define PIMS scope — identify all PII processing activities | 03-CLAUSE4-CONTEXT/PIMS-SCOPE-STATEMENT.md |
| 1.3 | Build PII Processing Inventory (Record of Processing Activities) | 03-CLAUSE4-CONTEXT/PII-PROCESSING-INVENTORY.md |
| 1.4 | Identify privacy-specific context and interested parties | 03-CLAUSE4-CONTEXT/ |
| 1.5 | Map legal and regulatory requirements (GDPR, UAE PDPL, etc.) | 03-CLAUSE4-CONTEXT/LEGAL-REGULATORY-REQUIREMENTS-REGISTER.md |
| 1.6 | Confirm top management commitment to privacy | 04-CLAUSE5-LEADERSHIP/LEADERSHIP-COMMITMENT-STATEMENT.md |
| 1.7 | Draft and approve Privacy Policy | 02-PIMS-POLICY/PRIVACY-POLICY.md |
| 1.8 | Appoint or formalise the DPO role | 04-CLAUSE5-LEADERSHIP/DPO-TERMS-OF-REFERENCE.md |
| 1.9 | Define PIMS roles and responsibilities | 04-CLAUSE5-LEADERSHIP/PRIVACY-ROLES-RESPONSIBILITIES-RACI.md |

### Phase 2 — Privacy Risk Assessment (Months 2–4)

| Step | Activity | Folder / File |
|---|---|---|
| 2.1 | Define privacy risk assessment methodology | 05-CLAUSE6-PLANNING/PRIVACY-RISK-ASSESSMENT-METHODOLOGY.md |
| 2.2 | Conduct privacy risk assessment for all PII processing activities | 05-CLAUSE6-PLANNING/PRIVACY-RISK-REGISTER.md |
| 2.3 | Determine privacy risk treatment decisions | 05-CLAUSE6-PLANNING/PRIVACY-RISK-TREATMENT-PLAN.md |
| 2.4 | Complete SoA for all 49 Annex A/B controls | 05-CLAUSE6-PLANNING/STATEMENT-OF-APPLICABILITY.md |
| 2.5 | Set measurable Privacy Objectives | 02-PIMS-POLICY/PIMS-OBJECTIVES.md |
| 2.6 | Conduct DPIAs for high-risk processing activities | 07-CLAUSE8-OPERATION/DATA-PROTECTION-IMPACT-ASSESSMENT.md |

### Phase 3 — Controls Implementation (Months 3–9)

| Step | Activity | Folder / File |
|---|---|---|
| 3.1 | Implement all applicable Annex A controller controls | 10-ANNEX-A-CONTROLS/ |
| 3.2 | Implement all applicable Annex B processor controls | 11-ANNEX-B-CONTROLS/ |
| 3.3 | Establish consent management procedures | 07-CLAUSE8-OPERATION/CONSENT-MANAGEMENT-PROCEDURE.md |
| 3.4 | Build data subject rights handling capability | 07-CLAUSE8-OPERATION/DATA-SUBJECT-RIGHTS-PROCEDURE.md |
| 3.5 | Implement privacy breach response procedure | 07-CLAUSE8-OPERATION/PRIVACY-BREACH-RESPONSE-PROCEDURE.md |
| 3.6 | Establish data retention and disposal policy | 07-CLAUSE8-OPERATION/DATA-RETENTION-AND-DISPOSAL-POLICY.md |
| 3.7 | Assess third-party processors and review contracts | 07-CLAUSE8-OPERATION/THIRD-PARTY-PRIVACY-ASSESSMENT.md |
| 3.8 | Document cross-border transfer mechanisms | 07-CLAUSE8-OPERATION/CROSS-BORDER-TRANSFER-PROCEDURE.md |
| 3.9 | Embed privacy by design into development/change processes | 07-CLAUSE8-OPERATION/PRIVACY-BY-DESIGN-PROCEDURE.md |
| 3.10 | Publish Privacy Notice for data subjects | 02-PIMS-POLICY/PRIVACY-NOTICE-TEMPLATE.md |
| 3.11 | Deliver privacy awareness training | 06-CLAUSE7-SUPPORT/PRIVACY-AWARENESS-PROGRAMME.md |

### Phase 4 — Operate and Monitor (Months 6–12)

| Step | Activity | Folder / File |
|---|---|---|
| 4.1 | Monitor privacy KPIs and metrics | 08-CLAUSE9-PERFORMANCE/PRIVACY-KPI-METRICS-DASHBOARD.md |
| 4.2 | Conduct PIMS internal audit (minimum annually) | 08-CLAUSE9-PERFORMANCE/PIMS-INTERNAL-AUDIT-PROGRAMME.md |
| 4.3 | Hold PIMS management review | 08-CLAUSE9-PERFORMANCE/PIMS-MANAGEMENT-REVIEW-TEMPLATE.md |
| 4.4 | Log and treat nonconformities | 09-CLAUSE10-IMPROVEMENT/NCR-CORRECTIVE-ACTION-REGISTER.md |
| 4.5 | Track continual improvement | 09-CLAUSE10-IMPROVEMENT/CONTINUAL-IMPROVEMENT-LOG.md |

### Phase 5 — Certification (Months 12–18)

| Step | Activity |
|---|---|
| 5.1 | Confirm ISO 27001 certification is in place (prerequisite for ISO 27701) |
| 5.2 | Select accredited certification body (BSI, DNV, Bureau Veritas, etc.) |
| 5.3 | Stage 1 audit — PIMS documentation review |
| 5.4 | Address Stage 1 findings |
| 5.5 | Stage 2 audit — evidence and implementation review |
| 5.6 | Address nonconformities raised |
| 5.7 | ISO 27701 certificate issued — valid 3 years with annual surveillance audits |

---

## Mandatory Documents Checklist

ISO 27701:2019 requires the following documented information as a minimum:

| # | Document | Clause | Status |
|---|---|---|---|
| 1 | PIMS Scope (extension of ISMS scope) | 4.3 extension | [ ] |
| 2 | Privacy Policy (extension of IS Policy) | 5.2 extension | [ ] |
| 3 | Privacy Objectives | 6.2 extension | [ ] |
| 4 | PII Processing Inventory / ROPA | 6.1.2 extension | [ ] |
| 5 | Privacy Risk Assessment Methodology | 6.1.2 extension | [ ] |
| 6 | Privacy Risk Assessment Results | 6.1.2 extension | [ ] |
| 7 | Privacy Risk Treatment Plan | 6.1.3 extension | [ ] |
| 8 | Statement of Applicability (Annex A/B controls) | 6.1.3(d) extension | [ ] |
| 9 | DPIA procedure and results (for high-risk processing) | 8.1 extension | [ ] |
| 10 | Consent records | 8.1 extension | [ ] |
| 11 | Data Subject Rights procedures and records | 8.1 extension | [ ] |
| 12 | Privacy Breach Response records | 8.1 extension | [ ] |
| 13 | Internal audit programme and results | 9.2 extension | [ ] |
| 14 | Management review results | 9.3 extension | [ ] |
| 15 | Nonconformities and corrective actions | 10.1 extension | [ ] |

---

## Controller vs Processor: Key Distinction

| Aspect | PII Controller | PII Processor |
|---|---|---|
| Definition | Determines the purpose and means of PII processing | Processes PII on behalf of a controller |
| Annex | Annex A (31 controls) | Annex B (18 controls) |
| Examples | Bank collecting customer data, employer holding HR data | Cloud provider, payroll bureau, marketing agency |
| Regulatory accountability | Primary accountability to regulators and data subjects | Contractual obligations to controller; some direct obligations |
| Key obligations | Lawful basis, consent, DSARs, DPIA, privacy notice | Processor agreements, sub-processor management, returning/deleting PII |

---

## How to Use the Worked Examples

The `12-WORKED-EXAMPLE/` folder contains completed versions of key templates using the fictional **Nexus Financial Services Ltd (NFS)** organisation. Use these to understand what a realistic, completed entry looks like before filling in your own templates.

> **Do not copy the worked examples verbatim** — they must be tailored to your organisation's specific context, PII processing activities, risks, and regulatory environment.

---

## Glossary of Key Terms

| Term | Definition |
|---|---|
| PIMS | Privacy Information Management System |
| PII | Personally Identifiable Information — any information that can identify a natural person directly or indirectly |
| PII Controller | Organisation that determines the purpose and means of PII processing |
| PII Processor | Organisation that processes PII on behalf of a controller |
| PII Principal | The natural person to whom the PII relates (also known as data subject) |
| DPO | Data Protection Officer — mandatory under GDPR for certain organisations |
| DPIA | Data Protection Impact Assessment — mandatory for high-risk processing activities |
| DSAR | Data Subject Access Request — a PII principal's right to access their data |
| SoA | Statement of Applicability — mandatory document listing all 49 controls with inclusion/exclusion justifications |
| Lawful basis | Legal grounds for processing PII (consent, contract, legal obligation, vital interests, public task, legitimate inte
