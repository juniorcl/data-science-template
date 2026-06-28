import sys

from .utils import (
    create_artifacts_directory,
    create_data_directory,
    create_docs_folder,
    create_license_file,
    create_notebooks_folder,
    create_readme_file,
    create_reference_folder,
    create_reports_directory,
    create_src_directory,
)


def main(project_name: str) -> None:
    create_readme_file(project_name=project_name)
    print("README.md file successfully created")

    create_license_file(author="Your Name")
    print("LICENSE file successfully created")

    create_data_directory()
    print("data folder successfully created")

    create_artifacts_directory()
    print("artifacts folder successfully created")

    create_notebooks_folder()
    print("notebooks folder successfully created")

    create_docs_folder()
    print("docs folder successfully created")

    create_reports_directory()
    print("reports directory successfully created")

    create_reference_folder()
    print("references folder successfully created")

    create_src_directory(project_name)
    print("src directory successfully created")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise ValueError("You must provide a project name")

    main(sys.argv[1])
