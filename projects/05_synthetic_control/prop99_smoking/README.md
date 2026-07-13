# 03 — Synthetic Control: California Prop 99 & Cigarette Sales

## Method
Synthetic Control (Abadie, Diamond & Hainmueller 2010)

## Dataset
California Prop 99 cigarette consumption panel data

## Dataset Links
- Abadie, Diamond & Hainmueller replication page: https://web.stanford.edu/~jhain/synthpage.html
- R `Synth` package (ships the `smoking` dataset): https://cran.r-project.org/package=Synth
- See `data/raw/SOURCE_NOTE.md` for manual download instructions.

## Research Question
Did California's 1988 tobacco control program (Proposition 99) reduce per-capita cigarette sales relative to a synthetic counterfactual constructed from other U.S. states?

## Identification Strategy
Synthetic control constructs a weighted combination of control states (the "donor pool") that best matches California's pre-treatment cigarette sales trajectory and predictors. Post-treatment divergence between California and the synthetic California estimates the policy effect.

```
α_1t = Y_1t - Σ_j w_j* · Y_jt    (t > T_0)
```

Weights `w_j*` are chosen to minimize pre-treatment fit. Inference uses placebo tests: run the same procedure for each donor state and compare California's post-treatment gap to the distribution of placebo gaps.

## Assumptions
1. **Convex hull** — California's pre-treatment outcomes lie within the convex hull of the donor pool (no extrapolation).
2. **No interference** — Prop 99 does not affect cigarette sales in donor states.
3. **No anticipation** — cigarette sales do not respond before 1988.
4. **Relevant donor pool** — control states resemble California on pre-treatment predictors.

## Planned Outputs
- [ ] Data preparation: state-year panel of cigarette sales and predictors
- [ ] Synthetic control optimization (quadratic programming)
- [ ] Plot: California vs. synthetic California cigarette sales 1970–2000
- [ ] Gap plot: California minus synthetic California
- [ ] Placebo inference: in-space placebo test across donor states
- [ ] Ratio plot: post/pre RMSPE for California vs. placebos

## Suggested Python Packages
- `pandas` — panel data wrangling
- `scipy.optimize` / `cvxpy` — quadratic programming for weights
- `matplotlib` — synthetic control and gap plots
- `numpy` — matrix operations
