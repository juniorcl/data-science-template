from pathlib import Path


def create_reference_folder(root="."):
    folder = Path(root) / "references"
    folder.mkdir(parents=True, exist_ok=True)
