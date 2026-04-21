# Worked Example: Privacy Risk Register Entries
## Nexus Financial Services Ltd (NFS)

> **WORKED EXAMPLE — FOR ILLUSTRATIVE PURPOSES ONLY**  
> NFS is a fictional organisation. These entries illustrate how to populate the Privacy Risk Register.

---

**Organisation:** Nexus Financial Services Ltd  
**Register Owner:** Sarah Chen, DPO  
**Period:** Q1 2025

---

## Risk Entry PRR-NFS-001: Unencrypted Email Transmission of Loan PII

| Field | Detail |
|-------|--------|
| **Risk ID** | PRR-NFS-001 |
| **Description** | Customer credit application PII (NI number, bank statements, income) sent unencrypted via email to underwriters |
| **PII Categories** | Name, DOB, NI number, income, bank statements, credit report |
| **Data Subjects** | Consumer loan applicants (~45,000) |
| **ISO 27701 Clause** | A.8.2.1 (Access control); 7.4.5 (Disclosure limitation) |
| **Likelihood** | 4 (High) — multiple instances observed in audit |
| **Impact** | 5 (Severe) — identity theft risk; regulatory breach; financial harm |
| **Risk Score** | **20 — Critical** |

**Treatment:** Enforce TLS encryption; implement email DLP; mandatory training; move to secure document portal.  
**Target Score:** 6 (Medium) | **Owner:** James O'Brien, CISO | **Due:** 2025-04-30

---

## Risk Entry PRR-NFS-002: Invalid Marketing Consent (Pre-Ticked Boxes)

| Field | Detail |
|-------|--------|
| **Risk ID** | PRR-NFS-002 |
| **Description** | ~85,000 marketing contacts have consent obtained via pre-ticked boxes — invalid under UK GDPR |
| **PII Categories** | Name, email address, marketing preferences |
| **Data Subjects** | ~85,000 marketing database contacts |
| **ISO 27701 Clause** | 7.3.3 (Consent management) |
| **Likelihood** | 5 (Very High) — confirmed by consent mechanism review |
| **Impact** | 3 (Moderate) — ICO enforcement; complaints; reputational damage |
| **Risk Score** | **15 — High** |

**Treatment:** Pause campaigns; conduct consent audit; re-consent campaign; implement double opt-in.  
**Target Score:** 4 (Low) | **Owner:** Sarah Chen, DPO | **Due:** 2025-03-31

---

## Risk Entry PRR-NFS-003: Unrestricted Offshore Admin Access to Customer PII

| Field | Detail |
|-------|--------|
| **Risk ID** | PRR-NFS-003 |
| **Description** | Bangalore IT support team has unrestricted admin access to all customer loan data with no audit logging |
| **PII Categories** | Customer name, financial data, loan accounts, transaction history |
| **Data Subjects** | All ~45,000 loan customers |
| **ISO 27701 Clause** | 8.5 (Processors); A.8.2.1 (Access control) |
| **Likelihood** | 3 (Medium) — admin access confirmed; monitoring gaps |
| **Impact** | 4 (Major) — large-scale exposure; cross-border transfer risk |
| **Risk Score** | **12 — High** |

**Treatment:** Restrict offshore admin access; implement PAM; enable audit logging; renew DPA with SCCs.  
**Target Score:** 4 (Low) | **Owner:** James O'Brien, CISO | **Due:** 2025-06-30

---

## Risk Entry PRR-NFS-004: DSAR Response Approaching Statutory Deadline

| Field | Detail |
|-------|--------|
| **Risk ID** | PRR-NFS-004 |
| **Description** | DSAR-2025-012 (John Hawkins) approaching 30-day UK GDPR deadline with no assigned owner or response prepared |
| **PII Categories** | All NFS-held PII relating to the data subject |
| **Data Subjects** | 1 individual |
| **ISO 27701 Clause** | 7.3.4 (Rights of PII principals) |
| **Likelihood** | 4 (High) — deadline is 2025-01-28; no action taken |
| **Impact** | 3 (Moderate) — ICO complaint; regulatory action; reputational damage |
| **Risk Score** | **12 — High (Urgent)** |

**Treatment:** Assign immediately to Customer Compliance; search all systems; issue response by deadline; implement DSR tracking log.  
**Target Score:** 4 (Low) | **Owner:** Sarah Chen, DPO | **Due:** 2025-01-28 (statutory deadline)

---

## Risk Entry PRR-NFS-005: New CRM Migration Without DPIA

| Field | Detail |
|-------|--------|
| **Risk ID** | PRR-NFS-005 |
| **Description** | Salesforce CRM migration planned for Q2 2025 involving 120,000+ customer records — no DPIA conducted |
| **PII Categories** | Name, contact details, purchase history, marketing preferences, interaction logs |
| **Data Subjects** | ~120,000 customers and prospects |
| **ISO 27701 Clause** | 7.2.5 (DPIA); 7.4.1 (Privacy by Design) |
| **Likelihood** | 3 (Medium) — migration confirmed; DPIA not scheduled |
| **Impact** | 4 (Major) — large-scale migration; new US processor involved; inadequate controls risk |
| **Risk Score** | **12 — High** |

**Treatment:** Complete DPIA before migration; review Salesforce DPA and SCCs; implement privacy by design in migration plan; DPO sign-off required before go-live.  
**Target Score:** 6 (Medium) | **Owner:** Sarah Chen, DPO | **Due:** 2025-03-31 (before migration)

---

*Worked example. NFS is a fictional organisation.*  
*ISO/IEC 27701:2019 PIMS Toolkit | NFS Privacy Risk Register Entries | NFS-PIMS-PLN-001*
