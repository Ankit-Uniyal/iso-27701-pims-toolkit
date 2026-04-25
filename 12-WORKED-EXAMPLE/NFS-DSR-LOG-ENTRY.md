# NFS Worked Example — Data Subject Rights Log Entries

> **FOR ILLUSTRATIVE PURPOSES ONLY** — Nexus Financial Services Ltd (NFS) is a fictional organisation.

| Field | Detail |
|-------|--------|
| **Document ID** | NFS-PIMS-DSR-001 |
| **Version** | 1.0 |
| **Date** | April 2025 |
| **Standard** | ISO/IEC 27701:2025 — A.7.6, A.7.7, GDPR Arts. 15-22 |
| **Classification** | Confidential — Internal Use |

---

## About This Worked Example

This document shows four completed Data Subject Rights (DSR) log entries for NFS, demonstrating how to maintain the DSR log in `07-CLAUSE8-OPERATION/DATA-SUBJECT-RIGHTS-PROCEDURE.md`. Each entry covers a different right and outcome.

---

## DSR Log Entry 1 — Subject Access Request (SAR)

| Log Field | NFS Entry |
|-----------|-----------|
| **DSR Reference** | NFS-DSR-2025-0047 |
| **Right Exercised** | Right of Access (GDPR Art. 15) |
| **Date Received** | 3 March 2025 |
| **Receipt Channel** | Email to dpo@nexusfinancial.co.uk |
| **Data Subject Category** | Retail customer (mortgage account holder) |
| **Identity Verified?** | Yes — via online banking portal two-factor authentication on 4 March 2025 |
| **Request Description** | All personal data held, specifically relating to mortgage application and communications. |
| **Departments Involved** | Mortgage Operations, IT, Legal, DPO |
| **Third-Party Data?** | Yes — one record includes third-party guarantor data. Redacted per DPA 2018 s.40. |
| **DPO Reviewed?** | Yes — signed off 18 March 2025 |
| **Response Sent** | 20 March 2025 (Day 17 of 30-day limit) |
| **Outcome** | Full disclosure. 47 pages provided via encrypted portal link. Third-party data redacted. |
| **Exemptions Applied** | Partial — third-party data redacted under DPA 2018 s.40 |
| **Closed** | Yes — 20 March 2025 |

---

## DSR Log Entry 2 — Right to Erasure

| Log Field | NFS Entry |
|-----------|-----------|
| **DSR Reference** | NFS-DSR-2025-0061 |
| **Right Exercised** | Right to Erasure (GDPR Art. 17) |
| **Date Received** | 15 March 2025 |
| **Data Subject Category** | Former mortgage customer (account closed October 2024) |
| **Request Description** | Deletion of all personal data following account closure. No further communications. |
| **Assessment** | Mortgage records must be retained 6 years post-closure (FCA SYSC 9.1, AML Regs 2017). Full erasure cannot be completed until October 2030. Marketing data erased immediately. |
| **Response Sent** | 4 April 2025 (Day 20) |
| **Outcome** | Partial erasure. Marketing data erased 28 March 2025. Core records placed under suppression flag. Full erasure scheduled October 2030. |
| **Exemptions Applied** | Art. 17(3)(b) — legal obligation to retain financial records |
| **Closed** | Yes — 4 April 2025 |

---

## DSR Log Entry 3 — Right to Rectification

| Log Field | NFS Entry |
|-----------|-----------|
| **DSR Reference** | NFS-DSR-2025-0078 |
| **Right Exercised** | Right to Rectification (GDPR Art. 16) |
| **Date Received** | 28 March 2025 |
| **Data Subject Category** | Business banking customer |
| **Request Description** | Registered business address incorrect — shows 2022 address. Current: 14 Station Road, Manchester M1 2AB. |
| **Assessment** | Address confirmed incorrect vs. Companies House record. Simple factual correction. |
| **Correction Made** | Address updated in NFS CBS and Salesforce CRM on 1 April 2025. AML re-screening passed. |
| **Response Sent** | 2 April 2025 (Day 5) |
| **Outcome** | Rectification completed. Confirmation sent to both old and new addresses. |
| **Closed** | Yes — 2 April 2025 |

---

## DSR Log Entry 4 — Objection to Automated Processing

| Log Field | NFS Entry |
|-----------|-----------|
| **DSR Reference** | NFS-DSR-2025-0091 |
| **Right Exercised** | Right to Object to Automated Decision-Making (GDPR Art. 22) |
| **Date Received** | 8 April 2025 |
| **Data Subject Category** | Loan applicant |
| **Request Description** | Automated loan decline received 7 April 2025. Subject objects and requests human review. |
| **Assessment** | Automated decisioning disclosed in Privacy Notice and pre-application fair processing notice. Subject has right to human review under Art. 22(3). NFS DPIA (NFS-DPIA-2025-001) confirms human review fallback exists. |
| **Escalated To** | Senior Lending Manager on 9 April 2025 |
| **Human Review Outcome** | Original decision upheld — debt-to-income ratio exceeds NFS lending policy threshold. Rationale documented. |
| **Response Sent** | 14 April 2025 (Day 6) |
| **Outcome** | Human review completed; decision upheld with full rationale. Subject informed of FCA/ICO complaint routes. |
| **Closed** | Yes — 14 April 2025 |

---

## DSR Log Summary Table

| Ref | Right | Received | Closed | Outcome | Days |
|-----|-------|----------|--------|---------|------|
| NFS-DSR-2025-0047 | Access (SAR) | 3 Mar 2025 | 20 Mar 2025 | Full disclosure | 17 |
| NFS-DSR-2025-0061 | Erasure | 15 Mar 2025 | 4 Apr 2025 | Partial — legal retention exemption | 20 |
| NFS-DSR-2025-0078 | Rectification | 28 Mar 2025 | 2 Apr 2025 | Completed | 5 |
| NFS-DSR-2025-0091 | Art. 22 Objection | 8 Apr 2025 | 14 Apr 2025 | Human review — decision upheld | 6 |

**Q1 2025 KPI:** All 4 DSRs closed within 30-day statutory limit. Average: 12 days.

---

## Cross-References

| Document | Reference |
|----------|-----------|
| DSR Procedure | `07-CLAUSE8-OPERATION/DATA-SUBJECT-RIGHTS-PROCEDURE.md` |
| DSR Form Template | `DATA-SUBJECT-REQUEST-FORM-TEMPLATE.md` |
| DPIA worked example | `12-WORKED-EXAMPLE/NFS-DPIA-ENTRY.md` |
| Privacy KPI Dashboard | `08-CLAUSE9-PERFORMANCE/PRIVACY-KPI-METRICS-DASHBOARD.md` |

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| 1.0 | April 2025 | Initial release — 4 NFS DSR log entries |

---

*ISO/IEC 27701:2025 PIMS Toolkit | NFS DSR Log Entries | NFS-PIMS-DSR-001*
