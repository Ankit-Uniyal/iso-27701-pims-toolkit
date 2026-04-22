# Data Protection Impact Assessment (DPIA) Template

| Field | Detail |
|---|---|
| **Document ID** | PIMS-OPS-002 |
| **Version** | 2.0 |
| **Date** | April 2025 |
| **Owner** | Data Protection Officer |
| **Classification** | Confidential — Internal Use |
| **Review Date** | April 2026 |
| **Standard** | ISO/IEC 27701:2025 — Clause A.7.2.5; GDPR Art. 35-36 |

---

## Purpose

This template is used to conduct a Data Protection Impact Assessment (DPIA) for processing activities that are likely to result in a high risk to the rights and freedoms of data subjects.

ISO/IEC 27701:2025 (control A.7.2.5) requires DPIAs for high-risk processing, with prescriptive trigger criteria. GDPR Art. 35 requires DPIAs before commencing high-risk processing. This template satisfies both requirements.

**How to use this template:**
1. Complete the Screening (Section 1) to confirm a DPIA is required.
2. Work through Sections 2-7 with the process owner, IT, and Legal.
3. Obtain DPO sign-off (Section 8) before the processing activity commences or continues.
4. File the completed DPIA in the DPIA Register and link it in the ROPA.

---

## PART A - DPIA SCREENING

### Section 1: DPIA Trigger Criteria (ISO 27701:2025 A.7.2.5)

A DPIA is **mandatory** if ANY of the following triggers apply:

| # | Trigger | Applies? |
|---|---|---|
| T1 | Systematic or large-scale profiling / evaluation of personal aspects | Yes / No |
| T2 | Large-scale processing of special category data | Yes / No |
| T3 | Systematic monitoring of publicly accessible areas | Yes / No |
| T4 | Novel or innovative technology (AI/ML, facial recognition, IoT, biometrics) | Yes / No |
| T5 | Automated decision-making producing legal or similarly significant effects | Yes / No |
| T6 | Processing that could deny individuals access to services or rights | Yes / No |
| T7 | Cross-matching datasets from two or more sources unexpectedly | Yes / No |
| T8 | Processing of vulnerable individuals (children, employees, patients) | Yes / No |
| T9 | Cross-border transfer without adequacy decision (TIA also required) | Yes / No |
| T10 | Scoring or ranking individuals based on personal data | Yes / No |
| T11 | High-volume processing not otherwise captured above | Yes / No |
| T12 | Supervisory authority has listed this processing as always requiring DPIA | Yes / No |

**Screening Outcome:** One or more triggers = DPIA required. Proceed to Part B.

**Screening completed by:** ___________________________
**Date:** _______________
**DPO consulted:** Yes / No

---

## PART B - FULL DPIA

### Section 2: Processing Activity Description

| Field | Detail |
|---|---|
| **DPIA Reference** | DPIA-[YYYY]-[NNN] |
| **DPIA Date** | |
| **DPIA Author** | |
| **Processing Activity Name** | |
| **ROPA Reference** | |
| **Related Project / System** | |
| **Processing Status** | New / Existing / Significant Change |
| **Processing Commencement Date** | |
| **DPO Assigned** | |

#### 2.1 Description of Processing Activity

[Enter detailed description of the processing activity - what data is processed, by whom, how, and for what purpose]

#### 2.2 Nature of Processing

| Field | Detail |
|---|---|
| **Operations** | Collection / Storage / Use / Disclosure / Erasure / Other |
| **Frequency** | Continuous / Regular / One-off / Ad hoc |
| **Duration** | |
| **Geographic Scope** | |
| **Systems / Applications Involved** | |
| **Third Parties Involved** | |

#### 2.3 Purpose(s) and Legal Basis

| Purpose | Legal Basis (GDPR Art. 6) | Additional Condition (Art. 9 if special category) |
|---|---|---|
| | | |
| | | |

#### 2.4 Categories of PII

| Data Category | Special Category? | Volume / Scale | Sensitivity |
|---|---|---|---|
| | Yes / No | | Low / Medium / High |
| | Yes / No | | Low / Medium / High |
| | Yes / No | | Low / Medium / High |

#### 2.5 Categories of Data Subjects

| Data Subject Category | Vulnerable? | Estimated Volume |
|---|---|---|
| | Yes / No | |
| | Yes / No | |

#### 2.6 Recipients and Third Parties

| Recipient | Role | Country | DPA in Place? |
|---|---|---|---|
| | Controller / Processor / Joint Controller | | Yes / No |
| | Controller / Processor / Joint Controller | | Yes / No |

#### 2.7 Joint Controller Arrangements (ISO 27701:2025 A.7.2.7)

| Field | Detail |
|---|---|
| Joint Controller identified? | Yes / No |
| Joint Controller name | |
| Joint Controller Agreement (JCA) in place? | Yes / No / In progress |
| JCA Reference | |
| Responsibilities allocated in JCA? | Yes / No |

---

### Section 3: Necessity and Proportionality Assessment

| Assessment Area | Finding | Notes |
|---|---|---|
| Purpose is specific, explicit and legitimate | Yes / No | |
| Processing is necessary and proportionate to purpose | Yes / No | |
| Less privacy-invasive alternative considered | Yes / No | |
| Data minimisation applied to all data fields | Yes / Partial / No | |
| Pseudonymisation or anonymisation considered | Yes / No | |
| Retention period defined | Yes / No | Period: |
| Privacy by Default applied (A.7.2.8) | Yes / No | |

#### 3.1 Data Subject Rights Feasibility

| Right | Technically Feasible? | Procedure in Place? | Notes |
|---|---|---|---|
| Access (DSAR) | Yes / No | Yes / No | |
| Rectification | Yes / No | Yes / No | |
| Erasure | Yes / No | Yes / No | |
| Restriction | Yes / No | Yes / No | |
| Portability | Yes / No | Yes / No | |
| Objection | Yes / No | Yes / No | |
| Automated decision-making (Art. 22) | Yes / No / N/A | Yes / No / N/A | |

---

### Section 4: Privacy Risk Assessment

**Scoring: Risk Score = Likelihood (1-5) x Impact (1-5)**

**Likelihood Scale:**

| Score | Level | Description |
|---|---|---|
| 1 | Very Low | Unlikely; strong controls in place; no precedent |
| 2 | Low | Could occur; partial controls; limited history |
| 3 | Medium | Might occur periodically; moderate controls |
| 4 | High | Likely to occur; weak controls; recurring issues |
| 5 | Very High | Almost certain; minimal controls; active threat |

**Impact Scale (Harm to Individuals):**

| Score | Level | Description |
|---|---|---|
| 1 | Negligible | No real harm to individuals; inconvenience only |
| 2 | Minor | Temporary embarrassment or minor data quality issue |
| 3 | Moderate | Discrimination, financial loss, reputational damage |
| 4 | Major | Identity theft, employment consequences, serious financial harm |
| 5 | Severe | Physical danger, severe discrimination, major financial ruin |

**Risk Rating Thresholds:**

| Score Range | Rating | Required Action |
|---|---|---|
| 20-25 | CRITICAL | Halt/suspend processing; immediate DPO escalation; mandatory treatment |
| 12-19 | HIGH | Documented treatment plan within 30 days; DPO informed |
| 6-11 | MEDIUM | Treatment plan required; review at next management meeting |
| 2-5 | LOW | Accept with monitoring; review annually |
| 1 | MINIMAL | Accept; note in register; no further action |

#### 4.1 Risk Register for This Processing Activity

| Risk ID | Risk Description | Threat Source | Likelihood (1-5) | Impact (1-5) | Score | Rating | Proposed Mitigation | Residual L | Residual I | Residual Score | Residual Rating |
|---|---|---|---|---|---|---|---|---|---|---|---|
| DPIA-R01 | | | | | | | | | | | |
| DPIA-R02 | | | | | | | | | | | |
| DPIA-R03 | | | | | | | | | | | |
| DPIA-R04 | | | | | | | | | | | |
| DPIA-R05 | | | | | | | | | | | |

*(Add rows as needed. Use common threat categories: unauthorised access, unlawful processing, inaccuracy, excessive retention, cross-border violations, third-party failures, rights failures, consent failures, automated decision-making risks, physical threats)*

---

### Section 5: Controls and Mitigations

| Control # | Type | Description | Addresses Risk(s) | Owner | Target Date | Status |
|---|---|---|---|---|---|---|
| C01 | Technical | | | | | Implemented / Planned |
| C02 | Organisational | | | | | Implemented / Planned |
| C03 | Technical | | | | | Implemented / Planned |
| C04 | Contractual | | | | | Implemented / Planned |
| C05 | Organisational | | | | | Implemented / Planned |

*(Add rows as needed)*

#### 5.1 Privacy by Design and Default Checklist (A.7.2.8 / ISO 31700:2023)

| Check | Confirmed? | Notes |
|---|---|---|
| Data minimisation applied in system design - only necessary fields collected | Yes / No | |
| Privacy settings default to most protective option for users | Yes / No | |
| Marketing and analytics tracking off by default | Yes / No | |
| Third-party sharing off by default | Yes / No | |
| Pseudonymisation or anonymisation applied where possible | Yes / No | |
| Encryption at rest and in transit implemented | Yes / No | |
| Access controls and audit logging in place | Yes / No | |
| Data subject rights technically supported in the system | Yes / No | |

---

### Section 6: Consultation

#### 6.1 Internal Consultation

| Stakeholder | Consulted? | Date | Key Feedback / Concerns |
|---|---|---|---|
| Data Protection Officer | Yes / No | | |
| IT / Security | Yes / No | | |
| Legal / Compliance | Yes / No | | |
| Business / Process Owner | Yes / No | | |
| HR (if employee data involved) | Yes / No / N/A | | |
| Procurement (if third parties involved) | Yes / No / N/A | | |

#### 6.2 Data Subject Consultation

| Question | Response |
|---|---|
| Were data subjects or their representatives consulted? | Yes / No |
| If no, justification for not consulting | |
| If yes, summary of outcomes | |

#### 6.3 Supervisory Authority Prior Consultation (GDPR Art. 36)

| Question | Response |
|---|---|
| After applying all controls, does HIGH or CRITICAL residual risk remain? | Yes / No |
| If yes - prior consultation with supervisory authority is REQUIRED before processing commences | Consultation initiated / Not yet initiated |
| Supervisory Authority (e.g., ICO, CNIL, etc.) | |
| SA Reference Number | |
| Consultation outcome / date | |

---

### Section 7: DPIA Outcome and Recommendation

#### 7.1 Overall Residual Risk Summary

| Risk ID | Risk Description | Residual Score | Residual Rating | Acceptable? |
|---|---|---|---|---|
| DPIA-R01 | | | | Yes / No |
| DPIA-R02 | | | | Yes / No |
| DPIA-R03 | | | | Yes / No |

#### 7.2 Recommendation

| Outcome | Decision |
|---|---|
| **PROCEED** - All residual risks are acceptable; all controls implemented or planned with firm dates | |
| **PROCEED WITH CONDITIONS** - Processing may commence only once the conditions listed below are met | |
| **DO NOT PROCEED** - Critical/High residual risks remain that cannot be adequately mitigated | |

**Selected recommendation:** ___________________________

**Conditions for proceeding (if applicable):**

| # | Condition / Outstanding Control | Owner | Deadline |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |

---

### Section 8: DPO Review and Sign-Off

| Field | Detail |
|---|---|
| **DPO Name** | |
| **DPO Review Date** | |
| **DPO Decision** | Approved / Approved with conditions / Rejected |
| **DPO Conditions (if any)** | |
| **DPO Signature** | ___________________________ |
| **Date of Sign-Off** | |

> The DPO must be consulted on ALL DPIAs. Where the DPO's recommendations are not followed, the controller must document its reasons (GDPR Art. 35(2)).

---

### Section 9: Review and Monitoring

DPIAs must be reviewed when:
- The processing activity changes materially
- A privacy breach occurs related to this activity
- Regulatory guidance changes relevant to this type of processing
- At least every **3 years** for ongoing high-risk processing activities

| Review Date | Reviewer | Material Changes Noted | DPIA Update Required? | Outcome |
|---|---|---|---|---|
| | | | Yes / No | |
| | | | Yes / No | |

---

### Section 10: DPIA Register Entry

Upon completion, record this DPIA in the central DPIA Register:

| Field | Detail |
|---|---|
| DPIA Reference | |
| Processing Activity Name | |
| ROPA Reference | |
| DPIA Completion Date | |
| DPO Sign-off Date | |
| Outcome | Proceed / Proceed with conditions / Do not proceed |
| Conditions Outstanding | |
| Next Review Date | |
| Location of Full DPIA Document | |

---

## Version History

| Version | Date | Description |
|---|---|---|
| 2.0 | April 2025 | Full rewrite for ISO/IEC 27701:2025 - prescriptive trigger criteria (A.7.2.5), joint controller section (A.7.2.7), Privacy by Default checklist (A.7.2.8), ISO 31700:2023 alignment, 5x5 risk matrix aligned with Privacy Risk Assessment Methodology (PIMS-PLN-003), GDPR Art. 36 regulatory consultation threshold, TIA cross-reference for cross-border transfers |
| 1.0 | 2024 | Initial release - ISO/IEC 27701:2019 |

---

*ISO/IEC 27701:2025 PIMS Toolkit | Data Protection Impact Assessment Template | PIMS-OPS-002 | v2.0 | Classification: Confidential*
