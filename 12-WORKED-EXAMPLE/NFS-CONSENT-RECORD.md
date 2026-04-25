# NFS Worked Example — Consent Records and Withdrawal Log

> **FOR ILLUSTRATIVE PURPOSES ONLY** — NFS is a fictional organisation. All examples are for educational use.

| Field | Detail |
|-------|--------|
| **Document ID** | NFS-PIMS-CST-001 |
| **Version** | 1.0 |
| **Date** | April 2025 |
| **Standard** | ISO/IEC 27701:2025 — A.7.2.3, A.7.2.4, GDPR Art. 7, Rec. 32 |
| **Classification** | Confidential — Internal Use |

---

## About This Worked Example

This document shows NFS consent records demonstrating how to complete `07-CLAUSE8-OPERATION/CONSENT-MANAGEMENT-PROCEDURE.md`. It covers three scenarios: marketing consent given, consent refreshed after system upgrade, and consent withdrawn.

---

## Consent Record 1 — Marketing Communications Consent (Given)

| Consent Field | NFS Entry |
|---------------|-----------|
| **Consent Reference** | NFS-CST-2025-004821 |
| **Data Subject ID** | [PSEUDONYMISED — internal hash: a7f3c9d1] |
| **Consent Type** | Marketing communications — email and SMS |
| **Collection Point** | NFS Online Banking onboarding flow — Step 5 of 7 (Preferences) |
| **Consent Statement Shown** | "I agree to receive personalised product recommendations and promotional offers from Nexus Financial Services by email and SMS. You can withdraw consent at any time via your online banking preferences." |
| **Granularity** | Separate tick-boxes for: (a) Email marketing ✓ selected; (b) SMS marketing ✓ selected; (c) Telephone marketing ✗ not selected |
| **Freely Given?** | Yes — consent is optional; account creation does not require it |
| **Specific?** | Yes — separate tick-boxes for each channel |
| **Informed?** | Yes — link to full Privacy Notice present on the same page |
| **Unambiguous?** | Yes — pre-ticked boxes not used; positive opt-in only |
| **Timestamp** | 2025-03-14T10:23:41Z |
| **IP Address** | [Pseudonymised — not retained beyond 30 days per NFS data minimisation policy] |
| **Platform Version** | OneTrust CMP v6.14.3 |
| **Consent Status** | Active |
| **Expiry / Refresh** | Consent refreshed annually or on material change to Privacy Notice |
| **Last Reviewed** | N/A — consent granted March 2025 |

---

## Consent Record 2 — Consent Refresh (Privacy Notice Update)

| Consent Field | NFS Entry |
|---------------|-----------|
| **Consent Reference** | NFS-CST-REFRESH-2025-0044 |
| **Trigger** | NFS updated Privacy Notice in January 2025 to reflect ISO/IEC 27701:2025 and new AI-driven marketing profiling activity |
| **Data Subjects Affected** | ~34,200 customers with active marketing consent as of 31 December 2024 |
| **Refresh Method** | Email notification sent 5 January 2025 with link to updated Privacy Notice and option to review/withdraw consent |
| **Refresh Email Subject** | "Important update to how we use your data — action required by 5 February 2025" |
| **Grace Period** | 30 days from notification — processing of marketing data suspended for non-responders from 6 February 2025 |
| **Outcomes** |  |
| — Consent confirmed | 22,847 customers (66.8%) re-confirmed consent via online banking portal |
| — Consent withdrawn | 4,211 customers (12.3%) withdrew consent |
| — No response | 7,142 customers (20.9%) — marketing processing suspended 6 February 2025 pending re-consent |
| **Re-consent campaign** | Follow-up email sent 1 March 2025 to non-responders; a further 1,890 re-confirmed |
| **Final consent rate** | 72.4% of original base |
| **DPO Review** | Refresh process reviewed and approved by DPO January 2025 |
| **Consent Refresh Record Archived** | OneTrust Consent Audit Log export NFS-AUDIT-CONSENT-2025-01 |

---

## Consent Record 3 — Consent Withdrawal

| Consent Field | NFS Entry |
|---------------|-----------|
| **Consent Reference** | NFS-CST-2025-004821-WD |
| **Original Consent Reference** | NFS-CST-2025-004821 (see Record 1 above) |
| **Withdrawal Method** | Online Banking preferences page — "Manage my marketing preferences" |
| **Withdrawal Timestamp** | 2025-04-01T14:55:02Z |
| **Channels Withdrawn** | All — email and SMS marketing |
| **Withdrawal Honoured By** | 2025-04-02T09:00:00Z (within 24 hours — NFS SLA is 72 hours) |
| **Actions Taken** | 1. Salesforce Marketing Cloud profile suppressed 2025-04-02. 2. Email preference centre updated to opt-out. 3. Any scheduled campaigns excluded subject from send list. 4. Suppression recorded in NFS consent database. |
| **Ongoing Legitimate Interest Processing?** | Yes — non-marketing processing (account management, legal compliance) continues under Art. 6(1)(b)/(c). Withdrawal does not affect these. |
| **Confirmation Sent to Subject?** | Yes — automated email: "You have successfully updated your marketing preferences. Changes took effect within 24 hours." |
| **Withdrawal Record Retained** | Yes — withdrawal record retained 6 years to demonstrate consent history |

---

## Consent Dashboard Summary (Q1 2025)

| Metric | Value |
|--------|-------|
| Total active marketing consent records | 24,737 |
| New consents collected Q1 2025 | 1,840 |
| Withdrawals processed Q1 2025 | 4,892 |
| Average withdrawal processing time | 18 hours |
| Consents pending annual refresh | 0 (all refreshed January 2025) |
| Consent records with expired/unknown basis | 0 |

---

## Cross-References

| Document | Reference |
|----------|-----------|
| Consent Management Procedure | `07-CLAUSE8-OPERATION/CONSENT-MANAGEMENT-PROCEDURE.md` |
| ROPA entries | `12-WORKED-EXAMPLE/NFS-ROPA-ENTRY.md` |
| Privacy Notice Template | `02-PIMS-POLICY/PRIVACY-NOTICE-TEMPLATE.md` |
| Data Subject Rights procedure | `07-CLAUSE8-OPERATION/DATA-SUBJECT-RIGHTS-PROCEDURE.md` |

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| 1.0 | April 2025 | Initial release — NFS consent given, refresh, and withdrawal records |

---

*ISO/IEC 27701:2025 PIMS Toolkit | NFS Consent Records | NFS-PIMS-CST-001*
