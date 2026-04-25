# Consent Management Procedure

**Document ID:** PIMS-OPS-005  
**Version:** 1.0  
**Date:** 2025-01-01  
**Owner:** Data Protection Officer  
**Classification:** Internal  
**Review Date:** 2026-01-01

---

## 1. Purpose

This procedure defines how the organisation obtains, records, manages, and honours consent from data subjects for PII processing activities where consent is the chosen legal basis. It ensures compliance with ISO/IEC 27701:2025 Clause 7.3.3, GDPR Articles 6–7, and the organisation's commitment to transparency and individual autonomy over personal data.

---

## 2. Scope

This procedure applies to:
- All processing activities where **consent** is the identified legal basis
- Marketing communications (email, SMS, post, phone)
- Non-essential website cookies and tracking technologies
- Sharing PII with third parties for marketing or profiling purposes
- Processing of special category data requiring explicit consent
- Processing of children's personal data

---

## 3. When Consent Is (and Is Not) Appropriate

### 3.1 Consent IS appropriate when:
- The processing is optional and the data subject has a genuine free choice
- No other legal basis adequately applies
- The organisation wants to demonstrate best practice transparency

### 3.2 Consent IS NOT appropriate when:
- There is an imbalance of power between the organisation and the data subject (e.g., employee consent for most employment purposes — use contract or legal obligation instead)
- Refusing consent means the data subject cannot receive a basic service they are entitled to (consent would not be freely given)
- The processing is required to perform a contract with the data subject
- The processing is required by law

---

## 4. Consent Standards

All consent obtained by the organisation must meet the following standards (aligned to GDPR Article 7 and ISO 27701 7.3.3):

| Standard | Requirement |
|----------|------------|
| **Freely Given** | No penalty or disadvantage for withholding or withdrawing consent; genuine choice |
| **Specific** | Consent must be tied to specific processing purpose(s); bundled consent is invalid |
| **Informed** | Data subject must understand who is processing, for what purpose, their rights, and how to withdraw |
| **Unambiguous** | Consent must be given by a clear affirmative act (no pre-ticked boxes, no silence) |
| **Explicit (special categories)** | Express consent required; oral consent must be documented |
| **Separate** | Consent must not be bundled with terms and conditions or other agreements |
| **Withdrawable** | Data subjects must be able to withdraw consent as easily as they gave it, at any time |
| **Age-appropriate** | Parental/guardian consent required for children under applicable minimum age (typically 16; varies by jurisdiction) |

---

## 5. Consent Collection Methods

### 5.1 Website / Online Consent

| Method | Standard |
|--------|---------|
| **Cookie consent banner** | CMP tool with granular category choices; no pre-ticked boxes; reject all option as prominent as accept all; records consent with timestamp and version |
| **Marketing sign-up forms** | Unchecked opt-in checkbox; granular channel consent (email/SMS/phone); linked to privacy notice |
| **Account registration** | Separate checkbox(es) for optional marketing; clear distinction from mandatory account terms |
| **Online service features** | Explicit opt-in for non-essential profiling, analytics, personalisation |

### 5.2 Paper / In-Person Consent

| Method | Standard |
|--------|---------|
| **Paper forms** | Tick box(es); person must actively tick; clear language; date; copy provided to data subject |
| **Verbal consent** | Documented in CRM/system immediately; follow-up written confirmation sent |
| **Event sign-up** | Separate consent fields; not buried in terms; staff trained to explain |

### 5.3 Children's Consent

- Age must be verified before consent for online services
- For children under 16 (or lower local minimum age), parental/guardian consent is required
- Privacy notices and consent language must be age-appropriate
- Preference engines and profiling must not target children without explicit parental consent

---

## 6. Consent Record-Keeping Requirements

For each consent record, the following must be captured and stored:

| Field | Description |
|-------|------------|
| **Data Subject ID** | Identifier linking consent to the individual |
| **Consent Date/Time** | Exact timestamp of consent |
| **Consent Version** | Version of privacy notice in force at time of consent |
| **Collection Method** | How consent was obtained (website, paper, verbal, etc.) |
| **Processing Purpose(s)** | Specific purpose(s) consented to |
| **Marketing Channels** | If applicable: email, SMS, phone, post |
| **IP Address** | For online consent (where legally permissible) |
| **Consent Form/Banner Version** | Version of the form/CMP at time of consent |
| **Withdrawal Date** | If consent is subsequently withdrawn |
| **Withdrawal Method** | How withdrawal was communicated |

---

## 7. Consent Withdrawal Process

### 7.1 Withdrawal Channels

Data subjects may withdraw consent via:
- **Unsubscribe link** in marketing emails (automated; processed within 10 business days)
- **Data Subject Request Form** on website
- **Written request** to the DPO (dpo@organisation.com)
- **In-person request** at customer service desk
- **Cookie preference centre** (for cookie consent — immediate effect)
- **Phone request** to customer service team

### 7.2 Withdrawal Processing Steps

1. Withdrawal request received and logged in DSR tracking system
2. Withdrawal acknowledged to data subject within **3 business days**
3. Processing ceased for withdrawn consent purposes within **10 business days**
4. Consent record updated with withdrawal date, method, and staff reference
5. Marketing lists / processing systems updated
6. Confirmation sent to data subject that withdrawal has been actioned
7. If withdrawal results in inability to provide a service, data subject notified

### 7.3 What Happens After Withdrawal

- PII processed solely on the basis of withdrawn consent must cease to be processed for that purpose
- If another legal basis exists for the same processing, it must be identified and the data subject informed
- Withdrawal does not affect the lawfulness of processing carried out before withdrawal
- Withdrawn consent records are retained to demonstrate compliance (retained as evidence, not for further processing)

---

## 8. Consent Refresh and Re-Consent

Consent must be refreshed when:

| Trigger | Action |
|---------|--------|
| Privacy notice materially updated (new processing purposes) | Re-consent required for affected processing activities |
| More than 3 years since original consent obtained | Proactive re-consent campaign recommended |
| Consent obtained in non-compliant manner identified in audit | Re-consent campaign required immediately |
| Change in third-party recipients not covered by original consent | Re-consent or use alternative legal basis |
| Post-Brexit / regulatory change affects transfer mechanisms | Re-consent if SCCs or other basis affected |

---

## 9. Consent Audits

The DPO shall conduct a consent audit **annually** covering:
- Review of all active consent records for completeness and validity
- Verification that consent mechanisms meet current standards
- Assessment of consent withdrawal rates and common withdrawal reasons
- Review of opt-in/opt-out rates as quality indicators
- Identification of any processing activities with no valid consent record

Audit findings are documented and presented at the Management Review.

---

## 10. Special Category Data — Explicit Consent Requirements

For special category processing under GDPR Article 9 (health, racial/ethnic origin, biometric, genetic, religious, political, trade union, sexual orientation), explicit consent must:
- Use the word "explicit" or "express" in the consent request language
- Clearly identify the special category being processed
- Be obtained separately from other consents
- Be logged with enhanced audit trail
- Never be obtained via pre-ticked boxes or implied agreement

---

## 11. Staff Responsibilities

| Role | Responsibility |
|------|---------------|
| **DPO** | Oversee consent management; approve consent wording and mechanisms; conduct annual audit |
| **Marketing Team** | Implement consent in all campaigns; maintain suppression lists; report withdrawal rates |
| **IT / Web Team** | Maintain CMP; ensure consent records are captured and stored; implement withdrawal automation |
| **Customer Service** | Handle withdrawal requests; escalate complex cases to DPO; document verbal consent |
| **All Staff** | Never process PII beyond the scope of consent given; report suspected consent violations |

---

## 12. Record of Changes

| Version | Date | Author | Change Description |
|---------|------|--------|--------------------|
| 1.0 | 2025-01-01 | DPO | Initial release |

---

*ISO/IEC 27701:2025 PIMS Toolkit | Consent Management Procedure | PIMS-OPS-005*
