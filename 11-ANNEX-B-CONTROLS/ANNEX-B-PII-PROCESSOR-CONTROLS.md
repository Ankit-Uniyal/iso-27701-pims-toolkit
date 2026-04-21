# Annex B — PII Processor Controls: Implementation Reference

| Field | Detail |
|-------|--------|
| **Document ID** | PIMS-ANNEXB-B8-001 |
| **Version** | 2.0 |
| **Date** | April 2025 |
| **Standard** | ISO/IEC 27701:2025 — Annex B (B.8) |
| **Applies To** | PII Processors |
| **Classification** | Internal |

---

## B.8 — PII Processor Obligations

This section provides implementation guidance for all Annex B controls applicable to organisations acting as PII Processors.

> **Reminder:** A PII Processor is an organisation that processes personal data/PII on behalf of a PII Controller. If you act as both controller AND processor, **both Annex A and Annex B apply** depending on the activity.

---

### B.8.1 — Conditions for Collection and Processing

#### B.8.1.1 — Processing only on documented controller instructions

**Requirement:** The processor shall process PII only on the documented, written instructions of the controller.

**Implementation guidance:**
- Data Processing Agreement (DPA) is the primary source of controller instructions
- Instructions must be received in writing before processing commences
- If controller gives verbal instructions, document and confirm in writing
- Processor must notify controller if instructions appear to infringe applicable law
- Processor must not act outside the scope of the DPA

**Key DPA provisions:**
- Subject matter and duration of processing
- Nature and purpose of processing
- Type of PII and categories of data subjects
- Controller's obligations and rights
- Processor's specific instructions

**Evidence:** Signed DPA with all mandatory provisions; instruction register; email confirmations for ad hoc instructions.

**GDPR mapping:** Art. 28(3)(a)

---

#### B.8.1.2 — Purposes limited to controller instructions

**Requirement:** The processor shall process PII only for the purposes specified in the controller's instructions and DPA.

**Implementation guidance:**
- Technical access controls limiting use of PII to contracted purposes
- Staff briefing on purpose limitations
- Alert process if controller instructs processing that may conflict with applicable law

**Evidence:** System access controls documentation; staff confidentiality training records.

**GDPR mapping:** Art. 28(3)

---

#### B.8.1.3 — Marketing and advertising restrictions

**Requirement:** The processor shall not use PII processed on behalf of a controller for the processor's own marketing or advertising purposes without explicit controller authorisation.

**Implementation guidance:**
- Technical and policy controls preventing PII from being used for own marketing
- Include prohibition in processor internal policies
- Audit controls to detect misuse

**Evidence:** Internal privacy policy; technical controls documentation; staff training.

---

#### B.8.1.4 — Sub-processor engagement

**Requirement:** The processor shall not engage sub-processors without prior specific or general written authorisation from the controller, and shall ensure equivalent DPA obligations are imposed on sub-processors.

**Implementation guidance:**
- DPA must specify whether general or specific sub-processor authorisation is granted
- Sub-processor register maintained and provided to controller
- New sub-processors: notify controller with opportunity to object
- Sub-processor DPAs must include all equivalent Art. 28 requirements
- Processor remains liable to controller for sub-processor's compliance

**Evidence:** Sub-processor register; sub-processor DPAs; controller notifications; general authorisation clause in DPA.

**GDPR mapping:** Art. 28(4)

---

### B.8.2 — Privacy Obligations

#### B.8.2.1 — Obligations to PII principals (processor)

**Requirement:** The processor shall provide assistance to the controller to fulfil the controller's obligations to data subjects.

**Implementation guidance:**
- Technical measures to support DSARs (data exports, deletion, rectification)
- Forward data subject requests to controller promptly
- Do not act on data subject requests directly without controller instruction
- Ensure systems support all data subject rights technically

**Evidence:** DSAR assistance procedure; data portability export capability; deletion mechanism.

**GDPR mapping:** Art. 28(3)(e)

---

#### B.8.2.2 — Legitimate purpose only

**Requirement:** The processor shall only process PII for legitimate purposes as defined in the controller's instructions.

**Implementation guidance:**
- Regular review of processing activities against DPA scope
- Change management process for new processing activities (requires controller approval)
- Technical controls preventing scope creep

**Evidence:** Periodic DPA compliance review records; change management records.

---

### B.8.3 — Privacy by Design and Privacy by Default *(Enhanced in ISO 27701:2025)*

#### B.8.3.1 — Privacy by design (processor standalone) *(NEW in ISO 27701:2025)*

**Requirement:** The processor shall implement privacy by design in its systems, services, and processing operations, aligned to ISO/IEC 31700:2023.

**Why added in 2025:** Processors increasingly design platforms and services used by multiple controllers. Privacy must be embedded in the design of these services, not just in the contractual DPA.

**Implementation guidance (ISO 31700:2023 aligned):**
- Privacy requirements embedded in product/service architecture from design phase
- Privacy impact review for all new processing capabilities
- Pseudonymisation and encryption by default in processor platform
- Data minimisation in processor system design (only collect what is needed operationally)
- Separation of processor operational data from controller PII data
- Audit logging of PII access by processor staff

**Evidence:** System architecture documentation showing privacy controls; Privacy by Design procedure; technical security documentation.

**GDPR mapping:** Art. 25, 32

---

#### B.8.3.2 — Temporary files (processor) *(NEW in ISO 27701:2025)*

**Requirement:** Temporary files created during processing operations shall be identified, managed, and deleted according to defined schedules.

**Implementation guidance:**
- Map all locations where temporary PII files are created (processing queues, logs, caches, backups, staging areas)
- Define retention/deletion schedule for each temporary file type
- Automated deletion where possible
- Include in DPA: temporary file handling obligations

**Evidence:** Temporary file inventory; automated cleanup schedule; system configuration.

---

#### B.8.3.3 — Return, transfer or disposal of PII (processor)

**Requirement:** At the end of the processing relationship, the processor shall return PII to the controller or securely delete it, as instructed by the controller, and provide evidence of disposal.

**Implementation guidance:**
- End-of-contract procedure defined in DPA
- Secure deletion of all PII copies (including backups) within agreed timeframe
- Deletion certificate issued to controller
- Evidence retained by processor for defined period

**Evidence:** End-of-contract DPA provisions; deletion certificates; disposal records.

**GDPR mapping:** Art. 28(3)(g)

---

### B.8.4 — Processor Obligations to Controller

#### B.8.4.1 — Assistance for data subject rights

**Requirement:** The processor shall assist the controller in responding to requests from data subjects exercising their rights, by implementing appropriate technical and organisational measures.

**Implementation guidance:**
- DSAR support: ability to search for and export individual data subject's PII
- Erasure: ability to delete or irreversibly anonymise specific individual's data
- Portability: ability to export in machine-readable format
- Rectification: ability to update specific PII fields
- Response to controller within agreed service level (typically 5 working days)

**Evidence:** Technical capability documentation; DSAR assistance SLA in DPA; test records.

**GDPR mapping:** Art. 28(3)(e)

---

#### B.8.4.2 — Notification of data subject requests

**Requirement:** The processor shall notify the controller promptly when it receives requests directly from data subjects, without acting on the request without controller instructions.

**Implementation guidance:**
- Forward DSARs to controller immediately (same day)
- Do not acknowledge or respond to data subject directly without controller instruction
- Log all data subject contacts

**Evidence:** Data subject request forwarding procedure; forwarding log.

---

#### B.8.4.3 — Privacy/security breach notification (processor)

**Requirement:** The processor shall notify the controller of any personal data breach without undue delay after becoming aware of it.

**Implementation guidance:**
- Breach detection procedure (aligned to ISO 27001:2022 incident management)
- Initial notification to controller as soon as practicable (best practice: within 24 hours)
- Notification must include available information on: nature of breach, categories/volume of PII, likely consequences, measures taken/proposed
- Controller then assesses 72-hour regulatory notification obligation
- Full breach report to follow initial notification

**Evidence:** Breach response procedure; breach notification records; DPA breach notification provision.

**GDPR mapping:** Art. 33 (processor obligation to notify controller)

---

### B.8.5 — Cross-Border Transfers (Processor)

#### B.8.5.1 — Basis for cross-border transfer (processor)

**Requirement:** The processor shall only transfer PII to third countries as authorised by the controller and using approved transfer mechanisms.

**Implementation guidance:**
- DPA must specify permitted transfer destinations and mechanisms
- No transfers to non-authorised countries without prior written controller approval
- If sub-processors are in third countries, adequate safeguards required (SCCs/BCRs)
- **Transfer Impact Assessment (TIA)** may be required by controller — processor must assist

**Evidence:** DPA transfer provisions; sub-processor DPAs with transfer mechanisms; TIA assistance records.

**GDPR mapping:** Art. 44

---

#### B.8.5.2 — Countries and international organisations

**Requirement:** Transfer destinations shall be documented and restricted to those authorised by the controller in the DPA.

**Evidence:** Transfer register; sub-processor register with countries; DPA authorised destinations list.

---

#### B.8.5.3 — Records of cross-border PII transfers (processor)

**Requirement:** The processor shall maintain records of cross-border PII transfers for the controller and regulatory review.

**Evidence:** Transfer log with dates, destinations, transfer mechanism, volume; Art. 30(2) GDPR records.

**GDPR mapping:** Art. 30(2)

---

### B.8.6 — Audit and Compliance *(Enhanced in ISO 27701:2025)*

#### B.8.6.1 — Audit rights *(NEW standalone control in ISO 27701:2025)*

**Requirement:** The processor shall explicitly support the controller's audit rights, including by making available all information necessary to demonstrate compliance and allowing and contributing to audits.

**Why added in 2025:** GDPR Art. 28(3)(h) mandates audit rights in DPAs but this was not a standalone control in 2019. The 2025 edition elevates this to an explicit Annex B control.

**Implementation guidance:**
- DPA must include audit rights provision (right to audit with reasonable notice)
- Processor must maintain compliance documentation available for controller review
- Third-party audit reports (SOC 2, ISO 27001 certificate) provided to controllers
- Physical audit access facilitated with reasonable notice
- Audit support team or DPA point of contact designated

**Evidence:** DPA audit rights clause; ISO 27001 certification; SOC 2 report; audit support procedure.

**GDPR mapping:** Art. 28(3)(h)

---

#### B.8.6.2 — Assistance for regulatory audits *(NEW in ISO 27701:2025)*

**Requirement:** The processor shall assist the controller in facilitating inspections and investigations by supervisory authorities.

**Implementation guidance:**
- Point of contact for regulatory inspections designated
- Cooperation procedure defined
- Relevant records and documentation retrievable within defined timeframe
- Include in DPA: obligation to cooperate with supervisory authorities

**Evidence:** Regulatory cooperation procedure; DPA cooperation clause; designated contact.

**GDPR mapping:** Art. 31

---

## Version History

| Version | Date | Description |
|---------|------|-------------|
| 2.0 | April 2025 | Updated for ISO/IEC 27701:2025 — new controls: B.8.3.1 (Privacy by Design standalone), B.8.3.2 (temporary files), B.8.6.1/B.8.6.2 (audit rights). Replaced wrong gap checklist content from prior commit. Full implementation guidance added. |
| 1.0 | 2024 | Initial release — ISO/IEC 27701:2019 |

---

*ISO/IEC 27701:2025 PIMS Toolkit | Annex B Implementation Reference | PIMS-ANNEXB-B8-001 | v2.0 | Classification: Internal*
