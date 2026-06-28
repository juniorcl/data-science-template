from dstemplate.utils import create_src_directory


def test_create_src_directory(project_root):
    project_name = "mypackage"

    create_src_directory(project_name, project_root)

    base = project_root / "src" / project_name

    assert base.is_dir()
    assert (base / "modeling").is_dir()

    expected_files = [
        "__init__.py",
        "config.py",
        "dataset.py",
        "features.py",
        "plots.py",
    ]

    for file in expected_files:
        assert (base / file).is_file()

    modeling_files = [
        base / "modeling" / "__init__.py",
        base / "modeling" / "train.py",
        base / "modeling" / "predict.py",
    ]

    for file in modeling_files:
        assert file.is_file()
