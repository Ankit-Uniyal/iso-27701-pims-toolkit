# Annex A — PII Controller Controls: Implementation Reference

| Field | Detail |
|-------|--------|
| **Document ID** | PIMS-ANNEXA-A7A8-001 |
| **Version** | 2.0 |
| **Date** | April 2025 |
| **Standard** | ISO/IEC 27701:2025 — Annex A (A.7 and A.8) |
| **Applies To** | PII Controllers |
| **Classification** | Internal |

---

## A.7 — Conditions for Collection and Processing

This section provides implementation guidance for all A.7 controls.

---

### A.7.2 — Identify and Document Purpose

#### A.7.2.1 — Identify and document the purposes of PII processing

**Requirement:** The organisation shall identify and document the specific purposes for which PII is collected and processed.

**Implementation guidance:**
- Document purposes in the Records of Processing Activities (ROPA)
- Purposes must be specific, explicit, and legitimate (not vague, e.g., "improve services")
- Each processing activity in the ROPA must have a stated purpose
- Purposes must be communicated to data subjects in the Privacy Notice

**Evidence:** ROPA with purpose column populated for all activities; Privacy Notice referencing purposes.

**GDPR mapping:** Art. 5(1)(b) — purpose limitation principle

---

#### A.7.2.2 — Identify the lawful basis for processing

**Requirement:** The organisation shall identify and document the lawful basis for each processing activity.

**Implementation guidance:**
- One of the six GDPR lawful bases must be identified per activity (or equivalent national law basis)
- Basis documented in ROPA
- Legal basis assessed by Legal/DPO before processing commences
- Special category data requires an additional condition (Art. 9 GDPR)

**Common bases:** Contract performance, Legal obligation, Legitimate interests (with LIA), Consent

**Evidence:** ROPA with legal basis column; Legitimate Interests Assessments (LIAs) where applicable.

**GDPR mapping:** Art. 6

---

#### A.7.2.3 — Determine when and how consent is to be obtained

**Requirement:** Where consent is used as the lawful basis, the organisation shall determine when and how consent is to be obtained before processing commences.

**Implementation guidance:**
- Define consent mechanism for each consent-based activity (web form, paper, verbal)
- Consent must be freely given, specific, informed, and unambiguous
- Granular consent required for different purposes (no blanket consent)
- Record how consent will be evidenced

**Evidence:** Consent design documentation; CMP configuration; privacy notice referencing consent.

**GDPR mapping:** Art. 7

---

#### A.7.2.4 — Obtain and record consent

**Requirement:** The organisation shall obtain consent from PII principals in accordance with the determined mechanism and maintain records of consent.

**Implementation guidance:**
- Implement CMP or consent tracking system
- Record: who consented, what they consented to, when, and how (audit trail)
- Consent records retained for the duration of processing + limitation period
- Consent records must be retrievable per individual

**Evidence:** Consent database/CMP records; consent timestamps and version tracking.

**GDPR mapping:** Art. 7

---

#### A.7.2.5 — Privacy impact assessment (DPIA)

**Requirement (2025 enhanced):** The organisation shall conduct DPIAs for processing activities that are likely to result in a high risk to data subjects.

**2025 trigger criteria (prescriptive):** DPIA mandatory when processing involves:
- Systematic profiling
- Special categories at scale
- Systematic monitoring of public areas
- New/innovative technologies (AI, biometrics, IoT)
- Cross-matching of datasets
- Vulnerable data subjects
- Automated decisions that produce legal/significant effects
- Large-scale transfer without adequacy decision (TIA also required)

**Evidence:** Completed DPIA records with DPO sign-off; DPIA trigger screening log.

**GDPR mapping:** Art. 35

---

#### A.7.2.6 — Contracts with PII processors

**Requirement:** The organisation shall ensure written agreements (DPAs) are in place with all processors, covering all requirements.

**Implementation guidance:**
- DPA required for every processor relationship
- DPA must cover all Art. 28(3) GDPR mandatory provisions
- Sub-processor provisions included
- Regular review cycle for DPAs

**Evidence:** Signed DPAs for all processors; processor register with DPA status.

**GDPR mapping:** Art. 28

---

#### A.7.2.7 — Joint PII controller arrangements *(NEW in ISO 27701:2025)*

**Requirement:** Where two or more organisations jointly determine the purposes and means of processing, their respective responsibilities shall be documented in a written joint controller agreement.

**Implementation guidance:**
- Identify all joint controller relationships (common in platforms, partnerships, group entities)
- Execute Joint Controller Agreement (JCA) covering:
  - Division of responsibilities for GDPR obligations
  - Point of contact for data subjects
  - Which entity handles DSARs/breach notifications
  - Information to be provided in Privacy Notices
- JCA must be available to data subjects on request (substance/key points)

**Evidence:** Signed Joint Controller Agreements; privacy notice referencing joint controllership.

**GDPR mapping:** Art. 26

---

#### A.7.2.8 — Privacy by default *(NEW standalone control in ISO 27701:2025)*

**Requirement:** The organisation shall implement technical and organisational measures to ensure that, by default, only PII that is necessary for each specific purpose is processed.

**Aligned to:** ISO/IEC 31700:2023 (Privacy by Design); GDPR Art. 25

**Implementation guidance:**
- Systems must default to maximum privacy-protective settings
- Users must opt-in to share more data, not opt-out to share less
- No pre-ticked consent boxes
- Profiling, analytics, and tracking off by default
- Third-party data sharing off by default
- Privacy by Design Procedure must embed this control in SDLC

**Evidence:** Privacy by Default checklist per system; Privacy by Design Procedure; system configuration documentation.

**GDPR mapping:** Art. 25

---

### A.7.3 — PII Minimisation

#### A.7.3.1 — Limit collection to what is necessary

**Requirement:** PII collected and processed shall be limited to what is adequate, relevant, and necessary for the identified purposes.

**Implementation guidance:**
- Review data fields collected for each activity — remove unnecessary fields
- Data minimisation review as part of DPIA and Privacy by Design
- Periodic data audit to identify and remove over-collected data

**Evidence:** Data architecture review records; DPIA data minimisation section.

**GDPR mapping:** Art. 5(1)(c)

---

#### A.7.3.2 — Limit processing to identified purposes

**Requirement:** PII shall not be processed in ways incompatible with the purposes for which it was collected.

**Implementation guidance:**
- Purpose compatibility assessment before using PII for new purposes
- Technical controls preventing PII use outside approved systems
- Staff training on purpose limitation

**Evidence:** Purpose limitation policy; technical access controls configuration.

**GDPR mapping:** Art. 5(1)(b)

---

#### A.7.3.3 — Accuracy of PII

**Requirement:** PII shall be kept accurate and up to date, with inaccurate data erased or rectified without delay.

**Implementation guidance:**
- Data quality controls in systems (validation, mandatory fields)
- Self-service update mechanisms for data subjects
- Periodic data quality reviews
- Process to action rectification requests

**Evidence:** Data quality procedure; rectification request log; system validation documentation.

**GDPR mapping:** Art. 5(1)(d)

---

#### A.7.3.4 — Retention and disposal

**Requirement:** PII shall not be kept longer than necessary; retention periods shall be defined, implemented, and enforced.

**Implementation guidance:**
- Retention schedule published for all PII categories
- Automated deletion/archiving where possible
- Secure disposal procedure for physical and digital PII
- Disposal records maintained

**Evidence:** Retention schedule; disposal records; system configuration for automated deletion.

**GDPR mapping:** Art. 5(1)(e)

---

### A.7.4 — PII De-identification and Deletion *(Expanded in ISO 27701:2025)*

#### A.7.4.1 — De-identification and anonymisation

**Requirement:** The organisation shall apply pseudonymisation or anonymisation techniques where appropriate to reduce privacy risk.

**Implementation guidance:**
- Identify where pseudonymisation/anonymisation reduces risk without defeating purpose
- Apply to: analytics datasets, test/dev environments, research data
- Anonymisation must be irreversible to qualify (pseudonymisation is reversible but still valuable)
- Document de-identification techniques used

**Evidence:** Data architecture documentation; de-identification procedure; test environment configuration.

---

#### A.7.4.2 — Temporary files

**Requirement:** Temporary files created during PII processing shall be identified, managed, and deleted in accordance with retention schedules.

**Implementation guidance:**
- Identify all temp file locations (processing queues, caches, logs, backups)
- Apply retention controls to temp files
- Automated cleanup where possible

**Evidence:** IT architecture showing temp file management; automated cleanup schedule.

---

#### A.7.4.3 — Return, transfer or disposal of PII at end of processing

**Requirement:** At the end of the processing agreement or relationship, PII shall be returned to the controller, transferred, or securely disposed of, with evidence provided.

**Implementation guidance:**
- Define end-of-contract procedure in DPAs
- Secure deletion certification available
- Transfer mechanism documented where data is handed back
- Disposal records retained

**Evidence:** End-of-contract PII disposal/return records; deletion certificates.

---

### A.7.5 — PII Disclosure Controls *(NEW in ISO 27701:2025)*

#### A.7.5.1 — Basis for PII transfer to third parties

**Requirement:** The organisation shall only transfer PII to third parties where a documented lawful basis exists for the transfer.

**Implementation guidance:**
- All third-party transfers documented in ROPA
- Transfer basis documented (contractual necessity, consent, legitimate interest)
- Cross-border transfers: adequacy decision OR appropriate safeguards (SCCs, BCRs)
- **Transfer Impact Assessment (TIA)** required where no adequacy decision applies

**Evidence:** ROPA with transfer destinations; TIA records; SCCs/BCR documentation.

**GDPR mapping:** Art. 44–49

---

#### A.7.5.2 — Records of PII disclosure to third parties

**Requirement:** A register of all PII disclosures to third parties shall be maintained.

**Implementation guidance:**
- Third-party disclosure register maintained (part of ROPA Art. 30)
- Record: recipient, category of PII, purpose, legal basis, transfer mechanism, date
- Cross-border transfer register separate entry

**Evidence:** ROPA Art. 30 records; cross-border transfer register.

**GDPR mapping:** Art. 30

---

#### A.7.5.3 — Notification of legally-binding disclosure requests

**Requirement:** The organisation shall have a process for handling legally-binding disclosure requests from law enforcement, regulators, or courts.

**Implementation guidance:**
- Defined process for receiving and assessing LE disclosure requests
- Legal review required before disclosure
- Notification to data subjects where legally permissible
- Records of all disclosure requests maintained

**Evidence:** LE request handling procedure; disclosure request log.

**GDPR mapping:** Art. 23

---

### A.7.6 — Privacy Notices

#### A.7.6.1 — Provide privacy notice to PII principals

**Requirement:** The organisation shall provide a privacy notice to data subjects that is accessible, clear, accurate, and covers all required elements.

**Required elements (GDPR Art. 13/14):**
- Identity and contact details of controller
- DPO contact details
- Purposes and legal basis for each processing activity
- Legitimate interests (where applicable)
- Recipients and transfers
- Retention periods
- Data subject rights
- Right to withdraw consent
- Right to lodge a complaint with supervisory authority

**Evidence:** Published Privacy Notice; version history; annual review record.

**GDPR mapping:** Art. 13–14

---

## A.8 — Obligations to PII Principals

### A.8.1 — Obligations

#### A.8.1.1 — Determine and document obligations to PII principals

**Requirement:** The organisation shall determine the privacy obligations owed to data subjects and establish procedures to fulfil them.

**Implementation guidance:**
- Map all applicable data subject rights for each jurisdiction
- Document procedures for each right
- Allocate ownership for each right to a named role
- Track response timelines per right

**Evidence:** Data Subject Rights Procedure; rights inventory; DSAR response log.

**GDPR mapping:** Art. 12–22

---

### A.8.2 — Access, Correction, Erasure

#### A.8.2.1 — Right of access | A.8.2.2 — Right to rectification | A.8.2.3 — Right to erasure

See **DATA-SUBJECT-RIGHTS-PROCEDURE.md** in `07-CLAUSE8-OPERATION/` for full procedure.

| Right | Deadline | Procedure |
|-------|----------|-----------|
| Access (DSAR) | 30 days (GDPR) | Verify identity, locate data, compile response |
| Rectification | Without undue delay | Verify, correct, notify third parties |
| Erasure | Without undue delay | Verify basis, delete across systems, notify |
| Portability | 30 days | Machine-readable format export |
| Object | Without undue delay | Assess, suspend processing if upheld |
| Restriction | Without undue delay | Flag and restrict processing |

---

#### A.8.2.6 — Automated decision-making and profiling *(NEW in ISO 27701:2025)*

**Requirement:** The organisation shall implement safeguards for data subjects subject to solely automated decisions that produce legal or similarly significant effects.

**Implementation guidance:**
- Identify all automated decision-making processes (credit scoring, fraud detection, HR screening, etc.)
- Provide right to human review for significant automated decisions
- Explain logic of automated decisions where requested
- Opt-out mechanism for profiling used for direct marketing
- DPIA mandatory for systematic profiling at scale

**Evidence:** Automated decision-making register; human review process; opt-out mechanism.

**GDPR mapping:** Art. 22

---

### A.8.3 — Consent Management

#### A.8.3.1 — Withdraw consent

**Requirement:** The organisation shall provide a mechanism for data subjects to withdraw consent that is as easy as giving it.

**Implementation guidance:**
- Unsubscribe link in all marketing communications
- Self-service preference centre
- Phone/email withdrawal mechanism
- Processing stopped promptly after withdrawal (not merely logged)

**Evidence:** Consent withdrawal mechanism; withdrawal request log; processing stop records.

---

#### A.8.3.2 — Consent refresh *(NEW in ISO 27701:2025)*

**Requirement:** Where processing relies on consent and the processing activity or privacy notice materially changes, consent shall be refreshed.

**Implementation guidance:**
- Triggers for consent refresh: change in purposes, change in data types, material change in processing
- Re-consent campaign process defined
- Old consent records archived; new consent records created
- Interim period: processing paused pending re-consent (or alternative legal basis used)

**Evidence:** Consent refresh policy; re-consent campaign records; consent version history.

---

### A.8.4 — Privacy Complaints

#### A.8.4.1 — Privacy complaints and appeals

**Requirement:** The organisation shall implement a procedure for handling privacy complaints from data subjects, including escalation to the supervisory authority.

**Implementation guidance:**
- Complaints intake mechanism (web form, email, phone)
- Acknowledgement within set timeframe
- Investigation and response process
- Escalation to supervisory authority if complaint unresolved
- Complaints log maintained

**Evidence:** Privacy complaints log; response records; supervisory authority referral process.

**GDPR mapping:** Art. 77

---

### A.8.5 — Processors

#### A.8.5.1 — Contracts with PII processors

**Requirement:** All PII processors shall be bound by written DPAs that meet the requirements of A.7.2.6 and applicable law.

See **DPA-TEMPLATE.md** in repo root for a full template.

**Evidence:** Signed DPAs for all processors; processor register.

---

## Version History

| Version | Date | Description |
|---------|------|-------------|
| 2.0 | April 2025 | Updated for ISO/IEC 27701:2025 — new controls A.7.2.7 (joint controllers), A.7.2.8 (Privacy by Default), A.7.4 (de-identification expanded), A.7.5 (disclosure controls), A.8.2.6 (automated decisions), A.8.3.2 (consent refresh). Replaced wrong content from prior commit. |
| 1.0 | 2024 | Initial release — ISO/IEC 27701:2019 |

---

*ISO/IEC 27701:2025 PIMS Toolkit | Annex A Implementation Reference | PIMS-ANNEXA-A7A8-001 | v2.0 | Classification: Internal*
