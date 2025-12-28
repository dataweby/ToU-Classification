# QA Checklist<br>**Classification Project**

Use this checklist to validate data quality, preprocessing, and evaluation before re-running training or reporting results. Fill in **Status** as `Pass`, `Fail`, or `TBD`. If any item fails, add a short fix plan in the last column.

| QA Section | Check | Status (Pass/Fail/TBD) | Evidence / Where to Verify | If Fail: Fix Plan |
|---|---|---:|---|---|
| **1. Schema Validation** | Confirm all expected columns are present in the modeling dataset. | Pass | Compare final columns to the data dictionary and pipeline feature names. | Rebuild the feature list and add an “expected columns” check. |
|  | Confirm column data types match the plan before encoding/scaling. | Pass | Check `df.dtypes` and the numeric/categorical column lists. | Cast types, then rerun preprocessing. |
|  | Check for unexpected or unused columns. | Pass | Scan columns for anything outside the planned feature set. | Drop extras and add a forbidden-column list. |
| **2. Missingness Audit** | Verify missingness is within acceptable thresholds per feature. | Pass | Review the missingness table/plot. | Drop the feature, add a missing flag, or adjust imputation. |
|  | Confirm imputation strategy is applied inside the pipeline and recorded. | Pass | Verify imputers exist in the pipeline and are fit on train only. | Add/adjust imputers in the pipeline and document the choice. |
| **3. Outlier Review** | Run outlier detection on all numeric features. | Pass-ish | Review numeric summaries and distribution plots. | Apply log/log1p or cap extremes, then rerun training. |
|  | Decide and document handling for outliers. | Pass | Confirm one consistent outlier rule is written down. | Standardize the rule in the pipeline and rerun evaluation. |
|  | Review extreme values with domain context. | Pass | Spot-check the largest values for plausibility. | Fix data issues or keep values with robust transforms. |
| **4. Class Balance Check** | Calculate and visualize class distribution in full data and in train/test splits. | Pass | Check class counts and that train/test proportions match. | Use stratified split and rerun evaluation. |
|  | Confirm minimum sample threshold per class. | Pass | Check per-class counts in train and test. | Merge labels, add data, or narrow claims. |
|  | Document any imbalance mitigation and why. | Pass | Check notes for macro metrics and class weighting/thresholding. | Add class weights or adjust thresholds; keep macro metrics. |
| **5. Encoding Validation** | Confirm categorical features are encoded exactly as planned. | Pass | Check encoder settings and one-hot feature names. | Fix encoder settings and rerun preprocessing. |
|  | Check for category collapse due to cleaning errors. | Fail | Compare raw category values to encoded categories. | Standardize labels and remap rare/unknown categories. |
|  | Confirm encoded matrix dimensions match expectations. | TBD | Check transformed train/test shapes and feature count. | Fix column selection/encoding and add a shape check. |
| **6. Scaling Verification** | Confirm scaling is applied only to numeric features. | Pass | Confirm the scaler is only in the numeric pipeline. | Move scaling to numeric only and rerun. |
|  | Confirm the scaler is fit only on the training set. | Pass | Confirm scaling happens inside the pipeline fit. | Remove any full-data scaling and refit on train only. |
|  | Visualize distributions before and after scaling for key numeric features. | Pass | Compare pre/post scaling plots or summaries. | Add plots and adjust transforms if needed. |
| **7. Leakage Prevention** | Confirm no future or label-derived features are included. | Pass | Check that all features use only pre-cutoff data and no outcome fields. | Remove leaky features and add a leakage check. |
|  | Confirm time-based features are filtered correctly with no future information. | Pass | Spot-check timestamps vs the cutoff rule. | Fix cutoff filtering and rebuild aggregates. |
|  | Confirm preprocessing is cleanly separated for train/test with no peeking during tuning. | Pass | Confirm CV/tuning uses pipelines end-to-end. | Move all preprocessing into the pipeline and rerun CV. |
| **8. Reproducibility** | Confirm preprocessing is version-controlled. | Pass-ish | Confirm notebooks/scripts are committed in the Codespaces repo. | Commit changes and test from a fresh Codespace. |
|  | Confirm key parameters are captured in a config file. | TBD | Confirm cutoff and feature settings are saved in one file. | Add a config file and load it in the pipeline. |
|  | Save environment details so results can be reproduced. | Pass | Confirm `devcontainer.json` and dependencies are committed. | Pin dependencies and rebuild the Codespace to verify. |
