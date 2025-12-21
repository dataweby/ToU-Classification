# Data Dictionary

See the `README.md` file for the project descritpion and content in which the dataset is used.

## 1. Dataset Provenance

**Primary source (downloaded files):**
- Kaggle dataset page: https://www.kaggle.com/datasets/anlgrbz/student-demographics-online-education-dataoulad

**Original dataset home and documentation:**
- OU Analyse (Open University): https://analyse.kmi.open.ac.uk/open-dataset

**Resources:**
- Kuzilek, Hlosta, Zdrahal (2017), *Open University Learning Analytics dataset* (Scientific Data)

**License:**
- CC BY 4.0 (Attribution 4.0 International). You must provide attribution when redistributing derived materials.

## 2. Repository Data Locations

**Raw inputs (need to be updated manually when cloned):**
- `inputs/raw/` (contains the CSVs exactly as provided from the source)

**Generated Artifacts:**
- `outputs/`

## 3. Required CSV Files

The following files that need to be added manually must match filenames exactly and stored in the `inputs/raw/` folder of the project:
- `courses.csv`
- `assessments.csv`
- `vle.csv`
- `studentInfo.csv`
- `studentRegistration.csv`
- `studentAssessment.csv`
- `studentVle.csv`

## 4. Conventions

- Day 0 roughly aligns with the start of a presentation
- Negative values related to dates can occur (events before official start)
- Any engineered feature must use only records where the date is between the start day and the cutoff day (date)

## 5. Target label definition (3-class risk mapping)

- The outcome field (from `studentInfo.csv`) is used for the `final_result` (with options being *Distinction*, *Pass*, *Fail*, *Withdrawn*)

- Labels used for models are *Low Risk*, *Medium Risk*, *High Risk*.

### 5.1. Mapping
- *Low Risk*  is mapped to *Distinction* OR *Pass*
- *Medium Risk* = *Fail*
- *High Risk* = *Withdrawn*

## 6. Schema

### 6.1 File: `studentInfo.csv`
- Identifiers: `id_student`, `code_module`, `code_presentation`
- Demographics/context: `gender`, `region`, `highest_education`, `imd_band`, `age_band`, `disability`
- Academic context: `studied_credits`, `num_of_prev_attempts`
- Outcome label: `final_result` (post-horizon)

### 6.2 File: `studentRegistration.csv`
- Identifiers: `id_student`, `code_module`, `code_presentation`
- Timing: `date_registration`, `date_unregistration`

### 6.3 File: `assessments.csv`
- Keys: `id_assessment`, `code_module`, `code_presentation`
- Metadata: `assessment_type`, `date`, `weight`

### 6.4 `studentAssessment.csv` 
- Keys: `id_student`, `id_assessment`
- Submission timing: `date_submitted`
- Score: `score`

### 6.5 `vle.csv`
- Keys: `id_site`, `code_module`, `code_presentation`
- Activity label: `activity_type`

### 86.6 `studentVle.csv`
- Keys: `id_student`, `id_site`, `code_module`, `code_presentation`
- Timing: `date`
- Engagement: `sum_click`

### 6.7 `courses.csv`
Key columns:
- `code_module`, `code_presentation`, `module_presentation_length`

## 7. Preprocessing Rules

Standard steps:
- Missing value imputation:
  - numeric: median
  - categorical: most-frequent
- Encoding:
  - categorical: one-hot encoding with `handle_unknown="ignore"`
- Scaling (if used for certain models):
  - numeric: standard scaling (optional depending on model)
- Output is used consistently across CV and final test evaluation to avoid leakage.

## 8. Sensitive Features

### 8.1. Sensitive Details (Features)
- `gender`, `age_band`, `disability` (demographic information)
- `imd_band` (deprivation index band)
- `region` (geographic information)

### 8.2. Responsible Guidlines
- The proposed solution is meant to be used for for support only, not evaluation.
- If a sensitive feature is of critical importance in the model, only use if deemed safe within the provided context or exclude otherwise.

## 9. Known Limitations

- There is information that may be relevant to understanding patters observed that is not captured by the dataset.
- Different metrics used, such as engagement as a quantities value counting clicks, may not be ideal.
- Class distributions may be imbalanced, especially across different course topics and composition of learners that may change from one cohort to another.
- The dataset is limited to a specific organization and delivery style. Therefore, it may not represent the situation at a different organization.