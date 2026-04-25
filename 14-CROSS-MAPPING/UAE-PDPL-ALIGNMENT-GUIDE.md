# UAE Personal Data Protection Law (PDPL) Alignment Guide

| Field | Detail |
|---|---|
| **Document ID** | PIMS-SUP-011 |
| **Version** | 2.0 |
| **Date** | April 2025 |
| **Owner** | Data Protection Officer |
| **Classification** | Public |
| **Review Date** | April 2026 |
| **Standard** | ISO/IEC 27701:2025 aligned |

> **IMPORTANT DISCLAIMER:** This guide is for informational purposes only and does not constitute legal advice. The UAE PDPL (Federal Decree-Law No. 45 of 2021) and its executive regulations are subject to ongoing regulatory guidance from the UAE Data Office. Always consult qualified UAE legal counsel for compliance advice.

---

## 1. Overview of UAE PDPL

The UAE Federal Decree-Law No. 45 of 2021 on the Protection of Personal Data (UAE PDPL) entered into force in January 2022, with executive regulations issued in 2023. It is the UAE first comprehensive federal personal data protection law.

| Field | Detail |
|---|---|
| **Law** | Federal Decree-Law No. 45 of 2021 |
| **Regulator** | UAE Data Office |
| **Scope** | Personal data of individuals in the UAE processed by organisations in the UAE |
| **Territorial Exclusions** | DIFC (separate DIFC DP Law 2020); ADGM (separate ADGM DPR 2021) |

---

## 2. UAE PDPL vs. GDPR - Key Similarities and Differences

| Aspect | UAE PDPL | GDPR | PIMS Toolkit Document |
|---|---|---|---|
| Legal bases | Consent, contract, legal obligation, vital interests, public interest, legitimate interests | Same six categories | PII-PROCESSING-INVENTORY.md |
| Consent requirements | Explicit, informed, withdrawable; no pre-ticked boxes | Same standards | CONSENT-MANAGEMENT-PROCEDURE.md |
| Privacy notices | Required at point of collection | Same | PRIVACY-NOTICE-TEMPLATE.md |
| Data subject rights | Access, correction, erasure, portability, objection | Very similar | DATA-SUBJECT-RIGHTS-PROCEDURE.md |
| Privacy Impact Assessment | Required for high-risk processing | DPIA (Art. 35) | DATA-PROTECTION-IMPACT-ASSESSMENT.md |
| Personal Data Officer | Required for certain organisations | DPO required in certain cases | DPO-TERMS-OF-REFERENCE.md |
| Breach notification | Notify UAE Data Office and individuals | 72 hours to SA; individuals if high risk | PRIVACY-BREACH-RESPONSE-PROCEDURE.md |
| International transfers | Adequate countries; safeguards otherwise | GDPR Chapter V | CROSS-BORDER-TRANSFER-PROCEDURE.md |
| Data retention | No longer than necessary | Same principle | DATA-RETENTION-AND-DISPOSAL-POLICY.md |
| Special categories | Health, biometric, genetic, racial/ethnic, criminal | Similar | DATA-PROTECTION-IMPACT-ASSESSMENT.md |
| Fines | Up to AED 5 million (escalating for serious violations) | Up to 4% global turnover or EUR 20M | - |
| Processing register | Required | Art. 30 ROPA | PII-PROCESSING-INVENTORY.md |

---

## 3. UAE PDPL Requirements Mapped to ISO 27701:2025 Controls

All control references use ISO/IEC 27701:2025 numbering.

| UAE PDPL Requirement | ISO 27701:2025 Clause / Control | PIMS Toolkit Document |
|---|---|---|
| Personal Data Officer (PDO) appointment | Clause 5.3 (roles and responsibilities) | DPO-TERMS-OF-REFERENCE.md |
| Register of processing activities | Clause 4.4; A.7.5.2 (records of PII disclosures) | PII-PROCESSING-INVENTORY.md |
| Privacy notice / transparency notice | A.7.6.1 (provide privacy notice to PII principals) | PRIVACY-NOTICE-TEMPLATE.md |
| Legal basis documentation | A.7.2.2 (identify lawful basis for processing) | PII-PROCESSING-INVENTORY.md |
| Purpose documentation | A.7.2.1 (identify and document purposes of processing) | PII-PROCESSING-INVENTORY.md |
| Consent - obtain and record | A.7.2.3; A.7.2.4 (consent determination and recording) | CONSENT-MANAGEMENT-PROCEDURE.md |
| Consent withdrawal | A.8.3.1 (withdraw consent) | CONSENT-MANAGEMENT-PROCEDURE.md |
| Consent refresh on material change | A.8.3.2 (consent refresh - NEW in ISO 27701:2025) | CONSENT-MANAGEMENT-PROCEDURE.md |
| Right of access (DSAR) | A.8.2.1 (right of access) | DATA-SUBJECT-RIGHTS-PROCEDURE.md |
| Right to correction / rectification | A.8.2.2 (right to rectification) | DATA-SUBJECT-RIGHTS-PROCEDURE.md |
| Right to erasure | A.8.2.3 (right to erasure) | DATA-SUBJECT-RIGHTS-PROCEDURE.md |
| Right to data portability | A.8.2.4 (right to data portability) | DATA-SUBJECT-RIGHTS-PROCEDURE.md |
| Right to object | A.8.2.5 (right to object) | DATA-SUBJECT-RIGHTS-PROCEDURE.md |
| Privacy Impact Assessment | A.7.2.5 (DPIA - enhanced 2025 trigger criteria) | DATA-PROTECTION-IMPACT-ASSESSMENT.md |
| Privacy by Design and Default | A.7.2.8 (privacy by default - standalone 2025 control); B.8.3.1 | PRIVACY-BY-DESIGN-PROCEDURE.md |
| Data minimisation | A.7.3.1 (limit collection to what is necessary) | PII-PROCESSING-INVENTORY.md |
| Purpose limitation | A.7.3.2 (limit processing to identified purposes) | PII-PROCESSING-INVENTORY.md |
| Accuracy of personal data | A.7.3.3 (accuracy of PII) | DATA-SUBJECT-RIGHTS-PROCEDURE.md |
| Data retention and deletion | A.7.3.4 (retention and disposal) | DATA-RETENTION-AND-DISPOSAL-POLICY.md |
| De-identification and anonymisation | A.7.4.1 (de-identification and anonymisation) | PRIVACY-BY-DESIGN-PROCEDURE.md |
| Temporary files management | A.7.4.2 (temporary files) | DATA-RETENTION-AND-DISPOSAL-POLICY.md |
| Return/transfer/disposal at end of processing | A.7.4.3 (return, transfer or disposal of PII) | DATA-RETENTION-AND-DISPOSAL-POLICY.md |
| Basis for transfer to third parties | A.7.5.1 (basis for PII transfer to third parties - includes TIA) | CROSS-BORDER-TRANSFER-PROCEDURE.md |
| Records of disclosures to third parties | A.7.5.2 (records of PII disclosure to third parties) | PII-PROCESSING-INVENTORY.md |
| Legally binding disclosure requests | A.7.5.3 (notification of legally-binding disclosure requests) | PRIVACY-BREACH-RESPONSE-PROCEDURE.md |
| Data breach notification | Clause 8.5 (breach response procedure) | PRIVACY-BREACH-RESPONSE-PROCEDURE.md |
| International transfer safeguards | A.7.5.1; B.8.5.1 (cross-border transfer controls) | CROSS-BORDER-TRANSFER-PROCEDURE.md |
| Transfer Impact Assessment | A.7.5.1 (TIA requirement - NEW in ISO 27701:2025) | CROSS-BORDER-TRANSFER-PROCEDURE.md |
| Joint controller arrangements | A.7.2.7 (joint PII controller arrangements - NEW in ISO 27701:2025) | DPA-TEMPLATE.md |
| Data processor agreements | A.7.2.6 (contracts with PII processors); A.8.5.1 | DPA-TEMPLATE.md |
| Sub-processor controls | B.8.1.4 (sub-processor engagement) | DPA-TEMPLATE.md |
| Special category data protections | Clause 6.1 (risk assessment); A.7.2.5 (DPIA mandatory) | DATA-PROTECTION-IMPACT-ASSESSMENT.md |
| Automated decision-making safeguards | A.8.2.6 (automated decision-making and profiling - NEW in ISO 27701:2025) | DATA-SUBJECT-RIGHTS-PROCEDURE.md |
| Privacy complaints handling | A.8.4.1 (privacy complaints and appeals) | DATA-SUBJECT-RIGHTS-PROCEDURE.md |

---

## 4. UAE PDPL Compliance Checklist

| # | Requirement | Status | Toolkit Document |
|---|---|---|---|
| 1 | Personal Data Officer (PDO) appointed | Not Started / In Progress / Complete | DPO-TERMS-OF-REFERENCE.md |
| 2 | PDO registered with UAE Data Office | Not Started / In Progress / Complete | DPO-TERMS-OF-REFERENCE.md |
| 3 | Privacy notice published in Arabic and English | Not Started / In Progress / Complete | PRIVACY-NOTICE-TEMPLATE.md |
| 4 | Register of processing activities maintained | Not Started / In Progress / Complete | PII-PROCESSING-INVENTORY.md |
| 5 | Legal basis documented for all processing | Not Started / In Progress / Complete | PII-PROCESSING-INVENTORY.md |
| 6 | Consent obtained and recorded for marketing | Not Started / In Progress / Complete | CONSENT-MANAGEMENT-PROCEDURE.md |
| 7 | Consent withdrawal mechanism in place | Not Started / In Progress / Complete | CONSENT-MANAGEMENT-PROCEDURE.md |
| 8 | Consent refresh process for material changes (A.8.3.2) | Not Started / In Progress / Complete | CONSENT-MANAGEMENT-PROCEDURE.md |
| 9 | Data Subject Request mechanism in place | Not Started / In Progress / Complete | DATA-SUBJECT-RIGHTS-PROCEDURE.md |
| 10 | DSR responses within 30 days | Not Started / In Progress / Complete | DATA-SUBJECT-RIGHTS-PROCEDURE.md |
| 11 | Privacy Impact Assessment for high-risk processing | Not Started / In Progress / Complete | DATA-PROTECTION-IMPACT-ASSESSMENT.md |
| 12 | Breach notification procedure in place | Not Started / In Progress / Complete | PRIVACY-BREACH-RESPONSE-PROCEDURE.md |
| 13 | Data Processing Agreements with all processors | Not Started / In Progress / Complete | DPA-TEMPLATE.md |
| 14 | Cross-border transfer assessment conducted | Not Started / In Progress / Complete | CROSS-BORDER-TRANSFER-PROCEDURE.md |
| 15 | Transfer Impact Assessment (TIA) where no adequacy | Not Started / In Progress / Complete | CROSS-BORDER-TRANSFER-PROCEDURE.md |
| 16 | Special category data protections implemented | Not Started / In Progress / Complete | DATA-PROTECTION-IMPACT-ASSESSMENT.md |
| 17 | Retention and deletion schedule established | Not Started / In Progress / Complete | DATA-RETENTION-AND-DISPOSAL-POLICY.md |
| 18 | Automated decision-making safeguards in place (A.8.2.6) | Not Started / In Progress / Complete | DATA-SUBJECT-RIGHTS-PROCEDURE.md |
| 19 | Joint Controller Agreements where applicable (A.7.2.7) | Not Started / In Progress / Complete | DPA-TEMPLATE.md |
| 20 | Privacy by Design embedded in systems (A.7.2.8) | Not Started / In Progress / Complete | PRIVACY-BY-DESIGN-PROCEDURE.md |

---

## 5. DIFC and ADGM Note

Organisations in the **Dubai International Financial Centre (DIFC)** are subject to the **DIFC Data Protection Law 2020** (DIFC Law No. 5 of 2020) - closely modelled on GDPR. Key differences: regulator is DIFC Commissioner of Data Protection (not UAE Data Office); DIFC Data Protection Register requirements apply.

Organisations in **Abu Dhabi Global Market (ADGM)** are subject to the **ADGM Data Protection Regulations 2021** - also closely GDPR-aligned.

---

## 6. Practical Guidance for UAE Organisations

1. Use all toolkit documents as the foundation - substantially compatible with UAE PDPL
2. Ensure privacy notices are available in **Arabic** for UAE-resident data subjects
3. Register your Personal Data Officer with the UAE Data Office when required
4. Check UAE Data Office guidance for sector-specific regulations (healthcare, financial services)
5. Monitor the UAE Data Office website for implementing regulations and adequacy decisions
6. For DIFC and ADGM entities, consult the relevant free zone regulator for specific requirements

---

## 7. Version History

| Version | Date | Description |
|---|---|---|
| 2.0 | April 2025 | Updated to ISO/IEC 27701:2025 - all control references corrected to 2025 numbering; new 2025 controls added (A.7.2.7 joint controllers, A.7.2.8 privacy by default, A.7.4 de-identification series, A.7.5 disclosure controls, A.7.6.1 privacy notice, A.8.2.6 automated decisions, A.8.3.2 consent refresh, TIA); compliance checklist expanded to 20 items |
| 1.0 | 2025-01-01 | Initial release - ISO/IEC 27701:2019 (incorrect control numbering - superseded by v2.0) |

---

*ISO/IEC 27701:2025 PIMS Toolkit | UAE PDPL Alignment Guide | PIMS-SUP-011 | v2.0 | Classification: Public*
