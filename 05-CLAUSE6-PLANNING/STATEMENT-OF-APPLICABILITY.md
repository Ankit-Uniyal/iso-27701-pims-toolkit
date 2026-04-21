# Statement of Applicability (SoA) — ISO/IEC 27701:2025

| Field | Detail |
|-------|--------|
| **Document ID** | PIMS-SOA-001 |
| **Version** | 2.0 |
| **Date** | April 2025 |
| **Owner** | Data Protection Officer |
| **Classification** | Confidential — Internal Use |
| **Review Date** | April 2026 |
| **Standard** | ISO/IEC 27701:2025 (Annex A — PII Controllers | Annex B — PII Processors) |

---

## 1. Introduction

This Statement of Applicability (SoA) defines which ISO/IEC 27701:2025 Annex A and Annex B controls are applicable to [Organisation Name] and provides justification for inclusion or exclusion of each control.

**Organisation's PIMS Role:** ☐ PII Controller only ☐ PII Processor only ☐ Both Controller and Processor

**Base ISMS:** ISO/IEC 27001:2022

**SoA Scope:** [Insert PIMS scope statement reference — must align with PIMS scope document]

### Inclusion/Exclusion Codes

| Code | Meaning |
|------|---------|
| **I** | Included — control applicable and implemented |
| **I-P** | Included — Partially implemented (gap exists) |
| **E-R** | Excluded — not a PII controller (role not applicable) |
| **E-P** | Excluded — not a PII processor (role not applicable) |
| **E-J** | Excluded — justified by risk/legal assessment |
| **NA** | Not applicable — specific sub-clause not relevant to our processing |

### Implementation Status Codes

| Code | Meaning |
|------|---------|
| **F** | Fully Implemented |
| **P** | Partially Implemented |
| **NI** | Not Yet Implemented |
| **NA** | Not Applicable |

---

## 2. Annex A — PII Controller Controls

*Annex A applies when the organisation acts as a **PII Controller** (determines the purposes and means of processing PII).*

### A.7 — Conditions for Collection and Processing

| Ref | Control Title | Included / Excluded | Justification | Implementation Status | Owner | Related GDPR Art. |
|-----|--------------|--------------------|--------------|-----------------------|-------|------------------|
| **A.7.2** | **Identify and document the purpose** | | | | | Art. 5(1)(b) |
| A.7.2.1 | Identify and document the purposes of PII processing | I | All processing activities must have documented purposes per GDPR Art. 5 and 27701:2025 Clause 6 | F / P / NI | DPO | Art. 5(1)(b) |
| A.7.2.2 | Identify the lawful basis for processing | I | Legal basis required for all processing activities | | DPO | Art. 6 |
| A.7.2.3 | Determine when and how consent is to be obtained | I | Consent used as lawful basis for marketing and optional processing | | Privacy Lead | Art. 7 |
| A.7.2.4 | Obtain and record consent | I | Consent records maintained in CMP | | Privacy Lead | Art. 7 |
| A.7.2.5 | Privacy impact assessment | I | DPIA mandatory for high-risk processing per 2025 trigger criteria | | DPO | Art. 35 |
| A.7.2.6 | Contracts with PII processors | I | All processors have DPAs in place | | Legal / DPO | Art. 28 |
| A.7.2.7 | Joint PII controller arrangements | I / NA | [Include if joint controller relationships exist] | | DPO | Art. 26 |
| A.7.2.8 | Privacy by default | I | Privacy by default applied — maximum privacy settings as default (ISO 31700:2023) | | CISO / DPO | Art. 25 |
| **A.7.3** | **PII minimisation** | | | | | Art. 5(1)(c) |
| A.7.3.1 | Limit collection to what is necessary | I | Data minimisation principle enforced across all systems | | IT / DPO | Art. 5(1)(c) |
| A.7.3.2 | Limit processing to identified purposes | I | Purpose limitation controls implemented | | DPO | Art. 5(1)(b) |
| A.7.3.3 | Accuracy of PII | I | Data quality controls and correction procedures in place | | Data Owners | Art. 5(1)(d) |
| A.7.3.4 | Retention and disposal | I | Retention schedule implemented; secure disposal procedures in place | | Data Owners | Art. 5(1)(e) |
| **A.7.4** | **PII de-identification and deletion** | | | | | |
| A.7.4.1 | De-identification and anonymisation | I | Pseudonymisation and anonymisation applied where appropriate | | IT / DPO | Art. 25, 32 |
| A.7.4.2 | Temporary files | I | Temporary file handling procedures implemented | | IT | Art. 32 |
| A.7.4.3 | Return, transfer or disposal of PII | I | End-of-contract PII return/disposal procedure in place | | DPO / Procurement | Art. 28 |
| **A.7.5** | **PII disclosure controls** | | | | | |
| A.7.5.1 | Basis for PII transfer to third parties | I | Third-party transfers only with controller authorisation and documented basis | | DPO / Legal | Art. 44 |
| A.7.5.2 | Records of PII disclosure to third parties | I | Third-party disclosure register maintained | | DPO | Art. 30 |
| A.7.5.3 | Notification of legally-binding disclosure requests | I | Process for handling law enforcement requests defined | | Legal / DPO | Art. 23 |
| **A.7.6** | **Privacy notices** | | | | | Art. 13–14 |
| A.7.6.1 | Provide privacy notice to PII principals | I | Privacy Notice published and accessible to all data subjects | | DPO | Art. 13–14 |

### A.8 — Obligations to PII Principals

| Ref | Control Title | Included / Excluded | Justification | Implementation Status | Owner | Related GDPR Art. |
|-----|--------------|--------------------|--------------|-----------------------|-------|------------------|
| **A.8.1** | **Obligations to data subjects** | | | | | |
| A.8.1.1 | Determine and document obligations to PII principals | I | All data subject rights documented and procedurally supported | | DPO | Art. 12–22 |
| **A.8.2** | **Access, correction and erasure** | | | | | |
| A.8.2.1 | Right of access | I | SAR/DSAR procedure implemented | | DPO | Art. 15 |
| A.8.2.2 | Right to rectification | I | Correction procedure implemented | | DPO | Art. 16 |
| A.8.2.3 | Right to erasure ("right to be forgotten") | I | Erasure procedure implemented with audit trail | | DPO / IT | Art. 17 |
| A.8.2.4 | Right to data portability | I | Data portability capability implemented | | IT / DPO | Art. 20 |
| A.8.2.5 | Right to object | I | Objection handling procedure in place | | DPO | Art. 21 |
| A.8.2.6 | Automated decision-making and profiling | I / NA | [Include if automated decisions are made] | | DPO / IT | Art. 22 |
| **A.8.3** | **Consent management** | | | | | Art. 7 |
| A.8.3.1 | Withdraw consent | I | Consent withdrawal mechanism implemented in all consent channels | | Privacy Lead | Art. 7(3) |
| A.8.3.2 | Consent refresh | I | Consent refresh triggered on material processing changes | | Privacy Lead | Art. 7 |
| **A.8.4** | **Privacy complaints and appeals** | | | | | |
| A.8.4.1 | Privacy complaints handling | I | Privacy complaints procedure implemented and tracked | | DPO | Art. 77 |
| **A.8.5** | **PII processors** | | | | | |
| A.8.5.1 | Contracts with PII processors | I | DPAs in place for all processors per 27701:2025 Annex A.7.2.6 | | Legal / DPO | Art. 28 |

---

## 3. Annex B — PII Processor Controls

*Annex B applies when the organisation acts as a **PII Processor** (processes PII on behalf of a controller).*

| Ref | Control Title | Included / Excluded | Justification | Implementation Status | Owner | Related GDPR Art. |
|-----|--------------|--------------------|--------------|-----------------------|-------|------------------|
| **B.8.1** | **Conditions for collection and processing (processor)** | | | | | |
| B.8.1.1 | Customer agreement / instructions | I | Processing only on documented controller instructions | | Operations / DPO | Art. 28(3) |
| B.8.1.2 | Purposes of PII processing (processor) | I | Processing purposes strictly limited to controller instructions | | DPO | Art. 28(3)(a) |
| B.8.1.3 | Marketing or advertising | E-P / I | [Exclude if no processing for own marketing purposes as a processor] | | DPO | Art. 28 |
| B.8.1.4 | Use of sub-processors | I | Sub-processor approval process and DPAs in place | | Procurement / DPO | Art. 28(4) |
| **B.8.2** | **Privacy obligations** | | | | | |
| B.8.2.1 | Obligations to PII principals (processor) | I | Obligations defined in DPA; assistance provided to controller | | DPO | Art. 28(3) |
| B.8.2.2 | Legitimate purpose for processing | I | Processing only for legitimate controller purposes | | DPO | Art. 28 |
| **B.8.3** | **Privacy by design and privacy by default** | | | | | |
| B.8.3.1 | Privacy by design | I | Privacy by design applied per ISO 31700:2023 approach | | CISO / DPO | Art. 25 |
| B.8.3.2 | Temporary files (processor) | I | Temporary file handling procedures implemented | | IT | Art. 32 |
| B.8.3.3 | Return, transfer or disposal of PII (processor) | I | PII returned or securely deleted at contract end per DPA | | IT / DPO | Art. 28(3)(g) |
| **B.8.4** | **Obligations to PII principals (processor access/correction)** | | | | | |
| B.8.4.1 | Assistance for data subject rights | I | Assistance to controller for all data subject rights requests | | Operations / DPO | Art. 28(3)(e) |
| B.8.4.2 | Notification of requests from PII principals | I | Data subject requests forwarded to controller promptly | | Operations / DPO | Art. 28 |
| B.8.4.3 | Privacy breach notification (processor) | I | Breach notification to controller within agreed timeframe (without undue delay) | | CISO / DPO | Art. 33 |
| **B.8.5** | **Cross-border transfers** | | | | | |
| B.8.5.1 | Basis for cross-border transfer (processor) | I | Transfers only per controller instructions and approved mechanisms | | DPO / Legal | Art. 44 |
| B.8.5.2 | Countries and international organisations | I | Transfer destinations documented and controlled | | DPO | Art. 44–49 |
| B.8.5.3 | Records of cross-border PII transfers (processor) | I | Transfer register maintained | | DPO | Art. 30 |

---

## 4. Summary Statistics

| Category | Total Controls | Included | Excluded (Justified) | Not Applicable | Fully Implemented | Partially Implemented |
|----------|---------------|----------|---------------------|---------------|-------------------|----------------------|
| Annex A — PII Controller | | | | | | |
| Annex B — PII Processor | | | | | | |
| **Total** | | | | | | |

---

## 5. Exclusion Justification Register

Document all excluded controls here:

| Control Ref | Control Title | Exclusion Code | Justification | Approved By | Date |
|-------------|--------------|----------------|--------------|-------------|------|
| | | | | | |

---

## 6. Version History

| Version | Date | Description |
|---------|------|-------------|
| 2.0 | April 2025 | Updated for ISO/IEC 27701:2025 — new controls added: A.7.2.7 (joint controllers), A.7.2.8 (privacy by default), A.7.4 (de-identification), A.7.5 (disclosure controls), TIA for cross-border transfers, ISO 31700 references |
| 1.0 | 2024 | Initial release — ISO/IEC 27701:2019 |

---

*ISO/IEC 27701:2025 PIMS Toolkit | Statement of Applicability | PIMS-SOA-001 | v2.0 | Classification: Confidential*
