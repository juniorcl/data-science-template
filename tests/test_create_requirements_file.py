from dstemplate.utils import create_requirements_file


def test_create_requirements_file(project_root):
    create_requirements_file(project_root)

    req = project_root / "requirements.txt"
    assert req.is_file()
    content = req.read_text()
    assert "pandas" in content
    assert "numpy" in content
    assert "scikit-learn" in content
    assert "matplotlib" in content
    assert "seaborn" in content
    assert "jupyter" in content
