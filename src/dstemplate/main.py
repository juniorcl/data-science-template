import argparse

from .utils import (
    create_artifacts_directory,
    create_data_directory,
    create_docs_folder,
    create_license_file,
    create_notebooks_folder,
    create_readme_file,
    create_reference_folder,
    create_reports_directory,
    create_requirements_file,
    create_src_directory,
)


def main(args: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Scaffold a Data Science project")
    parser.add_argument(
        "project_name", help="name of the project (used for the Python package)"
    )
    parser.add_argument(
        "--author", default="Your Name", help="author name for the LICENSE file"
    )
    parser.add_argument(
        "--python-version", default="3.10", help="target Python version"
    )
    parser.add_argument(
        "--no-notebooks", action="store_true", help="skip notebooks directory"
    )
    parser.add_argument("--no-docs", action="store_true", help="skip docs directory")

    parsed = parser.parse_args(args)
    pn = parsed.project_name

    create_readme_file(project_name=pn)
    print("README.md created")

    create_license_file(author=parsed.author)
    print("LICENSE created")

    create_requirements_file()
    print("requirements.txt created")

    create_data_directory()
    print("data/ created")

    create_artifacts_directory()
    print("artifacts/ created")

    if not parsed.no_notebooks:
        create_notebooks_folder()
        print("notebooks/ created")

    if not parsed.no_docs:
        create_docs_folder()
        print("docs/ created")

    create_reports_directory()
    print("reports/figures/ created")

    create_reference_folder()
    print("references/ created")

    create_src_directory(pn)
    print(f"src/{pn}/ created")


if __name__ == "__main__":
    main()
