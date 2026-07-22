# Synthetic Control: German Reunification & GDP per Capita

## Method
Synthetic Control (Abadie, Diamond & Hainmueller 2015 — "Comparative Politics and the Synthetic Control Method")

## Dataset
Panel of GDP per capita and economic predictors (inflation, trade openness, schooling, investment share, industry share) for West Germany and a donor pool of OECD countries, 1960–2003.

## Dataset Links
- Abadie, Diamond & Hainmueller replication page: https://web.stanford.edu/~jhain/synthpage.html
- Direct CSV mirror: https://raw.githubusercontent.com/sdfordham/pysyncon/main/data/germany.csv
- See `data/raw/SOURCE_NOTE.md` for manual download instructions.

## Research Question
Did German reunification in 1990 depress West Germany's GDP per capita relative to a synthetic counterfactual constructed from other OECD economies that were not reunified?

## Identification Strategy
Synthetic control constructs a weighted combination of donor countries (e.g. USA, Japan, Austria, Switzerland, Netherlands) that best reproduces West Germany's pre-1990 GDP trajectory and predictors. Post-1990 divergence between West Germany and its synthetic counterpart estimates the reunification effect.

```
α_1t = Y_1t - Σ_j w_j* · Y_jt    (t > 1990)
```

Weights `w_j*` minimize pre-treatment mean squared prediction error. Inference uses in-space placebo tests: rerun the procedure assigning "treatment" to each donor country in turn and compare West Germany's post-treatment gap to the placebo distribution.

## Assumptions
1. **Convex hull** — West Germany's pre-treatment outcomes lie within the convex hull of the donor pool.
2. **No interference** — reunification does not affect GDP in donor countries (SUTVA).
3. **No anticipation** — GDP does not respond in advance of 1990.
4. **Relevant donor pool** — control countries are comparable, non-reunified OECD economies.

## Planned Outputs
- [ ] Data preparation: country-year panel of GDP and predictors
- [ ] Synthetic control optimization (weights over donor pool)
- [ ] Plot: West Germany vs. synthetic West Germany GDP per capita, 1960–2003
- [ ] Gap plot: West Germany minus synthetic West Germany
- [ ] Placebo inference: in-space placebo test across donor countries
- [ ] Ratio plot: post/pre RMSPE for West Germany vs. placebos

## Suggested Python Packages
- `pandas` — panel data wrangling
- `pysyncon` or `scipy.optimize` / `cvxpy` — synthetic control weight optimization
- `matplotlib` — synthetic control and gap plots
- `numpy` — matrix operations
