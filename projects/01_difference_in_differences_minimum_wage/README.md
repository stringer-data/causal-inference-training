# 01 — Difference-in-Differences: Minimum Wage & Employment

## Method
Difference-in-Differences (DiD)

## Dataset
Card & Krueger (1994) NJ/PA fast-food survey data

## Dataset Link
- Direct download: http://davidcard.berkeley.edu/data_sets/njmin.zip
- Codebook: http://davidcard.berkeley.edu/data_sets/njmin3.zip

## Research Question
Did New Jersey's April 1992 minimum wage increase (from $4.25 to $5.05/hr) reduce fast-food employment relative to neighboring Pennsylvania, which had no change?

## Identification Strategy
New Jersey raised its minimum wage in April 1992; Pennsylvania did not. Card & Krueger surveyed fast-food restaurants in both states before (February 1992) and after (November 1992) the policy change. The treated group is NJ restaurants; the control group is PA restaurants. The DiD estimator is:

```
ATT = (NJ_post - NJ_pre) - (PA_post - PA_pre)
```

The key parallel-trends assumption: absent the NJ wage increase, employment trends in NJ and PA would have been the same.

## Assumptions
1. **Parallel trends** — NJ and PA fast-food employment would have evolved similarly without the policy change.
2. **No spillovers** — PA restaurants are not affected by the NJ wage change (SUTVA).
3. **Stable composition** — the set of surveyed restaurants does not change systematically between waves.
4. **No anticipation** — NJ employers did not begin adjusting employment before April 1992.

## Planned Outputs
- [ ] Exploratory data analysis: employment distributions by state and wave
- [ ] Basic 2x2 DiD table (means by state × period)
- [ ] OLS regression DiD with and without controls
- [ ] Parallel-trends pre-test (if pre-period data is available)
- [ ] Visualization: employment levels by state before and after
- [ ] Robustness: alternative control groups, placebo tests

## Suggested Python Packages
- `pandas` — data wrangling
- `statsmodels` — OLS regression
- `linearmodels` — panel DiD with fixed effects
- `matplotlib` / `seaborn` — visualization
