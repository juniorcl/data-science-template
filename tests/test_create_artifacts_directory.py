from dstemplate.utils import create_artifacts_directory

def test_create_artifacts_directory(project_root):
    create_artifacts_directory(project_root)

    expected_folders = [
        project_root / "artifacts" / "models",
        project_root / "artifacts" / "features",
        project_root / "artifacts" / "metrics",
    ]

    for folder in expected_folders:
        assert folder.is_dir()