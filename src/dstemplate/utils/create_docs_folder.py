from pathlib import Path


def create_docs_folder(root="."):
    folder = Path(root) / "docs"
    folder.mkdir(parents=True, exist_ok=True)
