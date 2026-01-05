from pathlib import Path

def create_model_folder():
    folder = Path("model")
    
    folder.mkdir(parents=True, exist_ok=True)
    
    print("Folder model successfully created 🚀")