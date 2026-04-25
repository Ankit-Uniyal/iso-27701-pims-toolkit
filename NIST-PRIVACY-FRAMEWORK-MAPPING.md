# NIST Privacy Framework 1.0 — ISO/IEC 27701:2025 Cross-Mapping

| Field | Detail |
|-------|--------|
| **Document ID** | PIMS-SUP-018 |
| **Version** | 1.0 |
| **Date** | April 2025 |
| **Classification** | Public |
| **Frameworks** | NIST Privacy Framework v1.0 (2020) x ISO/IEC 27701:2025 |

---

## 1. Overview

The **NIST Privacy Framework 1.0** (published January 2020) is a voluntary US framework for managing privacy risk, structured around five Core Functions: **Identify, Govern, Control, Communicate, Protect**. ISO/IEC 27701:2025 is the international standard for Privacy Information Management Systems.

Both frameworks are risk-based and principle-driven. An organisation implementing ISO/IEC 27701:2025 through this toolkit will satisfy the vast majority of NIST Privacy Framework Core outcomes. This guide maps the alignment and highlights any gaps.

**Key Structural Differences:**
- NIST PF is outcome-based (what to achieve); ISO 27701 is requirement-based (what you must do to certify)
- NIST PF has no certification scheme; ISO 27701 does (via ISO 27001 as the base ISMS)
- NIST PF is US-market oriented; ISO 27701 is globally applicable
- ISO 27701:2025 directly aligns to GDPR Article 42 certification provisions; NIST PF does not

---

## 2. Core Function Mapping

### IDENTIFY (ID) — Inventory and Map

| NIST PF Subcategory | Outcome | ISO 27701:2025 Mapping | Toolkit Document |
|---------------------|---------|----------------------|-----------------|
| ID.IM-P1 | Systems/products/services involving PII are inventoried | Cl. 4.3, A.7.2.1 | `03-CLAUSE4-CONTEXT/PII-PROCESSING-INVENTORY.md` |
| ID.IM-P2 | Owners/operators of systems involving PII are inventoried | Cl. 5.3, A.7.2.1 | `04-CLAUSE5-LEADERSHIP/PRIVACY-ROLES-RESPONSIBILITIES-RACI.md` |
| ID.IM-P3 | Categories of individuals and PII are inventoried | A.7.2.1, A.7.3.1 | `03-CLAUSE4-CONTEXT/PII-PROCESSING-INVENTORY.md` |
| ID.IM-P4 | PII actions (collection, use, disclosure, etc.) are inventoried | A.7.2.1, A.7.4.1 | `07-CLAUSE8-OPERATION/PII-PROCESSING-ACTIVITY-PROCEDURE.md` |
| ID.IM-P5 | Purposes for PII processing are identified | A.7.2.1, A.7.2.2 | `03-CLAUSE4-CONTEXT/PII-PROCESSING-INVENTORY.md` |
| ID.IM-P6 | Privacy risk to individuals is understood | Cl. 6.1.2, A.7.2.5 | `05-CLAUSE6-PLANNING/PRIVACY-RISK-REGISTER.md` |
| ID.IM-P7 | Roles and responsibilities for privacy are established | Cl. 5.3 | `04-CLAUSE5-LEADERSHIP/PRIVACY-ROLES-RESPONSIBILITIES-RACI.md` |
| ID.IM-P8 | Privacy risk associated with third-party sharing is identified | A.7.2.6, A.7.5.1 | `07-CLAUSE8-OPERATION/THIRD-PARTY-PRIVACY-ASSESSMENT.md` |

### GOVERN (GV) — Policies and Procedures

| NIST PF Subcategory | Outcome | ISO 27701:2025 Mapping | Toolkit Document |
|---------------------|---------|----------------------|-----------------|
| GV.PO-P1 | Organisational privacy values and policies established | Cl. 5.2 | `02-PIMS-POLICY/PRIVACY-POLICY.md` |
| GV.PO-P2 | Processes to implement privacy policies are established | Cl. 6.1, 8.1 | `05-CLAUSE6-PLANNING/PRIVACY-RISK-TREATMENT-PLAN.md` |
| GV.PO-P3 | Roles and responsibilities for privacy are established | Cl. 5.3 | `04-CLAUSE5-LEADERSHIP/DPO-TERMS-OF-REFERENCE.md` |
| GV.PO-P4 | Privacy risk is incorporated into enterprise risk | Cl. 6.1.2 | `05-CLAUSE6-PLANNING/PRIVACY-RISK-ASSESSMENT-METHODOLOGY.md` |
| GV.PO-P5 | Legal and regulatory requirements are understood | Cl. 4.2 | `03-CLAUSE4-CONTEXT/LEGAL-REGULATORY-REQUIREMENTS-REGISTER.md` |
| GV.PO-P6 | Privacy awareness and training exists | Cl. 7.2, 7.3 | `06-CLAUSE7-SUPPORT/PRIVACY-AWARENESS-PROGRAMME.md` |
| GV.MT-P1 | Privacy risk is monitored and measured | Cl. 9.1 | `08-CLAUSE9-PERFORMANCE/PRIVACY-KPI-METRICS-DASHBOARD.md` |
| GV.MT-P2 | Privacy risks, policies, and activities are reviewed | Cl. 9.3 | `08-CLAUSE9-PERFORMANCE/PIMS-MANAGEMENT-REVIEW-TEMPLATE.md` |

### CONTROL (CT) — Data Processing Management

| NIST PF Subcategory | Outcome | ISO 27701:2025 Mapping | Toolkit Document |
|---------------------|---------|----------------------|-----------------|
| CT.PO-P1 | Policies to manage PII are established | Cl. 5.2, A.7.2 | `02-PIMS-POLICY/PRIVACY-POLICY.md` |
| CT.PO-P2 | Policies for data processing decisions are established | A.7.2.2, A.7.2.3 | `07-CLAUSE8-OPERATION/CONSENT-MANAGEMENT-PROCEDURE.md` |
| CT.PO-P3 | Data minimisation practices exist | A.7.3.1, A.7.3.2 | `07-CLAUSE8-OPERATION/PII-PROCESSING-ACTIVITY-PROCEDURE.md` |
| CT.PO-P4 | PII is retained only as long as necessary | A.7.3.4 | `07-CLAUSE8-OPERATION/DATA-RETENTION-AND-DISPOSAL-POLICY.md` |
| CT.PO-P5 | Disposal of PII is conducted in a secure manner | A.7.3.4, A.8.3.2 | `07-CLAUSE8-OPERATION/DATA-RETENTION-AND-DISPOSAL-POLICY.md` |
| CT.DM-P3 | Privacy risk is assessed for new/changed systems | A.7.2.5 | `07-CLAUSE8-OPERATION/DATA-PROTECTION-IMPACT-ASSESSMENT.md` |
| CT.DM-P4 | Privacy by design and default applied | A.7.2.8 | `07-CLAUSE8-OPERATION/PRIVACY-BY-DESIGN-PROCEDURE.md` |
| CT.DM-P7 | Individuals' consent is managed | A.7.2.3, A.7.2.4 | `07-CLAUSE8-OPERATION/CONSENT-MANAGEMENT-PROCEDURE.md` |
| CT.DM-P8 | Audit/log records of PII processing exist | A.7.2.1, A.8.4.2 | `07-CLAUSE8-OPERATION/PII-PROCESSING-ACTIVITY-PROCEDURE.md` |

### COMMUNICATE (CM) — Transparency and Disclosure

| NIST PF Subcategory | Outcome | ISO 27701:2025 Mapping | Toolkit Document |
|---------------------|---------|----------------------|-----------------|
| CM.PO-P1 | Policies to communicate privacy practices to individuals | A.7.5.1 | `02-PIMS-POLICY/PRIVACY-NOTICE-TEMPLATE.md` |
| CM.PO-P2 | Procedures to respond to requests from individuals | A.7.6 | `07-CLAUSE8-OPERATION/DATA-SUBJECT-RIGHTS-PROCEDURE.md` |
| CM.AW-P1 | Individuals are aware of privacy practices | A.7.5.1 | `02-PIMS-POLICY/PRIVACY-NOTICE-TEMPLATE.md` |
| CM.AW-P2 | Individuals have access to privacy notices | A.7.5.1 | `02-PIMS-POLICY/PRIVACY-NOTICE-TEMPLATE.md` |
| CM.AW-P3 | Mechanisms for exercising privacy rights are provided | A.7.6.1, A.7.6.2 | `07-CLAUSE8-OPERATION/DATA-SUBJECT-RIGHTS-PROCEDURE.md` |

### PROTECT (PR) — Data Protection

| NIST PF Subcategory | Outcome | ISO 27701:2025 Mapping | Toolkit Document |
|---------------------|---------|----------------------|-----------------|
| PR.PO-P1 | Security and privacy policies for PII are established | Cl. 5.2, 6.1 | `02-PIMS-POLICY/PRIVACY-POLICY.md` |
| PR.PO-P4 | Workforce is trained on privacy | Cl. 7.2, 7.3 | `06-CLAUSE7-SUPPORT/PRIVACY-AWARENESS-PROGRAMME.md` |
| PR.PO-P5 | Privacy risks are identified and managed | Cl. 6.1.2 | `05-CLAUSE6-PLANNING/PRIVACY-RISK-REGISTER.md` |
| PR.DS-P1 | PII is protected during transmission | A.8.3 (via ISO 27001 controls) | SoA reference |
| PR.DS-P5 | Breaches involving PII are handled | A.7.8.3, A.7.8.4 | `07-CLAUSE8-OPERATION/PRIVACY-BREACH-RESPONSE-PROCEDURE.md` |

---

## 3. Coverage Summary

| NIST PF Function | ISO 27701:2025 Coverage | Gap Analysis |
|------------------|------------------------|--------------|
| IDENTIFY | Full — ISO 27701 Clauses 4-5 and A.7.2.1 directly cover all ID subcategories | None significant |
| GOVERN | Full — ISO 27701 Clauses 5-7 and 9-10 map comprehensively to all GV outcomes | None significant |
| CONTROL | Full — ISO 27701 Annex A.7.2-A.7.5 and Clause 8 cover all CT outcomes | None significant |
| COMMUNICATE | Full — ISO 27701 A.7.5 and A.7.6 directly address all CM outcomes | None significant |
| PROTECT | Substantial — ISO 27701 + ISO 27001 controls cover PR outcomes. Technical security controls (encryption, etc.) come from the base ISO 27001 ISMS | ISO 27701 alone does not cover all PR.DS security controls — the ISO 27001 SoA must also be reviewed |

**Overall:** ISO/IEC 27701:2025 implementation using this toolkit addresses **~95%** of NIST Privacy Framework 1.0 Core outcomes. The remaining 5% relates to US-specific technical control language in PR.DS that maps to ISO 27001 security controls rather than ISO 27701 privacy controls.

---

## 4. Using This Mapping

Organisations subject to both NIST Privacy Framework and ISO/IEC 27701:2025 (e.g., US multinationals or US federal contractors with international operations) can use this mapping to:
- **Map NIST PF Current Profile** to ISO 27701:2025 gap assessment scores (use `01-GAP-ASSESSMENT/PIMS-GAP-ASSESSMENT-CHECKLIST.md`)
- **Avoid duplicate documentation** — ISO 27701 documents satisfy NIST PF outcome evidence
- **Report to US stakeholders** using NIST PF language while maintaining ISO 27701 certification

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| 1.0 | April 2025 | Initial release — NIST Privacy Framework 1.0 to ISO/IEC 27701:2025 full cross-mapping |

---

*ISO/IEC 27701:2025 PIMS Toolkit | NIST Privacy Framework Mapping | PIMS-SUP-018*
