# Energy System Modeling - Learning

A repo to keep track of my work while re-learning energy system modelling.

Each notebook is a self-contained exercise, kept with its outputs so the results
are readable directly on GitHub.

## Contents

| Notebook | Topic |
| --- | --- |
| [`linopy_simple_dispatch.ipynb`](linopy_simple_dispatch.ipynb) | A minimal economic dispatch LP in [linopy](https://linopy.readthedocs.io): two generators with min/max capacity and different marginal costs, meeting a fixed 500 MW demand at least cost. |
| [`pypsa_simple_dispatch.ipynb`](pypsa_simple_dispatch.ipynb) | A PyPSA dispatch walkthrough: build a small network, optimize dispatch across three snapshots, and compare a scenario with solar generation and marginal prices. |
| [`case_studies.ipynb`](case_studies.ipynb) | PyPSA case studies: a wind turbine network and a solar plus battery storage (BESS) network over four snapshots. |
| [`snakemake/`](snakemake/README.md) | The capacity expansion model modularised into scripts and chained with Snakemake: one job per CO2 limit (sensitivity, solve), then an aggregation step that writes a cost-by-carrier CSV and a sensitivity plot. |

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install pypsa linopy pandas numpy highspy jupyterlab snakemake
```

The notebooks solve with the open-source [HiGHS](https://highs.dev) solver
(`solver_name="highs"`), installed via `highspy`.

```bash
jupyter lab
```
