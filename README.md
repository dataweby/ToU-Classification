
## Machine

Used GitHub Codespaces with a 4-Core, 16GM RAM, 32GB Storage Space

## Deliverables

 - **Deliverable 1: Problem Definition** <br>Available as a markdown file report in `reports/01_problem_definition.md`.

 - **Deliverable 2: Jupyter Notebook(s)** <br>Split across two Jupyter notebooks in the `/notebooks` folder. The first notebook `/notebooks/01_dataset_preprocessing.ipynb` handles the preprocessing of the data and inital steps for the model whereas the second notebook `/notebooks/02_models.ipynb` contains the solution implementation.

 - **Deliverable 3: Performance Report**<br> Available as markdown file in `/reports/02_performance_report.md`.

## Dataset Setup (Required)

This project expects the raw **OULAD** CSV files from the [Open University Learning Analytics Dataset (OULAD)](https://www.kaggle.com/datasets/anlgrbz/student-demographics-online-education-dataoulad).

Because Kaggle datasets typically require user consent and authentication, **the raw CSV files are not stored in this repository**. You must download them yourself and place them in `inputs/raw/`. 

### Required CSV files

Place **all** of the .CSV files in `inputs/raw/`. Your folder should look like:

```text
inputs/
└─── raw/
     ├─ courses.csv
     ├─ assessments.csv
     ├─ vle.csv
     ├─ studentInfo.csv
     ├─ studentRegistration.csv
     ├─ studentAssessment.csv
     └─ studentVle.cs
```

All other files used for the solution are part of this repository.

## Repository Structure

The following tree was generated using: [Github File Tree Generator Tools](https://www.readmecodegen.com/file-tree/tools)

```
📁 ToU-Classification/
├── 📁 __pycache__/
│   └── 📄 utils.cpython-312.pyc
├── 📁 .devcontainer/
│   └── 🔢 devcontainer.json
├── 📁 .vscode/
│   └── 🔢 settings.json
├── 📁 inputs/
│   ├── 📁 external/
│   │   ├── 📕 Data Description (Official).pdf
│   │   └── 🖼️ OULAD_database_ERD.png
│   └── 📁 raw/
│       └── 📄 .gitkeep
├── 📁 notebooks/
│   ├── 📄 01_dataset_preprocessing.ipynb
│   └── 📄 02_models.ipynb
├── 📁 outputs/
│   ├── 📁 data/
│   │   ├── 📁 processed/
│   │   │   ├── 📄 groups_train.csv
│   │   │   ├── 📄 X_test_raw.csv
│   │   │   ├── 📄 X_train_raw.csv
│   │   │   ├── 📄 y_test.csv
│   │   │   └── 📄 y_train.csv
│   │   ├── 📄 idx_1_train_indices.csv
│   │   ├── 📄 idx_2_test_indices.csv
│   │   └── 📄 test_predictions.csv
│   ├── 📁 figures/
│   │   ├── 🖼️ visual_1_module_presentation_length_histogram.png
│   │   ├── 🖼️ visual_2_timeline_prediction_time.png
│   │   ├── 🖼️ visual_3_risk_tier_distribution.png
│   │   ├── 🖼️ visual_4_risk_tier_distribution_after_exclusion.png
│   │   ├── 🖼️ visual_5_types_of_activities.png
│   │   ├── 🖼️ visual_6_missingness.png
│   │   ├── 🖼️ visual_7_total_clicks_by_risk.png
│   │   ├── 🖼️ visual_8_total_clicks_distribution.png
│   │   ├── 🖼️ visual_9_log_total_clicks_distribution.png
│   │   ├── 🖼️ visual_10_log1p_total_clicks_distribution.png
│   │   ├── 🖼️ visual_11_avg_assessment_score_cutoff_hist.png
│   │   ├── 🖼️ visual_12_avg_assessment_score_by_risk.png
│   │   ├── 🖼️ visual_13_correlation_heatmap.png
│   │   ├── 🖼️ visual_14_train_test_split_pie.png
│   │   ├── 🖼️ visual_15_confusion_matrix_test.png
│   │   ├── 🖼️ visual_16_roc_high_risk_vs_rest.png
│   │   ├── 🖼️ visual_17_pr_high_risk_vs_rest.png
│   │   └── 🖼️ visual_18_top_features_best_model.png
│   ├── 📁 models/
│   │   ├── 🔢 best_model_meta.json
│   │   ├── 📄 best_model.joblib
│   │   └── 📄 preprocess_pipeline.joblib
│   └── 📁 tables/
│       ├── 📁 features/
│       │   ├── 📄 1_numeric_features.csv
│       │   ├── 📄 2_categorical_features.csv
│       │   └── 📄 3_log_transformed_numeric_features.csv
│       ├── 📄 table_1_raw_file_inventory_md5.csv
│       ├── 📄 table_2_data_dictionary_snapshot.csv
│       ├── 📄 table_3_assessment_features_early_summary.csv
│       ├── 📄 table_4_vle_features_early_summary.csv
│       ├── 📄 table_5_missingness_summary.csv
│       ├── 📄 table_6_missingness_table.csv
│       ├── 📄 table_7_numeric_correlation_matrix.csv
│       ├── 📄 table_8_sorted_correlation_pairs.csv
│       ├── 📄 table_9_split_class_balance_pct.csv
│       ├── 📄 table_10_imbalance_severity.csv
│       ├── 📄 table_11_baseline_dummy_cv_train_only.csv
│       ├── 📄 table_12_model_comparison_cv_train_only.csv
│       ├── 📄 table_13_logreg_gridsearch_cv_results.csv
│       ├── 📄 table_14_rf_randomsearch_cv_results.csv
│       ├── 📄 table_15_baseline_vs_models_train_cv_summary.csv
│       ├── 📄 table_16_test_metrics_summary.csv
│       ├── 📄 table_17_test_classification_report.csv
│       ├── 📄 table_18_test_confusion_matrix.csv
│       ├── 📄 table_19_confusion_matrix_binary_highrisk.csv
│       ├── 📄 table_20_confusion_matrix_binary_mediumrisk.csv
│       ├── 📄 table_21_confusion_matrix_binary_lowrisk.csv
│       ├── 📄 table_22_misclassification_pairs_test.csv
│       └── 📄 table_23_feature_importance_best_model.csv
├── 📁 reports/
│   ├── 📄 01_problem_definition.md
│   └── 📄 02_performance_report.md
├── 📄 .gitignore
├── 📄 01_OULAD_readiness_checklist.md
├── 📄 02_DATA_DICTIONARY.md
├── 📄 03_feature_dictionary.xlsx
├── 📄 04_impact_statement.md
├── 📄 05_QA_CHECKLIST.md
├── 📄 LICENSE
├── 🖼️ output.png
├── 📄 README.md
├── 📄 requirements.txt
└── 📄 utils.py

```


