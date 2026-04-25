# India Digital Personal Data Protection Act (DPDPA) 2023 — Alignment Guide

| Field | Detail |
|-------|--------|
| **Document ID** | PIMS-SUP-017 |
| **Version** | 1.0 |
| **Date** | April 2025 |
| **Classification** | Public |
| **Applies To** | Organisations processing personal data of Indian data principals |

---

## 1. Overview

The **Digital Personal Data Protection Act 2023 (DPDPA)** is India's comprehensive data protection law, receiving Presidential assent on 11 August 2023. As of April 2025, the Act is in force with rules expected from the Data Protection Board (DPB). Organisations implementing ISO/IEC 27701:2025 can leverage their PIMS to achieve substantial DPDPA compliance, as both frameworks share foundational data protection principles.

**Key DPDPA Concepts:**
- **Data Fiduciary** — equivalent to GDPR Data Controller; determines purpose and means of processing
- **Data Processor** — equivalent to GDPR Data Processor; processes on behalf of fiduciary
- **Data Principal** — equivalent to GDPR Data Subject; the individual whose data is processed
- **Significant Data Fiduciary (SDF)** — high-risk category (large scale, sensitive data, national security risk); subject to additional obligations
- **Consent Manager** — accredited intermediary through which data principals manage consent

---

## 2. DPDPA to ISO/IEC 27701:2025 Cross-Mapping

### 2.1 Core Obligations

| DPDPA Section | Obligation | ISO/IEC 27701:2025 Mapping | Toolkit Document |
|---------------|------------|---------------------------|-----------------|
| S.4 — Grounds for processing | Consent or legitimate use; consent must be free, specific, informed, unconditional, unambiguous | A.7.2.3, A.7.2.4 | `07-CLAUSE8-OPERATION/CONSENT-MANAGEMENT-PROCEDURE.md` |
| S.5 — Notice | Clear notice before/at time of consent; purpose, data categories, withdrawal rights | A.7.5.1 | `02-PIMS-POLICY/PRIVACY-NOTICE-TEMPLATE.md` |
| S.6 — Consent | Positive opt-in; granular; revocable; must be as easy to withdraw as to give | A.7.2.3, A.7.2.4 | `07-CLAUSE8-OPERATION/CONSENT-MANAGEMENT-PROCEDURE.md` |
| S.7 — Legitimate use | Seven legitimate use grounds (legal obligation, emergency, employment, etc.) | A.7.2.2 | `03-CLAUSE4-CONTEXT/LEGAL-REGULATORY-REQUIREMENTS-REGISTER.md` |
| S.8(1) — Data quality | Ensure personal data is accurate and complete for intended use | A.7.3.3 | `07-CLAUSE8-OPERATION/PII-PROCESSING-ACTIVITY-PROCEDURE.md` |
| S.8(2) — Security | Technical and organisational measures; Annex I (to be prescribed by rules) | Cl. 6.1, A.8 | `05-CLAUSE6-PLANNING/PRIVACY-RISK-REGISTER.md` |
| S.8(3) — Breach notification | Notify Data Protection Board and data principal of breach in prescribed manner | A.7.8.3, A.7.8.4 | `07-CLAUSE8-OPERATION/PRIVACY-BREACH-RESPONSE-PROCEDURE.md` |
| S.8(4) — Erasure | Erase personal data when purpose fulfilled or consent withdrawn (unless legal retention) | A.7.3.4 | `07-CLAUSE8-OPERATION/DATA-RETENTION-AND-DISPOSAL-POLICY.md` |
| S.8(5) — Grievance officer | Appoint grievance officer; respond to data principal complaints within prescribed time | A.7.6 | `04-CLAUSE5-LEADERSHIP/DPO-TERMS-OF-REFERENCE.md` |
| S.9 — Processing of children's data | Verifiable parental consent for children under 18; no tracking or behavioural profiling | A.7.2.3 | `02-PIMS-POLICY/PRIVACY-POLICY.md` |
| S.10 — Significant data fiduciaries | Data Protection Impact Assessment (DPIA); DPO appointment; data audits | A.7.2.5, Cl. 5 | `07-CLAUSE8-OPERATION/DATA-PROTECTION-IMPACT-ASSESSMENT.md` |

### 2.2 Data Principal Rights (Chapter IV)

| DPDPA Section | Right | GDPR Equivalent | ISO 27701:2025 | Toolkit Document |
|---------------|-------|-----------------|---------------|-----------------|
| S.11 | Access to personal data | Art. 15 SAR | A.7.6.1 | `07-CLAUSE8-OPERATION/DATA-SUBJECT-RIGHTS-PROCEDURE.md` |
| S.12 | Correction and erasure | Art. 16, 17 | A.7.6.1 | `07-CLAUSE8-OPERATION/DATA-SUBJECT-RIGHTS-PROCEDURE.md` |
| S.13 | Grievance redressal | Art. 77 (DPA complaint) | A.7.6.2 | `04-CLAUSE5-LEADERSHIP/DPO-TERMS-OF-REFERENCE.md` |
| S.14 | Nominee rights | No direct GDPR equivalent | A.7.6 | Note: Unique to DPDPA — processes needed for nominee access on data principal incapacity/death |

### 2.3 Cross-Border Data Transfers

| DPDPA Provision | Details | ISO 27701:2025 Mapping |
|-----------------|---------|----------------------|
| S.16 — Transfer restrictions | Transfer permitted to countries not on Government-notified restricted list; Rules will specify permitted countries | A.7.4.3, A.7.5.1 |
| Transfer safeguards | Contractual safeguards expected (rules pending); interim: document transfer necessity and recipient country assessment | A.7.5.1; `07-CLAUSE8-OPERATION/CROSS-BORDER-TRANSFER-PROCEDURE.md` |

---

## 3. DPDPA-Specific Gaps in Standard ISO 27701:2025 Implementation

The following DPDPA requirements are unique or more stringent than ISO 27701:2025 defaults:

| DPDPA Requirement | Gap / Action Required |
|-------------------|-----------------------|
| **Nominee rights (S.14)** | Implement a procedure for nominee access to data on data principal incapacity/death. No direct GDPR/ISO 27701 equivalent. |
| **Consent Manager integration (S.6(6))** | If using a regulated Consent Manager intermediary, update consent management procedure to document the interface. |
| **Children's data verification (S.9)** | Implement verifiable parental consent mechanism; document in ROPA and DPIA for any service accessible to under-18s. |
| **DPB breach notification format** | Await DPB rules for prescribed breach notification format. Update breach response procedure when published. |
| **Significant Data Fiduciary designation** | Assess whether your organisation meets SDF criteria (to be defined by rules). If designated, DPO appointment and DPIA become mandatory. |
| **Data localisation** | DPDPA itself does not mandate data localisation, but sector-specific regulations (RBI, SEBI, IRDAI) may apply. Review sector rules separately. |

---

## 4. Penalties

| Violation | Maximum Penalty (Schedule to DPDPA) |
|-----------|--------------------------------------|
| Failure to take security safeguards (S.8(2)) | INR 250 crore (~USD 30 million) |
| Failure to notify data principal / DPB of breach (S.8(3)) | INR 200 crore (~USD 24 million) |
| Breach of children's data obligations (S.9) | INR 200 crore (~USD 24 million) |
| Breach of SDF additional obligations (S.10) | INR 150 crore (~USD 18 million) |
| Failure to comply with DPB orders | INR 50 crore (~USD 6 million) per instance |
| Other violations | INR 50 crore (~USD 6 million) |

*Note: Rules prescribing exact procedures, timelines, and DPB processes are expected from the Ministry of Electronics and Information Technology (MeitY). Monitor MeitY and DPB publications for updates.*

---

## 5. Implementation Checklist for DPDPA Compliance

| # | Action | Priority | Toolkit Resource |
|---|--------|----------|-----------------|
| 1 | Update ROPA/PII inventory to include purpose statement aligned to DPDPA S.4 grounds | High | `03-CLAUSE4-CONTEXT/PII-PROCESSING-INVENTORY.md` |
| 2 | Update Privacy Notice to DPDPA S.5 requirements (Sinhala/regional languages if applicable) | High | `02-PIMS-POLICY/PRIVACY-NOTICE-TEMPLATE.md` |
| 3 | Update Consent Management Procedure for DPDPA positive opt-in and revocation | High | `07-CLAUSE8-OPERATION/CONSENT-MANAGEMENT-PROCEDURE.md` |
| 4 | Add nominee rights procedure (DPDPA S.14 — unique requirement) | High | New procedure needed |
| 5 | Implement children's data age-verification and parental consent mechanism | High | `07-CLAUSE8-OPERATION/CONSENT-MANAGEMENT-PROCEDURE.md` |
| 6 | Update breach response procedure for DPB notification requirements (pending rules) | Medium | `07-CLAUSE8-OPERATION/PRIVACY-BREACH-RESPONSE-PROCEDURE.md` |
| 7 | Assess SDF designation risk and implement DPO/DPIA if designated | Medium | `04-CLAUSE5-LEADERSHIP/DPO-TERMS-OF-REFERENCE.md` |
| 8 | Update Legal Register with DPDPA obligations | Medium | `03-CLAUSE4-CONTEXT/LEGAL-REGULATORY-REQUIREMENTS-REGISTER.md` |
| 9 | Review cross-border transfer procedure for DPDPA S.16 permitted country list (monitor rules) | Medium | `07-CLAUSE8-OPERATION/CROSS-BORDER-TRANSFER-PROCEDURE.md` |
| 10 | Appoint Grievance Officer (domestic India entity) and publish contact details | High | `04-CLAUSE5-LEADERSHIP/DPO-TERMS-OF-REFERENCE.md` |

---

## 6. Related Regulatory Context

| Regulation | Relevance |
|-----------|-----------|
| **IT Act 2000 and SPDI Rules 2011** | Superseded by DPDPA for personal data; SPDI Rules remain applicable until DPDPA Rules published |
| **RBI Data Localisation** | RBI mandates payment data localisation; applies in addition to DPDPA |
| **SEBI Cybersecurity Framework** | Financial market participants must comply; cross-reference with ISO 27001/27701 controls |
| **IRDAI Data Guidelines** | Insurance sector-specific data handling requirements |
| **CERT-In Directions 2022** | 6-hour breach reporting to CERT-In for ICT incidents; narrower scope than DPDPA breach notification |

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| 1.0 | April 2025 | Initial release — DPDPA 2023 alignment guide for ISO/IEC 27701:2025 PIMS |

---

*ISO/IEC 27701:2025 PIMS Toolkit | India DPDPA Alignment Guide | PIMS-SUP-017*
