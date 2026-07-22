# Synthetic Control: Basque Terrorism & GDP per Capita

## Method
Synthetic Control (Abadie & Gardeazabal 2003 — "The Economic Costs of Conflict: A Case Study of the Basque Country")

## Dataset
Panel of GDP per capita and economic predictors (sector shares, schooling, population density, investment) for the Basque Country and a donor pool of other Spanish regions, 1955–1997.

## Dataset Links
- Abadie, Diamond & Hainmueller replication page: https://web.stanford.edu/~jhain/synthpage.html
- Direct CSV mirror: https://raw.githubusercontent.com/sdfordham/pysyncon/main/data/basque.csv
- R `Synth` package (ships the `basque` dataset): https://cran.r-project.org/package=Synth
- See `data/raw/SOURCE_NOTE.md` for manual download instructions.

## Research Question
Did the onset of ETA terrorist activity in the late 1960s/1970s reduce the Basque Country's GDP per capita relative to a synthetic counterfactual constructed from other Spanish regions unaffected by terrorism?

## Identification Strategy
Synthetic control constructs a weighted combination of donor regions (other Spanish autonomous communities, excluding regions with their own conflict-related confounders like Madrid or Catalonia if warranted) that best matches the Basque Country's pre-terrorism GDP trajectory and predictors. Post-treatment divergence estimates the economic cost of conflict.

```
α_1t = Y_1t - Σ_j w_j* · Y_jt    (t > treatment onset)
```

Weights `w_j*` minimize pre-treatment mean squared prediction error. Inference uses in-space placebo tests across donor regions, following Abadie & Gardeazabal's original ratio-of-RMSPE approach.

## Assumptions
1. **Convex hull** — the Basque Country's pre-treatment outcomes lie within the convex hull of the donor pool.
2. **No interference** — terrorism in the Basque Country does not spill over into donor regions' GDP.
3. **No anticipation** — GDP does not respond in advance of the terrorism onset.
4. **Relevant donor pool** — control regions are comparable Spanish regions without their own idiosyncratic shocks.

## Planned Outputs
- [ ] Data preparation: region-year panel of GDP and predictors
- [ ] Synthetic control optimization (weights over donor pool)
- [ ] Plot: Basque Country vs. synthetic Basque Country GDP per capita, 1955–1997
- [ ] Gap plot: Basque Country minus synthetic Basque Country
- [ ] Placebo inference: in-space placebo test across donor regions
- [ ] Ratio plot: post/pre RMSPE for Basque Country vs. placebos

## Suggested Python Packages
- `pandas` — panel data wrangling
- `pysyncon` or `scipy.optimize` / `cvxpy` — synthetic control weight optimization
- `matplotlib` — synthetic control and gap plots
- `numpy` — matrix operations
