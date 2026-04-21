# Privacy by Design and Privacy by Default Procedure

| Field | Detail |
|-------|--------|
| **Document ID** | PIMS-OPS-009 |
| **Version** | 2.0 |
| **Date** | April 2025 |
| **Owner** | Data Protection Officer / CISO |
| **Classification** | Confidential — Internal Use |
| **Review Date** | April 2026 |
| **Standard** | ISO/IEC 27701:2025 — **A.7.2.8 (Privacy by Default — standalone)**, B.8.3.1; ISO/IEC 31700:2023; GDPR Art. 25 |

---

## 1. Purpose

This procedure defines how [Organisation Name] embeds **Privacy by Design (PbD)** and **Privacy by Default (PbDef)** into its systems, services, processes, and products throughout their entire lifecycle.

**ISO/IEC 27701:2025 upgrade note:** The 2025 edition elevates Privacy by Default to a **standalone control (A.7.2.8)** for PII Controllers and **B.8.3.1** for PII Processors. This supersedes the 2019 approach where PbD was embedded across multiple controls. This procedure is updated to reflect this mandatory standalone status and alignment with **ISO/IEC 31700:2023** — the international standard dedicated to Privacy by Design.

---

## 2. Scope

This procedure applies to:
- All new systems, applications, services, and products that process PII
- All significant changes to existing systems that affect PII processing
- All new business processes that involve the collection, use, or disclosure of PII
- All third-party/vendor systems and services that process PII on behalf of the Organisation
- Cloud migrations, API integrations, and data sharing arrangements

---

## 3. Privacy by Design Principles

The Organisation applies the **seven foundational principles of Privacy by Design** (Cavoukian, adopted by ISO/IEC 31700:2023 and referenced in ISO 27701:2025):

| Principle | Description | Implementation Approach |
|-----------|-------------|------------------------|
| **1. Proactive not Reactive; Preventative not Remedial** | Anticipate and prevent privacy-invasive events before they occur | Privacy review at project initiation; privacy risk assessment before build |
| **2. Privacy as the Default Setting** | Maximum privacy protection automatically, without action from the data subject | All systems default to most privacy-protective settings |
| **3. Privacy Embedded into Design** | Privacy built in as an essential component, not bolted on after | Privacy requirements in system architecture and design specifications |
| **4. Full Functionality — Positive-Sum, not Zero-Sum** | Privacy and functionality achieved together; not at the expense of each other | Design for both security AND privacy objectives simultaneously |
| **5. End-to-End Security — Full Lifecycle Protection** | Strong security measures applied throughout the full data lifecycle | Data encrypted at rest and in transit; secure deletion at end of lifecycle |
| **6. Visibility and Transparency** | Openness about purposes and practices to data subjects and operators | Clear privacy notices; audit trails; privacy-transparent system design |
| **7. Respect for User Privacy** | Keep systems and processes people-centred; protect individual privacy interests | User controls; consent management; data subject rights baked in |

---

## 4. Privacy by Default (ISO 27701:2025 — A.7.2.8)

**Privacy by Default** is a standalone mandatory control in ISO 27701:2025. It requires that:

1. **Only the minimum PII necessary** for the specific purpose is processed by default
2. **PII is not shared** with third parties without explicit consent or legal basis by default
3. **Data retention** defaults to the minimum period necessary
4. **Privacy settings** presented to users default to the most privacy-protective option
5. **Features that share, publish, or expose PII** are off by default
6. **No action required by the data subject** to obtain basic privacy protections

### 4.1 Privacy by Default — Implementation Checklist

For every new system, service, or feature processing PII, the following defaults must be confirmed:

| Check | Requirement | Confirmed? |
|-------|-------------|-----------|
| PbDef-01 | Minimal data collection by default — only what is necessary for the primary function | ☐ |
| PbDef-02 | No social sharing or public visibility by default | ☐ |
| PbDef-03 | Privacy settings start at maximum protection | ☐ |
| PbDef-04 | Marketing / optional communications off by default | ☐ |
| PbDef-05 | Analytics/tracking minimal by default (cookie consent required for non-essential) | ☐ |
| PbDef-06 | Data retention set to minimum required period by default | ☐ |
| PbDef-07 | Third-party data sharing off by default | ☐ |
| PbDef-08 | Location data, biometrics, special categories off/opt-in by default | ☐ |
| PbDef-09 | API outputs anonymised/pseudonymised by default where possible | ☐ |
| PbDef-10 | Profiling and automated decision-making requires explicit opt-in | ☐ |

---

## 5. ISO/IEC 31700:2023 — Privacy by Design Standard

ISO/IEC 27701:2025 explicitly cross-references **ISO/IEC 31700:2023** as the implementation standard for Privacy by Design. The Organisation aligns its PbD approach to ISO 31700:2023, which:

- Provides a technology-neutral framework for PbD
- Establishes requirements for embedding privacy into products/services before launch
- Defines 30 PbD requirements across: accountability, privacy risk management, privacy controls, privacy capability, and monitoring
- Addresses the full product/service lifecycle from design through disposal

### 5.1 ISO 31700:2023 Key Requirement Mapping

| ISO 31700 Area | Requirement | PIMS Implementation |
|---------------|-------------|---------------------|
| Accountability | Designate responsible person for PbD | DPO + System Owner responsible for PbD review |
| Privacy risk management | Identify and mitigate privacy risks in design | DPIA / Privacy Risk Assessment for all new processing |
| Privacy controls | Implement controls that protect privacy by design | Technical controls (encryption, pseudonymisation, access control) built in |
| Privacy capability | Staff trained on PbD requirements | PbD training for developers, architects, product managers |
| Consumer-facing privacy | Privacy notices, consent, rights embedded in product | Privacy notice, consent UI, and DSAR mechanism built into product |
| Monitoring | Ongoing monitoring of privacy control effectiveness | Privacy KPIs; annual PbD review of systems |

---

## 6. Privacy by Design Integration Points

### 6.1 Project Initiation

At project kick-off, the Project Manager must:
1. Complete the **PbD Screening Questionnaire** (Section 8)
2. Involve the DPO/Privacy team from day one
3. Document privacy requirements in the project brief/PRD

### 6.2 System Design and Architecture

The Technical Architect must:
1. Include privacy architecture considerations in system design
2. Apply **data minimisation** in data model design (only necessary fields)
3. Apply **pseudonymisation** where data subjects are not needed to be identified by systems
4. Apply **encryption** at rest and in transit as default
5. Design for **data subject rights** — delete, export, restrict, rectify must be technically feasible
6. Design for **audit logging** of PII access and changes

### 6.3 Development and Build

Developers must:
1. Follow the **Privacy-Aware Coding Checklist**
2. Not log PII in application logs by default
3. Not hard-code PII or credentials
4. Build consent management into all data collection flows
5. Build data retention/deletion into the data model

### 6.4 Testing and QA

Test teams must:
1. Not use real/live PII in test environments (use synthetic or anonymised data)
2. Include privacy test cases in QA test plans
3. Verify Privacy by Default settings are active in test builds

### 6.5 Launch / Go-Live

Before go-live, the Privacy Gate Review must confirm:
1. DPIA completed (where triggered) and DPO sign-off obtained
2. Privacy Notice updated and published
3. Consent mechanism implemented (where required)
4. Data Subject Rights mechanism functional
5. Privacy by Default checklist completed
6. Retention and disposal mechanism operational

### 6.6 Ongoing Operation

Post-launch:
1. Annual privacy review of all live systems processing significant PII
2. Review triggered by significant system changes
3. Privacy KPIs monitored (see PRIVACY-KPI-METRICS-DASHBOARD.md)

---

## 7. Data Protection Impact Assessment (DPIA) Trigger Criteria

A DPIA is **mandatory** before processing commences when ANY of the following apply (ISO 27701:2025 enhanced criteria):

| Trigger | Description |
|---------|-------------|
| Systematic/large-scale profiling | Systematic evaluation of personal aspects including profiling |
| Special categories at scale | Large-scale processing of special categories of data (health, biometric, racial origin, etc.) |
| Systematic monitoring | Systematic monitoring of publicly accessible areas |
| Innovative technology | New technologies (AI/ML, facial recognition, tracking, IoT) |
| Denial of service risk | Processing that could result in individuals being denied access to services or contracts |
| Cross-matching datasets | Combining data from two or more sources where individuals don't expect this |
| Vulnerable data subjects | Processing data of children, employees, vulnerable individuals |
| Transfer without adequate safeguard | Cross-border transfer without adequacy decision (TIA also required) |
| Score or rank | Scoring or ranking individuals based on processing |
| High volume | Large-scale processing of PII not otherwise captured above |

> **Note:** GDPR supervisory authorities (including ICO) publish lists of processing that always requires DPIA. Refer to applicable authority's list.

---

## 8. PbD Screening Questionnaire

Complete at project initiation to determine privacy requirements:

| # | Question | Yes | No | Notes |
|---|----------|-----|----|-------|
| 1 | Does this project collect, use, or disclose PII? | | | |
| 2 | Is this a new type of PII processing not previously done? | | | |
| 3 | Does it process special categories of personal data? | | | |
| 4 | Does it involve children's data? | | | |
| 5 | Does it involve automated decision-making or profiling? | | | |
| 6 | Does it involve cross-border data transfers? | | | |
| 7 | Does it involve new third-party processors or sub-processors? | | | |
| 8 | Does it use new technology (AI, biometrics, tracking, IoT)? | | | |
| 9 | Does it involve large-scale monitoring of individuals? | | | |
| 10 | Could the processing result in individuals being denied services? | | | |

**Scoring:**
- 1 or more "Yes" → Privacy review and DPO consultation required
- 3 or more "Yes" → Full DPIA required before processing commences

---

## 9. Roles and Responsibilities

| Role | Responsibility |
|------|---------------|
| **DPO** | Privacy Gate Reviews; DPIA sign-off; PbD programme governance; ISO 31700 oversight |
| **CISO** | Technical privacy controls; security by design; encryption standards |
| **Architects / Developers** | Embed PbD into technical design; apply Privacy by Default; privacy-aware coding |
| **Product Managers** | PbD Screening Questionnaire at project initiation; include privacy requirements in product specs |
| **Project Managers** | Involve DPO from kick-off; Privacy Gate Review milestones |
| **Procurement** | PbD requirements in vendor contracts; assess supplier PbD capability |

---

## 10. Version History

| Version | Date | Description |
|---------|------|-------------|
| 2.0 | April 2025 | Updated for ISO/IEC 27701:2025 — **A.7.2.8 Privacy by Default now a standalone control**; ISO/IEC 31700:2023 explicit alignment; B.8.3.1 processor PbD; enhanced DPIA trigger criteria; seven PbD principles formally embedded |
| 1.0 | 2024 | Initial release — ISO/IEC 27701:2019 |

---

*ISO/IEC 27701:2025 PIMS Toolkit | Privacy by Design and Default Procedure | PIMS-OPS-009 | v2.0 | Classification: Confidential*
