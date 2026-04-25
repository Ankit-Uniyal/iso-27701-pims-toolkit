# Data Retention and Disposal Policy

**Document ID:** PIMS-OPS-006  
**Version:** 1.0  
**Date:** 2025-01-01  
**Owner:** Data Protection Officer  
**Classification:** Internal  
**Review Date:** 2026-01-01

---

## 1. Purpose

This policy establishes the organisation's approach to retaining and securely disposing of Personally Identifiable Information (PII) in accordance with the storage limitation principle under ISO/IEC 27701:2025 Clause 7.4.6, GDPR Article 5(1)(e), and applicable data protection regulations. PII shall not be retained for longer than necessary for the specified purpose.

---

## 2. Scope

This policy applies to:
- All PII held in electronic systems, cloud platforms, databases, and applications
- All PII held in physical / paper records
- All backup and archive systems
- PII held by authorised third-party processors on behalf of the organisation
- All staff, contractors, and data processors

---

## 3. Retention Principles

1. **Purpose-Linked Retention**: PII shall only be retained for as long as it is needed for the original processing purpose, or any compatible secondary purpose.
2. **Legal Minimum Periods**: Where legislation mandates minimum retention periods (e.g., employment law, financial regulations), these shall be observed.
3. **Maximum Retention Periods**: PII shall not be retained beyond the maximum period defined in this schedule, unless a specific legal or business justification is documented and approved by the DPO.
4. **Regular Review**: All personal data holdings shall be reviewed against this schedule at least annually.
5. **Secure Disposal**: PII disposal must be secure and irreversible; records of disposal shall be maintained.
6. **Third-Party Alignment**: Data processors shall be contractually required to comply with this policy.

---

## 4. Retention Schedule

### 4.1 Customer / Client Data

| Data Category | Retention Period | Legal Basis / Justification | Disposal Method |
|--------------|----------------|---------------------------|----------------|
| Customer contracts and correspondence | 7 years after contract end | Limitation Act / contractual disputes | Secure deletion / shredding |
| Customer PII in CRM (active customers) | Duration of relationship + 3 years | Legitimate interests / contract | Anonymise or delete from CRM |
| Customer PII in CRM (inactive — no purchase in 3 years) | 1 year after last contact attempt | LIA review required | Delete from CRM; suppress marketing |
| Payment transaction records | 7 years | Financial regulations / tax law | Secure deletion |
| Customer support tickets / enquiries | 3 years after resolution | Legitimate interests | Secure deletion |
| Signed NDAs and legal agreements | 10 years after expiry | Contractual disputes | Secure deletion / physical shredding |
| Marketing consent records | Duration of consent + 3 years | Proof of consent | Anonymise |
| DSAR and DSR records | 3 years after completion | Demonstrate compliance | Secure deletion |
| Complaint records | 6 years after resolution | Limitation Act | Secure deletion |

### 4.2 Employee / HR Data

| Data Category | Retention Period | Legal Basis / Justification | Disposal Method |
|--------------|----------------|---------------------------|----------------|
| Employee contracts | Duration of employment + 7 years | Employment law / disputes | Secure deletion / shredding |
| Payroll and salary records | 7 years after departure | HMRC / Tax law | Secure deletion |
| Pension records | 12 years after scheme closure | Pension legislation | Secure deletion |
| Performance reviews and appraisals | Duration of employment + 5 years | Employment disputes | Secure deletion |
| Disciplinary and grievance records | 5 years after resolution (or departure if earlier) | Employment disputes | Secure deletion |
| Recruitment records (unsuccessful applicants) | 6 months after decision | Equality / discrimination claims | Secure deletion |
| Recruitment records (successful applicants) | Absorbed into employment record | Employed | — |
| DBS / background check certificates | 6 months after decision (results only, not copies) | Safe Recruitment | Secure destruction of physical copies |
| Training and development records | Duration of employment + 2 years | Demonstrate competence | Secure deletion |
| Absence and sickness records | Duration of employment + 6 years | Employment law / disability claims | Secure deletion |
| CCTV recordings (employee areas) | 31 days unless incident identified | Legitimate interests | Automatic overwrite |
| Exit interview notes | 2 years after departure | Legitimate interests | Secure deletion |

### 4.3 Supplier / Third-Party Data

| Data Category | Retention Period | Legal Basis / Justification | Disposal Method |
|--------------|----------------|---------------------------|----------------|
| Supplier contracts and DPAs | Duration + 7 years | Contract / legal disputes | Secure deletion |
| Supplier contact directories | Duration of relationship + 1 year | Legitimate interests | Delete from systems |
| Supplier due diligence records | Duration of relationship + 5 years | Demonstrate compliance | Secure deletion |
| Purchase orders and invoices | 7 years | Tax / VAT law | Secure deletion |

### 4.4 Website and Digital Data

| Data Category | Retention Period | Legal Basis / Justification | Disposal Method |
|--------------|----------------|---------------------------|----------------|
| Website analytics data (personal) | 13 months then aggregate | Consent / LIA | Anonymise at 13 months |
| Email marketing click/open data | 3 years or withdrawal of consent | Consent | Suppress/delete |
| Web forms and enquiry submissions | 2 years after last interaction | LIA | Secure deletion |
| Account registration data (active) | Duration of account | Contract | — |
| Account registration data (dormant >3 years) | 1 year after notification, then delete | LIA | Secure deletion after notification |
| Cookie consent records | 3 years after consent | Demonstrate compliance | Secure deletion |
| Server/application logs (containing IP addresses) | 90 days | Security monitoring | Automatic deletion |

### 4.5 PIMS and Compliance Records

| Data Category | Retention Period | Legal Basis / Justification | Disposal Method |
|--------------|----------------|---------------------------|----------------|
| DPIA records | Life of processing + 5 years | Demonstrate compliance | Secure deletion |
| Privacy breach records | 5 years after resolution | Regulatory / limitation | Secure deletion |
| Audit records and findings | 7 years | Demonstrate compliance | Secure deletion |
| Consent records (active) | Duration of consent + 3 years | Demonstrate consent given | Anonymise |
| Consent records (withdrawn) | 3 years after withdrawal | Demonstrate compliance | Anonymise |
| ROPA | Continuously maintained | Legal obligation | Never deleted (updated) |
| Management review records | 7 years | Demonstrate compliance | Secure deletion |

---

## 5. Disposal Methods

### 5.1 Electronic / Digital Data

| Sensitivity | Disposal Method |
|-------------|----------------|
| **Confidential / Restricted PII** | Secure overwrite (minimum 3-pass or NIST 800-88 compliant) or cryptographic erasure; certificate of destruction required |
| **Internal PII** | Secure deletion using approved tools; IT sign-off required |
| **Backup media containing PII** | Physical destruction (degaussing + shredding) or cryptographic erasure of encryption keys |
| **Cloud-stored PII** | Deletion via provider API; certificate of deletion from cloud provider obtained |
| **Removable media (USB, hard drives)** | Physical destruction by approved contractor; certificate of destruction |

### 5.2 Physical / Paper Records

| Sensitivity | Disposal Method |
|-------------|----------------|
| **Confidential / Restricted PII** | Cross-cut shredding on-site or via approved confidential waste contractor; certificate of destruction |
| **Internal PII** | Cross-cut shredding |
| **Microfilm / microfiche** | Physical destruction |

### 5.3 Approved Disposal Tools and Contractors

| Type | Approved Tool/Contractor | Certification |
|------|------------------------|---------------|
| Electronic secure deletion | [Tool Name] | NIST 800-88 / Blancco certified |
| Physical media destruction | [Contractor Name] | ISO 27001 certified; provides certificates |
| Confidential paper shredding | [Contractor Name] | EN 15713 / BS 8470 |

---

## 6. Disposal Records

A disposal record must be created for every planned disposal exercise and retained for 5 years. The record must include:

| Field | Requirement |
|-------|------------|
| Date of disposal | Exact date |
| Data category / system | What was disposed of |
| Volume | Approximate number of records |
| Disposal method | How it was disposed of |
| Responsible staff member | Who authorised and executed disposal |
| Contractor used (if applicable) | Contractor name and certificate reference |
| Certificate of destruction | Attached where available |

---

## 7. Automated Retention Controls

Where technically feasible, systems shall be configured to automatically:
- Flag records approaching retention expiry for review
- Purge records that have exceeded their retention period (with DPO configuration approval)
- Anonymise records after retention expiry where deletion is not required

IT is responsible for implementing and maintaining automated retention controls. The DPO shall review automated deletion logs quarterly.

---

## 8. Exceptions Process

Exceptions to retention periods may be approved where:
- **Legal hold**: Records subject to litigation, regulatory investigation, or subject access request must not be disposed of until the hold is lifted (Legal Counsel notifies DPO)
- **Regulatory extension**: A regulator or court orders extended retention
- **Legitimate business justification**: DPO approves a documented extension with a defined end date

All exceptions must be documented and reviewed every 6 months.

---

## 9. Third-Party Processor Obligations

All Data Processing Agreements (DPAs) must include:
- Obligation to comply with this retention policy (or equivalent)
- Requirement to delete/return all PII within 30 days of contract termination or upon written instruction
- Obligation to provide evidence of deletion (certificate or confirmation)
- Right of audit to verify compliance with retention obligations

---

## 10. Non-Compliance

Failure to comply with this policy may constitute a breach of data protection law, leading to regulatory enforcement action and fines. Incidents of non-compliance shall be reported to the DPO and recorded as NCRs in the corrective action register.

---

## 11. Record of Changes

| Version | Date | Author | Change Description |
|---------|------|--------|--------------------|
| 1.0 | 2025-01-01 | DPO | Initial release |

---

*ISO/IEC 27701:2025 PIMS Toolkit | Data Retention and Disposal Policy | PIMS-OPS-006*
