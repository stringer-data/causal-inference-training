# 06 — Propensity Score Matching: Job Training & Earnings

## Method
Propensity Score Matching (PSM) / Inverse Probability Weighting (IPW)

## Dataset
LaLonde (1986) / Dehejia & Wahba NSW Job Training Data

## Dataset Links
- NSW treated group: https://users.nber.org/~rdehejia/data/nswre74_treated.txt
- NSW control group: https://users.nber.org/~rdehejia/data/nswre74_control.txt
- PSID comparison group: https://users.nber.org/~rdehejia/data/psid_controls.txt
- CPS comparison group: https://users.nber.org/~rdehejia/data/cps_controls.txt
- Dehejia's data page: https://users.nber.org/~rdehejia/nswdata.html

## Research Question
Did participation in the National Supported Work (NSW) job training program increase post-program earnings? LaLonde (1986) showed that non-experimental estimators fail to replicate the experimental benchmark when observational comparison groups are used — PSM attempts to recover unbiased estimates.

## Identification Strategy
The NSW was a randomized experiment. We can use the experimental benchmark (NSW treated vs. NSW control) as the ground truth, then replicate the analysis using non-experimental controls (PSID or CPS) and PSM to see how close we can get.

**Propensity score:** `P(D_i = 1 | X_i) = Pr(treated | covariates)`, estimated via logistic regression.

**Matching:** match each treated unit to the nearest-neighbor control unit on the propensity score. The ATT is:

```
ATT = E[Y(1) - Y(0) | D = 1]  ≈  mean(Y_treated) - mean(Y_matched_controls)
```

## Assumptions
1. **Conditional independence (unconfoundedness)** — conditional on observed covariates, treatment is independent of potential outcomes: `(Y(0), Y(1)) ⊥ D | X`.
2. **Common support (overlap)** — every treated unit has a comparable control: `0 < P(D=1|X) < 1` for all X.
3. **Correct propensity model** — the logistic regression for the PS is correctly specified.
4. **SUTVA** — no spillovers between participants and non-participants.

## Planned Outputs
- [ ] Experimental benchmark: raw DiD from randomized NSW data
- [ ] Propensity score estimation (logistic regression)
- [ ] Common support check and overlap plot
- [ ] 1-to-1 nearest-neighbor matching
- [ ] Post-matching covariate balance (standardized mean differences)
- [ ] IPW estimator (augmented IPW / doubly robust)
- [ ] Comparison table: experimental vs. PSM vs. OLS vs. unmatched
- [ ] Sensitivity analysis: Rosenbaum bounds

## Suggested Python Packages
- `scikit-learn` — logistic regression for propensity scores
- `statsmodels` — OLS, balance tests
- `causalml` — matching and IPW utilities
- `pandas` — data wrangling
- `matplotlib` / `seaborn` — overlap plots, balance plots
