# Privacy Risk Assessment Methodology

**Document ID:** PIMS-PLN-003  
**Version:** 1.0  
**Date:** 2025-01-01  
**Owner:** Data Protection Officer  
**Classification:** Internal  
**Review Date:** 2026-01-01

---

## 1. Purpose

This methodology defines the approach, criteria, and process for identifying, analysing, evaluating, and treating privacy risks to individuals (data subjects) arising from the organisation's PII processing activities. It supports compliance with ISO/IEC 27701:2019 Clause 6.1 and aligns with ISO 31000, GDPR Article 35, and the NIST Privacy Framework.

---

## 2. Scope

This methodology applies to:
- All PII processing activities identified in the ROPA / PII Processing Inventory
- New processing activities, systems, or significant changes (triggering a DPIA)
- Third-party processors and shared processing relationships
- Cross-border data transfers
- Automated decision-making and profiling activities

---

## 3. Definitions

| Term | Definition |
|------|-----------|
| **Privacy Risk** | The potential adverse effect on individuals (data subjects) arising from PII processing — including harm, embarrassment, discrimination, financial loss, or loss of control over personal data |
| **Likelihood** | The probability that a privacy risk event will materialise |
| **Impact** | The severity of harm to individuals if the risk event occurs |
| **Risk Score** | Likelihood × Impact (1–25 scale) |
| **Risk Owner** | The role accountable for managing and treating a specific risk |
| **Residual Risk** | The risk remaining after controls and mitigating measures are applied |
| **Risk Appetite** | The level of risk the organisation is willing to accept |

---

## 4. Privacy Risk Methodology Framework

### 4.1 Step 1 — Establish Context

Before assessing risks, establish:

**Internal Context:**
- Processing purpose and legal basis
- Categories and volumes of PII involved
- Technical and organisational controls already in place
- Applicable policies and procedures

**External Context:**
- Applicable laws and regulations (GDPR, UAE PDPL, LGPD, etc.)
- Regulatory guidance and supervisory authority priorities
- Industry standards (ISO 27701, NIST Privacy Framework, ISO 29100)
- Subject matter expectations and vulnerability factors

**Risk Criteria:**
- Risk appetite statement (see Section 8)
- Escalation thresholds
- Treatment mandatory thresholds

### 4.2 Step 2 — Identify Privacy Risks

Identify risks by examining:

**Threat Categories:**

| Threat Category | Examples |
|----------------|----------|
| **Unauthorised access** | Data breaches, insider threats, credential compromise |
| **Unlawful processing** | No valid legal basis, purpose limitation violations |
| **Inaccuracy / data quality** | Incorrect data leading to wrong decisions about individuals |
| **Excessive retention** | Data held beyond permitted periods |
| **Cross-border violations** | Transfers to inadequate third countries without safeguards |
| **Third-party failures** | Processor non-compliance, contractor data misuse |
| **Individual rights failures** | Failure to respond to DSARs, erasure requests |
| **Consent failures** | Invalid consent mechanisms, withdrawn consent not honoured |
| **Automated decision-making** | Profiling without transparency or right to contest |
| **Physical threats** | Lost devices, paper records mishandling |

**Risk Identification Methods:**
- Review of PII processing inventory / ROPA entries
- DPIA screening questionnaires
- Internal audit findings and NCRs
- Incident and breach history analysis
- Gap assessment against ISO 27701 controls
- Stakeholder workshops with process owners
- Regulatory guidance and enforcement action review

### 4.3 Step 3 — Analyse Risks

**Likelihood Scale:**

| Score | Likelihood | Description |
|-------|-----------|-------------|
| 1 | Very Low | Unlikely to occur; no historical precedent; strong preventive controls |
| 2 | Low | Could occur occasionally; limited instances; partial controls |
| 3 | Medium | Might occur periodically; some historical incidents; moderate controls |
| 4 | High | Likely to occur; recurring issues; weak controls |
| 5 | Very High | Almost certain to occur; known active threat; minimal controls |

**Impact Scale (Harm to Individuals):**

| Score | Impact Level | Description |
|-------|-------------|-------------|
| 1 | Negligible | Minimal or no actual harm to individuals; inconvenience only |
| 2 | Minor | Minor harm — temporary embarrassment, minor data quality issue |
| 3 | Moderate | Significant harm — discrimination, financial loss, reputational damage |
| 4 | Major | Serious harm — identity theft, employment consequences, financial fraud |
| 5 | Severe / Catastrophic | Life-altering harm — physical danger, severe discrimination, significant financial ruin |

**Impact Assessment Factors:**

When assessing impact on individuals, consider:
- Number of data subjects affected (scale)
- Sensitivity of PII categories (special category data scores higher)
- Reversibility of harm
- Vulnerability of affected data subjects (children, medical patients, employees)
- Cross-border implications
- Whether the harm can be mitigated after the event

### 4.4 Step 4 — Evaluate Risks (Risk Scoring)

**Risk Score = Likelihood × Impact**

**Risk Heat Map:**

|  | **Impact 1** | **Impact 2** | **Impact 3** | **Impact 4** | **Impact 5** |
|--|-------------|-------------|-------------|-------------|-------------|
| **Likelihood 5** | 5 | 10 | 15 | 20 | **25** |
| **Likelihood 4** | 4 | 8 | 12 | **16** | **20** |
| **Likelihood 3** | 3 | 6 | 9 | 12 | **15** |
| **Likelihood 2** | 2 | 4 | 6 | 8 | 10 |
| **Likelihood 1** | 1 | 2 | 3 | 4 | 5 |

**Risk Rating Table:**

| Score Range | Risk Rating | Action Required |
|-------------|------------|----------------|
| 20–25 | 🔴 **Critical** | Immediate escalation to DPO and senior management; processing must be suspended or immediate controls implemented; DPIA mandatory |
| 12–19 | 🟠 **High** | DPO must be informed; documented treatment plan with target date required within 30 days |
| 6–11 | 🟡 **Medium** | Treatment plan required; review at next management meeting; monitoring increased |
| 2–5 | 🟢 **Low** | Accept with monitoring; document in risk register; review annually |
| 1 | ⚪ **Minimal** | Accept; note in risk register; no further action required |

### 4.5 Step 5 — Treat Risks

**Treatment Options:**

| Option | Description | When to Use |
|--------|-------------|-------------|
| **Avoid** | Cease or do not commence the processing activity | Critical/High risks where controls insufficient or disproportionate |
| **Reduce / Mitigate** | Apply technical or organisational controls to lower likelihood or impact | Most risks where controls are available and proportionate |
| **Transfer** | Share risk through contractual arrangements (DPAs, insurance) | Third-party processor risks; financial risks |
| **Accept** | Formally document and accept the residual risk | Low/Minimal risks; where further mitigation is disproportionate |

**Treatment Controls Examples:**

| Risk Category | Example Controls |
|--------------|----------------|
| Unauthorised access | Encryption, access controls, MFA, DLP tools |
| Unlawful processing | Legal basis review, consent management system |
| Data quality | Validation rules, accuracy checks, correction procedures |
| Excessive retention | Automated retention schedules, disposal procedures |
| Cross-border transfers | SCCs, Binding Corporate Rules, adequacy decisions |
| Third-party risks | DPAs, supplier assessments, audit rights |
| Rights failures | DSR management system, response SLAs |

### 4.6 Step 6 — Monitor and Review

- Risk register reviewed at minimum **every 6 months** or following a material change
- All Critical and High risks reviewed **monthly** until treated to Medium or below
- Risk treatment effectiveness assessed through KPI monitoring and audit findings
- Privacy incidents trigger immediate risk register review for affected processing activities
- Annual full risk assessment conducted as input to Management Review

---

## 5. Privacy Risk Assessment Triggers (When to Assess)

A privacy risk assessment is triggered by:

| Trigger | Action Required |
|---------|----------------|
| New processing activity | Full risk assessment; DPIA screening required |
| Significant system change | Re-assess affected risks; DPIA if screening positive |
| New third-party processor | Supplier privacy assessment + risk review |
| New cross-border transfer | Transfer impact assessment + risk entry |
| Privacy incident or breach | Immediate risk review for affected processing |
| New legislation or regulation | Compliance gap assessment + risk review |
| Management Review | Annual full risk register review |
| Internal audit finding | Risk entry for identified gaps |

---

## 6. DPIA Threshold Criteria

A full DPIA is **mandatory** when processing is:
- Systematic and extensive profiling with significant effects
- Processing of special category data at scale
- Systematic monitoring of publicly accessible areas
- Processing of children's data in online services
- Cross-border transfer to a country without adequacy decision
- Novel technology or repurposed data with high uncertainty
- Any processing assessed as **Critical** risk (score 20–25)

---

## 7. Roles and Responsibilities

| Role | Responsibility |
|------|---------------|
| **DPO** | Owns and approves the methodology; reviews all High/Critical risks; presents to management review |
| **Risk Owner (Process Owner/BU)** | Identifies risks for their processing activities; implements treatments; reports progress |
| **CISO** | Supports technical risk identification; implements security controls |
| **Legal Counsel** | Advises on legal basis, regulatory risk, and cross-border transfer risks |
| **Internal Audit** | Independently reviews risk assessment outputs; identifies gaps |
| **Senior Management** | Approves risk appetite; receives escalations for Critical risks |

---

## 8. Risk Appetite Statement

**Overall Risk Appetite:** The organisation has a **LOW** appetite for privacy risks that could cause harm to individuals or result in regulatory enforcement action.

| Risk Category | Appetite | Maximum Acceptable Residual Score |
|--------------|---------|----------------------------------|
| Risk of harm to vulnerable individuals | Zero tolerance | 0 (Critical or High must be treated) |
| Regulatory non-compliance | Very Low | Maximum residual score: 5 |
| Reputational privacy risks | Low | Maximum residual score: 8 |
| Operational privacy risks | Medium | Maximum residual score: 11 |

---

## 9. Integration with PIMS

This methodology integrates with:

| PIMS Document | Integration Point |
|--------------|------------------|
| Privacy Risk Register (PIMS-PLN-001) | Output of risk assessment; records all identified risks |
| Privacy Risk Treatment Plan (PIMS-PLN-004) | Treatment actions for risks above appetite |
| DPIA Template (PIMS-OPS-001) | Full assessment for high-risk processing |
| Statement of Applicability (PIMS-PLN-002) | Controls selected as part of treatment |
| KPI Dashboard (PIMS-PER-001) | Risk metrics monitored and reported |
| Management Review (PIMS-PER-004) | Risk status presented to senior management |

---

## 10. Record of Changes

| Version | Date | Author | Change Description |
|---------|------|--------|--------------------|
| 1.0 | 2025-01-01 | DPO | Initial release |

---

*ISO/IEC 27701:2019 PIMS Toolkit | Privacy Risk Assessment Methodology | PIMS-PLN-003*
