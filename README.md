# Energy System Modeling - Learning

A repo to keep track of my work while re-learning energy system modelling.

Each notebook is a self-contained exercise, kept with its outputs so the results
are readable directly on GitHub.

## Contents

| Notebook | Topic |
| --- | --- |
| [`linopy_simple_dispatch.ipynb`](linopy_simple_dispatch.ipynb) | A minimal economic dispatch LP in [linopy](https://linopy.readthedocs.io): two generators with min/max capacity and different marginal costs, meeting a fixed 500 MW demand at least cost. |

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install linopy pandas numpy highspy jupyterlab
```

The notebooks solve with the open-source [HiGHS](https://highs.dev) solver
(`solver_name="highs"`), installed via `highspy`.

```bash
jupyter lab
```
