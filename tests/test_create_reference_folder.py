from dstemplate.utils import create_reference_folder


def test_create_reference_folder(project_root):
    create_reference_folder(project_root)
    assert (project_root / "references").is_dir()
