# NFS Worked Example — Third-Party Privacy Assessment

> **FOR ILLUSTRATIVE PURPOSES ONLY** — NFS is a fictional organisation. All examples are for educational use.

| Field | Detail |
|-------|--------|
| **Document ID** | NFS-PIMS-TPA-001 |
| **Version** | 1.0 |
| **Date** | April 2025 |
| **Standard** | ISO/IEC 27701:2025 — A.7.2.6, B.8.5, GDPR Art. 28 |
| **Classification** | Confidential — Internal Use |

---

## About This Worked Example

This document shows two completed Third-Party Privacy Assessment entries for NFS, demonstrating how to complete `07-CLAUSE8-OPERATION/THIRD-PARTY-PRIVACY-ASSESSMENT.md`. The assessments cover a cloud processor and a marketing technology provider.

---

## Assessment 1 — Salesforce (CRM and Marketing Cloud)

### Part A — Supplier Profile

| Field | Detail |
|-------|--------|
| **Assessment Reference** | NFS-TPA-2025-001 |
| **Supplier Name** | Salesforce Inc. |
| **Service Description** | Customer Relationship Management (Salesforce FSC) and Marketing Automation (Salesforce Marketing Cloud) |
| **Relationship Type** | PII Processor (processes NFS customer PII on NFS's instructions) |
| **PII Categories Processed** | Customer name, address, email, phone, product holdings, transaction history, marketing preferences |
| **Data Subjects Affected** | ~85,000 NFS retail customers |
| **Processing Locations** | EU (Dublin) primary; US (backup replication) |
| **Assessment Date** | February 2025 |
| **Assessment Lead** | DPO with IT Security review |
| **Next Review Date** | February 2026 |

### Part B — Privacy Controls Assessment

| Control Area | Assessment | Evidence Reviewed | Score (0-4) |
|--------------|------------|-------------------|-------------|
| Data Processing Agreement | Full GDPR Art. 28 DPA in place; NFS Standard DPA executed January 2025 | Signed DPA on file | 4 |
| Sub-processor transparency | Salesforce publishes sub-processor list at salesforce.com/content/dam/web/en_us/www/documents/legal/Agreements/data-processing-addendum.pdf; NFS notified of changes | Sub-processor list reviewed | 3 |
| ISO 27001 certification | Salesforce holds ISO 27001:2022 certification (BSI-certified); valid until March 2026 | Certificate ref. BS16085 | 4 |
| ISO 27701 / privacy certification | Salesforce holds ISO 27701:2025 certification for CRM services | Certificate ref. BS27701-2025-SF | 4 |
| Cross-border transfer safeguards | EU-US DPF participant; UK IDTA executed; EU SCCs (2021 modules) in DPA | DPA clauses reviewed | 4 |
| Transfer Impact Assessment | NFS TIA completed (NFS-TIA-001) — assessed US surveillance law (FISA 702, EO 14086 safeguards) | NFS-TIA-001 on file | 3 |
| Data deletion/return | DPA clause 12 — data deleted within 30 days of contract termination; deletion certificate provided | DPA reviewed | 4 |
| Breach notification | DPA clause 8 — Salesforce notifies NFS within 48 hours of confirmed breach | DPA reviewed | 4 |
| Audit rights | DPA clause 14 — NFS has right to audit or appoint third-party auditor; questionnaire right exercised annually | DPA reviewed | 3 |
| Data minimisation | NFS has configured field-level restrictions — only fields needed for CRM/Marketing are synced | Configuration review | 3 |

**Overall Score: 36/40 (90%) — APPROVED**

### Part C — Decision and Actions

| Field | Detail |
|-------|--------|
| **Assessment Outcome** | Approved — high-trust processor with strong certifications and contractual protections |
| **Risk Level** | Low — residual risk accepted |
| **DPA Status** | Executed January 2025 — valid |
| **Outstanding Actions** | 1. Request updated sub-processor list Q3 2025. 2. Schedule annual questionnaire June 2025. |
| **DPO Sign-Off** | Signed — February 2025 |

---

## Assessment 2 — Equifax Ltd (Credit Reference Agency)

### Part A — Supplier Profile

| Field | Detail |
|-------|--------|
| **Assessment Reference** | NFS-TPA-2025-002 |
| **Supplier Name** | Equifax Ltd (UK entity) |
| **Service Description** | Credit decisioning platform for loan and mortgage applications; identity verification; fraud screening |
| **Relationship Type** | Joint Controller and Processor (dual role — Equifax processes PII for NFS decisions AND uses data for its own credit reference purposes) |
| **PII Categories Processed** | Customer name, DOB, address history, NI number, financial history, credit score, fraud flags |
| **Special Category PII** | Potentially — financial vulnerability inferences may engage sensitive category rules |
| **Data Subjects Affected** | ~12,000 NFS loan applicants per year |
| **Processing Locations** | UK (primary); ROI (backup) — both adequate jurisdictions |
| **Assessment Date** | January 2025 |
| **Assessment Lead** | DPO, Retail Lending Head, Legal |
| **Next Review Date** | January 2026 |

### Part B — Privacy Controls Assessment

| Control Area | Assessment | Evidence Reviewed | Score (0-4) |
|--------------|------------|-------------------|-------------|
| Data Processing Agreement | Full GDPR Art. 28 DPA and Joint Controller Agreement (Art. 26) executed | DPA + JCA on file | 4 |
| ICO registration | Equifax Ltd registered with ICO (ZA068705) | ICO register checked | 4 |
| ISO 27001 certification | Equifax UK holds ISO 27001:2022 (LRQA-certified) | Certificate reviewed | 4 |
| Automated decisioning disclosure | Equifax-powered decisioning disclosed in NFS Privacy Notice and pre-application notice; Art. 22 rights upheld | Privacy Notice reviewed | 4 |
| Legitimate interests for credit referencing | Equifax's own processing based on legitimate interests (credit reference purpose) — documented in Equifax PIMS | Equifax Privacy Policy reviewed | 3 |
| Data accuracy obligations | Equifax maintains data accuracy procedures; NFS provides dispute referrals | DPA clause reviewed | 3 |
| Security controls | SOC 2 Type II report provided; penetration test summary shared (annual) | SOC 2 report Q4 2024 | 3 |
| Breach notification | 24-hour notification obligation under DPA clause 9 | DPA reviewed | 4 |
| Subject rights passthrough | Equifax operates ICO-approved dispute resolution for credit file corrections | Procedure documented | 4 |

**Overall Score: 33/36 (92%) — APPROVED (Joint Controller provisions in place)**

### Part C — Decision and Actions

| Field | Detail |
|-------|--------|
| **Assessment Outcome** | Approved — regulated entity, strong certifications, full JCA executed |
| **Risk Level** | Low-Medium — dual controller role requires ongoing monitoring |
| **DPIA Cross-Reference** | NFS loan decisioning DPIA (NFS-DPIA-2025-001) covers this relationship |
| **Outstanding Actions** | 1. Annual SOC 2 report request due January 2026. 2. Review Equifax sub-processor list Q2 2025. |
| **DPO Sign-Off** | Signed — January 2025 |

---

## Third-Party Register Summary

| Ref | Supplier | Type | Score | Status | Next Review |
|-----|----------|------|-------|--------|-------------|
| NFS-TPA-2025-001 | Salesforce Inc. | Processor | 90% | Approved | Feb 2026 |
| NFS-TPA-2025-002 | Equifax Ltd | Joint Controller + Processor | 92% | Approved | Jan 2026 |

---

## Cross-References

| Document | Reference |
|----------|-----------|
| Third-Party Assessment Procedure | `07-CLAUSE8-OPERATION/THIRD-PARTY-PRIVACY-ASSESSMENT.md` |
| Supplier Privacy Questionnaire | `SUPPLIER-PRIVACY-QUESTIONNAIRE.md` |
| DPA Template | `DPA-TEMPLATE.md` |
| DPIA worked example | `12-WORKED-EXAMPLE/NFS-DPIA-ENTRY.md` |
| Cross-Border Transfer Procedure | `07-CLAUSE8-OPERATION/CROSS-BORDER-TRANSFER-PROCEDURE.md` |

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| 1.0 | April 2025 | Initial release — 2 NFS third-party assessments (Salesforce, Equifax) |

---

*ISO/IEC 27701:2025 PIMS Toolkit | NFS Third-Party Privacy Assessment | NFS-PIMS-TPA-001*
