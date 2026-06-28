from dstemplate.utils import create_reports_directory


def test_create_reports_directory(project_root):
    create_reports_directory(project_root)
    assert (project_root / "reports" / "figures").is_dir()
