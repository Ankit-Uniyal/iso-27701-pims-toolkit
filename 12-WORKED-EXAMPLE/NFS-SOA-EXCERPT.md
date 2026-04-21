# Worked Example: Statement of Applicability — Excerpt

> **WORKED EXAMPLE — FOR ILLUSTRATIVE PURPOSES ONLY**
> NFS is a fictional organisation. This excerpt shows how to document SoA control applicability under ISO/IEC 27701:2025.

| Field | Detail |
|-------|--------|
| **Document ID** | NFS-PIMS-PLN-002 |
| **Version** | 2.0 |
| **Date** | April 2025 |
| **Owner** | Sarah Chen, DPO |
| **Standard** | ISO/IEC 27701:2025 |
| **Classification** | Confidential — Internal |

---

## Organisation Context

**NFS** acts as both **PII Controller** (retail banking, lending, HR) and **PII Processor** (insurance white-label for partner banks). Both Annex A and Annex B controls apply.

**PIMS scope:** All PII processing activities within UK HQ and EU Dublin office. Bangalore back-office operates under data processing agreements and separate controller instructions.

---

## Selected Annex A.7 Controls (PII Controller) — SoA Entries

---

### A.7.2.1 — Identify and document the purposes of PII processing

| Field | Detail |
|-------|--------|
| **Applicable?** | ✅ Yes |
| **Justification** | UK GDPR Art. 5(1)(b) requires purpose limitation. NFS processes PII for 8 distinct activities documented in ROPA. |
| **Status** | Partially Implemented |
| **Evidence** | ROPA v3.1 documents purpose for 6/8 activities. Recruitment and IT monitoring activities need purpose documentation update. |
| **Owner** | DPO |
| **Target Date** | 30 June 2025 |

---

### A.7.2.2 — Identify the lawful basis for processing

| Field | Detail |
|-------|--------|
| **Applicable?** | ✅ Yes |
| **Justification** | UK GDPR Art. 6 requires valid legal basis for all processing. |
| **Status** | Partially Implemented |
| **Evidence** | Legal basis documented in ROPA for 6/8 activities. Marketing consent basis confirmed invalid (pre-ticked box — see PRR-NFS-001). Legitimate Interests Assessments (LIAs) not yet completed for 2 activities. |
| **Owner** | DPO / Legal |
| **Gap** | PRR-NFS-001: Marketing consent invalid — re-consent campaign planned Q2 2025. |

---

### A.7.2.3 & A.7.2.4 — Consent management (obtain and record)

| Field | Detail |
|-------|--------|
| **Applicable?** | ✅ Yes |
| **Justification** | Consent is NFS's lawful basis for marketing communications (~120,000 contacts). |
| **Status** | Not Implemented (Remediation Required) |
| **Evidence** | Consent Management Procedure v0.1 drafted. Double opt-in not yet implemented. CMP platform procurement in progress. Historical consent records invalid (pre-ticked boxes). |
| **Gaps** | CMP not deployed; double opt-in missing; historical consent invalid; Privacy Notice inaccurate. |
| **Owner** | DPO / Marketing |
| **Target Date** | Re-consent campaign by 31 July 2025 |

---

### A.7.2.5 — Privacy impact assessment (DPIA) — *Enhanced 2025 trigger criteria*

| Field | Detail |
|-------|--------|
| **Applicable?** | ✅ Yes |
| **Justification** | NFS processes at scale for credit scoring, AI fraud detection, and customer analytics. Multiple 2025 DPIA triggers met. |
| **Status** | Partially Implemented |
| **Evidence** | DPIA completed for mortgage processing and credit scoring. DPIA **not yet completed** for AI fraud detection model (PRR-NFS-003 — HIGH RISK). Customer analytics DPIA in draft. |
| **Gaps** | AI fraud detection DPIA overdue; DPO consultation required. |
| **Owner** | DPO |
| **Target Date** | 15 May 2025 |

---

### A.7.2.7 — Joint PII controller arrangements *(NEW in ISO 27701:2025)*

| Field | Detail |
|-------|--------|
| **Applicable?** | ✅ Yes |
| **Justification** | NFS and its marketing data co-op partner jointly determine marketing list purposes and means — joint controllership exists. |
| **Status** | Not Implemented |
| **Evidence** | Joint Controller Agreement (JCA) not yet in place. Marketing data sharing arrangement has been operating without formal JCA. |
| **Gaps** | JCA urgently required; privacy notice must reference co-controller. |
| **Owner** | Legal / DPO |
| **Target Date** | 30 April 2025 — urgent |

---

### A.7.2.8 — Privacy by default *(NEW standalone control in ISO 27701:2025)*

| Field | Detail |
|-------|--------|
| **Applicable?** | ✅ Yes |
| **Justification** | ISO 27701:2025 A.7.2.8 and GDPR Art. 25 require maximum privacy settings as default. |
| **Status** | Partially Implemented |
| **Evidence** | Online banking portal: analytics tracking NOT off by default (gap). Mobile app: marketing preferences default to opt-in for NFS affiliate products (gap). Privacy by Design Procedure v2.0 in review. |
| **Gaps** | Analytics tracking and marketing defaults need updating; privacy by design checklist not yet embedded in SDLC. |
| **Owner** | CISO / DPO |
| **Target Date** | 30 June 2025 |

---

### A.7.5.1 — Basis for PII transfer to third parties / TIA *(NEW in ISO 27701:2025)*

| Field | Detail |
|-------|--------|
| **Applicable?** | ✅ Yes |
| **Justification** | NFS transfers PII to Bangalore back-office (India — no adequacy decision). SCCs in place but no Transfer Impact Assessment (TIA) conducted. |
| **Status** | Partially Implemented |
| **Evidence** | SCCs (2021 version) in place for Bangalore transfers. TIA **not yet completed** (PRR-NFS-002 — HIGH RISK). India DPDPA 2023 assessment not yet completed. |
| **Gaps** | TIA required urgently for Bangalore transfers; India DPDPA supplementary clauses may be needed. |
| **Owner** | DPO / Legal |
| **Target Date** | 15 May 2025 |

---

### A.8.2.1 — Right of access (DSARs)

| Field | Detail |
|-------|--------|
| **Applicable?** | ✅ Yes |
| **Justification** | UK GDPR Art. 15 mandates response within 30 days. NFS receives ~20 DSARs/month. |
| **Status** | Partially Implemented |
| **Evidence** | DSR Procedure v1.1 and web form exist. Active DSAR-2025-012 approaching 30-day deadline without response (**High Risk — PRR-NFS-004**). No DSAR tracking system or designated coordinator. |
| **Gaps** | No DSAR tracking log; no coordinator role designated; DSAR-2025-012 urgent. |
| **Owner** | DPO |
| **Target Date** | IMMEDIATE for DSAR-2025-012; tracking system by 30 April 2025 |

---

### A.8.2.6 — Automated decision-making and profiling *(NEW in ISO 27701:2025)*

| Field | Detail |
|-------|--------|
| **Applicable?** | ✅ Yes |
| **Justification** | NFS uses automated credit scoring (legal/significant effect) and AI fraud detection model. Art. 22 rights apply. |
| **Status** | Not Implemented |
| **Evidence** | No documented process for data subjects to request human review of automated credit decisions. AI fraud detection model not registered as automated decision-making activity. |
| **Gaps** | Human review process for credit decisions needed; fraud detection model DPIA and ADM registration required. |
| **Owner** | DPO / Product / IT |
| **Target Date** | 30 June 2025 |

---

## Selected Annex B.8 Controls (PII Processor) — SoA Entries

NFS acts as a PII Processor for white-label insurance products for three partner banks.

---

### B.8.1.1 — Processing only on controller instructions

| Field | Detail |
|-------|--------|
| **Applicable?** | ✅ Yes |
| **Status** | Fully Implemented |
| **Evidence** | DPAs with all three partner banks in place. Instructions documented in DPA schedules. Change request process for ad hoc instructions in place. |
| **Owner** | Operations / DPO |

---

### B.8.6.1 — Audit rights *(NEW in ISO 27701:2025)*

| Field | Detail |
|-------|--------|
| **Applicable?** | ✅ Yes |
| **Status** | Partially Implemented |
| **Evidence** | DPAs include audit rights clause. ISO 27001:2022 certificate provided to all partners. SOC 2 Type II report being commissioned (gap: not yet available). |
| **Gaps** | SOC 2 report not yet available; audit support procedure not documented. |
| **Owner** | DPO / IT |
| **Target Date** | SOC 2 by Q3 2025 |

---

## SoA Summary (Q1 2025)

| Status | Count | % of Applicable |
|--------|-------|----------------|
| ✅ Fully Implemented | 12 | 27% |
| 🟡 Partially Implemented | 20 | 45% |
| 🔴 Not Implemented | 9 | 20% |
| ⬜ Not Applicable | 8 | — |
| **Total Applicable** | **41** | **Target: 100% by Q4 2025** |

**New 2025 controls not yet implemented:** A.7.2.7, A.7.2.8, A.7.5.1 (TIA), A.8.2.6, A.8.3.2, B.8.6.1

---

## Version History

| Version | Date | Description |
|---------|------|-------------|
| 2.0 | April 2025 | Updated for ISO/IEC 27701:2025 — new controls added (A.7.2.7, A.7.2.8, A.7.5.1/TIA, A.8.2.6, B.8.6.1), footer updated, NFS context refreshed |
| 1.0 | 2024 | Initial release — ISO/IEC 27701:2019 |

---

> Worked example. NFS is a fictional organisation. Created for educational purposes.

*ISO/IEC 27701:2025 PIMS Toolkit | NFS SoA Excerpt | NFS-PIMS-PLN-002 | v2.0 | Classification: Confidential*
