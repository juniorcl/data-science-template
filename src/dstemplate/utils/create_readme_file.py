from pathlib import Path

README_TEMPLATE = """# {project_name}

## Project Structure

```
data/
├── raw/
├── interim/
├── processed/
└── external/
notebooks/
src/{project_name}/
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
"""


def create_readme_file(project_name: str = "myproject", root: str = ".") -> None:
    file = Path(root) / "README.md"
    file.write_text(README_TEMPLATE.format(project_name=project_name))
