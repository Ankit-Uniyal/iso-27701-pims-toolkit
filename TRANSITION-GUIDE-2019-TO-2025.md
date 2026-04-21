# Transition Guide: ISO/IEC 27701:2019 → ISO/IEC 27701:2025

| Field | Detail |
|-------|--------|
| **Document ID** | PIMS-TRANSITION-001 |
| **Version** | 1.0 |
| **Date** | April 2025 |
| **Owner** | Data Protection Officer / PIMS Programme Manager |
| **Classification** | Public |
| **Review Date** | April 2026 |

---

## 1. Overview

ISO/IEC 27701:2025 was published in 2025, superseding ISO/IEC 27701:2019. This guide is for organisations and certification bodies transitioning from the 2019 edition to the 2025 edition.

The 2025 revision represents a **structural and substantive update** — not merely a refresh. The primary drivers were:
1. Alignment with **ISO/IEC 27001:2022** (Harmonised Structure / High Level Structure)
2. Alignment with **ISO/IEC 27002:2022** (updated control set)
3. New privacy-specific requirements driven by global regulatory developments (GDPR enforcement, Schrems II, EDPB guidance)
4. Integration of **ISO/IEC 31700:2023** (Privacy by Design)
5. Enhanced cross-border transfer requirements (Transfer Impact Assessments)
6. Improved coverage of joint controller arrangements

---

## 2. Key Structural Changes

### 2.1 Alignment with ISO 27001:2022 (HLS)

| Area | 2019 | 2025 |
|------|------|------|
| Base standard reference | ISO 27001:2013 | ISO 27001:2022 |
| Structure | Parallel to ISO 27001:2013 | Harmonised with ISO 27001:2022 HLS |
| Clause numbering | Mirrors 27001:2013 | Mirrors 27001:2022 |
| Documented information | Clause 7.5 | Clause 7.5 (updated content requirements) |
| Planning of changes | Not explicit | Clause 6.3 (planning changes to PIMS) |
| Communication | Clause 7.4 | Clause 7.4 (clarified external communication requirements) |

> **Action Required:** Organisations certified to ISO 27001:2013 must transition to ISO 27001:2022 **before or alongside** transitioning to ISO 27701:2025.

### 2.2 Annex A/B Control Updates

The control structure of Annex A and B has been updated to align with ISO 27002:2022 (which restructured from 114 to 93 controls).

| Aspect | 2019 | 2025 |
|--------|------|------|
| Annex A (Controller) controls | ~31 controls | Expanded — new sub-clauses added |
| Annex B (Processor) controls | ~18 controls | Expanded — new standalone controls |
| Control families | A.7 and A.8 (controller), B.8 (processor) | Same families; extended sub-clauses |
| New controller controls | N/A | A.7.2.7 (joint controllers), A.7.2.8 (Privacy by Default), A.7.4 (de-identification), A.7.5 (disclosure controls), A.8.2.6 (automated decisions), A.8.3.2 (consent refresh) |
| New processor controls | N/A | B.8.3.1 (Privacy by Design — standalone), B.8.3.2 (temporary files), B.8.6 (audit rights) |

---

## 3. New Controls in ISO 27701:2025

### 3.1 New PII Controller Controls (Annex A)

| New Control | Title | Why Added |
|------------|-------|-----------|
| **A.7.2.7** | Joint PII Controller Arrangements | GDPR Art. 26 enforcement; organisations increasingly operate as joint controllers in ecosystems, platforms, and partnerships |
| **A.7.2.8** | Privacy by Default | Art. 25 GDPR; ISO 31700:2023; makes "most privacy-protective as default" an explicit, standalone control |
| **A.7.4** | PII De-identification and Deletion | Expanded from single clause — now includes: de-identification (A.7.4.1), temporary files (A.7.4.2), return/transfer/disposal (A.7.4.3) |
| **A.7.5** | PII Disclosure Controls | New sub-clause covering: basis for transfers to third parties (A.7.5.1), disclosure records (A.7.5.2), legally-binding disclosure requests (A.7.5.3) |
| **A.8.2.6** | Automated Decision-Making and Profiling | GDPR Art. 22; growing use of AI/ML; specific right to not be subject to solely automated decisions |
| **A.8.3.2** | Consent Refresh | Regulatory guidance on consent validity over time; consent must be refreshed for long-duration or materially changed processing |

### 3.2 New PII Processor Controls (Annex B)

| New Control | Title | Why Added |
|------------|-------|-----------|
| **B.8.3.1** | Privacy by Design (Processor) | Processors must apply PbD to their services; ISO 31700:2023 alignment |
| **B.8.3.2** | Temporary Files (Processor) | Temporary PII files created during processing must be managed and deleted |
| **B.8.6.1** | Audit Rights | Explicit control requiring processors to support controller audit rights (GDPR Art. 28(3)(h)) |
| **B.8.6.2** | Regulatory Audit Assistance | Processors must assist controllers during supervisory authority investigations |

### 3.3 Transfer Impact Assessment (TIA) — New Requirement

Following the **Schrems II ruling** (CJEU C-311/18) and subsequent EDPB guidance, the 2025 edition introduces an explicit **Transfer Impact Assessment (TIA)** requirement for cross-border transfers where no adequacy decision exists:

- **Who it applies to:** PII Controllers (A.7.4.3, A.7.5.1) and PII Processors (B.8.5.1)
- **When required:** When transferring PII to a third country without an EU/EEA adequacy decision
- **What it requires:** Assessment of the destination country's legal framework, law enforcement access rights, and effectiveness of the chosen transfer safeguard
- **Output:** TIA report documenting the assessment; supplementary measures if required

---

## 4. Terminology Changes

| 2019 Term | 2025 Term | Notes |
|-----------|-----------|-------|
| "PII principal" | "PII principal" / "data subject" | Terms used interchangeably; harmonised with GDPR vocabulary |
| "PII" primarily | "PII" and "personal data" | Both terms accepted; harmonised for global applicability |
| "Customer" (in processor context) | "PII controller" (more explicit) | Clearer role definition |
| No explicit "joint controller" | "Joint PII controller" | New defined role |

---

## 5. Gap Assessment: What You Need to Implement

If you have an existing ISO 27701:2019 PIMS, here is what you need to add/update for the 2025 transition:

### 5.1 Mandatory New Activities

| Activity | Control / Clause | Priority |
|----------|-----------------|----------|
| Identify all joint controller relationships and execute joint controller agreements | A.7.2.7 | High |
| Implement Privacy by Default as a standalone control (review all systems for default settings) | A.7.2.8 | High |
| Conduct Transfer Impact Assessment for all cross-border transfers without adequacy decisions | A.7.4.3, A.7.5.1, B.8.5.1 | High |
| Update consent management to include refresh mechanism | A.8.3.2 | High |
| Implement controls for automated decision-making and profiling | A.8.2.6 | High (if applicable) |
| Update DPIA template and trigger criteria per 2025 enhanced requirements | A.7.2.5 | High |
| Implement de-identification controls formally | A.7.4.1 | Medium |
| Implement temporary file controls | A.7.4.2, B.8.3.2 | Medium |
| Update disclosure controls — especially for law enforcement requests | A.7.5.3 | Medium |
| Grant and document audit rights in DPAs | B.8.6.1 | Medium |
| Apply Privacy by Design controls as a processor | B.8.3.1 | Medium (processors) |

### 5.2 Document Updates Required

| Document | What to Update |
|---------|---------------|
| Privacy Policy | Add joint controller provisions, ISO 31700 reference, TIA requirement, updated standard reference |
| Statement of Applicability | Add all new 2025 controls; re-assess include/exclude decisions |
| Gap Assessment Checklist | Update to 2025 control set |
| DPIA Template | Update trigger criteria; add joint controller scenario |
| Cross-Border Transfer Procedure | Add TIA requirement and template |
| Consent Management Procedure | Add consent refresh process |
| Privacy by Design Procedure | Elevate to standalone control; reference ISO 31700:2023 |
| Data Subject Rights Procedure | Add automated decision-making (Art. 22) |
| DPA Template | Add audit rights provision; update to 2025 processor control requirements |
| All document headers | Update version, date, and standard reference from 2019 → 2025 |

### 5.3 Version History Updates

Update the version history of all PIMS documents when they are revised for 2025 compliance. The recommended convention is:

- **v2.0** = Updated for ISO/IEC 27701:2025
- **v1.x** = Amendments within the 2019 framework
- **v1.0** = Original 2019 release

---

## 6. Certification Transition Timeline

| Milestone | Typical Timeframe |
|-----------|-----------------|
| Standard published | 2025 |
| ISO Transition Period begins | 2025 |
| Typical transition deadline (certification bodies) | 3 years from publication (2028) |
| Recommended transition start | Immediately — advantage of early adoption |
| Gap assessment | Month 1–2 |
| Implement new controls | Month 2–6 |
| Update documentation | Month 3–6 |
| Internal audit against 2025 | Month 6–9 |
| Management review and approval | Month 9 |
| Certification audit (transition) | Month 9–12 |

> **Note:** Contact your certification body for their specific transition requirements and deadlines.

---

## 7. How This Toolkit Has Been Updated

This toolkit has been updated from v1.0 (ISO 27701:2019) to **v2.0 (ISO 27701:2025)**:

| File | Change |
|------|--------|
| README.md | Updated to 2025 — new controls table, version history |
| 00-IMPLEMENTATION-GUIDE.md | Updated phases, added TIA, joint controller, ISO 31700 |
| 01-GAP-ASSESSMENT/PIMS-GAP-ASSESSMENT-CHECKLIST.md | Updated to 2025 control set — all new controls added |
| 02-PIMS-POLICY/PRIVACY-POLICY.md | Updated — joint controllers, PbD, TIA, DPIA triggers |
| 05-CLAUSE6-PLANNING/STATEMENT-OF-APPLICABILITY.md | Updated — all new 2025 Annex A/B controls added |
| 10-ANNEX-A-CONTROLS/README.md | Updated — new controls documented with implementation guidance |
| 11-ANNEX-B-CONTROLS/README.md | Updated — new processor controls documented |
| GDPR-MAPPING-CROSS-REFERENCE.md | Updated — TIA, joint controllers, automated decisions mapped |
| All document headers | Version bumped to 2.0 / April 2025 / ISO 27701:2025 |
| **TRANSITION-GUIDE-2019-TO-2025.md** | **New — this file** |

---

## 8. Related Standards and References

| Standard | Relevance to ISO 27701:2025 |
|---------|---------------------------|
| ISO/IEC 27001:2022 | Base ISMS — must be in place before PIMS certification |
| ISO/IEC 27002:2022 | Security controls — Annex A/B aligned to this structure |
| ISO/IEC 27005:2022 | Risk assessment methodology — updated privacy risk approach |
| ISO/IEC 29100:2011 | Privacy framework — 11 privacy principles (deeper integration in 2025) |
| **ISO/IEC 31700:2023** | **Privacy by Design — explicitly cross-referenced in 2025 (new)** |
| GDPR (EU) 2016/679 | Primary regulatory driver for many 2025 changes |
| EDPB Guidelines on TIA | Informs new TIA requirement |
| CJEU Schrems II ruling | Drives TIA for cross-border transfers |

---

## Version History

| Version | Date | Description |
|---------|------|-------------|
| 1.0 | April 2025 | Initial release — transition guide from 27701:2019 to 27701:2025 |

---

*ISO/IEC 27701:2025 PIMS Toolkit | Transition Guide 2019→2025 | PIMS-TRANSITION-001 | v1.0 | Classification: Public*
