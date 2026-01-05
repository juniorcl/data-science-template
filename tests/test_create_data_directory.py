from dstemplate.utils import create_data_directory

def test_create_data_directory(project_root):
    create_data_directory(project_root)

    expected_folders = [
        project_root / "data" / "external",
        project_root / "data" / "interim",
        project_root / "data" / "processed",
        project_root / "data" / "raw",
    ]

    for folder in expected_folders:
        assert folder.is_dir()