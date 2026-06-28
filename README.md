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
│   ├── config.py
│   ├── dataset.py
│   ├── features.py
│   ├── plots.py
│   └── modeling/
│       ├── __init__.py
│       ├── train.py
│       └── predict.py
├── artifacts/
│   ├── models/
│   ├── features/
│   └── metrics/
├── docs/
├── reports/figures/
├── references/
├── README.md
└── LICENSE
```

## Generated structure

| Directory | Purpose |
|-----------|---------|
| `data/` | Raw, interim, processed, and external data |
| `notebooks/` | Jupyter notebooks for exploration and analysis |
| `src/{project}/` | Modular Python package: config, dataset, features, plots, training (train) and prediction (predict) |
| `artifacts/` | Trained models, feature engineering pipelines, and metrics |
| `docs/` | Project documentation |
| `reports/figures/` | Generated figures and reports |
| `references/` | Reference materials |

## Tests

```bash
pytest -v
```

## CI

GitHub Actions runs tests on Python 3.10, 3.11, 3.12, and 3.13 on every push.

## License

MIT