# NFS Worked Example — ROPA / PII Processing Inventory Entry

> **FOR ILLUSTRATIVE PURPOSES ONLY** — Nexus Financial Services Ltd (NFS) is a fictional organisation. All examples are for educational use to demonstrate ISO/IEC 27701:2025 PIMS templates. Do not use real personal data.

| Field | Detail |
|-------|--------|
| **Document ID** | NFS-PIMS-OPS-004 |
| **Version** | 1.0 |
| **Date** | April 2025 |
| **Standard** | ISO/IEC 27701:2025 — Clause A.7.2.1, A.7.2.2, GDPR Art. 30 |
| **Classification** | Confidential — Internal Use |

---

## About This Worked Example

This document shows three completed ROPA (Record of Processing Activities) / PII Processing Inventory entries for NFS, demonstrating how to complete `03-CLAUSE4-CONTEXT/PII-PROCESSING-INVENTORY.md` and `07-CLAUSE8-OPERATION/PII-PROCESSING-ACTIVITY-PROCEDURE.md`.

---

## ROPA Entry 1 — Customer KYC and Onboarding

| ROPA Field | NFS Entry |
|------------|-----------|
| **Activity ID** | NFS-PROC-001 |
| **Activity Name** | Customer Know-Your-Customer (KYC) and Account Onboarding |
| **Description** | Collection and verification of customer identity, financial history, and risk profile during account opening for retail banking and lending products. |
| **PIMS Role** | PII Controller |
| **Data Controller** | Nexus Financial Services Ltd, 45 Canary Wharf, London E14 5AB |
| **DPO Contact** | dpo@nexusfinancial.co.uk |
| **Categories of PII** | Full name, date of birth, national insurance number, passport/driving licence number, home address (historical), email address, phone number, employment status, income, credit history, politically exposed person (PEP) status |
| **Special Category PII** | None routinely; PEP status may engage Art. 9 for biometric verification in enhanced due diligence |
| **Data Subjects** | Retail banking customers (prospective and existing) |
| **Estimated Volume** | ~12,000 new customers per year; ~85,000 total records |
| **Purpose** | Legal obligation (AML/KYC compliance); Contract performance (account opening) |
| **Lawful Basis** | Art. 6(1)(b) Contract; Art. 6(1)(c) Legal obligation (FCA SYSC, Money Laundering Regs 2017) |
| **Retention Period** | 6 years from account closure (Money Laundering Regulations 2017 Reg. 40) |
| **Recipients / Disclosures** | Experian (credit reference agency — DPA in place); HMRC (legal obligation); FCA (regulatory reporting); Callcredit (fraud screening — DPA in place) |
| **Cross-Border Transfers** | None. All processors UK/EEA-based. |
| **DPIA Required?** | Yes — automated credit decisioning triggers DPIA (GDPR Art. 35(3)(a)); see NFS-DPIA-ENTRY.md |
| **System/Asset** | Salesforce FSC (CRM), Equifax Decisioning Platform, NFS Core Banking System (CBS) |
| **Owner** | Head of Retail Banking Operations |
| **DPO Review Date** | April 2026 |

---

## ROPA Entry 2 — Employee HR Processing

| ROPA Field | NFS Entry |
|------------|-----------|
| **Activity ID** | NFS-PROC-002 |
| **Activity Name** | Employee Recruitment, Payroll, and HR Management |
| **Description** | Processing employee and contractor personal data for recruitment, onboarding, payroll, performance management, absence tracking, benefits administration, and offboarding. |
| **PIMS Role** | PII Controller |
| **Data Controller** | Nexus Financial Services Ltd |
| **Categories of PII** | Full name, address, NI number, date of birth, bank account details (payroll), salary, performance reviews, disciplinary records, absence/sickness records, CV and employment history, emergency contact details |
| **Special Category PII** | Health data (sickness absence, occupational health referrals); trade union membership (if applicable) |
| **Data Subjects** | Employees (permanent and fixed-term), contractors, job applicants |
| **Estimated Volume** | ~1,400 employees; ~200 contractors; ~3,000 applicants per year |
| **Purpose** | Employment contract administration, payroll, statutory reporting, performance management, legal compliance |
| **Lawful Basis** | Art. 6(1)(b) Contract; Art. 6(1)(c) Legal obligation (PAYE, NI, FCA fit-and-proper); Art. 6(1)(f) Legitimate interests (performance management) |
| **Special Category Basis** | Art. 9(2)(b) Employment law obligations (health data); Art. 9(2)(a) Consent (where applicable) |
| **Retention Period** | 6 years post-employment for payroll records (HMRC); 7 years for disciplinary; 2 years for unsuccessful applicants |
| **Recipients / Disclosures** | ADP (payroll processor — DPA in place); Vitality Health (occupational health — DPA in place); HMRC, DWP (statutory); pension providers |
| **Cross-Border Transfers** | ADP processes some data in Ireland (adequate country); standard SCCs in place for US-based analytics module |
| **DPIA Required?** | No — processing is standard HR; sickness data reviewed annually by DPO |
| **System/Asset** | Workday HCM, ADP Payroll, MS SharePoint (HR files) |
| **Owner** | Head of Human Resources |
| **DPO Review Date** | April 2026 |

---

## ROPA Entry 3 — Marketing Analytics and Profiling

| ROPA Field | NFS Entry |
|------------|-----------|
| **Activity ID** | NFS-PROC-003 |
| **Activity Name** | Customer Behavioural Analytics and Marketing Profiling |
| **Description** | Analysis of customer transactional behaviour, product usage, and web/app interactions to create customer segments and personalised marketing communications. |
| **PIMS Role** | PII Controller |
| **Data Controller** | Nexus Financial Services Ltd |
| **Categories of PII** | Customer ID, transaction history, product holdings, digital behaviour (app/web clicks, session data), inferred preferences and risk appetite |
| **Special Category PII** | None directly; inferences may indirectly reveal financial vulnerability (DPO to review annually) |
| **Data Subjects** | Existing retail customers who have not opted out of marketing |
| **Estimated Volume** | ~55,000 active customer profiles |
| **Purpose** | Personalised product recommendations; targeted marketing campaigns; customer retention analytics |
| **Lawful Basis** | Art. 6(1)(a) Consent (marketing communications); Art. 6(1)(f) Legitimate interests (analytics — LIA on file NFS-LIA-003) |
| **Consent Record** | Managed via OneTrust consent platform; consent withdrawal honoured within 72 hours |
| **Retention Period** | Profile data retained for 3 years from last interaction; deleted on opt-out within 30 days |
| **Recipients / Disclosures** | Salesforce Marketing Cloud (processor — DPA in place); Google Analytics 4 (pseudonymised data only — no direct identifiers transferred) |
| **Cross-Border Transfers** | Salesforce US data centre — UK IDTA and EU SCCs in place; Transfer Impact Assessment completed (NFS-TIA-003) |
| **DPIA Required?** | Yes — profiling at scale triggers DPIA (GDPR Art. 35(3)(a)); DPIA completed March 2025 |
| **System/Asset** | Salesforce Marketing Cloud, Adobe Analytics, NFS Data Warehouse |
| **Owner** | Head of Marketing / Chief Data Officer |
| **DPO Review Date** | October 2025 (6-monthly review due to profiling risk) |

---

## Cross-References

| Document | Reference |
|----------|-----------|
| PII Processing Inventory template | `03-CLAUSE4-CONTEXT/PII-PROCESSING-INVENTORY.md` |
| PII Processing Activity Procedure | `07-CLAUSE8-OPERATION/PII-PROCESSING-ACTIVITY-PROCEDURE.md` |
| DPIA worked example | `12-WORKED-EXAMPLE/NFS-DPIA-ENTRY.md` |
| Consent management | `07-CLAUSE8-OPERATION/CONSENT-MANAGEMENT-PROCEDURE.md` |
| Cross-border transfers | `07-CLAUSE8-OPERATION/CROSS-BORDER-TRANSFER-PROCEDURE.md` |
| SoA reference | `12-WORKED-EXAMPLE/NFS-SOA-EXCERPT.md` |

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| 1.0 | April 2025 | Initial release — 3 NFS ROPA entries (KYC, HR, Marketing) |

---

*ISO/IEC 27701:2025 PIMS Toolkit | NFS ROPA Entries | NFS-PIMS-OPS-004*
