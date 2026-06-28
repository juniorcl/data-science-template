from dstemplate.utils import create_docs_folder


def test_create_docs_folder(project_root):
    create_docs_folder(project_root)
    assert (project_root / "docs").is_dir()
