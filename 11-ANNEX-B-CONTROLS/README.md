# 11 — Annex B: PII Processor Controls

This folder contains implementation guidance and control templates for organisations acting as **PII Processors** under ISO/IEC 27701:2019 Annex B.

## What is Annex B?

Annex B of ISO/IEC 27701:2019 provides additional controls for organisations that process PII **on behalf of and under the authority of a PII Controller**. These controls extend ISO/IEC 27001 with processor-specific privacy requirements.

Annex B maps to **GDPR Article 28** (processor obligations) and covers processor obligations for compliance with controller instructions, sub-processor management, and supporting data subject rights.

## Files in This Folder

| File | Description |
|------|------------|
| [ANNEX-B-PII-PROCESSOR-CONTROLS.md](ANNEX-B-PII-PROCESSOR-CONTROLS.md) | Comprehensive control matrix for all Annex B controls with implementation guidance, ISO 27701 clause references, and GDPR Article 28 cross-mapping |

## Annex B Control Categories

| Section | Description |
|---------|-------------|
| B.8.1 | Conditions for Collection — Processor acting on instructions only |
| B.8.2 | Obligations to PII Principals — Processor supporting controller obligations |
| B.8.3 | Privacy by Design — Processor technical measures |
| B.8.4 | PII Sharing and Disclosure — Processor disclosure limitations |
| B.8.5 | Sub-processor Management — Engaging and managing sub-processors |

## When Do Annex B Controls Apply?

Your organisation must apply Annex B controls when you:
- Process customer data on behalf of a client organisation
- Operate a SaaS platform that processes client employees or customer data
- Provide outsourced HR, payroll, IT support, or customer service functions
- Act as a cloud hosting or data centre provider for client PII
- Act as a marketing agency processing client marketing data

Your organisation may need **both Annex A and Annex B controls** if you are both a Controller for some processing (e.g., your own employees) and a Processor for others (e.g., client customer data).

## Key Processor Obligations

1. Process PII only on documented instructions from the Controller
2. Ensure all personnel with access to PII are bound by confidentiality obligations
3. Implement appropriate technical and organisational security measures
4. Assist the Controller in responding to data subject rights requests
5. Support the Controller in meeting DPIA and breach notification obligations
6. Delete or return all PII upon contract termination (as instructed by Controller)
7. Provide evidence of compliance (audit rights, certifications)
8. Obtain prior written approval before engaging sub-processors
9. Impose equivalent data protection obligations on sub-processors

## How to Use

1. Review the SOA (05-CLAUSE6-PLANNING/STATEMENT-OF-APPLICABILITY.md) for applicable Annex B controls
2. Implement measures described in ANNEX-B-PII-PROCESSOR-CONTROLS.md
3. Ensure all Data Processing Agreements include Annex B-aligned processor commitments
4. Reference the DPA template: DPA-TEMPLATE.md (root folder)

## Related Documents

- 07-CLAUSE8-OPERATION/THIRD-PARTY-PRIVACY-ASSESSMENT.md — Supplier assessment (used by controllers to assess you)
- DPA-TEMPLATE.md — Data Processing Agreement template (root folder)
- 05-CLAUSE6-PLANNING/STATEMENT-OF-APPLICABILITY.md — SOA

---

*ISO/IEC 27701:2019 PIMS Toolkit | Annex B — PII Processor Controls*
