from pathlib import Path

def create_data_structure():
    data = Path("data")

    folders = [data / sub for sub in ["external", "interim", "processed", "raw"]]

    for folder in folders:
        folder.mkdir(parents=True, exist_ok=True)

    print("Folder data successfully created 🚀")