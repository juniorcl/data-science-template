from pathlib import Path

def create_reference_folder():
    folder = Path("references")
    
    folder.mkdir(parents=True, exist_ok=True)
    
    print("Folder references successfully created 🚀")