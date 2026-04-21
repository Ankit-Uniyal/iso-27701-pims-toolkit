# Worked Example: PIMS Scope Statement
## Nexus Financial Services Ltd (NFS)

> **WORKED EXAMPLE — FOR ILLUSTRATIVE PURPOSES ONLY**  
> NFS is a fictional organisation. Adapt for your own context.

---

**Document ID:** NFS-PIMS-CTX-001  
**Version:** 1.0  
**Date:** 2025-01-01  
**Owner:** NFS Data Protection Officer  
**Approved By:** NFS Chief Executive Officer

---

## 1. Organisation Profile

| Field | Detail |
|-------|--------|
| **Name** | Nexus Financial Services Ltd (NFS) |
| **Address** | 14 Capital Square, London, EC2N 4AB, UK |
| **ICO Registration** | ZA123456 |
| **Sector** | Financial Services — Consumer Lending and Insurance Broking |
| **Staff** | 320 (280 UK; 40 India offshore support) |
| **Regulators** | FCA, ICO |

---

## 2. PIMS Scope

The PIMS covers PII processing in connection with the following activities, locations, and systems:

### 2.1 In-Scope Processing Activities

| # | Activity | PII Categories | Legal Basis | Volume |
|---|---------|--------------|-----------|--------|
| 1 | Consumer loan applications and servicing | Name, address, DOB, NI, income, credit history, bank details | Contract; Legal Obligation | ~45,000 customers |
| 2 | Insurance broking — quotes and policies | Name, address, vehicle/property details, health data (critical illness) | Contract; Legal Obligation | ~18,000 customers |
| 3 | Employee HR management | Name, address, payroll, performance, absence, DBS | Contract; Legal Obligation | 320 staff |
| 4 | Marketing communications | Name, email, phone, marketing preferences | Consent; Legitimate Interests | ~120,000 contacts |
| 5 | Fraud prevention and AML | Name, transaction data, account behaviour | Legal Obligation; Legitimate Interests | All customers |
| 6 | Customer support | Name, account details, query content | Contract | All customers |
| 7 | Recruitment | CV, interview notes, right to work docs | Pre-contract; Legal Obligation | ~500 applicants/year |
| 8 | IT access and security monitoring | User IDs, access logs, email metadata | Legitimate Interests | All staff |

### 2.2 In-Scope Locations

| Location | Type | PII Processed |
|---------|------|-------------|
| London HQ — 14 Capital Square | Primary Operations | All categories |
| Manchester Office — 7 Exchange Quay | Sales / Customer Service | Customer PII |
| Bangalore Support Centre — Whitefield, India | Offshore IT Support | IT logs (no customer financial PII) |
| AWS EU-West-1 (Ireland) | Primary Cloud | All categories |
| Azure UK South | DR / Backup | All categories |

### 2.3 Key Systems In-Scope

| System | Vendor | PII Held | Location |
|--------|--------|---------|---------|
| Loan Origination System | Fintech Partner Ltd | Customer financial + personal | AWS EU |
| CRM Platform | Salesforce | Customer contact + interaction | US (SCCs) |
| HR System | BambooHR | Employee HR | US (SCCs) |
| Email Platform | Microsoft 365 | Staff and customer emails | EU Data Boundary |
| Core Banking | NFS proprietary | Accounts, transactions | AWS EU |
| Marketing Automation | HubSpot | Prospect/customer data | US (SCCs) |

### 2.4 Key Third-Party Processors

| Processor | Service | DPA | Tier |
|---------|---------|-----|------|
| Fintech Partner Ltd | LOS platform | Signed | 1 |
| Salesforce | CRM | Signed + SCCs | 1 |
| BambooHR | HRIS | Signed + SCCs | 1 |
| TransUnion | Credit referencing | Data sharing agreement | 1 |
| Experian | Credit referencing | Data sharing agreement | 1 |
| HubSpot | Marketing | Signed + SCCs | 2 |
| Wipro Technologies | IT support (Bangalore) | Signed + SCCs | 2 |

---

## 3. Exclusions

| Excluded Item | Reason |
|--------------|--------|
| NFS Capital Ltd (Group Treasury) | Separate legal entity; own PIMS |
| Anonymised analytics data | Not PII |
| Physical legacy archive (pre-2015) | Under review for Year 2 inclusion |

---

## 4. Organisational Context

**Internal factors:** FCA-regulated firm; rapid 30% YoY customer growth; offshore delivery model; legacy system migration underway; DPO newly appointed Q4 2024.

**External factors:** ICO enforcement focus on FS consent practices; FCA Consumer Duty obligations; potential UK GDPR reform; sophisticated fraud targeting customer PII.

---

## 5. Key Roles

| Role | Name | Responsibility |
|------|------|---------------|
| DPO | Sarah Chen | PIMS ownership; regulatory interface |
| CISO | James O'Brien | Technical controls; incident response |
| CEO | Mark Williams | PIMS sponsor; management review chair |
| Head of Compliance | Priya Sharma | FCA compliance; PIMS integration |

---

## 6. Approval

**Approved by:** Mark Williams, CEO  
**Date:** 2025-01-01  
**Next Review:** 2026-01-01

---

*Worked example for illustrative purposes. NFS is fictional.*  
*ISO/IEC 27701:2019 PIMS Toolkit | NFS PIMS Scope Statement | NFS-PIMS-CTX-001*
