# PII Processing Inventory (Record of Processing Activities — ROPA)

| Field | Detail |
|-------|--------|
| **Document ID** | PIMS-CTX-005 |
| **Version** | 2.0 |
| **Date** | April 2025 |
| **Owner** | Data Protection Officer |
| **Classification** | Confidential — Restricted |
| **Review Date** | Annual or upon new processing activity |

---

## Purpose

This document serves as [Organisation Name]'s Record of Processing Activities (ROPA), documenting all PII processing activities as required by ISO/IEC 27701:2025 Clause 4 (extension) and GDPR Article 30. It enables the organisation to maintain transparency, demonstrate compliance, and assess privacy risks.

---

## Instructions

For each processing activity, complete all fields below. Add a new entry for each distinct processing purpose. Review and update when any new processing activity is introduced, modified, or discontinued.

---

## Processing Activity Register

### Entry 1: Customer Relationship Management

| Field | Detail |
|-------|--------|
| **Activity ID** | ROPA-001 |
| **Processing Activity** | Customer data management and CRM |
| **Purpose** | Managing customer accounts, orders, and communications |
| **Controller / Processor Role** | PII Controller |
| **Lawful Basis (GDPR Art. 6)** | Contract (Art. 6(1)(b)); Legitimate interests (Art. 6(1)(f)) |
| **Special Category Data?** | No |
| **PII Categories** | Name, email, phone, postal address, purchase history |
| **Data Subjects** | Customers / clients |
| **Recipients** | CRM platform vendor (processor); Customer support team |
| **Third Country Transfers** | [Yes/No] — [Transfer mechanism if Yes, e.g. SCCs] |
| **Retention Period** | Duration of contract + 7 years (legal requirement) |
| **Security Measures** | Encryption at rest and in transit; access controls; audit logs |
| **DPIA Required?** | No (low-risk standard processing) |
| **ISO 27701:2025 Controls** | A.7.2.1, A.7.2.2, A.7.2.3, A.7.3.2 |
| **Review Date** | Annual |

---

### Entry 2: Employee HR Processing

| Field | Detail |
|-------|--------|
| **Activity ID** | ROPA-002 |
| **Processing Activity** | Human Resources and payroll administration |
| **Purpose** | Employment management, payroll, benefits, performance |
| **Controller / Processor Role** | PII Controller |
| **Lawful Basis (GDPR Art. 6)** | Contract (Art. 6(1)(b)); Legal obligation (Art. 6(1)(c)) |
| **Special Category Data?** | Yes — health data (for sick leave/disability); Art. 9(2)(b) |
| **PII Categories** | Name, NI/ID number, bank details, salary, health records, performance data |
| **Data Subjects** | Employees, contractors |
| **Recipients** | Payroll processor; HMRC/tax authority; pension provider |
| **Third Country Transfers** | [Yes/No] — [Transfer mechanism if Yes] |
| **Retention Period** | Employment duration + 6 years |
| **Security Measures** | HR system access controls; encryption; segregation of duties |
| **DPIA Required?** | Assess if special category data volume is high |
| **ISO 27701:2025 Controls** | A.7.2.1, A.7.2.4, A.7.3.2 |
| **Review Date** | Annual |

---

### Entry 3: Marketing and Direct Communications

| Field | Detail |
|-------|--------|
| **Activity ID** | ROPA-003 |
| **Processing Activity** | Email marketing and promotional campaigns |
| **Purpose** | Sending marketing communications to opted-in contacts |
| **Controller / Processor Role** | PII Controller |
| **Lawful Basis (GDPR Art. 6)** | Consent (Art. 6(1)(a)) |
| **Special Category Data?** | No |
| **PII Categories** | Email address, name, marketing preferences, click/open data |
| **Data Subjects** | Customers; prospects (with consent) |
| **Recipients** | Email marketing platform (processor) |
| **Third Country Transfers** | [Yes/No] — [Transfer mechanism if Yes] |
| **Retention Period** | Until consent withdrawn + 1 year for records |
| **Security Measures** | Consent records; unsubscribe mechanism; platform access controls |
| **DPIA Required?** | No (with valid consent and opt-out mechanism) |
| **ISO 27701:2025 Controls** | A.7.2.3, A.7.2.4, A.8.3.1, A.8.3.2 |
| **Review Date** | Annual |

---

### Entry 4: Website Analytics

| Field | Detail |
|-------|--------|
| **Activity ID** | ROPA-004 |
| **Processing Activity** | Website visitor tracking and analytics |
| **Purpose** | Understanding website usage; improving user experience |
| **Controller / Processor Role** | PII Controller |
| **Lawful Basis (GDPR Art. 6)** | Consent (Art. 6(1)(a)) for non-essential cookies; Legitimate interests (Art. 6(1)(f)) for essential analytics |
| **Special Category Data?** | No |
| **PII Categories** | IP address, browser fingerprint, pages visited, session duration |
| **Data Subjects** | Website visitors |
| **Recipients** | Analytics platform vendor (processor) |
| **Third Country Transfers** | [Yes/No] — [Transfer mechanism — note US analytics providers] |
| **Retention Period** | [X] months |
| **Security Measures** | Cookie consent banner; IP anonymisation; analytics access controls |
| **DPIA Required?** | Assess if behavioural profiling is involved |
| **ISO 27701:2025 Controls** | A.7.2.3, A.7.2.8, A.8.2.6 |
| **Review Date** | Annual |

---

### Entry 5: [Add Additional Processing Activity]

| Field | Detail |
|-------|--------|
| **Activity ID** | ROPA-005 |
| **Processing Activity** | [Name of processing activity] |
| **Purpose** | [Describe purpose clearly] |
| **Controller / Processor Role** | [Controller / Processor / Joint Controller] |
| **Lawful Basis (GDPR Art. 6)** | [Lawful basis] |
| **Special Category Data?** | [Yes/No — if Yes, Art. 9 basis] |
| **PII Categories** | [List PII categories] |
| **Data Subjects** | [Categories of data subjects] |
| **Recipients** | [Internal teams and external processors/recipients] |
| **Third Country Transfers** | [Yes/No — transfer mechanism if applicable] |
| **Retention Period** | [Retention schedule] |
| **Security Measures** | [Technical and organisational measures] |
| **DPIA Required?** | [Yes/No — rationale] |
| **ISO 27701:2025 Controls** | [Relevant Annex A / Annex B controls] |
| **Review Date** | [Date] |

---

## Register Maintenance

This ROPA is maintained by the DPO and reviewed:
- **At least annually**
- - **When a new processing activity is introduced**
  - - **When an existing processing activity is significantly changed**
    - - **When a new third-party processor is engaged**
     
      - ---

      ## Version History

      | Version | Date | Changes |
      |---------|------|---------|
      | 2.0 | April 2025 | Updated to ISO/IEC 27701:2025 — added A.8.2.6 (profiling), A.8.3.2 (consent refresh), TIA references for transfers; ROPA format enhanced |
      | 1.0 | 2024 | Initial release — ISO/IEC 27701:2019 |

      ---

      *ISO/IEC 27701:2025 PIMS Toolkit | PII Processing Inventory (ROPA) | PIMS-CTX-005 | v2.0 | Classification: Confidential*
