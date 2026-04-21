# Cross-Border PII Transfer Procedure

| Field | Detail |
|-------|--------|
| **Document ID** | PIMS-OPS-008 |
| **Version** | 2.0 |
| **Date** | April 2025 |
| **Owner** | Data Protection Officer |
| **Classification** | Confidential — Internal Use |
| **Review Date** | April 2026 |
| **Standard** | ISO/IEC 27701:2025 — Clause A.7.4.3, A.7.5.1, B.8.5; GDPR Art. 44–49 |

---

## 1. Purpose

This procedure defines how [Organisation Name] identifies, authorises, documents, and controls the transfer of personally identifiable information (PII / personal data) across jurisdictional boundaries (international data transfers).

This procedure is updated for **ISO/IEC 27701:2025**, which introduces explicit **Transfer Impact Assessment (TIA)** requirements for cross-border transfers where no adequacy decision exists — reflecting post-Schrems II regulatory requirements and EDPB guidance.

---

## 2. Scope

This procedure applies to:
- All transfers of PII from the Organisation's home jurisdiction to third countries or international organisations
- Transfers by the Organisation acting as a PII Controller (Annex A.7.5.1)
- Transfers made by PII Processors on the Organisation's instructions (Annex B.8.5)
- Cloud services, SaaS platforms, sub-processors, and service providers in third countries
- Intra-group transfers where data crosses jurisdictional boundaries

---

## 3. Legal Framework

### 3.1 Transfer Mechanisms

PII may only be transferred to third countries where one of the following safeguards applies:

| Mechanism | Basis | When to Use |
|-----------|-------|-------------|
| **Adequacy Decision** | Art. 45 GDPR | Destination country/territory has been deemed adequate by the European Commission (or relevant authority) |
| **Standard Contractual Clauses (SCCs)** | Art. 46(2)(c) GDPR | No adequacy decision; use EDPB-approved SCCs (updated 2021 set) — **TIA required** |
| **Binding Corporate Rules (BCRs)** | Art. 47 GDPR | Intra-group transfers; BCRs approved by supervisory authority — **TIA review required** |
| **Approved Codes of Conduct / Certification** | Art. 46(2)(e)(f) GDPR | Sector-specific approved codes or ISO 27701 certification schemes — **TIA may be required** |
| **Derogations** | Art. 49 GDPR | Only for specific, non-repetitive situations (explicit consent, contract necessity, legal claims, vital interests, public register) |

### 3.2 ISO 27701:2025 TIA Requirement

**NEW in 2025:** ISO 27701:2025 control A.7.5.1 and related cross-border transfer controls now explicitly require a **Transfer Impact Assessment (TIA)** when transferring PII to countries without an adequacy decision.

A TIA assesses:
1. Whether the transfer mechanism (e.g., SCCs) provides effective protection given the destination country's legal framework
2. Whether local laws/regulations in the destination country could undermine the protection offered by the transfer mechanism
3. Whether supplementary measures are needed to bring protection up to the EU/EEA standard

---

## 4. Transfer Identification and Classification

### 4.1 Identifying Transfers

All cross-border PII transfers must be identified via:
- Records of Processing Activities (ROPA) — column: "Third Country Recipients"
- Third-party/processor contracts — data location and sub-processor geography
- IT asset inventory — cloud service regions, CDN locations, backup locations
- Annual transfer audit

### 4.2 Transfer Register

All identified cross-border transfers must be entered in the **Cross-Border Transfer Register**:

| Transfer ID | Description | PII Categories | Destination Country | Recipient | Transfer Mechanism | TIA Required? | TIA Status | Review Date |
|------------|-------------|---------------|--------------------|-----------|--------------------|--------------|-----------|-------------|
| CBT-001 | | | | | | Yes / No | | |
| CBT-002 | | | | | | | | |

---

## 5. Transfer Impact Assessment (TIA) — ISO 27701:2025

### 5.1 When is a TIA Required?

A TIA is **mandatory** when:
- The destination country/territory has **no adequacy decision** from the relevant supervisory authority, AND
- The organisation relies on SCCs, BCRs, approved codes, or certification as the transfer mechanism

A TIA is **not required** when:
- An adequacy decision is in force for the destination country and the specific transfer type
- The transfer uses Art. 49 derogations (but derogation basis must be documented)

### 5.2 TIA Process

**Step 1 — Identify the Transfer**
Document the transfer in the Cross-Border Transfer Register (Transfer ID, PII categories, purpose, destination, recipient, mechanism).

**Step 2 — Check for Adequacy**
Check the current list of adequate countries/territories (EU Commission / relevant authority). If adequate → proceed with transfer under adequacy decision; no TIA required.

**Step 3 — Select Transfer Mechanism**
If no adequacy decision, select the appropriate transfer mechanism (typically SCCs). Execute the relevant contractual arrangements.

**Step 4 — Conduct Transfer Impact Assessment**
The TIA must assess:

| TIA Element | Description |
|------------|-------------|
| **Country legal assessment** | Does the destination country's law provide equivalent protection to EU/EEA law? Assess: data protection laws, government access laws (surveillance, law enforcement), judicial remedies |
| **Effectiveness of mechanism** | Does the selected transfer safeguard (e.g., SCCs) provide effective protection given the legal landscape? |
| **Risk assessment** | What is the likelihood that the transfer safeguard will be overridden by local law? |
| **Supplementary measures** | Are additional technical, contractual, or organisational measures needed? |
| **Conclusion** | Can the transfer proceed? If yes, on what basis? If supplementary measures needed, what are they? |

**Step 5 — Document and Approve TIA**
The TIA report must be:
- Documented using the TIA Report Template (Section 6 below)
- Reviewed and approved by the DPO
- Filed in the Cross-Border Transfer Register
- Retained as evidence for supervisory authority review

**Step 6 — Implement Supplementary Measures (if required)**
Examples of supplementary measures:
- End-to-end encryption (with key management in the EU/EEA)
- Pseudonymisation before transfer
- Split processing (sensitive data elements remain in EU/EEA)
- Contractual provisions (enhanced obligations on recipient)
- Technical measures (VPNs, data residency controls)

**Step 7 — Monitor and Review**
TIAs must be reviewed:
- Annually, or
- When there is a material change in the destination country's legal framework
- When the adequacy status of a country changes
- Following a relevant court ruling or regulatory guidance update

### 5.3 TIA Report Template

```
TRANSFER IMPACT ASSESSMENT (TIA) REPORT

TIA Reference: TIA-[YYYY]-[NNN]
Date: 
Transfer ID(s): 
Destination Country: 
Recipient Organisation: 
PII Categories: 
Transfer Mechanism: 
DPO Reviewer: 

1. COUNTRY LEGAL ASSESSMENT
   1.1 Data Protection Law: [Country's data protection framework]
   1.2 Government/Law Enforcement Access: [Powers, oversight, remedies]
   1.3 Judicial Remedies Available to Data Subjects: [Yes/No/Partial]
   1.4 International Agreements: [EU adequacy status, treaties, frameworks]
   
2. EFFECTIVENESS OF TRANSFER MECHANISM
   2.1 Does the transfer mechanism (e.g., SCCs) provide effective protection? [Yes/No/Conditional]
   2.2 Is there a realistic risk that local law will override the mechanism? [Low/Medium/High]
   2.3 Assessment rationale:
   
3. SUPPLEMENTARY MEASURES
   3.1 Are supplementary measures required? [Yes/No]
   3.2 Measures implemented:
       - Technical: 
       - Contractual: 
       - Organisational: 
   
4. CONCLUSION
   4.1 Can the transfer proceed? [Yes / Yes with measures / No]
   4.2 Conditions:
   4.3 Next review date:

5. APPROVAL
   DPO Signature: _______________  Date: _______________
```

---

## 6. Processor Obligations for Cross-Border Transfers

When the Organisation acts as a **PII Processor** (Annex B.8.5):

- Cross-border transfers are only made with **explicit controller authorisation**
- Transfer destinations are pre-approved in the Data Processing Agreement
- Any new transfer destinations require controller approval before transfer commences
- The Organisation's own sub-processors may not make cross-border transfers without equivalent authorisation
- Transfer records are maintained and available to the controller

---

## 7. Roles and Responsibilities

| Role | Responsibility |
|------|---------------|
| **DPO** | Approve TIAs; maintain transfer register; monitor adequacy status changes; advise on transfer mechanisms |
| **Legal / Compliance** | Assess country legal frameworks; review and advise on transfer mechanisms; execute SCCs/BCRs |
| **IT / Security** | Implement technical supplementary measures; identify cloud/SaaS data locations |
| **Procurement** | Identify supplier data locations; include transfer controls in contracts |
| **Business Owners** | Notify DPO of new international transfers before initiation |

---

## 8. Monitoring and Review

| Activity | Frequency | Owner |
|---------|-----------|-------|
| Review adequacy decision status for all destination countries | Quarterly | DPO |
| Review and update Cross-Border Transfer Register | Annually / on change | DPO |
| Review TIAs for destination countries | Annually / on legal change | DPO / Legal |
| Audit transfer controls for processors | Annually | DPO / Audit |
| Report cross-border transfer status to management review | Annually | DPO |

---

## 9. Version History

| Version | Date | Description |
|---------|------|-------------|
| 2.0 | April 2025 | Updated for ISO/IEC 27701:2025 — **TIA requirements added** (A.7.5.1 explicit control), Schrems II post-ruling alignment, EDPB guidance on supplementary measures, TIA report template, adequacy monitoring requirements |
| 1.0 | 2024 | Initial release — ISO/IEC 27701:2019 |

---

*ISO/IEC 27701:2025 PIMS Toolkit | Cross-Border PII Transfer Procedure | PIMS-OPS-008 | v2.0 | Classification: Confidential*
