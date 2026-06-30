# 13 — Generalized Propensity Score: Education & Earnings

## Method
Generalized Propensity Score (GPS) — Hirano & Imbens (2004)

## Dataset
LaLonde (1986) / Dehejia & Wahba (1999) NSW experimental data  
Same source as project 06, different treatment variable.

## Research Question
What is the causal dose-response relationship between years of education
and 1978 earnings, after controlling for observed confounders?

Unlike binary PSM (treated vs. not), GPS estimates a **dose-response curve** —
how earnings change across the full range of educational attainment.

## Treatment and Outcome
| Variable | Description |
|---|---|
| `educ` | Treatment: years of education (continuous, ~4–16 years) |
| `re78` | Outcome: real earnings in 1978 (USD) |

## Key Covariates
| Variable | Description |
|---|---|
| `age` | Age in years |
| `black` | Race indicator (1 = Black) |
| `hisp` | Ethnicity indicator (1 = Hispanic) |
| `married` | Marital status (1 = married) |
| `nodegree` | No high school degree (1 = true) |
| `re74` | Real earnings in 1974 (pre-treatment) |
| `re75` | Real earnings in 1975 (pre-treatment) |

## How GPS Differs from Binary PSM

| | Binary PSM | Generalized PS (GPS) |
|---|---|---|
| Treatment | Binary (0/1) | Continuous |
| Treatment model | Logistic regression | OLS / Normal distribution |
| Propensity score | P(T=1 \| X) — probability | f(T \| X) — conditional density |
| Output | Single ATT | Dose-response curve |

## Identification Strategy
Education is not randomly assigned — older individuals, married individuals,
and those with higher prior earnings all have systematically different
educational attainment. GPS conditions on these confounders to estimate
the causal effect at each level of education.

## Assumptions
1. **Weak unconfoundedness** — conditional on X, potential outcomes are
   independent of treatment at every level: Y(t) ⊥ T | X for all t
2. **Common support** — every education level has overlapping covariate
   distributions across treated and control observations
3. **Correct treatment model** — the normal regression for education is
   correctly specified

## Planned Outputs
- [ ] EDA: education distribution and pre-adjustment balance
- [ ] GPS estimation (OLS, normal conditional density)
- [ ] Covariate balance check across education strata
- [ ] Dose-response function estimation
- [ ] Dose-response curve plot
