# Privacy by Design Procedure

**Document ID:** PIMS-OPS-009  
**Version:** 1.0  
**Date:** 2025-01-01  
**Owner:** Data Protection Officer  
**Classification:** Internal  
**Review Date:** 2026-01-01

---

## 1. Purpose

This procedure establishes the organisation's approach to embedding privacy protections into systems, processes, products, and services by design and by default. It implements ISO/IEC 27701:2019 Clause 7.4.1, GDPR Article 25, and the Privacy by Design Framework.

---

## 2. The Seven Foundational Principles

| # | Principle | Meaning |
|---|-----------|---------|
| 1 | Proactive, not Reactive | Anticipate and prevent privacy events before they occur |
| 2 | Privacy as the Default | Automatically protect personal data without individual action |
| 3 | Privacy Embedded into Design | Built into architecture, not added afterwards |
| 4 | Full Functionality | Privacy and functionality achieved together (positive-sum) |
| 5 | End-to-End Security | Secure lifecycle from collection to deletion |
| 6 | Visibility and Transparency | Stakeholders can verify privacy promises |
| 7 | Respect for User Privacy | User-centric; strong privacy defaults and empowerment |

---

## 3. Project Lifecycle Integration

| Project Phase | Privacy by Design Requirement |
|--------------|------------------------------|
| Initiation | Privacy pre-screening; DPO notified |
| Requirements / Design | Privacy requirements defined; DPIA screening completed |
| Development | Controls implemented; data minimisation; encryption |
| Testing / UAT | Privacy test cases; no production data in test |
| Pre-Launch | DPIA signed off; privacy notice updated; DPO approval |
| Post-Launch | Incident monitoring; periodic DPIA review |

---

## 4. Privacy by Design Checklist

### Section 1 — Data Minimisation

| Requirement | Met? |
|------------|------|
| Only strictly necessary PII collected | Yes / No |
| Optional fields clearly distinguished | Yes / No |
| Pseudonymisation / anonymisation applied where possible | Yes / No |

### Section 2 — Security Controls

| Requirement | Met? |
|------------|------|
| Role-based access controls (least privilege) | Yes / No |
| PII encrypted at rest (AES-256 or equivalent) | Yes / No |
| PII encrypted in transit (TLS 1.2+) | Yes / No |
| MFA required for sensitive PII systems | Yes / No |
| Audit logging for all PII access | Yes / No |
| Production data not used in test environments | Yes / No |

### Section 3 — Transparency and User Control

| Requirement | Met? |
|------------|------|
| Privacy notice updated to cover new processing | Yes / No |
| Consent mechanism in place (if consent is legal basis) | Yes / No |
| Data subject rights exercisable for this data | Yes / No |

### Section 4 — Retention and Deletion

| Requirement | Met? |
|------------|------|
| Retention period defined and aligned to policy | Yes / No |
| Automated deletion or anonymisation configured | Yes / No |
| Deletion/disposal method documented | Yes / No |

### Section 5 — Third Parties

| Requirement | Met? |
|------------|------|
| All third-party recipients identified and assessed | Yes / No |
| DPAs in place for all processors | Yes / No |
| Cross-border transfers assessed and mechanism in place | Yes / No |

### Section 6 — DPIA and Risk

| Requirement | Met? |
|------------|------|
| DPIA screening completed | Yes / No |
| Full DPIA completed (if required) | Yes / No / N/A |
| Privacy risks treated | Yes / No |
| DPO sign-off obtained before go-live | Yes / No |

---

## 5. Privacy by Default Standards

| Default Setting | Requirement |
|----------------|------------|
| Marketing opt-in | Unchecked by default |
| Non-essential cookies | Disabled by default; require active consent |
| Profile visibility | Private by default |
| Data sharing with third parties | Off by default |
| Account retention | Inactive accounts flagged for deletion |

---

## 6. Roles and Responsibilities

| Role | Responsibility |
|------|---------------|
| Architects / Developers | Embed privacy controls in design; consult DPO at design stage |
| Product Managers | Complete checklist; include privacy requirements in user stories |
| QA / Testers | Verify controls work; use synthetic test data only |
| Project Managers | Ensure DPO consulted at gates; obtain privacy sign-off before launch |
| DPO | Review checklist; approve go-live; advise on requirements |

---

## 7. Record of Changes

| Version | Date | Author | Change Description |
|---------|------|--------|--------------------|
| 1.0 | 2025-01-01 | DPO | Initial release |

---

*ISO/IEC 27701:2019 PIMS Toolkit | Privacy by Design Procedure | PIMS-OPS-009*
