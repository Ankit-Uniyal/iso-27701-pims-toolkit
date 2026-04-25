# Privacy Risk Treatment Plan

**Document ID:** PIMS-PLN-004  
**Version:** 1.0  
**Date:** 2025-01-01  
**Owner:** Data Protection Officer  
**Classification:** Internal — Restricted  
**Review Date:** 2026-06-01

---

## 1. Purpose

This Privacy Risk Treatment Plan documents the agreed treatment actions for privacy risks identified in the Privacy Risk Register (PIMS-PLN-001). For each risk above the organisation's risk appetite, it defines the treatment option, controls to be implemented, responsible owner, target completion date, and success criteria.

---

## 2. Scope

This plan covers all risks rated **Medium (6–11), High (12–19), and Critical (20–25)** from the current Privacy Risk Register. Risks rated Low (2–5) or Minimal (1) are accepted and documented in the register but do not require formal treatment plans.

---

## 3. Risk Treatment Options

| Option | Code | Description |
|--------|------|-------------|
| Mitigate | M | Implement controls to reduce likelihood or impact |
| Avoid | AV | Cease or restructure the processing activity |
| Transfer | T | Contractual/insurance transfer of risk |
| Accept | AC | Formally accept residual risk with DPO sign-off |

---

## 4. Active Risk Treatment Plans

### RTP-001: Unauthorised Access to PII via Unsecured Endpoints

| Field | Detail |
|-------|--------|
| **Risk ID** | PRR-001 |
| **Risk Description** | Employee devices accessing PII without encryption or MDM controls |
| **Current Risk Score** | Likelihood: 4 | Impact: 4 | **Score: 16 (High)** |
| **Treatment Option** | Mitigate |
| **Risk Owner** | CISO |
| **Treatment Lead** | IT Security Manager |

**Treatment Actions:**

| Action | Control Reference | Target Date | Status | Evidence |
|--------|-----------------|-------------|--------|---------|
| Deploy full-disk encryption on all endpoints | ISO 27701 A.8.2.1 | 2025-03-31 | In Progress | MDM deployment report |
| Implement Mobile Device Management (MDM) policy | ISO 27701 A.8.2.1 | 2025-03-31 | Planned | MDM policy sign-off |
| Enable remote wipe capability for all mobile devices | ISO 27701 A.8.2.1 | 2025-04-30 | Planned | MDM configuration record |
| Conduct user awareness training on device security | ISO 27701 7.3 | 2025-05-31 | Planned | Training completion records |

**Target Residual Score:** Likelihood: 2 | Impact: 3 | **Target Score: 6 (Medium)**

---

### RTP-002: Absence of Valid Legal Basis for Marketing Processing

| Field | Detail |
|-------|--------|
| **Risk ID** | PRR-002 |
| **Risk Description** | Direct marketing emails sent without confirmed opt-in consent or documented legitimate interests assessment |
| **Current Risk Score** | Likelihood: 3 | Impact: 4 | **Score: 12 (High)** |
| **Treatment Option** | Mitigate |
| **Risk Owner** | DPO |
| **Treatment Lead** | Head of Marketing / Legal Counsel |

**Treatment Actions:**

| Action | Control Reference | Target Date | Status | Evidence |
|--------|-----------------|-------------|--------|---------|
| Conduct Legitimate Interests Assessment (LIA) for all marketing activities | GDPR Art. 6(1)(f) | 2025-02-28 | Planned | Completed LIA documents |
| Implement double opt-in consent mechanism on website | ISO 27701 7.3.3 | 2025-03-31 | In Progress | Consent platform config |
| Audit and cleanse existing marketing lists for valid consent | ISO 27701 7.3.3 | 2025-04-30 | Planned | Audit report + list cleansing log |
| Update privacy notice to reflect marketing processing | ISO 27701 7.3.2 | 2025-03-31 | Planned | Updated privacy notice |
| Implement consent withdrawal mechanism | ISO 27701 7.3.3 | 2025-03-31 | Planned | Unsubscribe test records |

**Target Residual Score:** Likelihood: 2 | Impact: 3 | **Target Score: 6 (Medium)**

---

### RTP-003: Processor Non-Compliance — Cloud Storage Provider

| Field | Detail |
|-------|--------|
| **Risk ID** | PRR-003 |
| **Risk Description** | Key cloud storage provider holds PII without a current GDPR-compliant Data Processing Agreement |
| **Current Risk Score** | Likelihood: 3 | Impact: 5 | **Score: 15 (High)** |
| **Treatment Option** | Mitigate / Transfer |
| **Risk Owner** | DPO |
| **Treatment Lead** | Legal Counsel / Procurement |

**Treatment Actions:**

| Action | Control Reference | Target Date | Status | Evidence |
|--------|-----------------|-------------|--------|---------|
| Execute Data Processing Agreement with cloud storage provider | ISO 27701 8.5.1 | 2025-02-28 | In Progress | Signed DPA |
| Review provider's security certifications (ISO 27001, SOC 2) | ISO 27701 8.5.5 | 2025-03-31 | Planned | Certification copies |
| Conduct supplier privacy questionnaire assessment | ISO 27701 8.5.4 | 2025-04-30 | Planned | Completed questionnaire |
| Establish annual review cadence for supplier compliance | ISO 27701 8.5.6 | 2025-06-30 | Planned | Supplier review schedule |

**Target Residual Score:** Likelihood: 2 | Impact: 3 | **Target Score: 6 (Medium)**

---

### RTP-004: Inadequate Data Subject Rights Response Process

| Field | Detail |
|-------|--------|
| **Risk ID** | PRR-004 |
| **Risk Description** | No formal DSR management process; risk of missing statutory response deadlines (30 days GDPR) |
| **Current Risk Score** | Likelihood: 4 | Impact: 3 | **Score: 12 (High)** |
| **Treatment Option** | Mitigate |
| **Risk Owner** | DPO |
| **Treatment Lead** | DPO / IT |

**Treatment Actions:**

| Action | Control Reference | Target Date | Status | Evidence |
|--------|-----------------|-------------|--------|---------|
| Implement DSR intake form on website | ISO 27701 7.3.4 | 2025-02-28 | In Progress | Form URL + screenshots |
| Create DSR tracking log / workflow | ISO 27701 7.3.4 | 2025-03-15 | Planned | DSR log template |
| Train customer service team on DSR handling | ISO 27701 7.3 | 2025-04-30 | Planned | Training records |
| Establish 10-day internal SLA for initial DSR triage | ISO 27701 7.3.4 | 2025-03-15 | Planned | SLA documentation |
| Test DSR end-to-end process via simulated exercise | ISO 27701 7.3.4 | 2025-06-30 | Planned | Exercise report |

**Target Residual Score:** Likelihood: 2 | Impact: 3 | **Target Score: 6 (Medium)**

---

### RTP-005: Cross-Border Transfer Without Adequate Safeguards

| Field | Detail |
|-------|--------|
| **Risk ID** | PRR-005 |
| **Risk Description** | PII transferred to US-based analytics tool without SCCs or equivalent transfer mechanism |
| **Current Risk Score** | Likelihood: 3 | Impact: 4 | **Score: 12 (High)** |
| **Treatment Option** | Mitigate / Avoid |
| **Risk Owner** | DPO |
| **Treatment Lead** | Legal Counsel / CTO |

**Treatment Actions:**

| Action | Control Reference | Target Date | Status | Evidence |
|--------|-----------------|-------------|--------|---------|
| Conduct transfer impact assessment for US analytics provider | ISO 27701 7.5 | 2025-03-15 | Planned | TIA document |
| Execute Standard Contractual Clauses with US provider | ISO 27701 7.5 / GDPR Art. 46 | 2025-04-30 | Planned | Executed SCCs |
| Evaluate EU-based analytics alternative (privacy-first) | ISO 27701 7.5 | 2025-03-31 | In Progress | Vendor comparison report |
| Update privacy notice to disclose international transfers | ISO 27701 7.3.2 | 2025-04-30 | Planned | Updated notice |

**Target Residual Score:** Likelihood: 2 | Impact: 3 | **Target Score: 6 (Medium)**

---

### RTP-006: Excessive Data Retention — HR Records

| Field | Detail |
|-------|--------|
| **Risk ID** | PRR-006 |
| **Risk Description** | Former employee HR records retained indefinitely without a documented retention schedule |
| **Current Risk Score** | Likelihood: 4 | Impact: 3 | **Score: 12 (High)** |
| **Treatment Option** | Mitigate |
| **Risk Owner** | HR Manager |
| **Treatment Lead** | HR / IT |

**Treatment Actions:**

| Action | Control Reference | Target Date | Status | Evidence |
|--------|-----------------|-------------|--------|---------|
| Publish HR data retention schedule aligned to legal requirements | ISO 27701 7.4.6 | 2025-03-31 | Planned | Approved retention schedule |
| Configure HR system to flag records for review at retention end | ISO 27701 7.4.6 | 2025-06-30 | Planned | System configuration |
| Conduct initial audit and disposal of records past retention date | ISO 27701 7.4.6 | 2025-06-30 | Planned | Disposal log |
| Train HR team on retention obligations | ISO 27701 7.3 | 2025-04-30 | Planned | Training records |

**Target Residual Score:** Likelihood: 2 | Impact: 2 | **Target Score: 4 (Low)**

---

### RTP-007: DPIA Not Conducted for New CRM Implementation

| Field | Detail |
|-------|--------|
| **Risk ID** | PRR-007 |
| **Risk Description** | New CRM system processes customer PII at scale without DPIA |
| **Current Risk Score** | Likelihood: 3 | Impact: 4 | **Score: 12 (High)** |
| **Treatment Option** | Mitigate |
| **Risk Owner** | DPO |
| **Treatment Lead** | DPO / CTO |

**Treatment Actions:**

| Action | Control Reference | Target Date | Status | Evidence |
|--------|-----------------|-------------|--------|---------|
| Complete DPIA for CRM system | ISO 27701 7.2.5 | 2025-02-28 | In Progress | Completed DPIA |
| Implement privacy by design review in IT change process | ISO 27701 7.4.1 | 2025-04-30 | Planned | Updated change policy |
| Review and approve DPIA findings with senior management | ISO 27701 7.2.5 | 2025-03-31 | Planned | Management sign-off |
| Add CRM to ROPA with full processing details | ISO 27701 7.2.8 | 2025-02-28 | In Progress | Updated ROPA |

**Target Residual Score:** Likelihood: 2 | Impact: 3 | **Target Score: 6 (Medium)**

---

## 5. Medium Risk Monitoring Table

| Risk ID | Risk Description | Score | Risk Owner | Review Date | Notes |
|---------|----------------|-------|-----------|-------------|-------|
| PRR-008 | Phishing attack leading to PII disclosure | 9 | CISO | 2025-06-30 | Phishing simulation programme in place |
| PRR-009 | Paper records containing PII not locked overnight | 8 | Office Manager | 2025-06-30 | Clear desk policy being enforced |
| PRR-010 | Staff sharing PII via personal email | 6 | HR/DPO | 2025-12-31 | AUP training scheduled |
| PRR-011 | Cookie consent not compliant with latest guidance | 8 | DPO | 2025-03-31 | Cookie audit scheduled |

---

## 6. Treatment Plan Progress Summary

| RTP ID | Risk Description | Current Score | Target Score | Status | Target Date |
|--------|----------------|--------------|-------------|--------|-------------|
| RTP-001 | Unauthorised endpoint access | 16 (High) | 6 (Medium) | In Progress | 2025-05-31 |
| RTP-002 | Invalid marketing legal basis | 12 (High) | 6 (Medium) | In Progress | 2025-04-30 |
| RTP-003 | Processor without DPA | 15 (High) | 6 (Medium) | In Progress | 2025-06-30 |
| RTP-004 | Inadequate DSR process | 12 (High) | 6 (Medium) | In Progress | 2025-06-30 |
| RTP-005 | Cross-border transfer — SCCs | 12 (High) | 6 (Medium) | In Progress | 2025-04-30 |
| RTP-006 | Excessive HR retention | 12 (High) | 4 (Low) | Planned | 2025-06-30 |
| RTP-007 | DPIA not done for CRM | 12 (High) | 6 (Medium) | In Progress | 2025-03-31 |

---

## 7. Residual Risk Acceptance

Any residual risk remaining after treatment shall be formally documented in the Privacy Risk Register, reviewed by the DPO, escalated to senior management if residual score remains 12 or above, and reported in the quarterly Management Review.

---

## 8. Record of Changes

| Version | Date | Author | Change Description |
|---------|------|--------|--------------------|
| 1.0 | 2025-01-01 | DPO | Initial release |

---

*ISO/IEC 27701:2025 PIMS Toolkit | Privacy Risk Treatment Plan | PIMS-PLN-004*
