# Causal Inference Playground

A portfolio of causal inference methods applied to public datasets. Every dataset is downloadable from a direct URL or has a documented source page — no hidden package data.

Run `python scripts/download_data.py` to fetch all datasets before opening notebooks.

---

## Projects

| # | Project | Causal Method | Dataset | Research Question | Main Packages |
|---|---------|---------------|---------|-------------------|---------------|
| 1 | [Minimum Wage & Employment](projects/01_difference_in_differences_minimum_wage/) | Difference-in-Differences | Card & Krueger NJ/PA fast-food data | Did NJ's minimum wage increase reduce employment? | `statsmodels`, `linearmodels` |
| 2 | [COVID & Unemployment](projects/02_event_study_covid_unemployment/) | Event Study | FRED state unemployment rates | How did unemployment evolve around COVID restrictions? | `statsmodels`, `pandas_datareader` |
| 3 | [Prop 99 & Smoking](projects/03_synthetic_control_prop99_smoking/) | Synthetic Control | California Prop 99 smoking data | Did CA's anti-smoking policy reduce cigarette sales? | `scipy`, `cvxpy` |
| 4 | [Close Elections](projects/04_regression_discontinuity_close_elections/) | Regression Discontinuity | Close elections data (Harvard Dataverse) | Does barely winning an election change future outcomes? | `rdrobust`, `statsmodels` |
| 5 | [Returns to Education](projects/05_instrumental_variables_college_proximity/) | Instrumental Variables | Card college proximity / wages | What is the causal effect of education on wages? | `linearmodels`, `statsmodels` |
| 6 | [Job Training & Earnings](projects/06_propensity_score_matching_lalonde/) | Propensity Score Matching | LaLonde / NSW job training data | Did job training increase earnings? | `scikit-learn`, `causalml` |
| 7 | [Treatment Effects Under Confounding](projects/07_double_ml_acic/) | Double Machine Learning | ACIC challenge data | Can DML recover treatment effects under confounding? | `doubleml`, `econml` |
| 8 | [Email Marketing Uplift](projects/08_causal_forest_hillstrom_email/) | Causal Forest / Uplift | Hillstrom email marketing challenge | Which customers benefit most from marketing emails? | `econml`, `causalml` |
| 9 | [Geo Lift on Air Travel](projects/09_geo_experiment_air_travel/) | Geo Experiment | TSA passenger throughput | Can we simulate a geo lift experiment on travel demand? | `pandas`, `statsmodels` |
| 10 | [Marijuana Legalization Effects](projects/10_staggered_did_marijuana_policy/) | Staggered DiD | Marijuana legalization dates + BLS outcomes | What happens to labor outcomes after staggered policy adoption? | `linearmodels`, `pyfixest` |
| 11 | [German Reunification & GDP](projects/05_synthetic_control/german_reunification/) | Synthetic Control | OECD country panel (Abadie, Diamond & Hainmueller 2015) | Did German reunification depress West German GDP per capita? | `pysyncon`, `scipy` |
| 12 | [Basque Terrorism & GDP](projects/05_synthetic_control/basque_terrorism/) | Synthetic Control | Spanish region panel (Abadie & Gardeazabal 2003) | Did ETA terrorism reduce the Basque Country's GDP per capita? | `pysyncon`, `scipy` |
| 13 | [Texas Prison Construction & Incarceration](projects/05_synthetic_control/texas_prison_incarceration/) | Synthetic Control | State panel (Cunningham, *Causal Inference: The Mixtape*) | Did Texas's prison construction program raise Black male incarceration rates? | `pysyncon`, `scipy` |

---

## Setup

```bash
# 1. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Download all datasets
python scripts/download_data.py

# 4. Launch Jupyter
jupyter notebook
```

## Repository Structure

```
causal-inference-playground/
  README.md
  requirements.txt
  DATA_SOURCES.md          # all source URLs in one place
  scripts/
    download_data.py       # fetches / documents all datasets
  projects/
    01_*/
      README.md            # method, data, strategy, assumptions
      data/raw/            # raw downloaded files (gitignored except .gitkeep)
      notebooks/           # Jupyter analysis notebooks
      src/                 # helper Python modules
    ...
```

## Data Policy

All datasets are either:
- **Direct download** — the script fetches them automatically to `data/raw/`.
- **Manual download** — a `SOURCE_NOTE.md` in `data/raw/` explains exactly where to go and what to download.

No data files are bundled in this repo. See `DATA_SOURCES.md` for the full source list.

## Reading List

See [ARTICLES.md](ARTICLES.md) for a curated collection of industry/research articles on causal inference worth referring back to.

## Methods Covered

- Difference-in-Differences (DiD)
- Event Study
- Synthetic Control
- Regression Discontinuity Design (RDD)
- Instrumental Variables (IV / 2SLS)
- Propensity Score Matching (PSM)
- Double/Debiased Machine Learning (DML)
- Causal Forest / Heterogeneous Treatment Effects
- Geo Experiments
- Staggered DiD (Callaway-Sant'Anna, Sun-Abraham)
