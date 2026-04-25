
# Third-Party Privacy Assessment

| Field | Detail |
|-------|--------|
| **Document ID** | PIMS-OPS-007 |
| **Version** | 2.0 |
| **Date** | April 2025 |
| **Owner** | Data Protection Officer / Procurement |
| **Classification** | Confidential |
| **Review Date** | Annual or upon new third-party engagement |

---

## Purpose

This document defines the process for assessing and managing privacy risks associated with third-party vendors, suppliers, and PII processors. It ensures that [Organisation Name] meets its obligations under ISO/IEC 27701:2025 Controls A.7.5.2 (Organisations providing access to PII), A.7.5.3 (Processor accountability), and Annex B (PII Processor obligations), as well as GDPR Article 28 (processor contracts) and equivalent regulations.

---

## 1. Scope of Third-Party Assessment

This procedure applies to all third parties who:

- Process PII on behalf of [Organisation Name] (processors and sub-processors)
- - Have access to [Organisation Name]'s systems or environments containing PII
  - - Provide cloud or SaaS services that store or process PII
    - - Are joint PII controllers with [Organisation Name]
     
      - ---

      ## 2. Third-Party Risk Tiers

      | Tier | Description | Assessment Level |
      |------|-------------|-----------------|
      | Tier 1 — Critical | Processes large volumes of sensitive / special category PII; cross-border transfers; core business systems | Full due diligence + DPA + annual review |
      | Tier 2 — High | Processes regular customer or employee PII; cloud-hosted services | Standard due diligence + DPA + biennial review |
      | Tier 3 — Medium | Incidental access to PII; limited processing; low volumes | Questionnaire + contractual clauses + triennial review |
      | Tier 4 — Low | No PII access; public information only; or purely anonymised data | No formal assessment required |

      ---

      ## 3. Pre-Engagement Assessment Process

      ### Step 1: Privacy Risk Screening

      Before engaging any new third party that may process PII, the requesting business owner must complete the Privacy Risk Screening:

      - Does the third party require access to PII? → If Yes, proceed to Step 2
      - - What tier does the third party fall into? → Determine tier (Section 2)
        - - Has the DPO been notified? → Required before contracting
         
          - ### Step 2: Due Diligence
         
          - For Tier 1–3 suppliers, complete the following:
         
          - | Due Diligence Item | Tier 1 | Tier 2 | Tier 3 |
          - |-------------------|--------|--------|--------|
          - | Completed [Supplier Privacy Questionnaire](../SUPPLIER-PRIVACY-QUESTIONNAIRE.md) | Required | Required | Simplified |
          - | Evidence of ISO 27001 / SOC 2 / equivalent certification | Required | Preferred | Not required |
          - | Review of Privacy Policy and DPA terms | Required | Required | Required |
          - | Evidence of sub-processor controls | Required | Required | Optional |
          - | Cross-border transfer mechanism confirmed | Required | Required | If applicable |
          - | Transfer Impact Assessment (TIA) completed (if non-adequate country) | Required | Required | If applicable |
         
          - ### Step 3: Data Processing Agreement
         
          - All Tier 1–3 processors must sign a Data Processing Agreement (DPA) before processing any PII. The DPA must include (GDPR Art. 28):
         
          - - Subject matter, duration, nature, and purpose of processing
            - - Type of PII and categories of data subjects
              - - Obligations and rights of the controller
                - - Sub-processor restrictions and consent requirements
                  - - Data security requirements
                    - - Assistance with data subject rights
                      - - Deletion or return of PII at contract end
                        - - Audit rights and cooperation
                         
                          - Use [DPA-TEMPLATE.md](../DPA-TEMPLATE.md) as the standard template.
                         
                          - ### Step 4: Approval and Onboarding
                         
                          - 1. DPO reviews and approves the assessment
                            2. 2. Legal reviews and countersigns the DPA
                               3. 3. Procurement / Finance add the supplier to the Approved Supplier Register
                                  4. 4. Record the third party in the Third-Party Privacy Register (Section 7)
                                    
                                     5. ---
                                    
                                     6. ## 4. Ongoing Monitoring
                                    
                                     7. | Activity | Tier 1 | Tier 2 | Tier 3 | Owner |
                                     8. |----------|--------|--------|--------|-------|
                                     9. | Annual privacy review / re-assessment | Yes | No | No | DPO |
                                     10. | Biennial review | N/A | Yes | No | DPO |
                                     11. | Triennial review | N/A | N/A | Yes | DPO / Procurement |
                                     12. | Review DPA currency (upon contract renewal) | Yes | Yes | Yes | DPO / Legal |
                                     13. | Monitor for processor certification changes | Yes | Yes | Optional | DPO |
                                     14. | Sub-processor change notification tracking | Yes | Yes | N/A | DPO |
                                    
                                     15. ---
                                    
                                     16. ## 5. Processor Breach Notification
                                    
                                     17. All processors must notify [Organisation Name] without undue delay upon becoming aware of a PII breach affecting data processed on behalf of [Organisation Name]. This obligation must be included in all DPAs.
                                    
                                     18. [Organisation Name] will:
                                     19. 1. Record processor-reported breaches in the Privacy Breach Register (PIMS-OPS-005)
                                         2. 2. Assess whether regulatory or data subject notification is required
                                            3. 3. Coordinate response and containment with the processor
                                              
                                               4. ---
                                              
                                               5. ## 6. Sub-Processor Management
                                              
                                               6. Where processors engage sub-processors:
                                              
                                               7. 1. [Organisation Name]'s prior written consent is required (specific or general authorisation)
                                                  2. 2. Processors must flow down equivalent data protection obligations to sub-processors
                                                     3. 3. [Organisation Name] maintains a list of approved sub-processors
                                                        4. 4. Changes to sub-processors must be notified with adequate time for objection (typically 30 days)
                                                          
                                                           5. ---
                                                          
                                                           6. ## 7. Third-Party Privacy Register
                                                          
                                                           7. All assessed third parties are recorded in the Third-Party Privacy Register:
                                                          
                                                           8. | Field | Detail |
                                                           9. |-------|--------|
                                                           10. | Supplier ID | TP-YYYY-NNN |
                                                           11. | Supplier Name | [Name] |
                                                           12. | Service Provided | [Description] |
                                                           13. | Tier | 1 / 2 / 3 / 4 |
                                                           14. | PII Categories Processed | [List] |
                                                           15. | DPA Signed? | Yes / No — [Date] |
                                                           16. | Transfer Mechanism | SCCs / Adequacy / DPF / N/A |
                                                           17. | TIA Required / Completed | Yes / No |
                                                           18. | Last Assessed | [Date] |
                                                           19. | Next Review Date | [Date] |
                                                           20. | DPO Sign-off | [Name / Date] |
                                                          
                                                           21. ---
                                                          
                                                           22. ## Version History
                                                          
                                                           23. | Version | Date | Changes |
                                                           24. |---------|------|---------|
                                                           25. | 2.0 | April 2025 | Initial full content — created per ISO/IEC 27701:2025 Controls A.7.5.2, A.7.5.3, B.8.5.1; added TIA requirement for cross-border transfers; tier model; sub-processor management; EU-US DPF transfer mechanism |
                                                           26. | 1.0 | 2024 | Placeholder created — no content |
                                                          
                                                           27. ---
                                                          
                                                           28. *ISO/IEC 27701:2025 PIMS Toolkit | Third-Party Privacy Assessment | PIMS-OPS-007 | v2.0 | Classification: Confidential*
