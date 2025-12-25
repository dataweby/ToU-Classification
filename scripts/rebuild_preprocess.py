"""Rebuild preprocessing pipeline from saved processed CSVs and save joblib.

This avoids executing the entire notebook and ensures the pipeline uses
`np.log1p` instead of a notebook-local `safe_log1p` function.
"""
from pathlib import Path
import pandas as pd
import numpy as np
import joblib
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer, OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer


OUT_DIR = Path("outputs")
DATA_DIR = OUT_DIR / "data" / "processed"
MODEL_DIR = OUT_DIR / "models"

X_train_path = DATA_DIR / "X_train_raw.csv"
if not X_train_path.exists():
    raise FileNotFoundError(f"Missing {X_train_path}")

X_train = pd.read_csv(X_train_path)

# Identify categorical and numeric columns
cat_cols = X_train.select_dtypes(include=["object"]).columns.tolist()
num_cols = [c for c in X_train.columns if c not in cat_cols]

# Heuristic for log columns (as used in notebook)
log_keywords = ["click", "interaction", "assessment", "submitted", "weighted"]
log_cols = [c for c in num_cols if any(tok in c.lower() for tok in log_keywords)]
std_cols = [c for c in num_cols if c not in log_cols]

print(f"Found numeric={len(num_cols)}, log={len(log_cols)}, std={len(std_cols)}, cat={len(cat_cols)}")

# Pipelines
log_pipe = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median")),
    ("log1p", FunctionTransformer(np.log1p, feature_names_out="one-to-one")),
    ("scaler", StandardScaler()),
])

std_pipe = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler()),
])

cat_pipe = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("onehot", OneHotEncoder(handle_unknown="ignore")),
])

preprocess = ColumnTransformer(
    transformers=[
        ("num_log", log_pipe, log_cols),
        ("num_std", std_pipe, std_cols),
        ("cat", cat_pipe, cat_cols),
    ],
    remainder="drop",
)

MODEL_DIR.mkdir(parents=True, exist_ok=True)
joblib.dump(preprocess, MODEL_DIR / "preprocess_pipeline.joblib")
print("Wrote:", MODEL_DIR / "preprocess_pipeline.joblib")
