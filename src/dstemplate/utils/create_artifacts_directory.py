from pathlib import Path

def create_artifacts_directory(root="."):
    data = Path(root) / "artifacts"

    folders = [data / sub for sub in ["models", "features", "metrics"]]
    
    for folder in folders:
        folder.mkdir(parents=True, exist_ok=True)