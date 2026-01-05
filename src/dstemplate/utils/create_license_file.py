from pathlib import Path

def create_license_file():
    file = Path(".") / "LICENSE"
    file.touch(exist_ok=True)