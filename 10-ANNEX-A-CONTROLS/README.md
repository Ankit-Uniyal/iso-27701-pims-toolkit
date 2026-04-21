# Annex A — PII Controller Controls (ISO/IEC 27701:2025)

| Field | Detail |
|-------|--------|
| **Document ID** | PIMS-ANNEXA-README-001 |
| **Version** | 2.0 |
| **Date** | April 2025 |
| **Standard** | ISO/IEC 27701:2025 — Annex A |
| **Applies To** | Organisations acting as PII Controllers |
| **Classification** | Public |

---

## Overview

This folder contains reference guides for **Annex A** of ISO/IEC 27701:2025 — the controls applicable to **PII Controllers** (organisations that determine the purposes and means of processing personally identifiable information / personal data).

Annex A extends the controls of ISO/IEC 27002:2022 with additional privacy-specific guidance for PII controllers across two main control families:

- **A.7 — Conditions for Collection and Processing**
- **A.8 — Obligations to PII Principals (Data Subjects)**

---

## What Changed in ISO/IEC 27701:2025 vs. 2019?

The 2025 edition updated and expanded Annex A to align with **ISO 27002:2022** and incorporate new privacy requirements:

| Change Area | 2019 | 2025 |
|------------|------|------|
| Control alignment | ISO 27002:2013 structure | ISO 27002:2022 structure (93-control approach) |
| Privacy by Default | Embedded in A.7 | **New standalone control — A.7.2.8** |
| Joint controllers | Limited | **New control — A.7.2.7** |
| De-identification | Brief reference | **Expanded — new A.7.4 sub-clause** |
| Disclosure controls | Partial | **New A.7.5 (disclosure to third parties, LE requests)** |
| Transfer Impact Assessment | Not explicit | **TIA now required where no adequacy decision** |
| ISO 31700 alignment | Not referenced | **Privacy by Design cross-referenced (A.7.2.8)** |
| Consent lifecycle | Basic | **Extended: collection, recording, withdrawal, refresh** |
| Automated decision-making | Brief | **Explicit control (A.8.2.6)** |

---

## Annex A Control Index (ISO/IEC 27701:2025)

### A.7 — Conditions for Collection and Processing

| Control Ref | Control Title | Key Requirement | GDPR Mapping |
|------------|--------------|----------------|-------------|
| **A.7.2 — Identify and Document Purpose** | | | |
| A.7.2.1 | Identify and document purposes | All processing activities have documented, specified purposes | Art. 5(1)(b) |
| A.7.2.2 | Identify lawful basis | Legal basis identified and documented for each processing activity | Art. 6 |
| A.7.2.3 | Determine consent requirements | When and how consent will be obtained determined | Art. 7 |
| A.7.2.4 | Obtain and record consent | Consent obtained validly; records maintained (consent lifecycle managed) | Art. 7 |
| A.7.2.5 | Privacy impact assessment | DPIA conducted for high-risk processing (per 2025 trigger criteria) | Art. 35 |
| A.7.2.6 | Contracts with PII processors | All processors have DPAs with required privacy obligations | Art. 28 |
| **A.7.2.7** *(NEW 2025)* | **Joint PII controller agreements** | Joint controller responsibilities documented and agreed in writing | Art. 26 |
| **A.7.2.8** *(NEW 2025)* | **Privacy by default** | Maximum privacy settings applied by default; ISO 31700:2023 aligned | Art. 25 |
| **A.7.3 — PII Minimisation** | | | |
| A.7.3.1 | Limit collection | PII limited to what is adequate, relevant and necessary | Art. 5(1)(c) |
| A.7.3.2 | Limit processing to purpose | Processing limited to identified, documented purposes | Art. 5(1)(b) |
| A.7.3.3 | Accuracy | PII kept accurate and up to date | Art. 5(1)(d) |
| A.7.3.4 | Retention and disposal | Retention schedules enforced; secure disposal implemented | Art. 5(1)(e) |
| **A.7.4 — PII De-identification and Deletion** *(Expanded 2025)* | | | |
| A.7.4.1 | De-identification and anonymisation | Pseudonymisation/anonymisation applied where appropriate | Art. 25, 32 |
| A.7.4.2 | Temporary files | Temporary PII files managed and deleted per policy | Art. 32 |
| A.7.4.3 | Return, transfer or disposal | PII returned, transferred or disposed of securely at end of processing | Art. 28(3)(g) |
| **A.7.5 — PII Disclosure Controls** *(NEW 2025)* | | | |
| A.7.5.1 | Basis for PII transfer to third parties | Transfers only with documented lawful basis and controller authorisation | Art. 44 |
| A.7.5.2 | Records of PII disclosure | Third-party disclosure register maintained | Art. 30 |
| A.7.5.3 | Notification of legally-binding disclosure requests | Law enforcement / supervisory authority requests managed with legal review | Art. 23 |
| **A.7.6 — Privacy Notices** | | | |
| A.7.6.1 | Provide privacy notice | Privacy notice provided to all data subjects — accessible, clear, accurate | Art. 13–14 |

### A.8 — Obligations to PII Principals

| Control Ref | Control Title | Key Requirement | GDPR Mapping |
|------------|--------------|----------------|-------------|
| **A.8.1 — Obligations** | | | |
| A.8.1.1 | Determine obligations to PII principals | All data subject rights identified, documented, and procedurally supported | Art. 12–22 |
| **A.8.2 — Access, Correction, Erasure** | | | |
| A.8.2.1 | Right of access | Data Subject Access Request (DSAR) process implemented | Art. 15 |
| A.8.2.2 | Right to rectification | Correction/update procedure implemented | Art. 16 |
| A.8.2.3 | Right to erasure | "Right to be forgotten" procedure with audit trail | Art. 17 |
| A.8.2.4 | Right to data portability | Portable format data export capability implemented | Art. 20 |
| A.8.2.5 | Right to object | Objection handling procedure in place | Art. 21 |
| **A.8.2.6** *(NEW 2025)* | **Automated decision-making and profiling** | Rights regarding solely automated decisions (including profiling) supported | Art. 22 |
| **A.8.3 — Consent Management** | | | |
| A.8.3.1 | Withdraw consent | Consent withdrawal mechanism as easy as giving consent | Art. 7(3) |
| A.8.3.2 | Consent refresh | Consent refreshed when material changes occur to processing | Art. 7 |
| **A.8.4 — Privacy Complaints** | | | |
| A.8.4.1 | Privacy complaints and appeals | Privacy complaints procedure implemented; supervisory authority complaints pathway clear | Art. 77 |
| **A.8.5 — Processors** | | | |
| A.8.5.1 | Contracts with PII processors | DPAs in place covering all A.7.2.6 requirements | Art. 28 |

---

## Control Implementation Summary

| Control Family | Total Controls | Newly Added (2025) | Expanded (2025) |
|---------------|---------------|-------------------|----------------|
| A.7 — Collection & Processing | 19 | 3 (A.7.2.7, A.7.2.8, A.7.5.x) | 2 (A.7.4, A.7.3) |
| A.8 — Obligations to Data Subjects | 11 | 1 (A.8.2.6) | 1 (A.8.3) |
| **Total** | **30** | **4** | **3** |

---

## How to Use This Folder

1. **Review** the control index above to understand all applicable Annex A controls
2. **Reference** the detailed control files (A7 and A8) for implementation guidance
3. **Complete** the Statement of Applicability (SoA) at `05-CLAUSE6-PLANNING/STATEMENT-OF-APPLICABILITY.md`
4. **Evidence** implementation in your operational procedures (`07-CLAUSE8-OPERATION/`)
5. **Monitor** control implementation via the Gap Assessment Checklist (`01-GAP-ASSESSMENT/`)

---

## Related Documents

| Document | Location |
|---------|---------|
| A7-CONDITIONS-FOR-COLLECTION-USE.md | This folder |
| A8-OBLIGATIONS-TO-PII-PRINCIPALS.md | This folder |
| Statement of Applicability | `05-CLAUSE6-PLANNING/STATEMENT-OF-APPLICABILITY.md` |
| DPIA Template | `07-CLAUSE8-OPERATION/DATA-PROTECTION-IMPACT-ASSESSMENT.md` |
| Consent Management Procedure | `07-CLAUSE8-OPERATION/CONSENT-MANAGEMENT-PROCEDURE.md` |
| Data Subject Rights Procedure | `07-CLAUSE8-OPERATION/DATA-SUBJECT-RIGHTS-PROCEDURE.md` |
| Cross-Border Transfer Procedure | `07-CLAUSE8-OPERATION/CROSS-BORDER-TRANSFER-PROCEDURE.md` |
| Privacy by Design Procedure | `07-CLAUSE8-OPERATION/PRIVACY-BY-DESIGN-PROCEDURE.md` |
| GDPR Cross-Reference | `GDPR-MAPPING-CROSS-REFERENCE.md` (root) |

---

## Version History

| Version | Date | Description |
|---------|------|-------------|
| 2.0 | April 2025 | Updated for ISO/IEC 27701:2025 — new controls A.7.2.7 (joint controllers), A.7.2.8 (Privacy by Default), A.7.4 (de-identification), A.7.5 (disclosure), A.8.2.6 (automated decisions), TIA, ISO 31700 reference |
| 1.0 | 2024 | Initial release — ISO/IEC 27701:2019 |

---

*ISO/IEC 27701:2025 PIMS Toolkit | Annex A — PII Controller Controls | PIMS-ANNEXA-README-001 | v2.0 | Classification: Public*
