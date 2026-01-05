from pathlib import Path

def create_readme_file():
    file = Path(".") / "README.md"
    file.touch(exist_ok=True)