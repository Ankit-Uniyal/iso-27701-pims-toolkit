# ISO/IEC 27701:2025 PIMS Implementation Guide

| Field | Detail |
|-------|--------|
| **Document ID** | PIMS-IMPL-GUIDE-001 |
| **Version** | 2.0 |
| **Date** | April 2025 |
| **Owner** | Data Protection Officer / PIMS Programme Manager |
| **Classification** | Public |
| **Review Date** | April 2026 |
| **Standard** | ISO/IEC 27701:2025 (supersedes ISO/IEC 27701:2019) |

---

## 1. Introduction

### 1.1 Purpose

This guide provides a structured, step-by-step roadmap for implementing a **Privacy Information Management System (PIMS)** in accordance with **ISO/IEC 27701:2025**. It is designed for:

- Organisations already certified to **ISO 27001:2022** seeking PIMS certification
- Organisations transitioning from ISO 27001:2013 + ISO 27701:2019 to the 2025 editions
- Privacy and GRC practitioners building a PIMS from scratch
- Data Protection Officers (DPOs) establishing a governance framework

### 1.2 What Is ISO/IEC 27701:2025?

ISO/IEC 27701:2025 is a **privacy extension to ISO/IEC 27001:2022**. It specifies requirements and provides guidance for establishing, implementing, maintaining, and continually improving a PIMS. The 2025 edition introduces:

- **Full alignment with ISO 27001:2022** (High Level Structure / Harmonised Approach)
- **Expanded Annex A/B controls** aligned to ISO 27002:2022 structure
- **Enhanced DPIA requirements** with prescriptive trigger criteria
- **Joint controller provisions** with explicit responsibility allocation
- **Transfer Impact Assessment (TIA)** for cross-border data transfers
- **Privacy by Default** as a standalone control (cross-referenced to ISO 31700:2023)
- **Harmonised terminology** — "personal data" and "PII" used interchangeably
- **Deeper ISO 29100 alignment** across all 11 privacy principles

### 1.3 Key Difference from 2019 Edition

| Aspect | 2019 Edition | 2025 Edition |
|--------|-------------|-------------|
| Base standard | ISO 27001:2013 | ISO 27001:2022 |
| Control structure | Annex A (31) + B (18) = 49 controls | Expanded, ISO 27002:2022-aligned |
| Privacy by Default | Embedded in Annex A | Standalone explicit control |
| Joint controllers | Limited | Dedicated provisions |
| DPIA triggers | General | Prescriptive criteria |
| Cross-border transfers | Safeguard references | Transfer Impact Assessment (TIA) |
| Terminology | "PII" primary | "PII" and "personal data" harmonised |
| ISO 31700 (PbD) | Not referenced | Explicitly cross-referenced |

---

## 2. Prerequisites

Before starting PIMS implementation, confirm the following prerequisites:

### 2.1 ISO 27001:2022 Foundation

ISO 27701:2025 **extends** ISO 27001:2022. Your organisation must have (or be implementing) an ISMS based on ISO 27001:2022:

- [ ] ISO 27001:2022 ISMS scope defined
- [ ] Information security risk assessment completed
- [ ] ISO 27001:2022 Statement of Applicability (SoA) established
- [ ] Management system documentation in place
- [ ] Internal audit programme operational
- [ ] Management review process established

> **Note:** If you are currently on ISO 27001:2013, you must transition to the 2022 edition before or alongside implementing ISO 27701:2025.

### 2.2 Organisational Readiness

- [ ] Senior management commitment to PIMS implementation
- [ ] Data Protection Officer (DPO) or Privacy Lead appointed
- [ ] Budget allocated for PIMS programme
- [ ] Legal/compliance function engaged
- [ ] Privacy Champion network identified across business units

### 2.3 Regulatory Landscape Confirmed

- [ ] Applicable privacy laws identified (GDPR, UAE PDPL, India DPDPA, UK GDPR, CCPA, etc.)
- [ ] PII processing activities inventoried (initial ROPA)
- [ ] Regulatory obligations documented

---

## 3. Implementation Roadmap

### Phase 1: Gap Assessment (Weeks 1–3)

**Objective:** Establish current state and identify gaps against ISO 27701:2025.

**Activities:**
1. Conduct PIMS Gap Assessment using `01-GAP-ASSESSMENT/PIMS-GAP-ASSESSMENT-CHECKLIST.md`
2. Score each control area using `GAP-ASSESSMENT-SCORING-GUIDE.md`
3. Identify all PII processing activities (initial ROPA)
4. Map existing ISMS documents to PIMS extension requirements
5. Identify joint controller relationships and sub-processor chains
6. Document the gap assessment findings and remediation priorities

**Key outputs:**
- Gap Assessment Report with maturity scores per clause
- Prioritised remediation backlog
- Initial PII processing inventory (ROPA v0.1)
- Project charter and resource plan

**Documents to use:**
- `01-GAP-ASSESSMENT/PIMS-GAP-ASSESSMENT-CHECKLIST.md`
- `01-GAP-ASSESSMENT/GAP-ASSESSMENT-SCORING-GUIDE.md`

---

### Phase 2: Context and Leadership (Weeks 3–5)

**Objective:** Define PIMS scope, establish governance, and secure leadership commitment.

**Activities:**
1. Define PIMS scope — specify which PII processing activities are in scope
2. Conduct context analysis — internal/external issues with privacy lens
3. Map interested parties — data subjects, regulators, controllers, processors, joint controllers
4. Identify all applicable legal/regulatory requirements
5. Issue Leadership Commitment Statement
6. Formalise DPO Terms of Reference
7. Establish Privacy RACI matrix
8. Publish Privacy Acceptable Use Policy

**Key outputs:**
- PIMS Scope Statement
- Context and Issues Register (privacy-extended)
- Interested Parties Register
- Legal and Regulatory Requirements Register
- Leadership Commitment Statement
- DPO Terms of Reference
- Privacy Roles and RACI Matrix

**Documents to use:**
- `03-CLAUSE4-CONTEXT/` — all 5 files
- `04-CLAUSE5-LEADERSHIP/` — all 4 files
- `02-PIMS-POLICY/PRIVACY-POLICY.md`

---

### Phase 3: Privacy Policy and Objectives (Weeks 4–6)

**Objective:** Establish the top-level Privacy Policy and measurable Privacy Objectives.

**Activities:**
1. Draft/update the Privacy Policy (extending the Information Security Policy)
2. Define measurable Privacy Objectives aligned to business context and regulatory requirements
3. Create external-facing Privacy Notice
4. Establish Privacy Acceptable Use Policy

**Key outputs:**
- Privacy Policy (Clause 5.2 extension)
- Privacy Objectives (Clause 6.2 extension)
- Privacy Notice (for data subjects)

**Documents to use:**
- `02-PIMS-POLICY/` — all 3 files

---

### Phase 4: Privacy Risk Assessment and Planning (Weeks 5–8)

**Objective:** Establish the PIMS risk assessment methodology, complete privacy risk assessment, and define the SoA.

**Activities:**
1. Define Privacy Risk Assessment Methodology (extending ISMS risk methodology)
2. Conduct Privacy Risk Assessment — identify PII-related risks for all processing activities
3. Populate Privacy Risk Register
4. Define Privacy Risk Treatment Plan
5. Select and justify applicable Annex A/B controls
6. Produce Statement of Applicability (SoA) for all updated controls
7. Identify DPIA-mandatory processing activities (using 2025 trigger criteria)

**Key outputs:**
- Privacy Risk Assessment Methodology
- Privacy Risk Register
- Privacy Risk Treatment Plan
- Statement of Applicability (SoA) — all updated Annex A/B controls
- DPIA trigger assessment results

**Documents to use:**
- `05-CLAUSE6-PLANNING/` — all 4 files

> **2025 Update:** The risk assessment must now explicitly address joint controller scenarios and cross-border transfer risks (requiring Transfer Impact Assessments).

---

### Phase 5: Support Structures (Weeks 7–10)

**Objective:** Build the supporting infrastructure for PIMS operation.

**Activities:**
1. Establish Privacy Competence and Training Register
2. Launch Privacy Awareness Programme
3. Develop Privacy Communications Plan (internal and external)
4. Implement Document Control Procedure for PIMS documents
5. Create PIMS Document Master List

**Key outputs:**
- Competence and Training Register
- Privacy Awareness Programme
- Privacy Communications Plan
- PIMS Document Control Procedure
- PIMS Document Master List

**Documents to use:**
- `06-CLAUSE7-SUPPORT/` — all 5 files

---

### Phase 6: Operational Controls (Weeks 8–14)

**Objective:** Implement all operational PIMS controls.

**Activities:**
1. Document all PII processing activities in ROPA
2. Conduct DPIAs for all high-risk processing activities (using 2025 enhanced template)
3. Implement Consent Management controls (consent lifecycle: collect, record, withdraw, refresh)
4. Establish Data Subject Rights procedure (DSAR, erasure, portability, objection, restriction)
5. Implement Privacy Breach Response procedure
6. Define Data Retention and Disposal schedules
7. Conduct Third-Party Privacy Assessments for all processors
8. Implement Cross-Border Transfer controls (including Transfer Impact Assessments where required)
9. Embed Privacy by Design and Default into project lifecycle (ISO 31700:2023 aligned)

**Key outputs:**
- Records of Processing Activities (ROPA)
- Completed DPIAs for high-risk activities
- Consent records and consent management process
- DSAR procedure and tracking mechanism
- Privacy Breach Response procedure and log
- Retention schedule and disposal records
- Processor assessment records and DPAs
- Transfer mechanism records and TIAs (where applicable)
- Privacy by Design checklist integrated into SDLC/project management

**Documents to use:**
- `07-CLAUSE8-OPERATION/` — all 9 files
- `DPA-TEMPLATE.md` (root)
- `DATA-SUBJECT-REQUEST-FORM-TEMPLATE.md` (root)

> **2025 Update:** DPIA triggers are now more prescriptive. Review the enhanced DPIA template for mandatory trigger criteria. TIAs are now an explicit requirement for cross-border transfers where adequacy decisions are absent.

---

### Phase 7: Performance Evaluation (Weeks 14–18)

**Objective:** Establish measurement, monitoring, and review mechanisms.

**Activities:**
1. Define Privacy KPIs and Metrics
2. Establish Privacy Dashboard / reporting cycle
3. Plan and conduct PIMS Internal Audit (using updated audit criteria)
4. Conduct PIMS Management Review
5. Report performance to senior management

**Key outputs:**
- Privacy KPI Metrics Dashboard
- PIMS Internal Audit Programme
- PIMS Internal Audit Report
- PIMS Management Review Minutes

**Documents to use:**
- `08-CLAUSE9-PERFORMANCE/` — all 4 files

---

### Phase 8: Improvement (Ongoing)

**Objective:** Drive continual improvement and manage nonconformities.

**Activities:**
1. Manage nonconformities and corrective actions (NCR Register)
2. Log and track continual improvement initiatives
3. Review and update PIMS documents annually or following significant changes
4. Re-assess privacy risks following incidents, new processing activities, or regulatory changes

**Key outputs:**
- NCR and Corrective Action Register
- Continual Improvement Log

**Documents to use:**
- `09-CLAUSE10-IMPROVEMENT/` — both files

---

### Phase 9: Certification Readiness (Weeks 18–24)

**Objective:** Prepare for ISO 27701:2025 certification audit.

**Pre-certification checklist:**

**Governance:**
- [ ] PIMS scope statement approved
- [ ] Privacy Policy signed by top management
- [ ] DPO appointed and Terms of Reference signed
- [ ] RACI matrix published and communicated

**Risk Management:**
- [ ] Privacy Risk Assessment completed and documented
- [ ] SoA completed — all controls addressed (include/exclude with justification)
- [ ] Privacy Risk Treatment Plan implemented and evidenced

**Operational Controls:**
- [ ] ROPA complete and current
- [ ] DPIAs completed for all high-risk activities
- [ ] Consent mechanisms implemented and auditable
- [ ] DSR procedure tested and evidenced
- [ ] Breach response procedure tested (tabletop exercise minimum)
- [ ] All third-party processors assessed and DPAs in place
- [ ] Transfer mechanisms established for all cross-border transfers
- [ ] TIAs completed where required
- [ ] Privacy by Design embedded in project/SDLC process

**Performance:**
- [ ] Internal PIMS audit completed (covering all clauses + Annex A/B)
- [ ] Audit findings documented with corrective actions
- [ ] Management Review completed with privacy agenda items
- [ ] KPI reporting cycle established

**Documentation:**
- [ ] All required PIMS documents in place
- [ ] Document control applied to all PIMS documents
- [ ] Version history maintained
- [ ] Records of all key PIMS activities retained

---

## 4. PIMS Document Architecture

### Hierarchy

```
Level 1:  Privacy Policy (top-level commitment)
Level 2:  PIMS Procedures and Standards (how we do it)
Level 3:  Work Instructions and Registers (what we record)
Level 4:  Records and Evidence (proof it happened)
```

### Mandatory Documents (ISO 27701:2025)

| Clause | Required Document |
|--------|------------------|
| 4.1 / 4.2 | Context analysis and interested parties register |
| 4.3 | PIMS Scope Statement |
| 5.1 | Leadership Commitment Statement |
| 5.2 | Privacy Policy |
| 6.1 | Privacy Risk Assessment Methodology and Results |
| 6.2 | Privacy Objectives |
| 7.2 | Competence records |
| 7.5 | Documented Information Procedure |
| 8.1 | PII Processing Activity Records (ROPA) |
| 8.2 / Annex A | DPIA records (where triggered) |
| 9.1 | Performance monitoring records |
| 9.2 | Internal Audit Programme and Reports |
| 9.3 | Management Review minutes |
| 10.1 | Corrective action records |
| Annex A | SoA (including all Annex A and B controls) |

---

## 5. Using the Python Scripts

Three Python GRC automation scripts are included in `13-SCRIPTS/`:

### pims_soa_tracker.py

Tracks SoA control completion status across all updated Annex A/B controls.

```bash
python 13-SCRIPTS/pims_soa_tracker.py
```

### pims_gap_checker.py

Automated gap assessment checker — maps your current state against PIMS clause requirements.

```bash
python 13-SCRIPTS/pims_gap_checker.py
```

### dpia_risk_scorer.py

DPIA risk scoring tool with threshold alerts. Supports interactive mode and batch CSV processing.

```bash
# Interactive mode
python 13-SCRIPTS/dpia_risk_scorer.py

# Demo mode
python 13-SCRIPTS/dpia_risk_scorer.py --demo

# Batch mode
python 13-SCRIPTS/dpia_risk_scorer.py --batch input.csv
```

---

## 6. Worked Examples

The `12-WORKED-EXAMPLE/` folder contains completed examples using the fictional **Nexus Financial Services Ltd (NFS)** organisation. Use these as reference when populating your own PIMS documents.

Available examples:
- NFS PIMS Scope Statement
- NFS Privacy Risk Register Entry (3 sample risks)
- NFS SoA Excerpt (Annex A controller controls)
- NFS DPIA Entry (customer onboarding analytics)
- NFS Privacy Breach Log Entry (employee laptop loss)

---

## 7. Certification Pathway

```
ISO 27001:2022           ISO 27701:2025
    ISMS          +      PIMS Extension
      |                       |
      +----------+------------+
                 |
         Combined Audit
                 |
         Dual Certification
     (ISO 27001 + ISO 27701)
```

ISO 27701:2025 certification is achieved through a **combined audit** with ISO 27001:2022. The certification body audits both the ISMS and the PIMS extension simultaneously.

**Typical timeline:** 12–18 months from initiation to certification (for organisations building from scratch).

**For transition from 27701:2019:** Allow 6–9 months for gap assessment, control updates, and re-audit against the 2025 edition. Transition deadline is typically set by your certification body (commonly 3 years from publication of the 2025 edition).

---

## 8. Version History

| Version | Date | Description |
|---------|------|-------------|
| 2.0 | April 2025 | Updated for ISO/IEC 27701:2025 — HLS alignment, DPIA enhancements, TIA, joint controllers, ISO 31700 cross-reference, India DPDPA added |
| 1.0 | 2024 | Initial release — ISO/IEC 27701:2019 edition |

---

*ISO/IEC 27701:2025 PIMS Toolkit | Implementation Guide | PIMS-IMPL-GUIDE-001 | v2.0 | Classification: Public*
