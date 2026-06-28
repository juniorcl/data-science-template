from pathlib import Path

import pytest


@pytest.fixture
def project_root(tmp_path: Path) -> Path:
    """
    Simula o diretório onde o usuário roda o comando.
    Todas as pastas (data, docs, src, etc.) serão criadas aqui.
    """
    return tmp_path
