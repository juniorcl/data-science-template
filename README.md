# Data Science Template

CLI para scaffolding de projetos de Data Science. Gera estrutura padronizada de diretórios, arquivos e configuração inicial para novos projetos.

## Instalação (desenvolvimento)

```bash
git clone https://github.com/juniorcl/data-science-template.git
cd data-science-template
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

Isso instala o pacote em modo editável com dependências de desenvolvimento (pytest, ruff, black, ipykernel).

## Uso

```bash
dstemplate meu_projeto
```

O comando cria a seguinte estrutura no diretório atual:

```
meu_projeto/
├── data/
│   ├── raw/
│   ├── interim/
│   ├── processed/
│   └── external/
├── notebooks/
├── src/meu_projeto/
│   ├── __init__.py
│   ├── config.py
│   ├── dataset.py
│   ├── features.py
│   ├── plots.py
│   └── modeling/
│       ├── __init__.py
│       ├── train.py
│       └── predict.py
├── artifacts/
│   ├── models/
│   ├── features/
│   └── metrics/
├── docs/
├── reports/figures/
├── references/
├── README.md
└── LICENSE
```

## Estrutura gerada

| Diretório | Finalidade |
|-----------|-----------|
| `data/` | Dados brutos (raw), intermediários (interim), processados (processed) e externos (external) |
| `notebooks/` | Jupyter notebooks para exploração e análise |
| `src/{projeto}/` | Pacote Python modular: config, dataset, features, plots, treino (train) e predição (predict) |
| `artifacts/` | Modelos treinados, pipelines de feature engineering e métricas |
| `docs/` | Documentação do projeto |
| `reports/figures/` | Figuras e relatórios gerados |
| `references/` | Materiais de referência |

## Testes

```bash
pytest -v
```

## CI

GitHub Actions executa testes em Python 3.10, 3.11, 3.12 e 3.13 a cada push.

## Licença

MIT