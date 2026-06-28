"""
Download all datasets for causal-inference-playground.

Direct-download sources are fetched automatically.
Source-page-only datasets get a SOURCE_NOTE.md explaining manual steps.

Usage:
    python scripts/download_data.py
"""

import logging
import zipfile
from io import BytesIO
from pathlib import Path

import requests

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)

REPO_ROOT = Path(__file__).resolve().parent.parent
PROJECTS = REPO_ROOT / "projects"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def raw_dir(project: str) -> Path:
    path = PROJECTS / project / "data" / "raw"
    path.mkdir(parents=True, exist_ok=True)
    return path


def download(url: str, dest: Path, description: str = "") -> bool:
    """Download url to dest. Returns True on success."""
    label = description or dest.name
    if dest.exists():
        log.info("  already exists — skipping: %s", dest.name)
        return True
    log.info("  downloading %s ...", label)
    try:
        resp = requests.get(url, timeout=60, stream=True)
        resp.raise_for_status()
        dest.write_bytes(resp.content)
        log.info("  saved %d KB -> %s", len(resp.content) // 1024, dest)
        return True
    except Exception as exc:
        log.warning("  FAILED %s: %s", label, exc)
        return False


def download_zip(url: str, dest_dir: Path, description: str = "") -> bool:
    """Download a zip from url and extract into dest_dir."""
    label = description or url
    log.info("  downloading zip %s ...", label)
    try:
        resp = requests.get(url, timeout=120)
        resp.raise_for_status()
        with zipfile.ZipFile(BytesIO(resp.content)) as zf:
            zf.extractall(dest_dir)
        log.info("  extracted %d files -> %s", len(zf.namelist()), dest_dir)
        return True
    except Exception as exc:
        log.warning("  FAILED zip %s: %s", label, exc)
        return False


def write_source_note(dest_dir: Path, title: str, source_url: str, instructions: str) -> None:
    note = dest_dir / "SOURCE_NOTE.md"
    note.write_text(
        f"# {title}\n\n"
        f"**Source page:** {source_url}\n\n"
        f"## Manual download steps\n\n{instructions}\n"
    )
    log.info("  wrote SOURCE_NOTE.md -> %s", note)


# ---------------------------------------------------------------------------
# Project 01 — DiD: Card & Krueger NJ/PA minimum wage
# ---------------------------------------------------------------------------

def project_01():
    log.info("[01] Difference-in-Differences — Card & Krueger minimum wage")
    dest = raw_dir("01_difference_in_differences_minimum_wage")

    # Direct zip from David Card's Berkeley page
    url = "http://davidcard.berkeley.edu/data_sets/njmin.zip"
    success = download_zip(url, dest, "njmin.zip")
    if not success:
        # Fallback: write a source note
        write_source_note(
            dest,
            title="Card & Krueger NJ/PA Minimum Wage Data",
            source_url="http://davidcard.berkeley.edu/data_sets.html",
            instructions=(
                "1. Visit http://davidcard.berkeley.edu/data_sets.html\n"
                "2. Download `njmin.zip`\n"
                "3. Extract contents into this directory (`data/raw/`).\n\n"
                "Key files:\n"
                "- `njmin.dat` — main survey data\n"
                "- `codebook` — variable descriptions\n"
            ),
        )


# ---------------------------------------------------------------------------
# Project 02 — Event Study: FRED state unemployment + COVID dates
# ---------------------------------------------------------------------------

def project_02():
    log.info("[02] Event Study — FRED state unemployment rates")
    dest = raw_dir("02_event_study_covid_unemployment")

    # Download a selection of representative state UR series from FRED
    # Format: https://fred.stlouisfed.org/graph/fredgraph.csv?id=<SERIES>
    states = {
        "CA": "CAUR",
        "NY": "NYUR",
        "TX": "TXUR",
        "FL": "FLUR",
        "IL": "ILUR",
        "WA": "WAUR",
    }
    fred_base = "https://fred.stlouisfed.org/graph/fredgraph.csv?id="
    for abbr, series_id in states.items():
        download(
            url=f"{fred_base}{series_id}",
            dest=dest / f"{series_id}.csv",
            description=f"FRED {abbr} unemployment rate ({series_id})",
        )

    # COVID policy dates — note for manual compilation
    write_source_note(
        dest,
        title="COVID Policy Dates",
        source_url="https://github.com/COVID19StatePolicy/SocialDistancing",
        instructions=(
            "Download the CSV of state-level COVID social distancing policies:\n\n"
            "1. Visit https://github.com/COVID19StatePolicy/SocialDistancing\n"
            "2. Download `USstatesCov19distancingpolicy.csv` and place it here.\n\n"
            "Alternatively, the Oxford COVID-19 Government Response Tracker provides\n"
            "comparable data: https://www.bsg.ox.ac.uk/research/covid-19-government-response-tracker\n"
        ),
    )


# ---------------------------------------------------------------------------
# Project 03 — Synthetic Control: Prop 99 smoking
# ---------------------------------------------------------------------------

def project_03():
    log.info("[03] Synthetic Control — California Prop 99 smoking")
    dest = raw_dir("03_synthetic_control_prop99_smoking")

    # Jens Hainmueller's synth page hosts the data; no direct CSV link is stable.
    # The dataset also ships with the R `Synth` package; we document both.
    write_source_note(
        dest,
        title="California Prop 99 Smoking Data",
        source_url="https://web.stanford.edu/~jhain/synthpage.html",
        instructions=(
            "Option A — R package export:\n"
            "  In R: `library(Synth); data(basque); write.csv(basque, 'basque.csv')`\n"
            "  The California Prop 99 data is in the `smoking` dataset:\n"
            "  `data(smoking); write.csv(smoking, 'smoking.csv')`\n\n"
            "Option B — Abadie, Diamond & Hainmueller replication files:\n"
            "  1. Visit https://web.stanford.edu/~jhain/synthpage.html\n"
            "  2. Download 'Replication files for California' zip.\n"
            "  3. Extract `smoking.csv` (or the Stata .dta) into this directory.\n\n"
            "Option C — Direct CSV from community mirrors:\n"
            "  https://raw.githubusercontent.com/jeremyxu212/synthetic-control/main/smoking.csv\n"
            "  (verify the data matches the original before using)\n"
        ),
    )


# ---------------------------------------------------------------------------
# Project 04 — RDD: Close elections
# ---------------------------------------------------------------------------

def project_04():
    log.info("[04] Regression Discontinuity — Close elections")
    dest = raw_dir("04_regression_discontinuity_close_elections")

    write_source_note(
        dest,
        title="Close Elections Data (Lee 2008 / Cattaneo et al.)",
        source_url="https://dataverse.harvard.edu/",
        instructions=(
            "The standard close-elections RDD dataset is from Lee (2008).\n\n"
            "Option A — Cattaneo, Idrobo & Titiunik replication data:\n"
            "  1. Visit https://dataverse.harvard.edu/\n"
            "  2. Search for 'rdrobust' or 'Cattaneo Titiunik close elections'\n"
            "  3. Download `senate.csv` or `house.csv` from the replication archive.\n\n"
            "Option B — rdrobust package built-in data (Python):\n"
            "  `from rdrobust import rdbwselect`  — the package ships `rdrobust_senate` data.\n"
            "  `import rdrobust; help(rdrobust)` to find the bundled datasets.\n\n"
            "Option C — Direct CSV:\n"
            "  https://raw.githubusercontent.com/rdpackages/rdrobust/master/R/rdrobust/data-raw/senate.csv\n"
        ),
    )

    # Attempt the direct GitHub raw CSV
    senate_url = (
        "https://raw.githubusercontent.com/rdpackages/rdrobust/master/R/rdrobust/data-raw/senate.csv"
    )
    download(senate_url, dest / "senate.csv", "rdrobust senate close elections CSV")


# ---------------------------------------------------------------------------
# Project 05 — IV: Card college proximity / returns to education
# ---------------------------------------------------------------------------

def project_05():
    log.info("[05] Instrumental Variables — Card college proximity")
    dest = raw_dir("05_instrumental_variables_college_proximity")

    write_source_note(
        dest,
        title="Card (1995) College Proximity / Returns to Education",
        source_url="https://www.nber.org/research/data",
        instructions=(
            "The Card (1995) college-proximity IV dataset ships with several R packages\n"
            "and is available via NBER.\n\n"
            "Option A — `wooldridge` R package:\n"
            "  `library(wooldridge); data(card); write.csv(card, 'card.csv')`\n\n"
            "Option B — `AER` R package:\n"
            "  `library(AER); data(CollegeDistance); write.csv(CollegeDistance, 'CollegeDistance.csv')`\n\n"
            "Option C — statsmodels Python (partial data):\n"
            "  `import statsmodels.api as sm; sm.datasets.engel.load_pandas()`\n"
            "  (use the Card data from wooldridge via rpy2 or export from R)\n\n"
            "Once downloaded, place the CSV here as `card.csv`.\n"
        ),
    )


# ---------------------------------------------------------------------------
# Project 06 — PSM: LaLonde NSW job training
# ---------------------------------------------------------------------------

def project_06():
    log.info("[06] Propensity Score Matching — LaLonde NSW job training")
    dest = raw_dir("06_propensity_score_matching_lalonde")

    files = {
        "nswre74_treated.txt": "https://users.nber.org/~rdehejia/data/nswre74_treated.txt",
        "nswre74_control.txt": "https://users.nber.org/~rdehejia/data/nswre74_control.txt",
        "psid_controls.txt":   "https://users.nber.org/~rdehejia/data/psid_controls.txt",
        "cps_controls.txt":    "https://users.nber.org/~rdehejia/data/cps_controls.txt",
    }
    for filename, url in files.items():
        download(url, dest / filename, filename)


# ---------------------------------------------------------------------------
# Project 07 — Double ML: ACIC challenge
# ---------------------------------------------------------------------------

def project_07():
    log.info("[07] Double Machine Learning — ACIC challenge data")
    dest = raw_dir("07_double_ml_acic")

    write_source_note(
        dest,
        title="ACIC Data Challenge",
        source_url="https://aciccomp.org/",
        instructions=(
            "The ACIC (Atlantic Causal Inference Conference) data challenges provide\n"
            "semi-synthetic benchmark datasets for causal inference.\n\n"
            "Option A — ACIC 2016 challenge data:\n"
            "  1. Visit https://aciccomp.org/2016-software-challenge/\n"
            "  2. Register (free) and download the data files.\n\n"
            "Option B — IBM causal inference benchmarking framework:\n"
            "  pip install causallib\n"
            "  from causallib.datasets import load_acic16\n"
            "  data = load_acic16(); data.to_csv('acic2016.csv')\n\n"
            "Option C — IHDP semi-synthetic data (commonly used substitute):\n"
            "  https://www.fredjo.com/files/ihdp_npci_1-100.train.npz\n"
            "  https://www.fredjo.com/files/ihdp_npci_1-100.test.npz\n\n"
            "Place downloaded files in this directory.\n"
        ),
    )

    # Attempt IHDP as a concrete downloadable alternative
    ihdp_train = "https://www.fredjo.com/files/ihdp_npci_1-100.train.npz"
    ihdp_test  = "https://www.fredjo.com/files/ihdp_npci_1-100.test.npz"
    download(ihdp_train, dest / "ihdp_npci_1-100.train.npz", "IHDP train (npz)")
    download(ihdp_test,  dest / "ihdp_npci_1-100.test.npz",  "IHDP test (npz)")


# ---------------------------------------------------------------------------
# Project 08 — Causal Forest: Hillstrom email marketing
# ---------------------------------------------------------------------------

def project_08():
    log.info("[08] Causal Forest — Hillstrom email marketing")
    dest = raw_dir("08_causal_forest_hillstrom_email")

    url = (
        "http://www.minethatdata.com/Kevin_Hillstrom_MineThatData_E-MailAnalytics_"
        "DataMiningChallenge_2008.03.20.csv"
    )
    download(url, dest / "hillstrom_email.csv", "Hillstrom email marketing CSV")


# ---------------------------------------------------------------------------
# Project 09 — Geo Experiment: TSA passenger throughput
# ---------------------------------------------------------------------------

def project_09():
    log.info("[09] Geo Experiment — TSA passenger throughput")
    dest = raw_dir("09_geo_experiment_air_travel")

    write_source_note(
        dest,
        title="TSA Passenger Throughput Data",
        source_url="https://www.tsa.gov/travel/passenger-volumes",
        instructions=(
            "TSA publishes daily passenger throughput numbers as an Excel file.\n\n"
            "1. Visit https://www.tsa.gov/travel/passenger-volumes\n"
            "2. Click the Excel download link on the page.\n"
            "3. Save the file as `tsa_passenger_throughput.xlsx` in this directory.\n\n"
            "The file contains daily totals and year-over-year comparisons going back to 2019.\n"
            "It is suitable for simulating a geo-lift experiment (treat some days/periods\n"
            "as 'treated regions' and estimate lift via synthetic control or DiD).\n"
        ),
    )


# ---------------------------------------------------------------------------
# Project 10 — Staggered DiD: Marijuana legalization + BLS
# ---------------------------------------------------------------------------

def project_10():
    log.info("[10] Staggered DiD — Marijuana legalization + BLS outcomes")
    dest = raw_dir("10_staggered_did_marijuana_policy")

    write_source_note(
        dest,
        title="Marijuana Legalization Dates & BLS Labor Outcomes",
        source_url="https://www.mpp.org/policy/state-by-state/",
        instructions=(
            "## Part 1 — Marijuana legalization dates\n\n"
            "Curated date tables:\n"
            "  - https://www.mpp.org/policy/state-by-state/  (Marijuana Policy Project)\n"
            "  - https://disa.com/marijuana-legality-by-state  (DISA map)\n\n"
            "A community-maintained CSV is also available:\n"
            "  https://raw.githubusercontent.com/OpenDataDE/State-zip-code-GeoJSON/master/"
            "(search GitHub for 'marijuana legalization dates csv')\n\n"
            "Create a CSV called `legalization_dates.csv` with columns:\n"
            "  state, fips, medical_year, recreational_year\n\n"
            "## Part 2 — BLS state-level labor outcomes\n\n"
            "1. Visit https://www.bls.gov/data/\n"
            "2. Use the BLS Data Finder or Series Report tool to pull:\n"
            "   - State unemployment rates (series IDs: LASST<FIPS>0000000000003)\n"
            "   - State employment series as desired\n"
            "3. Save as `bls_state_unemployment.csv` in this directory.\n\n"
            "Alternatively, use the FRED bulk download for state UR series\n"
            "(see project 02 for the URL pattern).\n"
        ),
    )

    # Download a few BLS-via-FRED state UR series as a starting point
    states = {
        "CO": "COUR",   # Colorado (early recreational legalization)
        "WA": "WAUR",   # Washington
        "OR": "ORUR",   # Oregon
        "CA": "CAUR",   # California
        "AK": "AKUR",   # Alaska
        "NV": "NVUR",   # Nevada
        "MA": "MAUR",   # Massachusetts
        "ME": "MEUR",   # Maine
    }
    fred_base = "https://fred.stlouisfed.org/graph/fredgraph.csv?id="
    for abbr, series_id in states.items():
        download(
            url=f"{fred_base}{series_id}",
            dest=dest / f"{series_id}.csv",
            description=f"FRED {abbr} unemployment rate ({series_id})",
        )


# ---------------------------------------------------------------------------
# DATA_SOURCES.md
# ---------------------------------------------------------------------------

DATA_SOURCES_CONTENT = """\
# Data Sources

All datasets used in causal-inference-playground.

| Project | Dataset | Source / URL | Access |
|---------|---------|--------------|--------|
| 01 DiD | Card & Krueger NJ/PA fast-food | http://davidcard.berkeley.edu/data_sets/njmin.zip | Direct download |
| 02 Event Study | FRED state unemployment rates | https://fred.stlouisfed.org/graph/fredgraph.csv?id=CAUR (pattern) | Direct download |
| 02 Event Study | COVID policy dates | https://github.com/COVID19StatePolicy/SocialDistancing | Manual download |
| 03 Synthetic Control | CA Prop 99 smoking | https://web.stanford.edu/~jhain/synthpage.html | Manual / R package |
| 04 RDD | Close elections (senate.csv) | https://dataverse.harvard.edu/ | Direct download (attempted) |
| 05 IV | Card college proximity | https://www.nber.org/research/data | Manual / R package |
| 06 PSM | LaLonde NSW treated | https://users.nber.org/~rdehejia/data/nswre74_treated.txt | Direct download |
| 06 PSM | LaLonde NSW control | https://users.nber.org/~rdehejia/data/nswre74_control.txt | Direct download |
| 06 PSM | LaLonde PSID controls | https://users.nber.org/~rdehejia/data/psid_controls.txt | Direct download |
| 06 PSM | LaLonde CPS controls | https://users.nber.org/~rdehejia/data/cps_controls.txt | Direct download |
| 07 DML | ACIC challenge | https://aciccomp.org/ | Manual (registration) |
| 07 DML | IHDP (alternative) | https://www.fredjo.com/files/ihdp_npci_1-100.train.npz | Direct download |
| 08 Causal Forest | Hillstrom email | http://www.minethatdata.com/Kevin_Hillstrom_MineThatData_E-MailAnalytics_DataMiningChallenge_2008.03.20.csv | Direct download |
| 09 Geo Experiment | TSA passenger volumes | https://www.tsa.gov/travel/passenger-volumes | Manual download |
| 10 Staggered DiD | Marijuana legalization dates | https://www.mpp.org/policy/state-by-state/ | Manual |
| 10 Staggered DiD | BLS state unemployment | https://www.bls.gov/data/ | Manual / FRED |
"""


def write_data_sources():
    path = REPO_ROOT / "DATA_SOURCES.md"
    path.write_text(DATA_SOURCES_CONTENT)
    log.info("Wrote DATA_SOURCES.md")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    log.info("=== causal-inference-playground data download ===")
    log.info("Repository root: %s", REPO_ROOT)

    steps = [
        project_01,
        project_02,
        project_03,
        project_04,
        project_05,
        project_06,
        project_07,
        project_08,
        project_09,
        project_10,
        write_data_sources,
    ]

    errors = 0
    for step in steps:
        try:
            step()
        except Exception as exc:
            log.error("Unexpected error in %s: %s", step.__name__, exc)
            errors += 1

    log.info("=== Done. %d step(s) had unexpected errors. ===", errors)
    if errors:
        log.warning("Check logs above for details.")


if __name__ == "__main__":
    main()
