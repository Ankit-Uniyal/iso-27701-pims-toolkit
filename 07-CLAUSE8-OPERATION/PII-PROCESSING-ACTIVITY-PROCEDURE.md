# PII Processing Activity Procedure

**Document ID:** PIMS-OPS-004  
**Version:** 1.0  
**Date:** 2025-01-01  
**Owner:** Data Protection Officer  
**Classification:** Internal  
**Review Date:** 2026-01-01

---

## 1. Purpose

This procedure defines how the organisation identifies, documents, approves, monitors, and controls all activities involving the processing of Personally Identifiable Information (PII). It ensures that PII processing is lawful, transparent, purpose-limited, and aligned with ISO/IEC 27701:2019 and applicable data protection regulations.

---

## 2. Scope

This procedure applies to:
- All staff, contractors, and third parties who process PII on behalf of the organisation
- All systems, applications, and manual processes involving PII
- New processing activities prior to commencement
- Significant changes to existing processing activities

---

## 3. Definitions

| Term | Definition |
|------|-----------|
| **PII** | Any information that can identify a natural person, directly or indirectly |
| **Processing** | Any operation performed on PII (collection, storage, use, disclosure, deletion) |
| **Legal Basis** | The lawful ground under GDPR/applicable law authorising the processing |
| **Purpose Limitation** | PII collected for specified purposes may not be further processed incompatibly |
| **ROPA** | Record of Processing Activities — the organisation's PII inventory |
| **Controller** | The entity determining the purposes and means of processing PII |
| **Processor** | The entity processing PII on behalf of the Controller |

---

## 4. Responsibilities

| Role | Responsibility |
|------|---------------|
| **DPO** | Approve new processing activities; maintain ROPA; provide compliance advice |
| **Process Owners / Business Units** | Identify and document all PII processing in their area; complete intake forms |
| **IT / Systems Owners** | Implement technical controls; provide system-level processing details |
| **Legal Counsel** | Confirm legal basis; advise on cross-border transfer mechanisms |
| **Procurement** | Ensure third-party processors have DPAs before processing commences |
| **All Staff** | Process PII only for authorised purposes; report suspicious activity |

---

## 5. New PII Processing Activity — Approval Workflow

### Step 1: Request and Intake

Before commencing any new PII processing activity, the Process Owner must complete the **PII Processing Intake Form** (below) and submit it to the DPO.

**Triggers requiring intake:**
- New business process or system involving PII
- New product or service feature involving customer/employee PII
- New third-party service provider accessing PII
- Significant change to existing processing (new categories, new purposes, new retention)
- New marketing campaign involving personal data

### Step 2: DPO Initial Review (within 5 business days)

The DPO reviews the intake form and determines:

| Outcome | Action |
|---------|--------|
| **Proceed — Low Risk** | DPO approves; ROPA entry created; processing may commence |
| **DPIA Required** | Full DPIA must be completed before processing commences (score ≥12 or DPIA triggers met) |
| **Modifications Required** | Process Owner must address identified issues; resubmit |
| **Not Approved** | Processing may not commence; DPO documents rationale |

### Step 3: DPIA (if required)

See DATA-PROTECTION-IMPACT-ASSESSMENT.md for DPIA procedure.

### Step 4: ROPA Entry Creation

Upon approval, the DPO or nominated staff creates an entry in the PII Processing Inventory (ROPA) capturing all required fields.

### Step 5: Control Implementation

Before processing commences, the following must be confirmed:
- [ ] Legal basis confirmed and documented
- [ ] Privacy notice updated (if new disclosure required)
- [ ] Data Processing Agreement in place (if third-party processor involved)
- [ ] Retention period defined and system controls configured
- [ ] Access controls and role-based permissions implemented
- [ ] Staff training completed for new processing activity
- [ ] DPIA completed and approved (if required)

### Step 6: Go-Live Sign-Off

The DPO provides written approval (email or documented sign-off) before processing commences.

---

## 6. PII Processing Intake Form

**To be completed by Process Owner and submitted to DPO:**

| Field | Response |
|-------|---------|
| **Processing Activity Name** | |
| **Business Unit / Department** | |
| **Process Owner** | |
| **Date of Request** | |
| **Processing Purpose** | Describe specifically what PII will be processed and why |
| **PII Categories** | (e.g., name, email, financial data, health data, location) |
| **Special Category Data?** | Yes / No — if Yes, specify categories |
| **Data Subjects** | (e.g., customers, employees, job applicants, children) |
| **Volume (approx.)** | Number of records / subjects affected |
| **Legal Basis** | Consent / Contract / Legal Obligation / Vital Interests / Public Task / Legitimate Interests |
| **Legitimate Interests Assessment?** | Required if legal basis is LIA — Yes / No |
| **Data Source** | How is PII collected? (directly, third party, publicly available) |
| **Recipients / Disclosures** | Who will PII be shared with? |
| **Third-Party Processor?** | Yes / No — if Yes, provider name and DPA status |
| **Cross-Border Transfer?** | Yes / No — if Yes, destination country and transfer mechanism |
| **Proposed Retention Period** | |
| **Technical Systems Involved** | |
| **Existing Security Controls** | |
| **Privacy Notice Update Required?** | Yes / No |
| **DPIA Pre-Assessment Score** | (from Risk Assessment Methodology — likelihood × impact) |

---

## 7. Ongoing Management of PII Processing Activities

### 7.1 Regular Review

All ROPA entries are reviewed:
- **Annually** as part of the management review cycle
- **When a material change** occurs to the processing activity
- **Following a privacy incident** affecting the processing activity
- **Upon processor contract renewal**

### 7.2 Change Management

Any significant change to an existing processing activity (new PII categories, new purposes, new processors, new transfers) must be treated as a new activity and follow the approval workflow in Section 5.

Minor changes (minor system updates, internal contact changes) may be updated directly in the ROPA with DPO notification.

### 7.3 Cessation of Processing

When a processing activity ceases:
- The ROPA entry must be updated with cessation date and marked as inactive
- PII must be deleted or anonymised in accordance with the retention schedule
- Third-party processor must be instructed in writing to delete/return data
- Deletion is evidenced by a disposal record
- The DPO is notified of cessation

---

## 8. Special Controls for High-Risk Processing

The following processing activities require enhanced controls:

| Processing Type | Additional Controls Required |
|----------------|------------------------------|
| **Special category data** (health, biometric, racial/ethnic origin, etc.) | Explicit consent or Art. 9 exemption documented; DPA clause 9 provisions; restricted access |
| **Children's PII** | Age verification; parental consent mechanism; privacy notice in child-appropriate language |
| **Automated decision-making / profiling** | Explicit disclosure in privacy notice; human review mechanism; right to contest process |
| **Large-scale processing** | DPIA mandatory; DPO consultation; enhanced monitoring |
| **Cross-border transfers** | Transfer mechanism documented; TIA completed; privacy notice disclosure |
| **Employee monitoring** | Necessity and proportionality assessment; staff notification; union consultation where applicable |

---

## 9. Lawful Basis Reference Guide

| Legal Basis | When to Use | Key Requirements |
|-------------|------------|-----------------|
| **Consent (Art. 6(1)(a))** | Where no other basis applies; marketing; non-essential cookies | Freely given, specific, informed, unambiguous; withdrawable; recorded |
| **Contract (Art. 6(1)(b))** | Processing necessary to perform a contract with the data subject | Contract must exist or be in contemplation; necessity test applies |
| **Legal Obligation (Art. 6(1)(c))** | Processing required by law (tax, employment, health & safety) | Specific law must be identified; purpose limited to legal obligation |
| **Vital Interests (Art. 6(1)(d))** | Life-or-death situations | Last resort; natural person must be incapable of giving consent |
| **Public Task (Art. 6(1)(e))** | Public authority exercising official functions | Task must be laid down in law; public interest test |
| **Legitimate Interests (Art. 6(1)(f))** | Fraud prevention, network security, direct marketing (B2B) | Three-part LIA test must be documented; data subject rights override if harm outweighs interests |

---

## 10. Record Keeping

The following records shall be maintained:

| Record | Location | Retention |
|--------|---------|-----------|
| PII Processing Intake Forms | DPO SharePoint | 5 years after processing ceases |
| ROPA / PII Processing Inventory | PIMS-CTX-002 | Continuously updated; retained indefinitely |
| DPO Approval Sign-offs | DPO Email Archive | 5 years |
| DPIA Records | PIMS-OPS-001 folder | Life of processing + 3 years |
| Disposal Records | IT Security archive | 5 years |

---

## 11. Record of Changes

| Version | Date | Author | Change Description |
|---------|------|--------|--------------------|
| 1.0 | 2025-01-01 | DPO | Initial release |

---

*ISO/IEC 27701:2019 PIMS Toolkit | PII Processing Activity Procedure | PIMS-OPS-004*
