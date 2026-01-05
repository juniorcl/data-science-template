from pathlib import Path

def create_notebooks_folder():
    folder = Path("notebooks")
    
    folder.mkdir(parents=True, exist_ok=True)
    
    print("Folder notebooks successfully created 🚀")