from dstemplate.utils import create_notebooks_folder


def test_create_notebooks_folder(project_root):
    create_notebooks_folder(project_root)
    assert (project_root / "notebooks").is_dir()
