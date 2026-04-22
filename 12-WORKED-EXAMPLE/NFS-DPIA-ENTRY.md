# Worked Example: DPIA Entry — Marketing Profiling
## Nexus Financial Services Ltd (NFS)

> **WORKED EXAMPLE — FOR ILLUSTRATIVE PURPOSES ONLY**  
> NFS is a fictional organisation.

---

**DPIA Reference:** NFS-DPIA-2025-004  
**Project:** Automated Lead Scoring and Customer Segmentation  
**DPIA Author:** Sarah Chen, DPO | **Date:** 2025-01-20

---

## 1. Project Description

NFS Marketing team proposes implementing an automated lead scoring algorithm within HubSpot that analyses customer behaviour data (email opens, website visits, loan application history, product interest signals) to assign a "propensity to buy" score (0–100) and segment customers into product recommendation categories.

---

## 2. DPIA Screening

| Question | Answer |
|---------|--------|
| Systematic profiling with significant effects? | Yes — used to decide which products to offer |
| Special category data involved? | No |
| Large-scale processing? | Yes — 120,000 contacts |
| Automated decision-making? | Yes — scoring is automated |
| Novel technology? | Partially — AI scoring within HubSpot |
| **DPIA Required?** | **YES** |

---

## 3. PII and Processing Details

| Field | Detail |
|-------|--------|
| **PII Involved** | Email, name, marketing preferences, web behaviour, loan application status, product history |
| **Legal Basis** | Legitimate Interests (for existing customers); Consent required for third-party data integration |
| **LIA Status** | Legitimate Interests Assessment completed — outcome: LI appropriate for existing customer scoring only |
| **Automated Decision?** | Scoring is automated; final product recommendation to customer is automated (no human review) |

---

## 4. Risks and Mitigations

| Risk | Score | Mitigation |
|------|-------|-----------|
| Customers profiled without knowledge | 12 (High) | Disclose profiling in privacy notice; add to ROPA; notify existing customers |
| Consent not obtained for third-party data enrichment | 9 (Medium) | Remove third-party data enrichment from scope — use first-party data only |
| Profiling produces biased recommendations (disadvantaging certain groups) | 6 (Medium) | Algorithm bias review by IT/Marketing; quarterly accuracy check; manual override capability |
| Right to object to profiling not honoured | 8 (Medium) | Implement self-service opt-out via preference centre; DSR procedure updated |
| HubSpot US transfer without updated SCCs | 12 (High) | Review HubSpot DPA and SCCs; verify EU data processing option in HubSpot settings |

---

## 5. Recommended Controls

1. Update privacy notice to disclose automated profiling and right to object
2. Implement preference centre with profiling opt-out option
3. Restrict scoring to first-party data only (no third-party enrichment)
4. Execute updated SCCs with HubSpot
5. Conduct algorithm bias review before launch
6. Add lead scoring to ROPA with LIA document attached
7. Quarterly review of scoring accuracy and fairness

---

## 6. DPO Conclusion

**Residual risk after mitigations:** All risks reduced to Low (≤5)

**Conclusion:** Proceed with implementation subject to controls 1–7 above being completed before launch.

**DPO Sign-Off:** Sarah Chen, DPO | **Date:** 2025-01-20  
**Prior ICO Consultation?** No — residual risks within acceptable threshold

---

*Worked example. NFS is a fictional organisation.*  
*ISO/IEC 27701:2025 PIMS Toolkit | NFS DPIA Entry — Lead Scoring | NFS-DPIA-2025-004*
