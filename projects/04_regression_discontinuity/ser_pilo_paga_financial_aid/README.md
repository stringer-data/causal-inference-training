# 04 — Regression Discontinuity: Ser Pilo Paga Financial Aid (Fuzzy RD)

## Method
Fuzzy Regression Discontinuity Design (RDD)

## Dataset
Colombia's Ser Pilo Paga (SPP) merit-based college financial aid program (Londoño-Vélez,
Rodríguez & Sánchez 2020), via Cattaneo, Idrobo & Titiunik's RD methods textbook
replication data.

## Dataset Links
- GitHub (rdpackages-replication): https://github.com/rdpackages-replication/CIT_2024_CUP
- Direct CSV: https://raw.githubusercontent.com/rdpackages-replication/CIT_2024_CUP/main/CIT_2024_CUP_fuzzy.csv
- See `data/raw/SOURCE_NOTE.md` for details and column definitions.

## Research Question
Does receiving merit-based financial aid (conditional on being poverty-eligible) cause
a student to immediately enroll in higher education?

## Identification Strategy
The forcing variable (`X1`) is a student's distance to Colombia's SISBEN poverty-index
eligibility cutoff. Crossing the cutoff (`T`) makes a student *eligible* for the
scholarship, but eligibility doesn't guarantee actual enrollment via the program (`D`):
some eligible students didn't take it up, and — confirmed directly in the data — no
ineligible student received it (one-sided noncompliance). This is a genuine **fuzzy**
RDD: `T` is an instrument for `D`, not `D` itself.

The estimator is a ratio of two jumps at the cutoff — a local Wald estimator,
structurally the same idea as an IV/2SLS ratio, with eligibility as the "instrument"
for actual treatment receipt:

```
τ = jump in E[Y | X1 = x] at x = 0
    ───────────────────────────────
    jump in E[D | X1 = x] at x = 0
```

## Assumptions
1. **Continuity** — potential enrollment outcomes are continuous in the running
   variable at the cutoff.
2. **First stage** — crossing the SISBEN cutoff meaningfully increases the probability
   of receiving the scholarship (this is the denominator of the estimator, so it can't
   be near zero — check this directly before trusting the ratio).
3. **No sorting** — households cannot precisely manipulate their SISBEN score to land
   just on the eligible side of the cutoff.
4. **Monotonicity** — no student is induced to *decline* the scholarship by becoming
   eligible (the fuzzy-RD analogue of the IV monotonicity/no-defiers assumption).

## Planned Outputs
- [ ] Density test: manipulation check on `X1`
- [ ] First-stage plot: `D` (treatment receipt) vs. `X1`, showing the jump in enrollment rate at the cutoff
- [ ] Reduced-form plot: `Y` (HEI enrollment) vs. `X1`, showing the jump in the outcome
- [ ] Fuzzy RD (Wald) estimate: reduced-form jump ÷ first-stage jump, with a standard error
- [ ] Covariate balance checks (`icfes_female`, `icfes_age`, `icfes_urm`, `icfes_stratum`, `icfes_famsize`) at the cutoff
- [ ] Sensitivity: varying bandwidth

## Suggested Python Packages
- `pandas` / `numpy` — binning, local sample construction
- `statsmodels` — OLS regression with treatment × running-variable interaction (first-stage and reduced-form)
- `matplotlib` — RD scatter plots
