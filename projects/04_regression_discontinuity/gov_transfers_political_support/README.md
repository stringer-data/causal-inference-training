# 04 — Regression Discontinuity: Government Transfers & Political Support

## Method
Sharp Regression Discontinuity Design (RDD)

**Note:** this was originally scoped as a fuzzy RDD (the source paper has imperfect
compliance in the underlying survey). The `causaldata` package's bundled extract used
here turns out to have perfect compliance — `Participation` is exactly determined by
which side of the income cutoff a household falls on (verified directly: crosstabbing
`income_centered < 0` against `participation` shows zero off-diagonal cells). With the
first-stage jump equal to 1, the fuzzy Wald ratio collapses to the reduced-form jump
itself, so this is analyzed as a sharp design.

## Dataset
Uruguay PANES anti-poverty transfer program, household survey data (Manacorda, Miguel &
Vigorito 2011)

## Dataset Links
- `causaldata` Python package (`pip install causaldata`) — see `data/raw/SOURCE_NOTE.md`
  for exact regeneration steps.

## Research Question
Does receiving a means-tested government cash transfer cause recipients to become more
politically supportive of the government that provided it?

## Identification Strategy
The forcing variable is household income, centered on the program's eligibility cutoff
(`Income_Centered < 0` means eligible). Since eligibility perfectly determines
participation in this data, treatment status (`participation`) and the threshold
indicator (`threshold = 1[Income_Centered >= 0]`) are the same variable — `participation`
carries no information beyond what `threshold` already captures. We estimate the
standard sharp-RD local linear model, controlling for the running variable directly:

```
E[Support_i | Income_Centered_i = x] = α + τ · 1[x >= 0] + f(x) + ε_i
```

where `f(x)` is a linear (or higher-order) fit in `income_centered`, allowed to differ
on each side of the cutoff via an interaction term, and `τ` is the RD treatment effect.

## Assumptions
1. **Continuity** — potential support outcomes are continuous in income at the cutoff.
2. **No sorting** — households cannot precisely manipulate reported income to land just
   under the eligibility threshold.
3. **Correct functional form** — the linear (or polynomial) fit correctly captures the
   conditional expectation of support away from the cutoff.

## Planned Outputs
- [ ] Density test: manipulation check on `Income_Centered`, run on `gov_transfers_density.csv`
  (the wider file), not the pre-limited `gov_transfers.csv` analysis sample
- [ ] RD plot: political support vs. income, showing the jump at the cutoff
- [ ] Local linear RD estimate with confidence intervals, controlling for the running variable
- [ ] Covariate balance checks (`education`, `age`) at the cutoff
- [ ] Sensitivity: varying bandwidth

## Suggested Python Packages
- `pandas` / `numpy` — binning, local sample construction
- `statsmodels` — OLS regression with treatment × running-variable interaction
- `matplotlib` — RD scatter plots
