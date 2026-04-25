# NFS Worked Example — PIMS Internal Audit Report

> **FOR ILLUSTRATIVE PURPOSES ONLY** — NFS is a fictional organisation. All examples are for educational use.

| Field | Detail |
|-------|--------|
| **Document ID** | NFS-PIMS-AUD-2025-001 |
| **Version** | 1.0 |
| **Date** | April 2025 |
| **Standard** | ISO/IEC 27701:2025 — Clause 9.2 |
| **Classification** | Confidential — Restricted |

---

## PIMS INTERNAL AUDIT REPORT

| Field | Detail |
|-------|--------|
| **Audit Reference** | NFS-AUDIT-2025-001 |
| **Audit Title** | PIMS Operational Controls Audit — Q1 2025 |
| **Audit Scope** | ISO/IEC 27701:2025 Clauses 8 (Operation) and Annex A Controls A.7.2–A.7.8 |
| **Audit Date(s)** | 17–21 March 2025 |
| **Report Date** | 1 April 2025 |
| **Lead Auditor** | Sarah Chen, CIPP/E, CIPM (Internal Audit) |
| **Audit Team** | Sarah Chen (Lead); James Patel (IT Audit); Maria Torres (Legal/Compliance observer) |
| **Auditee(s)** | DPO (Priya Sharma); Head of Retail Banking Ops; Head of IT; Head of Marketing |
| **Distribution** | DPO, CISO, CEO, Internal Audit file |

---

## 1. Executive Summary

This audit assessed NFS's operational privacy controls under ISO/IEC 27701:2025 for Q1 2025. The audit covered 8 operational areas across 4 departments over 5 audit days, reviewing 23 specific control requirements. Overall, NFS demonstrated a **Largely Conformant** PIMS with strong foundational controls. Three nonconformities and two observations were identified.

| Finding Type | Count |
|--------------|-------|
| Major Nonconformity | 0 |
| Minor Nonconformity | 3 |
| Observation | 2 |
| Opportunity for Improvement | 1 |

**Overall Audit Opinion:** The PIMS is substantially implemented and operating effectively. Minor gaps in consent refresh scheduling and third-party audit exercise require attention before the Stage 2 certification audit scheduled for September 2025.

---

## 2. Audit Scope and Objectives

**Objectives:**
- Verify that NFS's operational privacy controls comply with ISO/IEC 27701:2025 Clause 8 and Annex A requirements
- Assess the effectiveness of the DPIA process, DSR handling, consent management, and third-party controls
- Identify nonconformities and opportunities for improvement prior to the Stage 2 certification audit

**In scope:** Clause 8 (Operation), Annex A Controls A.7.2.1–A.7.8.4 (PII Controller controls), DSR log Q4 2024 – Q1 2025, DPIA register, Consent management records

**Out of scope:** Clause 4–7 (covered in separate Audit NFS-AUDIT-2024-002), Annex B (NFS does not act as processor in scope)

---

## 3. Audit Methodology

The audit was conducted using the following evidence-gathering techniques:

| Method | Details |
|--------|---------|
| Document review | ROPA (NFS-PIMS-OPS-004), DPIA register, DSR log Q4 2024–Q1 2025, consent records, third-party agreements |
| Interviews | DPO, Head of IT, Marketing Ops Manager, Customer Services Manager |
| System walkthrough | OneTrust CMP, Salesforce (consent suppression), DSR case management system |
| Sample testing | 10 DSR cases reviewed (5 SARs, 3 erasures, 2 Art. 22 objections); 15 DPIA screening decisions reviewed |

---

## 4. Findings

### 4.1 Nonconformity NC-001 — Consent Refresh Not Scheduled for Legacy Records

| Finding Field | Detail |
|---------------|--------|
| **Reference** | NFS-NC-2025-001 |
| **Clause** | ISO/IEC 27701:2025 A.7.2.4 — Obtain and record consent |
| **Finding Type** | Minor Nonconformity |
| **Description** | 7,142 customer consent records from pre-2023 (before OneTrust was deployed) have not been refreshed. These records were captured on a legacy CRM and lack the granularity and positive opt-in confirmation required by GDPR Art. 7 and ISO 27701:2025 A.7.2.4. NFS is aware of this population but has not scheduled a consent refresh campaign. |
| **Evidence** | OneTrust consent audit export NFS-AUDIT-CONSENT-2024; legacy CRM extract reviewed 18 March 2025 |
| **Risk** | Medium — processing marketing communications to these 7,142 subjects may lack valid consent |
| **Required Action** | Schedule and complete consent refresh campaign for all legacy records by 30 June 2025. Suspend marketing communications to non-refreshed subjects immediately. |
| **Target Completion** | 30 June 2025 |
| **Owner** | DPO / Head of Marketing |

### 4.2 Nonconformity NC-002 — DPIA Not Completed for New AI Profiling Activity

| Finding Field | Detail |
|---------------|--------|
| **Reference** | NFS-NC-2025-002 |
| **Clause** | ISO/IEC 27701:2025 A.7.2.5 — Privacy impact assessment |
| **Finding Type** | Minor Nonconformity |
| **Description** | NFS launched an AI-driven affordability profiling tool in January 2025 for mortgage applications. The DPIA register shows this activity was screened (trigger confirmed) but the full DPIA has not been completed 11 weeks post-launch. Under GDPR Art. 35 and ISO 27701:2025 A.7.2.5, a DPIA must be completed before high-risk processing commences. |
| **Evidence** | DPIA register reviewed 19 March 2025; confirmed DPIA-SCREEN-2025-007 screened January 2025, DPIA not yet started |
| **Risk** | High — processing commenced without required DPIA; potential ICO enforcement risk |
| **Required Action** | Complete DPIA for NFS-AI-AFFORD-001 tool within 14 days and obtain DPO sign-off before next mortgage processing cycle. |
| **Target Completion** | 15 April 2025 |
| **Owner** | DPO / Head of Mortgage Products |

### 4.3 Nonconformity NC-003 — Supplier Audit Right Not Exercised for Equifax

| Finding Field | Detail |
|---------------|--------|
| **Reference** | NFS-NC-2025-003 |
| **Clause** | ISO/IEC 27701:2025 A.7.2.6 — Contracts with PII processors |
| **Finding Type** | Minor Nonconformity |
| **Description** | The NFS-Equifax DPA (executed January 2024) includes an annual audit right. No audit or questionnaire has been sent in the 14 months since contract execution. The third-party assessment for Equifax (NFS-TPA-2025-002) was completed but relied on Equifax's self-reported certifications only. |
| **Evidence** | DPA clause 14 reviewed; NFS-TPA-2025-002 reviewed; no evidence of questionnaire dispatch |
| **Risk** | Low-Medium — audit right provides accountability assurance; non-exercise undermines governance |
| **Required Action** | Dispatch Equifax annual privacy questionnaire by 30 April 2025. Record response in third-party register. |
| **Target Completion** | 30 April 2025 |
| **Owner** | DPO / Head of Procurement |

### 4.4 Observations

| Ref | Clause | Observation |
|-----|--------|-------------|
| NFS-OBS-2025-001 | A.7.3.4 Retention | Data retention deletion runs are scheduled quarterly. Consider moving to monthly to reduce window of non-compliant retention. |
| NFS-OBS-2025-002 | A.7.6 DSR | DSR acknowledgement emails are sent manually by DPO assistant. Automating acknowledgement via OneTrust would reduce risk of missed timelines. |

---

## 5. Positive Findings

The audit identified the following areas of strong control performance:

| Area | Finding |
|------|---------|
| DSR Management | All 23 DSRs reviewed closed within statutory 30-day limit. Average response time 11 days. Exceeds benchmark. |
| DPIA Quality | 14 of 15 DPIAs reviewed were complete, well-documented, and DPO-approved. Evidence trail strong. |
| Consent Withdrawal | All 4 tested consent withdrawals honoured within NFS 72-hour SLA. One honoured within 4 hours. |
| Third-Party Controls | Salesforce and ADP DPAs current; sub-processor lists reviewed; TIAs completed for US transfers. |
| Breach Response | Breach register complete; NFS-BREACH-2025-007 (see NFS-BREACH-LOG-ENTRY.md) responded to within regulatory timelines. |

---

## 6. Audit Conclusion

NFS's PIMS operational controls are substantially implemented and demonstrate a **Level 4 — Managed** maturity profile. The three minor nonconformities are addressable before the September 2025 Stage 2 certification audit. No major nonconformities were identified. The DPO and management team demonstrated strong awareness of ISO/IEC 27701:2025 requirements.

**Auditor Declaration:** This audit was conducted in accordance with the NFS PIMS Internal Audit Programme (NFS-PIMS-PER-001) and ISO/IEC 27007 guidelines.

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Lead Auditor | Sarah Chen | S.Chen | 1 April 2025 |
| DPO Review | Priya Sharma | P.Sharma | 3 April 2025 |
| Management Acceptance | James Worthington (CEO) | J.Worthington | 7 April 2025 |

---

## 7. Corrective Action Summary

| NCR Ref | Description | Owner | Due Date | Status |
|---------|-------------|-------|----------|--------|
| NFS-NC-2025-001 | Consent refresh for 7,142 legacy records | DPO / Marketing | 30 Jun 2025 | Open |
| NFS-NC-2025-002 | DPIA for AI affordability profiling tool | DPO / Mortgage | 15 Apr 2025 | Open |
| NFS-NC-2025-003 | Equifax annual questionnaire dispatch | DPO / Procurement | 30 Apr 2025 | Open |

---

## Cross-References

| Document | Reference |
|----------|-----------|
| Internal Audit Report Template | `08-CLAUSE9-PERFORMANCE/PIMS-INTERNAL-AUDIT-REPORT-TEMPLATE.md` |
| Internal Audit Programme | `08-CLAUSE9-PERFORMANCE/PIMS-INTERNAL-AUDIT-PROGRAMME.md` |
| NCR Register | `09-CLAUSE10-IMPROVEMENT/NCR-CORRECTIVE-ACTION-REGISTER.md` |
| NFS Breach Log | `12-WORKED-EXAMPLE/NFS-BREACH-LOG-ENTRY.md` |
| NFS DPIA Entry | `12-WORKED-EXAMPLE/NFS-DPIA-ENTRY.md` |

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| 1.0 | April 2025 | Initial release — NFS Q1 2025 PIMS Internal Audit Report |

---

*ISO/IEC 27701:2025 PIMS Toolkit | NFS Internal Audit Report | NFS-PIMS-AUD-2025-001*
