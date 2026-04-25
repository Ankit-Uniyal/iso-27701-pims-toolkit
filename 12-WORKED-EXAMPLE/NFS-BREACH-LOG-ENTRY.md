# Worked Example: Privacy Breach Log Entry
## Nexus Financial Services Ltd (NFS)

> **WORKED EXAMPLE — FOR ILLUSTRATIVE PURPOSES ONLY**  
> NFS is a fictional organisation. This illustrates how to document a privacy breach.

---

## Breach Record: NFS-BREACH-2025-007

---

### Section 1: Breach Identification

| Field | Detail |
|-------|--------|
| **Breach Reference** | NFS-BREACH-2025-007 |
| **Date Detected** | 2025-03-14 09:47 GMT |
| **Detected By** | Customer Service Team (Rachel Davies) — customer complaint |
| **Reported to DPO** | 2025-03-14 10:15 GMT |
| **Incident Type** | Confidentiality breach — misdirected loan correspondence |
| **Classification** | Notifiable (assessed — see Section 4) |

---

### Section 2: Breach Description

**What happened:**  
A customer loan statement (containing name, address, loan balance, payment history, and partial account number) for customer REF-NFS-42876 (Ms. Amara Okafor) was sent by post to an incorrect address. The error was caused by a data entry error in the CRM — the customer's new address was updated in the HR system but not in the loan servicing system. NFS became aware when Ms. Okafor called to report she had not received her statement and that she had reason to believe correspondence had gone to a previous address.

**Root Cause:**  
Lack of automated address synchronisation between HR system (BambooHR) and Loan Servicing System. Manual update required but not completed due to staff oversight.

**Data Involved:**

| PII Category | Detail |
|-------------|--------|
| Name | Ms. Amara Okafor |
| Current address | Disclosed on statement |
| Previous address | Mailing destination |
| Loan balance | £12,450 remaining |
| Payment history | Last 3 months |
| Partial account number | Last 4 digits only |

**Number of Data Subjects:** 1  
**Nature of Records:** 1 paper loan statement

---

### Section 3: Containment Actions

| Action | Owner | Completed |
|--------|-------|-----------|
| Informed customer of the error and apologised | Customer Service / DPO | 2025-03-14 11:00 |
| Confirmed current resident at previous address (via council records) | DPO | 2025-03-14 12:00 |
| Contacted previous address resident by phone to request destruction of document | DPO | 2025-03-14 14:00 |
| Sent prepaid return envelope for document destruction | DPO | 2025-03-15 |
| Blocked further postal correspondence to old address | IT | 2025-03-14 11:30 |
| Address corrected in all NFS systems | IT | 2025-03-14 13:00 |

**Current resident cooperation:** Resident at previous address confirmed receipt of letter and agreed to destroy it. Written confirmation received 2025-03-18.

---

### Section 4: Risk Assessment and Notifiability

**Step 1 — Severity assessment:**

| Factor | Assessment |
|--------|-----------|
| Sensitivity of data | Medium — financial data; no special categories; no full account number |
| Number of individuals | 1 |
| Nature of exposure | Misdirected post — single document |
| Likelihood of harm | Low to Medium — document received by previous address resident (now confirmed destroyed) |
| Reversibility | Partially reversible — document destruction confirmed |

**Step 2 — Harm assessment:**

Potential harms to Ms. Okafor:
- Financial fraud risk: LOW — partial account number only; no payment credentials disclosed
- Reputational harm: LOW — previous resident is unknown to customer
- Identity theft: LOW — no NI, no DOB, no full account number
- Distress: MODERATE — customer upset; loan balance disclosed

**Notifiability Decision:**  
After consultation between DPO and Legal Counsel (Priya Sharma):

**ICO Notification Required?** Yes — financial data disclosed; meets the threshold of a personal data breach likely to result in risk to rights and freedoms.

**Individual Notification Required?** Yes — Ms. Okafor must be notified.

---

### Section 5: ICO Notification

| Field | Detail |
|-------|--------|
| **ICO Notification Reference** | ICO-NFS-2025-0043 |
| **Notified via** | ICO Online Reporting Tool |
| **Date / Time Notified** | 2025-03-15 16:30 GMT (within 72 hours of detection) |
| **72-Hour Deadline** | 2025-03-17 09:47 GMT |
| **Within Deadline?** | ✅ Yes — notified within 31 hours |
| **ICO Case Officer Assigned** | Pending |

---

### Section 6: Individual Notification

| Field | Detail |
|-------|--------|
| **Notification Method** | Phone call + follow-up letter |
| **Date Notified** | 2025-03-14 11:00 GMT (phone); letter sent 2025-03-15 |
| **Information Provided** | Description of breach; data involved; steps taken; remediation; DPO contact details; right to complain to ICO |
| **Customer Response** | Customer concerned; accepted apology; no immediate legal threat; asked for follow-up in 2 weeks |

---

### Section 7: Corrective Actions (Root Cause)

| # | Action | Owner | Target | Status |
|---|--------|-------|--------|--------|
| 1 | Investigate address sync gap between BambooHR and Loan Servicing System | IT | 2025-04-15 | In Progress |
| 2 | Implement automated address sync between systems | IT | 2025-06-30 | Planned |
| 3 | Manual address change audit — identify other mismatched records | IT/DPO | 2025-04-30 | Planned |
| 4 | Staff training refresher on address change verification | HR | 2025-05-31 | Planned |
| 5 | Add address verification step to address change procedure | DPO | 2025-04-30 | Planned |

**NCR Created:** NCR-2025-008 (Address sync process gap)

---

### Section 8: Post-Incident Review

**Review Date:** 2025-04-15  
**Review Conducted By:** Sarah Chen, DPO / James O'Brien, CISO  
**Lessons Learned:** Address sync between systems must be automated; address changes should trigger a verification confirmation email to customer; staff training on data accuracy gaps needed.

**Outcome:** Breach reported. Corrective actions on track. ICO acknowledged notification. No regulatory enforcement action proposed at this stage.

---

### Section 9: Sign-Off

| Role | Name | Date |
|------|------|------|
| DPO | Sarah Chen | 2025-03-14 |
| CISO (notified) | James O'Brien | 2025-03-14 |
| Legal Counsel | Priya Sharma | 2025-03-15 |
| Post-Incident Review | Sarah Chen | 2025-04-15 |

---

*Worked example. NFS is a fictional organisation.*  
*ISO/IEC 27701:2025 PIMS Toolkit | NFS Breach Log Entry | NFS-BREACH-2025-007*
