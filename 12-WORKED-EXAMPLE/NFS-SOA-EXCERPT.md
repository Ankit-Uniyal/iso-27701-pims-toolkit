# Worked Example: Statement of Applicability — Excerpt
## Nexus Financial Services Ltd (NFS)

> **WORKED EXAMPLE — FOR ILLUSTRATIVE PURPOSES ONLY**  
> NFS is a fictional organisation. This excerpt shows how to document SOA control applicability.

---

**Document ID:** NFS-PIMS-PLN-002  
**Version:** 1.0 | **Date:** 2025-01-01  
**Owner:** Sarah Chen, DPO

---

## Selected Annex A.7 Controls (PII Controller)

### A.7.1 — Identify and document purpose

| Field | Detail |
|-------|--------|
| **Applicable?** | ✅ Yes |
| **Justification** | UK GDPR Art. 5(1)(b) requires purpose limitation. NFS processes PII for 8 distinct activities. |
| **Status** | Partially Implemented |
| **Evidence** | ROPA documents purpose for 6/8 activities. Recruitment and IT monitoring need update. |
| **Owner** | DPO | **Target** | 2025-03-31 |

---

### A.7.2 — Identify legal basis

| Field | Detail |
|-------|--------|
| **Applicable?** | ✅ Yes |
| **Justification** | UK GDPR Art. 6 requires valid legal basis for all processing. |
| **Status** | Partially Implemented |
| **Evidence** | Legal basis in ROPA for 6/8 activities. Marketing consent basis confirmed invalid (pre-ticked box — PRR-NFS-002). |
| **Owner** | DPO / Legal | **Target** | 2025-03-31 |

---

### A.7.3 — Consent management

| Field | Detail |
|-------|--------|
| **Applicable?** | ✅ Yes |
| **Justification** | Consent used for marketing (~120,000 contacts). Invalid historical consent is critical risk. |
| **Status** | Not Implemented (Remediation Required) |
| **Evidence** | Consent Management Procedure drafted. Double opt-in not implemented. CMP platform not deployed. Re-consent campaign planned. |
| **Gaps** | CMP not deployed; double opt-in missing; historical consent invalid; privacy notice inaccurate |
| **Owner** | DPO / Marketing | **Target** | 2025-03-31 |

---

### A.7.4 — Privacy notice to PII principals

| Field | Detail |
|-------|--------|
| **Applicable?** | ✅ Yes |
| **Justification** | UK GDPR Art. 13/14 requires privacy notices at point of collection. |
| **Status** | Partially Implemented |
| **Evidence** | Privacy Notice Version 1.2 (2023) published. Does not reflect: Bangalore transfers; Salesforce CRM US transfers; current marketing legal basis. |
| **Gaps** | Privacy notice requires update (3 gaps identified) |
| **Owner** | DPO / Legal | **Target** | 2025-02-28 |

---

### A.7.5 — Provide choices to PII principals

| Field | Detail |
|-------|--------|
| **Applicable?** | ✅ Yes — for marketing; not for contractual/legal processing |
| **Justification** | PECR opt-out rights; UK GDPR Art. 21 right to object must be honoured. |
| **Status** | Partially Implemented |
| **Evidence** | Unsubscribe links functional. No self-service preference centre. Object to profiling not formalised. |
| **Gaps** | No preference centre; object to profiling process needs formalising |
| **Owner** | Marketing / DPO | **Target** | 2025-06-30 |

---

### A.7.8 — Access, correction, and deletion

| Field | Detail |
|-------|--------|
| **Applicable?** | ✅ Yes |
| **Justification** | UK GDPR Art. 15-17 mandate response to access, rectification, erasure requests. |
| **Status** | Partially Implemented |
| **Evidence** | DSR Procedure and web form exist. Active DSAR-2025-012 approaching deadline without response (High Risk — PRR-NFS-004). No tracking log or coordinator. |
| **Gaps** | No DSR tracking log; no coordinator; DSAR-2025-012 urgent |
| **Owner** | DPO | **Target** | 2025-01-28 (DSAR immediate); 2025-02-15 (process) |

---

## SOA Summary (Q1 2025)

| Status | Count | % of Applicable |
|--------|-------|----------------|
| Fully Implemented | 12 | 31% |
| Partially Implemented | 22 | 56% |
| Not Implemented | 5 | 13% |
| Not Applicable | 8 | — |
| **Total Applicable** | **39** | **69% complete** |

**Target:** 100% by end 2025.

---

*Worked example. NFS is a fictional organisation.*  
*ISO/IEC 27701:2019 PIMS Toolkit | NFS SOA Excerpt | NFS-PIMS-PLN-002*
