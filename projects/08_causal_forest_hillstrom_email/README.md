# 08 — Causal Forest / Uplift: Hillstrom Email Marketing

## Method
Causal Forest / Heterogeneous Treatment Effects (HTE) / Uplift Modeling

## Dataset
Kevin Hillstrom MineThatData Email Analytics Challenge (2008)

## Dataset Link
- Direct CSV download:
  http://www.minethatdata.com/Kevin_Hillstrom_MineThatData_E-MailAnalytics_DataMiningChallenge_2008.03.20.csv

## Research Question
Which customers benefit most from receiving a marketing email? Rather than estimating a single average treatment effect, causal forest estimates the conditional average treatment effect (CATE) for each customer: `τ(x) = E[Y(1) - Y(0) | X = x]`.

## Identification Strategy
The Hillstrom dataset is a randomized experiment: customers were randomly assigned to receive a men's email, a women's email, or no email. Randomization enables unbiased CATE estimation.

Causal forest (Wager & Athey 2018) is a non-parametric forest-based method that:
1. Builds honest random forests (uses separate subsamples for splitting and estimation).
2. Estimates a local regression at each leaf to produce a per-observation CATE.
3. Provides asymptotically normal, valid confidence intervals via the infinitesimal jackknife.

```
τ̂(x) = causal_forest(X, Y, W).predict(x)
```

## Assumptions
1. **Overlap (randomization)** — experiment ensures `P(W=1|X) = 0.5` approximately.
2. **Unconfoundedness** — randomization ensures no unmeasured confounders.
3. **Honesty** — causal forest splits on one subsample and estimates on another to prevent overfitting.
4. **SUTVA** — one customer's email assignment doesn't affect another's outcomes.

## Planned Outputs
- [ ] EDA: distribution of outcomes by treatment arm
- [ ] ATE estimate (overall average treatment effect)
- [ ] Causal forest CATE estimation (`econml.CausalForestDML`)
- [ ] CATE distribution plot: histogram of individual treatment effects
- [ ] Feature importance: which covariates predict treatment effect heterogeneity?
- [ ] Targeting policy: rank customers by estimated uplift, plot Qini curve
- [ ] Best linear predictor test for HTE significance
- [ ] Comparison: men's email vs. women's email treatment arms

## Suggested Python Packages
- `econml` — `CausalForestDML`, `LinearDML`
- `causalml` — uplift tree, Qini curve, AUUC
- `scikit-learn` — preprocessing, cross-validation
- `pandas` — data wrangling
- `matplotlib` / `seaborn` — CATE plots, Qini curve
