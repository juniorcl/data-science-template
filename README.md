# testpkg

## Project Structure

```
data/
├── raw/
├── interim/
├── processed/
└── external/
notebooks/
src/testpkg/
├── __init__.py
├── config.py
├── dataset.py
├── features.py
├── plots.py
└── modeling/
    ├── __init__.py
    ├── train.py
    └── predict.py
artifacts/
├── models/
├── features/
└── metrics/
docs/
reports/figures/
references/
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
