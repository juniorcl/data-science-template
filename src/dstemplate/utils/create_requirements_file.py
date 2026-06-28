from pathlib import Path

REQUIREMENTS = """pandas>=2.0
numpy>=1.24
scikit-learn>=1.3
matplotlib>=3.7
seaborn>=0.12
jupyter>=1.0
"""


def create_requirements_file(root: str = ".") -> None:
    Path(root, "requirements.txt").write_text(REQUIREMENTS)
