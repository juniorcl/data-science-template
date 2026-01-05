from pathlib import Path

def create_docs_folder():
    folder = Path("docs")
    
    folder.mkdir(parents=True, exist_ok=True)
    
    print("Folder docs successfully created 🚀")