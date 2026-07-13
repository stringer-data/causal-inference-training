# 02 — Event Study: COVID Restrictions & Unemployment

## Method
Event Study (dynamic DiD / distributed lag model)

## Dataset
FRED state-level monthly unemployment rates + COVID policy dates

## Dataset Links
- FRED state unemployment series (URL pattern):
  `https://fred.stlouisfed.org/graph/fredgraph.csv?id=CAUR` (replace `CAUR` with state series ID)
- COVID policy dates: https://github.com/COVID19StatePolicy/SocialDistancing
- Oxford COVID-19 Government Response Tracker: https://www.bsg.ox.ac.uk/research/covid-19-government-response-tracker

## Research Question
How did state unemployment rates evolve around the onset of COVID-19 stay-at-home orders? Did states with earlier or stricter restrictions experience different unemployment trajectories?

## Identification Strategy
An event study plots the dynamic treatment effect at each time period relative to the event (policy implementation date). For each state, we define time-to-treatment as months relative to the first stay-at-home order. We estimate:

```
UR_st = α_s + λ_t + Σ_k β_k · D_st^k + ε_st
```

where `D_st^k` is an indicator for being k periods from the event. The `β_k` coefficients trace out the dynamic treatment path. Pre-event coefficients (`k < 0`) test the parallel-trends assumption.

## Assumptions
1. **Parallel trends (pre-treatment)** — states on similar unemployment trajectories before the policy.
2. **No anticipation** — unemployment does not respond to *future* restrictions (pre-event betas ≈ 0).
3. **Staggered adoption is handled** — use Callaway-Sant'Anna or Sun-Abraham aggregation to avoid bias from heterogeneous timing.
4. **No interference** — policy in one state does not cause unemployment in other states (may be violated for border states).

## Planned Outputs
- [ ] Download and merge FRED UR series with COVID policy dates
- [ ] Event-time alignment: assign relative-time indicators per state
- [ ] Event study plot: β_k coefficients ± 95% CI across event time
- [ ] Pre-trend test: joint F-test on pre-event betas
- [ ] Comparison: strict vs. lenient restriction states
- [ ] Aggregated ATT estimate

## Suggested Python Packages
- `pandas` — data wrangling and reshaping
- `statsmodels` — OLS with fixed effects
- `linearmodels` — panel models with two-way FE
- `matplotlib` / `seaborn` — event study plot
- `pandas_datareader` — optional FRED API access
