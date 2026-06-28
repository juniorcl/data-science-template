from pathlib import Path

CONFIG_PY = """from pathlib import Path


class Config:
    data_dir = Path("data")
    raw_dir = data_dir / "raw"
    interim_dir = data_dir / "interim"
    processed_dir = data_dir / "processed"
    external_dir = data_dir / "external"
    artifacts_dir = Path("artifacts")
    models_dir = artifacts_dir / "models"
    features_dir = artifacts_dir / "features"
    metrics_dir = artifacts_dir / "metrics"
    random_state = 42
    test_size = 0.2
"""

DATASET_PY = """from pathlib import Path

import pandas as pd


def load_data(path: Path | str) -> pd.DataFrame:
    path = Path(path)
    if path.suffix == ".csv":
        return pd.read_csv(path)
    if path.suffix == ".parquet":
        return pd.read_parquet(path)
    raise ValueError(f"Unsupported format: {path.suffix}")
"""

FEATURES_PY = """import pandas as pd


def create_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    return df
"""

PLOTS_PY = """import matplotlib.pyplot as plt
import seaborn as sns


def plot_correlation_matrix(df, figsize=(10, 8)):
    fig, ax = plt.subplots(figsize=figsize)
    sns.heatmap(df.corr(), annot=True, fmt=".2f", ax=ax)
    return fig
"""

TRAIN_PY = """import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

from config import Config


def train(X_train, y_train):
    model = RandomForestClassifier(random_state=Config.random_state)
    model.fit(X_train, y_train)
    return model


if __name__ == "__main__":
    df = pd.read_csv(Config.processed_dir / "dataset.csv")
    X = df.drop("target", axis=1)
    y = df["target"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=Config.test_size, random_state=Config.random_state
    )

    model = train(X_train, y_train)
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))
"""

PREDICT_PY = """import joblib
import pandas as pd
from pathlib import Path


def predict(model, X):
    return model.predict(X)


if __name__ == "__main__":
    model = joblib.load(Path("artifacts") / "models" / "model.pkl")
    df = pd.read_csv(Path("data") / "processed" / "dataset.csv")
    predictions = predict(model, df)
    print(predictions)
"""

SRC_TEMPLATES: dict[str, str] = {
    "__init__.py": "",
    "config.py": CONFIG_PY,
    "dataset.py": DATASET_PY,
    "features.py": FEATURES_PY,
    "plots.py": PLOTS_PY,
    "modeling/__init__.py": "",
    "modeling/train.py": TRAIN_PY,
    "modeling/predict.py": PREDICT_PY,
}


def create_src_directory(project_name: str, root: str = ".") -> None:
    base = Path(root) / "src" / project_name

    folders = [
        base,
        base / "modeling",
    ]

    files = [
        base / "__init__.py",
        base / "config.py",
        base / "dataset.py",
        base / "features.py",
        base / "plots.py",
        base / "modeling" / "__init__.py",
        base / "modeling" / "train.py",
        base / "modeling" / "predict.py",
    ]

    for folder in folders:
        folder.mkdir(parents=True, exist_ok=True)

    for file in files:
        rel = file.relative_to(base)
        content = SRC_TEMPLATES.get(str(rel), "")
        file.write_text(content)
