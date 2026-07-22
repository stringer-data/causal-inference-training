# Synthetic Control: Texas Prison Construction & Black Male Incarceration

## Method
Synthetic Control (as applied in Scott Cunningham's *Causal Inference: The Mixtape*, synthetic control chapter)

## Dataset
State-year panel of Black and white male prison populations, incarceration rates, and predictors (crack index, alcohol consumption, income, unemployment, poverty, demographics, parole/probation counts, prison capacity) for Texas and a donor pool of other U.S. states.

## Dataset Links
- Mixtape chapter: https://mixtape.scunning.com/09-synthetic_control
- Direct CSV mirror: https://raw.githubusercontent.com/sdfordham/pysyncon/main/data/texas.csv
- See `data/raw/SOURCE_NOTE.md` for manual download instructions.

## Research Question
Did Texas's large-scale prison construction program raise the Black male incarceration rate relative to a synthetic counterfactual Texas built from other states that did not undertake comparable prison expansion?

## Identification Strategy
Synthetic control constructs a weighted combination of donor states that best matches Texas's pre-treatment Black male incarceration trajectory and predictors. Post-treatment divergence estimates the effect of the prison construction program.

```
α_1t = Y_1t - Σ_j w_j* · Y_jt    (t > treatment onset)
```

Weights `w_j*` minimize pre-treatment mean squared prediction error. The known reference solution (per pysyncon's reproduction) weights the synthetic control as approximately 0.409 California + 0.108 Florida + 0.361 Illinois + 0.122 Louisiana — useful as a sanity check on the notebook's optimization.

## Assumptions
1. **Convex hull** — Texas's pre-treatment outcomes lie within the convex hull of the donor pool.
2. **No interference** — Texas's prison construction does not affect incarceration rates in donor states.
3. **No anticipation** — incarceration rates do not respond in advance of the construction program.
4. **Relevant donor pool** — control states are comparable and did not undertake similar prison expansions during the study period.

## Planned Outputs
- [ ] Data preparation: state-year panel of incarceration rates and predictors
- [ ] Synthetic control optimization (weights over donor pool)
- [ ] Plot: Texas vs. synthetic Texas Black male incarceration rate
- [ ] Gap plot: Texas minus synthetic Texas
- [ ] Placebo inference: in-space placebo test across donor states
- [ ] Cross-check optimized weights against the reference solution above

## Suggested Python Packages
- `pandas` — panel data wrangling
- `pysyncon` or `scipy.optimize` / `cvxpy` — synthetic control weight optimization
- `matplotlib` — synthetic control and gap plots
- `numpy` — matrix operations
