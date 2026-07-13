# 11 — Propensity Score Matching: Smoking Cessation & Weight Gain

## Method
Propensity Score Matching (PSM) / Inverse Probability Weighting (IPW)

## Dataset
NHEFS — National Health and Nutrition Examination Survey Epidemiologic Follow-up Study  
Distributed via Hernán & Robins, *Causal Inference: What If?* (2020)

## Dataset Links
- Book website: https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/
- Rdatasets mirror: https://vincentarelbundock.github.io/Rdatasets/doc/causaldata/nhefs_complete.html

## Research Question
Does quitting smoking cause weight gain? Using observational data from NHEFS (1971–1982), we estimate the average treatment effect on the treated (ATT) of smoking cessation (`qsmk = 1`) on weight change (`wt82_71`, kg) using propensity score matching.

## Identification Strategy
Treatment (`qsmk`) is not randomly assigned — quitters differ systematically from non-quitters on age, baseline weight, smoking intensity, exercise habits, etc. PSM conditions on these observed confounders to construct a comparable control group.

**Propensity score:** `P(qsmk_i = 1 | X_i)`, estimated via logistic regression on pre-treatment covariates.

**Matching:** match each treated unit (quitter) to the nearest-neighbor control unit on the propensity score. The ATT is:

```
ATT = E[Y(1) - Y(0) | D = 1]  ≈  mean(wt82_71 | quitters) - mean(wt82_71 | matched non-quitters)
```

## Key Variables
| Variable | Description |
|---|---|
| `qsmk` | Treatment: quit smoking between 1971 and 1982 (1 = yes) |
| `wt82_71` | Outcome: weight change in kg (1982 − 1971) |
| `age` | Age in 1971 |
| `sex` | Sex (0 = male) |
| `race` | Race (0 = white) |
| `school` | Years of education |
| `smokeintensity` | Cigarettes per day in 1971 |
| `smokeyrs` | Years of smoking |
| `exercise` | Physical activity level |
| `active` | Activity level at work |
| `wt71` | Baseline weight in kg (1971) |

## Assumptions
1. **Conditional independence (unconfoundedness)** — conditional on observed covariates, treatment is independent of potential outcomes: `(Y(0), Y(1)) ⊥ D | X`.
2. **Common support (overlap)** — every treated unit has a comparable control: `0 < P(D=1|X) < 1` for all X.
3. **Correct propensity model** — the logistic regression for the PS is correctly specified.
4. **SUTVA** — no interference between individuals.

## Planned Outputs
- [ ] EDA: covariate distributions by treatment group (pre-matching imbalance)
- [ ] Propensity score estimation (logistic regression)
- [ ] Common support check and overlap plot
- [ ] 1-to-1 nearest-neighbor matching
- [ ] Post-matching covariate balance (standardized mean differences / love plot)
- [ ] ATT estimate with confidence intervals
- [ ] IPW / augmented IPW (doubly robust) estimator
- [ ] Sensitivity analysis: Rosenbaum bounds

## Suggested Python Packages
- `scikit-learn` — logistic regression for propensity scores
- `statsmodels` — OLS, balance tests
- `causalml` — matching and IPW utilities
- `pandas` / `numpy` — data wrangling
- `matplotlib` / `seaborn` — overlap plots, balance plots
