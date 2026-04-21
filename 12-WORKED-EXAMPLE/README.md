# Worked Examples — Nexus Financial Services Ltd (NFS)

> **FOR ILLUSTRATIVE PURPOSES ONLY** — NFS is a fictional organisation. All examples are created for educational use to demonstrate how to complete ISO/IEC 27701:2025 PIMS templates. Do not use real personal data.

| Field | Detail |
|-------|--------|
| **Document ID** | NFS-WORKED-README-001 |
| **Version** | 2.0 |
| **Date** | April 2025 |
| **Standard** | ISO/IEC 27701:2025 |
| **Classification** | Public — Educational Reference |

---

## About Nexus Financial Services Ltd (NFS)

**Nexus Financial Services Ltd (NFS)** is a fictional UK-based financial services company used throughout this toolkit as a worked example organisation. NFS represents a mid-sized business with a mature GRC function implementing ISO/IEC 27701:2025.

### Organisation Profile

| Attribute | Detail |
|-----------|--------|
| **Organisation** | Nexus Financial Services Ltd (NFS) — fictional |
| **Sector** | Financial services (retail banking, loans, insurance) |
| **Jurisdiction** | UK (HQ) with processing in EU (Dublin office) and India (Bangalore back-office) |
| **Employees** | ~2,400 |
| **Customers** | ~380,000 retail customers; ~12,000 SME customers |
| **PIMS Role** | PII Controller (primary) and PII Processor (for partner white-label products) |
| **Applicable Law** | UK GDPR, UK DPA 2018, EU GDPR (Dublin), India DPDPA 2023 |
| **DPO** | Sarah Chen, CIPP/E, CIPM |
| **ISMS Certification** | ISO 27001:2022 (certified since 2022) |
| **PIMS Status** | Implementing ISO/IEC 27701:2025 — targeting certification by Q4 2025 |

### Key PII Processing Activities

| Activity | PII Categories | Volume | Legal Basis |
|---------|----------------|--------|-------------|
| Retail current account management | Name, address, DOB, NI, financial data | ~380,000 | Contract |
| Credit scoring and lending decisions | Financial history, employment, credit reference data | ~45,000 p.a. | Contract + Legal obligation |
| Marketing and cross-sell | Name, email, transaction data, preferences | ~120,000 (consented) | Consent |
| Fraud detection and prevention | Transaction data, device data, behavioural patterns | All customers | Legitimate interests |
| HR and payroll | Employee PII, salary, performance, health data | ~2,400 employees | Contract + Legal obligation |
| Mortgage processing | Name, address, financial, credit, property data | ~8,000 p.a. | Contract |
| Insurance underwriting (white-label) | Health declarations, vehicle/property data | ~35,000 p.a. | Contract (as Processor) |
| Analytics and product development | Pseudonymised transaction data | All customers (pseudonymised) | Legitimate interests |

### PIMS Gap Assessment Status (as at Q1 2025)

| Section | Score | Status |
|---------|-------|--------|
| Clause 4 — Context | 3.8/5 | Largely conformant |
| Clause 5 — Leadership | 4.2/5 | Good |
| Clause 6 — Planning | 3.0/5 | Developing — SoA and risk register need completion |
| Clause 7 — Support | 3.5/5 | Largely conformant |
| Clause 8 — Operation | 2.8/5 | **Gap area** — DPIA, consent management, TIA need work |
| Clause 9 — Performance | 2.5/5 | **Gap area** — KPIs and audit programme not yet established |
| Clause 10 — Improvement | 3.0/5 | Developing |
| Annex A Controls | 2.9/5 | Developing — new 2025 controls not yet implemented |
| Annex B Controls | 3.2/5 | Developing |
| **Overall** | **3.1/5** | **62% ready — active programme underway** |

### Key Privacy Risks Identified

| Risk ID | Risk | Inherent | Residual | Treatment |
|---------|------|----------|----------|-----------|
| PRR-NFS-001 | Invalid marketing consent (pre-ticked boxes — ~120K contacts) | Critical | High | Re-consent campaign Q2 2025 |
| PRR-NFS-002 | Cross-border transfer to Bangalore without TIA | High | High | TIA being conducted; SCCs being updated |
| PRR-NFS-003 | DPIA not completed for AI fraud detection model | High | Medium | DPIA in progress; DPO engaged |
| PRR-NFS-004 | DSR response capability — no tracking system | High | Medium | DSR tracker being implemented |
| PRR-NFS-005 | Privacy Notice out of date (does not reflect Bangalore transfers or AI processing) | Medium | Low | Privacy Notice v2.0 approved, pending publishing |

---

## Worked Example Files

The following completed example documents are provided for reference:

| # | File | What It Demonstrates |
|---|------|---------------------|
| 1 | [NFS-PIMS-SCOPE-STATEMENT.md](NFS-PIMS-SCOPE-STATEMENT.md) | How to complete the PIMS Scope Statement with NFS context |
| 2 | [NFS-PRIVACY-RISK-REGISTER-ENTRY.md](NFS-PRIVACY-RISK-REGISTER-ENTRY.md) | Three completed privacy risk register entries with scoring |
| 3 | [NFS-SOA-EXCERPT.md](NFS-SOA-EXCERPT.md) | Sample SoA excerpt showing include/exclude decisions for key controls |
| 4 | [NFS-DPIA-ENTRY.md](NFS-DPIA-ENTRY.md) | Completed DPIA for NFS customer analytics processing activity |
| 5 | [NFS-BREACH-LOG-ENTRY.md](NFS-BREACH-LOG-ENTRY.md) | Completed privacy breach log entry (employee laptop loss) |

---

## How to Use These Examples

1. **Read the NFS profile above** to understand the organisational context
2. **Open each worked example** to see how templates are completed in practice
3. **Use as a reference** when completing your own PIMS templates
4. **Do not copy directly** — adapt to your organisation's specific context and risk profile

> All NFS examples reflect ISO/IEC 27701:2025 requirements and should be used alongside the corresponding blank templates in the relevant clause folders.

---

## Key Differences: NFS 2025 vs. 2019 Templates

These worked examples have been updated from the 2019 edition to reflect ISO/IEC 27701:2025:

| Change | 2019 Templates | 2025 Templates |
|--------|---------------|---------------|
| Standard reference | ISO 27701:2019 | ISO 27701:2025 |
| SoA controls | 49 controls (A.7.1–A.8.5, B.8.1–B.8.5) | Updated control set including new 2025 controls |
| DPIA triggers | General | 2025 prescriptive trigger criteria |
| Cross-border transfers | Transfer mechanism | Transfer mechanism + TIA where required |
| Consent | Basic lifecycle | Full lifecycle including refresh requirement |
| Joint controllers | Not addressed | NFS joint controller arrangements identified |
| Privacy by Default | Embedded | Explicit control — checklist included in scope |
| Risk methodology | ISO 27005 general | ISO 27005:2022 aligned |

---

## Version History

| Version | Date | Description |
|---------|------|-------------|
| 2.0 | April 2025 | Updated for ISO/IEC 27701:2025 — NFS profile updated, 2025 gap scores, TIA and consent risks added, new control references. Replaced incorrect gap checklist content from prior version. |
| 1.0 | 2024 | Initial release — ISO/IEC 27701:2019 |

---

*ISO/IEC 27701:2025 PIMS Toolkit | Worked Examples — NFS | NFS-WORKED-README-001 | v2.0 | Classification: Public*
