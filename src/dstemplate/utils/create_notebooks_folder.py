from pathlib import Path


def create_notebooks_folder(root="."):
    folder = Path(root) / "notebooks"
    folder.mkdir(parents=True, exist_ok=True)
