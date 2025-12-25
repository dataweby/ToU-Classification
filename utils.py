import numpy as np

# An implementation of log1p used in Notebooks 1 and 2
def safe_log1p(x):
    arr = np.asarray(x)
    return np.log1p(arr)

# Scoring metrics for model evaluation (used in 02_models.ipynb)
SCORING_METRICS = {
    "macro_f1": "f1_macro",
    "balanced_acc": "balanced_accuracy",
    "precision_macro": "precision_macro",
    "recall_macro": "recall_macro"
}

# Helper function to summarize CV outputs into a single row (used in 02_models.ipynb)
# cross_validate returns arrays like:
# - cv_results["test_macro_f1"] = [score_fold1, score_fold2, ..., score_fold5]
# This function converts those arrays into:
# - mean and std across folds for each metric
# - mean fit time (rough computational cost indicator)
# The utput is a small dictionary suitable for building a comparison DataFrame.

def summarize_cv(name: str, cv_results: dict) -> dict:
    out = {"model": name}  # label the row with the model/pipeline name

    # For each metric in our scoring dict, compute mean and std across folds
    for k in SCORING_METRICS.keys():
        out[f"{k}_mean"] = float(np.mean(cv_results[f"test_{k}"]))  # average test metric across folds
        out[f"{k}_std"]  = float(np.std(cv_results[f"test_{k}"]))   # variability across folds

    # Average training time across folds
    out["fit_time_mean"] = float(np.mean(cv_results["fit_time"]))

    return out
