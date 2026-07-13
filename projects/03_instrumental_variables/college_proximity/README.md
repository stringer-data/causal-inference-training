# 05 — Instrumental Variables: Returns to Education

## Method
Instrumental Variables (IV) / Two-Stage Least Squares (2SLS)

## Dataset
Card (1995) college proximity and wages data

## Dataset Links
- NBER data page: https://www.nber.org/research/data
- R `wooldridge` package: `data(card)` — direct export to CSV
- R `AER` package: `data(CollegeDistance)`
- See `data/raw/SOURCE_NOTE.md` for export instructions.

## Research Question
What is the causal effect of an additional year of education on wages? OLS is biased upward because high-ability individuals both get more education and earn higher wages (ability is unobserved). Card (1995) uses proximity to a four-year college as an instrument.

## Identification Strategy
Two-stage least squares (2SLS) uses college proximity as an instrument for years of schooling:

**First stage:** `Education_i = π_0 + π_1 · NearCollege_i + X_i'γ + u_i`

**Second stage:** `log(Wage_i) = β_0 + β_1 · Education_i_hat + X_i'δ + ε_i`

The instrument `NearCollege_i` affects wages *only through* its effect on education (exclusion restriction).

## Assumptions
1. **Relevance** — college proximity significantly predicts years of schooling (testable: F-stat > 10 in first stage).
2. **Exclusion restriction** — proximity to college affects wages only through the education channel, not directly (e.g., not through local labor market effects).
3. **Monotonicity** — proximity either increases or has no effect on each individual's education (no defiers).
4. **Independence** — proximity is as-good-as-random conditional on controls (family background, location selection concern).

## Planned Outputs
- [ ] OLS wage regression (naive, biased)
- [ ] First-stage regression: proximity → education (F-statistic, relevance test)
- [ ] 2SLS via `linearmodels.IV2SLS`
- [ ] Hausman test: OLS vs. IV (endogeneity test)
- [ ] Weak instrument diagnostics (Kleibergen-Paap, Cragg-Donald)
- [ ] Interpretation: LATE vs. ATE distinction

## Suggested Python Packages
- `linearmodels` — `IV2SLS`, `IVLIML`, `IVGMM`
- `statsmodels` — OLS baseline
- `pandas` — data wrangling
- `matplotlib` — first-stage and wage distribution plots
