# 10 — Staggered DiD: Marijuana Legalization

## Method
Staggered Difference-in-Differences (Callaway-Sant'Anna / Sun-Abraham)

## Dataset
State marijuana legalization dates (MPP) + BLS state unemployment rates

## Dataset Links
- Marijuana Policy Project (legalization dates): https://www.mpp.org/policy/state-by-state/
- BLS data portal: https://www.bls.gov/data/
- FRED state unemployment (URL pattern): `https://fred.stlouisfed.org/graph/fredgraph.csv?id=COUR`
- See `data/raw/SOURCE_NOTE.md` for construction instructions.

## Research Question
What are the dynamic effects of recreational marijuana legalization on state-level unemployment rates, labor force participation, or tax revenues? With states legalizing at different times over 2012–2023, how should we estimate treatment effects under staggered adoption?

## Identification Strategy
Classic two-way fixed effects (TWFE) DiD is biased under staggered treatment timing and heterogeneous treatment effects because later-treated units act as "controls" for earlier-treated units at wrong calendar times. Modern estimators address this:

**Callaway-Sant'Anna (2021):** Estimates group-time ATTs `ATT(g, t)` for each cohort `g` (year of legalization) at each time `t`, using "clean controls" (never-treated or not-yet-treated units). Aggregates into event-study or overall ATT.

**Sun-Abraham (2021):** Interacts treatment timing cohort dummies with event-time dummies to produce heterogeneity-robust event study coefficients within a regression framework.

```
ATT(g, t) = E[Y_t - Y_{g-1} | G = g] - E[Y_t - Y_{g-1} | C]
```

where `C` is a clean comparison group (never-treated).

## Assumptions
1. **Parallel trends (conditional)** — conditional on covariates, each cohort's outcomes would have evolved similarly to clean controls in the absence of legalization.
2. **No anticipation** — outcomes do not respond to future legalization dates.
3. **Overlap** — sufficient pre-treatment periods and clean control states for each cohort.
4. **No interference** — legalization in one state does not affect outcomes in never-treated states (may be violated for border states).

## Planned Outputs
- [ ] Compile legalization dates by state (medical vs. recreational)
- [ ] Merge with FRED/BLS unemployment panel
- [ ] Naive TWFE estimate (show the bias concern)
- [ ] Callaway-Sant'Anna ATT(g,t) estimation
- [ ] Sun-Abraham event study
- [ ] Event study plot: dynamic treatment effects relative to legalization year
- [ ] Cohort heterogeneity: do early vs. late legalizers differ?
- [ ] Robustness: never-treated-only controls vs. not-yet-treated controls

## Suggested Python Packages
- `linearmodels` — TWFE panel regression
- `pyfixest` — fast fixed effects with staggered DiD support
- `csdid` (if available) — Callaway-Sant'Anna Python port
- `pandas` — panel data construction
- `matplotlib` / `seaborn` — event study plots
