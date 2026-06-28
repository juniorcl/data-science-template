from dstemplate.utils import create_license_file, create_readme_file


def test_create_readme_file(project_root):
    create_readme_file("myproject", project_root)
    readme = project_root / "README.md"
    assert readme.is_file()
    content = readme.read_text()
    assert "# myproject" in content
    assert "myproject/" in content


def test_create_license_file(project_root):
    create_license_file("Test Author", project_root)
    license_file = project_root / "LICENSE"
    assert license_file.is_file()
    content = license_file.read_text()
    assert "Test Author" in content
    assert "MIT License" in content
