from pathlib import Path

from dstemplate.main import main


def test_main_creates_all_directories_and_files(project_root: Path, monkeypatch):
    project_name = "testpkg"
    root = project_root

    monkeypatch.chdir(root)
    main([project_name])

    assert (root / "data" / "raw").is_dir()
    assert (root / "data" / "processed").is_dir()
    assert (root / "data" / "external").is_dir()
    assert (root / "data" / "interim").is_dir()

    assert (root / "artifacts" / "models").is_dir()
    assert (root / "artifacts" / "features").is_dir()
    assert (root / "artifacts" / "metrics").is_dir()

    assert (root / "notebooks").is_dir()
    assert (root / "docs").is_dir()
    assert (root / "reports" / "figures").is_dir()
    assert (root / "references").is_dir()

    src = root / "src" / project_name
    assert src.is_dir()
    assert (src / "__init__.py").is_file()
    assert (src / "config.py").is_file()
    assert (src / "dataset.py").is_file()
    assert (src / "features.py").is_file()
    assert (src / "plots.py").is_file()
    assert (src / "modeling" / "__init__.py").is_file()
    assert (src / "modeling" / "train.py").is_file()
    assert (src / "modeling" / "predict.py").is_file()

    readme = root / "README.md"
    assert readme.is_file()
    assert readme.read_text().strip() != ""

    license_file = root / "LICENSE"
    assert license_file.is_file()
    assert license_file.read_text().strip() != ""

    req = root / "requirements.txt"
    assert req.is_file()
    assert "pandas" in req.read_text()


def test_main_with_author_flag(project_root: Path, monkeypatch):
    monkeypatch.chdir(project_root)
    main(["testpkg", "--author", "Clébio Júnior"])

    content = (project_root / "LICENSE").read_text()
    assert "Clébio Júnior" in content


def test_main_with_no_notebooks(project_root: Path, monkeypatch):
    monkeypatch.chdir(project_root)
    main(["testpkg", "--no-notebooks"])

    assert not (project_root / "notebooks").exists()
    assert (project_root / "docs").is_dir()


def test_main_with_no_docs(project_root: Path, monkeypatch):
    monkeypatch.chdir(project_root)
    main(["testpkg", "--no-docs"])

    assert (project_root / "notebooks").is_dir()
    assert not (project_root / "docs").exists()


def test_main_with_all_flags(project_root: Path, monkeypatch):
    monkeypatch.chdir(project_root)
    main(["testpkg", "--no-notebooks", "--no-docs", "--author", "Dev"])

    assert not (project_root / "notebooks").exists()
    assert not (project_root / "docs").exists()
    assert "Dev" in (project_root / "LICENSE").read_text()
