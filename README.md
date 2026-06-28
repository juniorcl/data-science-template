# Data Science Template

CLI for scaffolding Data Science projects. Generates a standardized directory structure, files, and initial configuration for new projects.

## Development install

```bash
git clone https://github.com/juniorcl/data-science-template.git
cd data-science-template
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

This installs the package in editable mode with dev dependencies (pytest, ruff, black, ipykernel).

## Usage

```bash
dstemplate myproject
```

Creates the following structure in the current directory:

```
myproject/
├── data/
│   ├── raw/
│   ├── interim/
│   ├── processed/
│   └── external/
├── notebooks/
├── src/myproject/
│   ├── __init__.py
│   ├── config.py          # Config class with paths and hyperparams
│   ├── dataset.py         # load_data() for CSV / Parquet
│   ├── features.py        # create_features() skeleton
│   ├── plots.py           # plot_correlation_matrix()
│   └── modeling/
│       ├── __init__.py
│       ├── train.py       # train() + CLI example with sklearn
│       └── predict.py     # predict() loading saved model
├── artifacts/
│   ├── models/
│   ├── features/
│   └── metrics/
├── docs/
├── reports/figures/
├── references/
├── requirements.txt       # pandas, numpy, scikit-learn, matplotlib, seaborn, jupyter
├── README.md
└── LICENSE
```

### CLI flags

| Flag | Default | Description |
|------|---------|-------------|
| `project_name` | (required) | Name of the project / Python package |
| `--author` | `Your Name` | Author name for the LICENSE file |
| `--no-notebooks` | `false` | Skip `notebooks/` directory |
| `--no-docs` | `false` | Skip `docs/` directory |

```bash
dstemplate myproject --author "Jane Doe"
dstemplate myproject --no-notebooks --no-docs
```

## Generated structure

| Directory / File | Purpose |
|------------------|---------|
| `data/` | Raw, interim, processed, and external data |
| `notebooks/` | Jupyter notebooks for exploration and analysis |
| `src/{project}/` | Modular Python package with starter code (config, dataset, features, plots, train, predict) |
| `artifacts/` | Trained models, feature engineering pipelines, and metrics |
| `docs/` | Project documentation |
| `reports/figures/` | Generated figures and reports |
| `references/` | Reference materials |
| `requirements.txt` | Common Data Science dependencies |

## Tests

```bash
pytest -v
```

## CI

GitHub Actions runs tests on Python 3.10, 3.11, 3.12, and 3.13 on every push.

## License

MIT