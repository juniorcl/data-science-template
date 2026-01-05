import sys
from .utils import (
    create_docs_folder,
    create_readme_file,
    create_license_file,
    create_model_folder,
    create_src_structure,
    create_reports_folder,
    create_data_structure,
    create_notebooks_folder,
    create_reference_folder,
)


def main(project_name: str) -> None:
    create_readme_file()
    create_license_file()
    create_data_structure()
    create_model_folder()
    create_notebooks_folder()
    create_docs_folder()
    create_reports_folder()
    create_reference_folder()
    create_src_structure(project_name)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise ValueError("You must provide a project name")

    main(sys.argv[1])
