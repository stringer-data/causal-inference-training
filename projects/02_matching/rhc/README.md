# 12 — Propensity Score Matching: Right Heart Catheterization

## Method
Propensity Score Matching (PSM)

## Dataset
Right Heart Catheterization (RHC) study — Connors et al. (1996)  
*The effectiveness of right heart catheterization in the initial care of critically ill patients*  
JAMA 276:889–897

## Dataset Links
- Data repository: https://hbiostat.org/data/repo/rhc.html

## Research Question
Does right heart catheterization (insertion of a Swan-Ganz catheter) on day 1 of ICU admission
affect 30-day survival in critically ill patients?

The original Connors et al. study found that RHC was associated with **increased mortality** —
a shocking result that challenged the clinical consensus and prompted widespread reconsideration
of the procedure. PSM is used to control for the fact that sicker patients were more likely to
receive RHC, which would otherwise bias a naive comparison.

## Treatment and Outcome
| Variable | Description |
|---|---|
| `swang1` | Treatment: received RHC on day 1 (Yes/No) |
| `death` | Outcome: died within 30 days of admission (Yes/No) |

## Key Covariates (72 total)
Demographics, vital signs, lab values, comorbidities, and disease severity scores — all
measured at baseline (day 1) before treatment assignment.

## Identification Strategy
RHC was not randomly assigned — physicians chose to use it based on clinical judgment, meaning
sicker patients were more likely to receive it. PSM conditions on observed severity indicators
to construct a comparable control group of patients who were equally sick but did not receive RHC.

## Assumptions
1. **Unconfoundedness** — conditional on observed baseline characteristics, RHC assignment is
   independent of potential outcomes
2. **Common support** — for every RHC patient, there exists a comparable non-RHC patient
3. **SUTVA** — one patient's treatment does not affect another's outcome

## Planned Outputs
- [ ] EDA: covariate distributions and pre-matching SMDs
- [ ] Propensity score model (logistic regression)
- [ ] Common support check
- [ ] 1-to-1 nearest-neighbour matching without replacement
- [ ] Post-matching balance (love plot)
- [ ] ATT estimate with 95% CI and p-value
- [ ] Comparison: naive vs. PSM estimate

## Suggested Python Packages
- `statsmodels` — logistic regression for propensity scores
- `sklearn` — NearestNeighbors for matching
- `pandas` / `numpy` — data wrangling
- `matplotlib` / `seaborn` — balance plots
