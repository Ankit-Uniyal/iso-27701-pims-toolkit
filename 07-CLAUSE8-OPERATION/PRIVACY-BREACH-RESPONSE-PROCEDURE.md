# Privacy Breach Response Procedure

| Field | Detail |
|-------|--------|
| **Document ID** | PIMS-OPS-005 |
| **Version** | 2.0 |
| **Date** | April 2025 |
| **Owner** | Data Protection Officer |
| **Classification** | Internal — Restricted |
| **Review Date** | Annual or following a breach |

---

## Purpose

This procedure defines how [Organisation Name] detects, contains, assesses, and responds to PII (personal data) breaches, in accordance with ISO/IEC 27701:2025 Clause A.7.3.3 (Notification of PII breach) and applicable regulations including GDPR Article 33/34, UAE PDPL, and India DPDPA 2023.

---

## 1. What Constitutes a PII Breach

A PII breach is a security incident that leads to the accidental or unlawful destruction, loss, alteration, unauthorised disclosure of, or access to, Personally Identifiable Information. This includes:

- Accidental loss of device containing unencrypted PII
- - Ransomware or malware attack resulting in PII encryption or exfiltration
  - - Unauthorised access to PII by internal or external parties
    - - Sending PII to wrong recipient (misdirected email, letter, or fax)
      - - System misconfiguration resulting in PII exposure
        - - Physical theft of documents or devices containing PII
          - - Insider threat — deliberate extraction or sharing of PII
           
            - ---

            ## 2. Breach Notification Deadlines

            | Regulation | Regulator Notification | Data Subject Notification | Threshold |
            |-----------|----------------------|--------------------------|-----------|
            | GDPR / UK GDPR | Within 72 hours of awareness | Without undue delay (if high risk) | Likely to result in risk to rights and freedoms |
            | UAE PDPL | As soon as reasonably practicable | If likely to affect data subjects | All material breaches |
            | India DPDPA 2023 | Within 72 hours of awareness | As directed by regulator | Prescribed categories of breach |
            | ISO/IEC 27701:2025 | Per applicable regulation | Per applicable regulation | Per applicable regulation |

            ---

            ## 3. Breach Response Phases

            ### Phase 1: Detection and Initial Reporting (0–4 hours)

            **Trigger:** Any staff member, IT alert, third party, or regulator reports a suspected or confirmed PII breach.

            **Actions:**
            1. Staff who discovers or suspects a breach contacts the DPO immediately via [dpo@organisation.com] / [emergency contact]
            2. 2. DPO logs the incident in the Privacy Breach Register with: date/time, reporter, description, affected systems/data, initial assessment
               3. 3. DPO assigns a Breach Response Lead (BRL) — typically the DPO unless a specific CISO or senior lead is designated
                  4. 4. BRL assembles the Breach Response Team (DPO, IT/CISO, Legal, relevant business owner)
                    
                     5. ### Phase 2: Containment (0–24 hours)
                    
                     6. **Actions:**
                     7. 1. Isolate affected systems if necessary (in coordination with IT/CISO) to prevent further loss or access
                        2. 2. Revoke compromised credentials or access
                           3. 3. Preserve evidence — forensic copy of affected systems/logs (do not delete)
                              4. 4. Identify the scope: what PII was affected, how many data subjects, what categories of PII, geographic location of data subjects
                                 5. 5. Engage with any relevant third-party processors to contain the incident on their systems
                                   
                                    6. ### Phase 3: Assessment and Risk Rating (Within 24–48 hours)
                                   
                                    7. **Actions:**
                                    8. 1. Assess the nature and scope of the breach using the Breach Risk Matrix:
                                      
                                       2. | Risk Factor | Low | Medium | High |
                                       3. |-------------|-----|--------|------|
                                       4. | PII categories | Basic contact data | Sensitive data (financial, health) | Special category / biometric |
                                       5. | Volume of records | < 100 | 100–10,000 | > 10,000 |
                                       6. | Likelihood of harm | Unlikely | Possible | Likely |
                                       7. | Malicious intent | No | Uncertain | Yes |
                                      
                                       8. 2. Determine overall risk level (Low / Medium / High / Critical)
                                          3. 3. Identify affected data subjects and their locations (for jurisdictional notification obligations)
                                             4. 4. Document assessment in the Breach Register
                                               
                                                5. ### Phase 4: Regulatory Notification (Within 72 hours of Awareness)
                                               
                                                6. **Actions:**
                                                7. 1. If the breach is likely to result in risk to data subjects' rights and freedoms (GDPR threshold), notify the relevant supervisory authority within 72 hours using the applicable reporting form/portal
                                                  
                                                   2. | Regulator | Portal / Contact |
                                                   3. |-----------|-----------------|
                                                   4. | ICO (UK) | ico.org.uk/report-a-breach |
                                                   5. | EU DPA (relevant national authority) | edpb.europa.eu — national DPA portal |
                                                   6. | UAE Data Office | uaedataoffice.gov.ae |
                                                   7. | India DPBI | [Portal to be confirmed per DPDPA rules] |
                                                  
                                                   8. 2. If the 72-hour deadline cannot be met, submit an initial notification with available information and supplement once further details are known
                                                      3. 3. Record notification reference numbers in the Breach Register
                                                        
                                                         4. ### Phase 5: Data Subject Notification (If High Risk)
                                                        
                                                         5. **Actions:**
                                                         6. 1. If the breach is likely to result in high risk to data subjects, notify affected individuals without undue delay
                                                            2. 2. Notification to data subjects must include:
                                                               3.    - Nature of the breach
                                                                     -    - Name and contact details of the DPO
                                                                          -    - Likely consequences of the breach
                                                                               -    - Measures taken or proposed to address the breach
                                                                                    - 3. Notification channel: email, letter, or website notice as appropriate
                                                                                      4. 4. Record notification in the Breach Register
                                                                                        
                                                                                         5. ### Phase 6: Recovery and Remediation (Ongoing)
                                                                                        
                                                                                         6. **Actions:**
                                                                                         7. 1. Restore affected systems/data from clean backups where possible
                                                                                            2. 2. Implement remediation measures to prevent recurrence
                                                                                               3. 3. Update security controls, access controls, and staff awareness as needed
                                                                                                  4. 4. Issue corrective action in the NCR Register (PIMS-IMP-001)
                                                                                                    
                                                                                                     5. ### Phase 7: Post-Incident Review (Within 30 days of Closure)
                                                                                                    
                                                                                                     6. **Actions:**
                                                                                                     7. 1. Conduct a post-incident review meeting with the Breach Response Team
                                                                                                        2. 2. Document lessons learned and root cause analysis
                                                                                                        3. Update the Privacy Breach Register with final status
                                                                                                        4. 4. Report to the next PIMS Management Review
                                                                                                           5. 5. Consider whether DPIA or privacy risk register needs updating
                                                                                                             
                                                                                                              6. ---
                                                                                                              7. 
                                                                                                              ## 4. Privacy Breach Register
                                                                                                              
                                                                                                              All breaches (actual and suspected) are logged in the Privacy Breach Register maintained by the DPO, capturing:
                                                                                                              
                                                                                                              | Field | Details |
                                                                                                              |-------|---------|
                                                                                                              | Breach ID | BR-YYYY-NNN |
                                                                                                              | Date/Time Detected | [Date] |
                                                                                                              | Date/Time Reported to DPO | [Date] |
                                                                                                              | Nature of Breach | [Description] |
                                                                                                              | PII Categories Affected | [List] |
                                                                                                              | Number of Data Subjects | [Number or estimate] |
                                                                                                              | Risk Level | Low / Medium / High / Critical |
                                                                                                              | Regulator Notified? | Yes/No — [Date] — [Reference] |
                                                                                                              | Data Subjects Notified? | Yes/No — [Date] — [Channel] |
                                                                                                              | Breach Contained? | Yes/No — [Date] |
                                                                                                              | Root Cause | [Description] |
                                                                                                              | Corrective Actions | [NCR reference] |
                                                                                                              | Date Closed | [Date] |
                                                                                                              
                                                                                                              ---
                                                                                                              
                                                                                                              ## 5. Roles and Responsibilities
                                                                                                              
                                                                                                              | Role | Responsibility |
                                                                                                              |------|---------------|
                                                                                                              | All staff | Report suspected breaches immediately to DPO |
                                                                                                              | DPO | Lead breach response; regulatory notification; data subject notification |
                                                                                                              | IT / CISO | Technical containment; forensic evidence preservation; system recovery |
                                                                                                              | Legal | Legal assessment; regulatory response; external communications |
                                                                                                              | CEO / Senior Management | A
