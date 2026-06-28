# 04 — Regression Discontinuity: Close Elections

## Method
Sharp Regression Discontinuity Design (RDD)

## Dataset
U.S. Senate close elections data (Lee 2008 / Cattaneo, Idrobo & Titiunik)

## Dataset Links
- Harvard Dataverse (rdrobust replication): https://dataverse.harvard.edu/
- rdrobust package raw data (GitHub):
  https://raw.githubusercontent.com/rdpackages/rdrobust/master/R/rdrobust/data-raw/senate.csv
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
- [ ] Density test: McCrary test / `rddensity` to check for manipulation
- [ ] RD plot: scatter + local polynomial fit on each side of threshold
- [ ] Optimal bandwidth selection (CCT)
- [ ] Local linear RD estimate with robust confidence intervals
- [ ] Covariate balance checks at the cutoff
- [ ] Sensitivity: varying bandwidth, polynomial order, kernel

## Suggested Python Packages
- `rdrobust` — RD estimation, bandwidth selection, plots
- `rddensity` — manipulation test
- `statsmodels` — OLS polynomial regression
- `matplotlib` — RD scatter plots
