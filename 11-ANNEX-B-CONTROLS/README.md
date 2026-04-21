# Annex B — PII Processor Controls (ISO/IEC 27701:2025)

| Field | Detail |
|-------|--------|
| **Document ID** | PIMS-ANNEXB-README-001 |
| **Version** | 2.0 |
| **Date** | April 2025 |
| **Standard** | ISO/IEC 27701:2025 — Annex B |
| **Applies To** | Organisations acting as PII Processors |
| **Classification** | Public |

---

## Overview

This folder contains reference guides for **Annex B** of ISO/IEC 27701:2025 — the controls applicable to **PII Processors** (organisations that process personally identifiable information / personal data on behalf of a PII Controller).

Annex B extends the controls of ISO/IEC 27002:2022 with processor-specific privacy guidance across one main control family:

- **B.8 — PII Processor Obligations**

> **Note:** If your organisation acts as both a PII Controller and a PII Processor (common in cloud services, outsourcing, and B2B scenarios), **both Annex A and Annex B apply** — with controls applied based on the specific processing activity's role.

---

## What Changed in ISO/IEC 27701:2025 vs. 2019?

| Change Area | 2019 | 2025 |
|------------|------|------|
| Control alignment | ISO 27002:2013 | ISO 27002:2022 structure |
| Privacy by Design (processor) | Brief | **Explicit standalone control — B.8.3.1** |
| Sub-processor chain | Basic | **Enhanced sub-processor controls and DPA requirements** |
| Breach notification | Brief | **More prescriptive — timelines and content specified** |
| Cross-border transfers | Basic | **Explicit controls for transfer safeguards per controller instructions** |
| Audit rights | Referenced in DPA | **Explicit Annex B control — B.8.4.1** |
| Temporary files | Not explicit | **New control — B.8.3.2** |
| Return/disposal at contract end | Partial | **Explicit — B.8.3.3** |

---

## Annex B Control Index (ISO/IEC 27701:2025)

### B.8 — PII Processor Obligations

| Control Ref | Control Title | Key Requirement | GDPR Mapping |
|------------|--------------|----------------|-------------|
| **B.8.1 — Conditions for Collection and Processing** | | | |
| B.8.1.1 | Customer agreement / processing instructions | Processing ONLY on documented, written instructions from controller | Art. 28(3)(a) |
| B.8.1.2 | Purposes limited to controller instructions | No processing beyond contracted and instructed purposes | Art. 28(3) |
| B.8.1.3 | Marketing and advertising restrictions | Processor must not use PII for own marketing without controller authorisation | Art. 28 |
| B.8.1.4 | Sub-processor engagement | Sub-processors only used with controller authorisation; equivalent DPAs required | Art. 28(4) |
| **B.8.2 — Privacy Obligations** | | | |
| B.8.2.1 | Obligations to PII principals (processor role) | Assistance provided to controller for data subject rights obligations | Art. 28(3)(e) |
| B.8.2.2 | Legitimate purpose only | Processing limited to legitimate controller purposes per DPA | Art. 28 |
| **B.8.3 — Privacy by Design and Privacy by Default** *(Enhanced 2025)* | | | |
| B.8.3.1 | Privacy by design *(NEW standalone control 2025)* | Privacy by design applied to processor systems and services; ISO 31700:2023 aligned | Art. 25, 32 |
| B.8.3.2 | Temporary files *(NEW 2025)* | Temporary PII created during processing managed and deleted per agreed schedules | Art. 32 |
| B.8.3.3 | Return, transfer or disposal of PII | PII returned to controller or securely deleted at contract end; evidence retained | Art. 28(3)(g) |
| **B.8.4 — Processor Obligations to Controller** | | | |
| B.8.4.1 | Assistance for data subject rights | Technical and organisational measures to assist controller with DSARs and rights | Art. 28(3)(e) |
| B.8.4.2 | Notification of data subject requests | Data subject requests forwarded to controller promptly; not acted on without instruction | Art. 28 |
| B.8.4.3 | Privacy/security breach notification | Breach notification to controller without undue delay (per agreed timeline in DPA); include required details | Art. 33 |
| **B.8.5 — Cross-Border Transfers (Processor)** *(Enhanced 2025)* | | | |
| B.8.5.1 | Basis for cross-border transfers | Transfers only per controller instructions and approved transfer mechanisms | Art. 44 |
| B.8.5.2 | Countries and international organisations | Transfer destinations documented; restrictions followed; no unauthorised transfers | Art. 44–49 |
| B.8.5.3 | Records of cross-border PII transfers | Transfer register maintained; evidence available for controller and supervisory authority | Art. 30(2) |
| **B.8.6 — Audit and Compliance (NEW/Enhanced 2025)** | | | |
| B.8.6.1 | Audit rights | Controller audit rights explicitly supported; third-party audit reports provided | Art. 28(3)(h) |
| B.8.6.2 | Assistance for regulatory audits | Assistance provided to controller for supervisory authority inspections and investigations | Art. 31 |

---

## What Does a Processor Need?

If your organisation is acting as a PII Processor, your PIMS must demonstrate:

### Contractual Framework
- Data Processing Agreements (DPAs) in place with each controller (`DPA-TEMPLATE.md` in root)
- Sub-processor DPAs in place (with equivalent obligations passed down)
- Audit rights provisions in all DPAs

### Operational Controls
- Processing ONLY on controller's documented instructions
- PII not used for processor's own purposes
- Staff confidentiality obligations
- Technical security measures appropriate to the risk (ISO 27001:2022 controls)

### Data Subject Support
- Mechanism to forward data subject requests to controller
- DSAR response assistance capability
- Complaints forwarding process

### Incident Management
- Breach detection and initial assessment capability
- Controller notification process (without undue delay — per DPA timeline)
- Breach notification content covering required elements

### Transfer Controls
- Cross-border transfer restrictions enforced
- Transfer mechanisms only per controller authorisation
- Transfer register maintained

### End of Contract
- Process for secure return or deletion of PII
- Evidence of disposal (certificates where required)

---

## How to Use This Folder

1. **Review** the control index above to understand all applicable Annex B controls
2. **Reference** the B8 detailed control file for implementation guidance
3. **Complete** the SoA Annex B section: `05-CLAUSE6-PLANNING/STATEMENT-OF-APPLICABILITY.md`
4. **Ensure** DPAs with all controllers contain the required provisions (`DPA-TEMPLATE.md`)
5. **Monitor** control implementation via the Gap Assessment Checklist (`01-GAP-ASSESSMENT/`)

---

## Related Documents

| Document | Location |
|---------|---------|
| B8-PROCESSOR-OBLIGATIONS.md | This folder |
| Statement of Applicability (Annex B) | `05-CLAUSE6-PLANNING/STATEMENT-OF-APPLICABILITY.md` |
| DPA Template | `DPA-TEMPLATE.md` (root) |
| Privacy Breach Response | `07-CLAUSE8-OPERATION/PRIVACY-BREACH-RESPONSE-PROCEDURE.md` |
| Cross-Border Transfer Procedure | `07-CLAUSE8-OPERATION/CROSS-BORDER-TRANSFER-PROCEDURE.md` |
| Privacy by Design Procedure | `07-CLAUSE8-OPERATION/PRIVACY-BY-DESIGN-PROCEDURE.md` |
| Third-Party Privacy Assessment | `07-CLAUSE8-OPERATION/THIRD-PARTY-PRIVACY-ASSESSMENT.md` |

---

## Version History

| Version | Date | Description |
|---------|------|-------------|
| 2.0 | April 2025 | Updated for ISO/IEC 27701:2025 — new controls: B.8.3.1 (Privacy by Design standalone), B.8.3.2 (temporary files), enhanced B.8.5 (cross-border), B.8.6 (audit rights), sub-processor enhancements |
| 1.0 | 2024 | Initial release — ISO/IEC 27701:2019 |

---

*ISO/IEC 27701:2025 PIMS Toolkit | Annex B — PII Processor Controls | PIMS-ANNEXB-README-001 | v2.0 | Classification: Public*
