from pathlib import Path

def create_reports_folder():
    folder = Path("reports") / "figures"
    
    folder.mkdir(parents=True, exist_ok=True)
    
    print("Folder notebooks successfully created 🚀")