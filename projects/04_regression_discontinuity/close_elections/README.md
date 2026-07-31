# 04 — Regression Discontinuity: Close Elections

## Method
Sharp Regression Discontinuity Design (RDD)

## Dataset
U.S. Senate close elections data (Lee 2008 / Cattaneo, Idrobo & Titiunik)

## Dataset Links
- Harvard Dataverse (rdrobust replication): https://dataverse.harvard.edu/
- rdrobust package raw data (GitHub):
  https://raw.githubusercontent.com/rdpackages/rdrobust/main/Python/rdrobust_senate.csv
- See `data/raw/SOURCE_NOTE.md` for details.

## Research Question
Does barely winning a U.S. Senate election (just above 50% of the vote) cause a candidate or party to be more likely to win the *next* election — the incumbency advantage?

## Identification Strategy
The forcing variable is the Democrat vote share margin (vote share minus 50%). The threshold is zero: candidates above win; candidates below lose. Near the threshold, who wins is essentially random (close elections are quasi-experiments). We estimate:

```
E[Y_i | X_i = x] = α + τ · D_i + f(x) + ε_i
```

where `D_i = 1[X_i ≥ 0]` is the indicator for winning, `f(x)` is a flexible polynomial or local linear fit on each side, and `τ` is the RD treatment effect at the cutoff.

Bandwidth selection follows Imbens-Kalyanaraman or Calonico-Cattaneo-Titiunik (CCT) optimal bandwidth.

## Assumptions
1. **Continuity** — potential outcomes are continuous at the threshold (no manipulation of the forcing variable).
2. **Local randomization** — units just above and just below the cutoff are comparable.
3. **Correct functional form** — the polynomial/local linear model correctly captures the conditional expectation away from the cutoff.
4. **No sorting** — candidates cannot precisely control their vote share to land just above 50%.

## Planned Outputs
- [x] Density test: manipulation check at the cutoff
- [x] RD plot: binned scatter + local linear fit on each side of threshold
- [x] Bandwidth choice, checked for stability across a range of values
- [x] Local linear RD estimate with confidence intervals
- [x] Covariate balance check at the cutoff
- [x] Sensitivity: varying bandwidth

See `notebooks/01_rdd_close_elections.ipynb`. Built from scratch with `pandas` /
`statsmodels` / `numpy` rather than `rdrobust`/`rddensity`, so every step (binning,
bandwidth, local regression) is visible in the notebook instead of hidden in a package
call. Headline result: barely winning a Senate election raises a party's vote share in
the next election for that seat by ~7pp (95% CI excludes 0), stable across bandwidths
5–50, consistent with Lee (2008). No evidence of manipulation at the cutoff and no
imbalance in state population, a predetermined covariate.

Not yet done: polynomial-order sensitivity (only linear fits tried) and an automatic
optimal-bandwidth formula (CCT/IK) — bandwidth here was chosen manually and checked for
stability instead.

## Suggested Python Packages
- `pandas` / `numpy` — binning, local sample construction
- `statsmodels` — OLS regression with treatment × running-variable interaction
- `scipy.stats` — binomial test for the manipulation check
- `matplotlib` — RD scatter and sensitivity plots
