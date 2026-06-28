# 09 — Geo Experiment: Air Travel Demand

## Method
Geo Experiment / Simulated Geo Lift

## Dataset
TSA Transportation Security Administration passenger throughput data

## Dataset Link
- TSA passenger volumes page: https://www.tsa.gov/travel/passenger-volumes
  (Download the Excel file; see `data/raw/SOURCE_NOTE.md` for steps.)

## Research Question
Can we design and evaluate a simulated geo lift experiment on air travel demand? Which "geo units" (treated by an imaginary marketing intervention) show the most reliable causal lift estimates, and how sensitive are results to the choice of control group?

## Identification Strategy
Geo experiments partition geographic units (here: simulated regions based on day-of-week or month groups as "geos") into treatment and control. A pre-treatment period establishes a baseline relationship between geos; post-treatment divergence is attributed to the intervention.

This project simulates a geo experiment on the TSA data by:
1. Defining "geo units" from the time-series structure (e.g., treat 2021 Q1 as "treated region").
2. Using synthetic control or matched DiD across time-blocks to estimate lift.
3. Evaluating detection power and minimum detectable effect (MDE) under different designs.

```
Lift = (Treated_post / Predicted_treated_post_counterfactual) - 1
```

The counterfactual is estimated via synthetic control, prophet forecasting, or matched DMA analysis.

## Assumptions
1. **Pre-treatment stability** — control units track treatment units before the experiment.
2. **No geo spillovers** — the intervention in treated units doesn't affect control units.
3. **Correct counterfactual** — the pre-period model accurately predicts what would have happened without treatment.
4. **Sufficient pre-period** — enough history to fit a reliable synthetic control.

## Planned Outputs
- [ ] Download and clean TSA daily throughput data
- [ ] Exploratory seasonality analysis (day-of-week, holiday effects)
- [ ] Design simulation: assign pseudo-treatment and control periods
- [ ] Synthetic control counterfactual for treated period
- [ ] Geo lift estimate with confidence interval
- [ ] Power analysis: MDE as a function of experiment duration and number of geos
- [ ] Comparison: synthetic control vs. DiD vs. regression-based lift

## Suggested Python Packages
- `pandas` — time series wrangling
- `statsmodels` — seasonal decomposition, regression
- `scipy.optimize` — synthetic control weights
- `matplotlib` — time series and lift plots
- `prophet` (optional) — forecasting-based counterfactual
