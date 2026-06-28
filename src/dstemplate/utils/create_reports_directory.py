from pathlib import Path


def create_reports_directory(root="."):
    folder = Path(root) / "reports" / "figures"
    folder.mkdir(parents=True, exist_ok=True)
