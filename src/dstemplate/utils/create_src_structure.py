from pathlib import Path

def create_src_structure(project_name: str) -> None:
    base = Path("src") / project_name

    folders = [
        base,
        base / "modeling",
    ]

    files = [
        base / "__init__.py",
        base / "config.py",
        base / "dataset.py",
        base / "features.py",
        base / "plots.py",
        base / "modeling" / "__init__.py",
        base / "modeling" / "train.py",
        base / "modeling" / "predict.py",
    ]

    for folder in folders:
        folder.mkdir(parents=True, exist_ok=True)

    for file in files:
        file.touch(exist_ok=True)