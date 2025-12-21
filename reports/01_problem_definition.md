# Deliverable 1 — Problem Definition (OULAD Early-Warning Classifier)

## 1. Background and motivation

Online and blended courses often have limited capacity for proactive support for learners who are struggling with the learning experience in the course. By the time a learner(student) has clearly disengaged, withdrew from the course, or fails a major assessment, it may be too late to intervene effectively. This project proposes an **early-warning classification model** that uses *early-course signals* (engagement + assessment behavior) to predict end-of-course risk tiers at **Week 8** which is a typical mid point for higher-education course offerings globally (about 50% of a semester).

In a previous project (*The Regression Challenge Capstone*), a regression solution based on the same dataset did not work as well as expected for identifying "at risk" students by predicting the final score and had some analytical gaps in the reporting.

**Intended Impact:**  
The model is designed to support *early supportive interventions*, such as:
- Targeted outreach (check-ins, guidance, and offering recommendations)
- Tutoring referrals
- Study planning support
- Resource recommendations
- Escalation to advisors for high-risk cases

> **Important Note:** <br>Predictions are framed for support, not punishment. The model is decision-support only and must be paired with human review and appropriate student services.

## 2. Classification Problem Statement

### 2.1. Framing (UNIT / EVENT / HORIZON / PREDICTION TIME)

Predict whether a **student in a given course** will fall into **Low / Medium / High risk** of course outcome **by end of course**, using data recorded up to **Week 8 (Day 56)**, so that course staff can **prioritize early supportive interventions** for learners most likely to need help.

### 2.2. The "Risk" Definition

This project defines risk as the **risk of not successfully completing the course**. We operationalize this as a **3-class label** derived from `final_result`:

1. **Low risk:** `Pass` or `Distinction` (which would be no risk) 
2. **Medium risk:** `Fail`  
3.  **High risk:** `Withdrawn`

This mapping creates a **risk severity ladder** where `Withdrawn` represents the highest risk outcome in terms of course non-completion.

## 3. Hypothesis

Early-course behavioral and performance signals available by a given day of the course (the models will use day 56), especially VLE engagement patterns and assessment performance, should contain enough signals to predict the 3-class risk tier better than a majority-class baseline.

## 4. Dataset Used

The [Open University Learning Analytics Dataset (OULAD)](https://www.kaggle.com/datasets/anlgrbz/student-demographics-online-education-dataoulad?resource=download) is an appropriate dataset for Week-8 early-warning classification because it contains:

1. **A clear outcome label**:<br>`final_result` in `studentInfo.csv` (end-of-course result)  
2. **Early engagement signals**:<br>clickstream interactions in `studentVle.csv` with a day-level timeline (`date`, `sum_click`)  
3. **Early performance signals**:<br>assessment events and scores (`assessments.csv`, `studentAssessment.csv`) with scheduled dates  
4. **Contextual features**:<br>demographics/background variables (`gender`, `age_band`, `highest_education`, `imd_band`, etc.) for modeling and auditing

These elements support a predictive capability as well as the ability to offer some interpretation based on accumulated industry experiecne (e.g., understanding whether disengagement or missed assessments drive risk). Furthermore, it is a transferable solution to other course providers (e.g., other universities and adult-education programs globally).

## 5. Inputs for the Solution

### 5.1. Required CSVs

The solution uses the following OULAD CSVs (stored locally in `inputs/raw/`):
- `studentInfo.csv` (primary student identifiers and demographics)
- `studentRegistration.csv` (registration data)
- `studentVle.csv` and `vle.csv` (engagement and activity in a course offering)
- `studentAssessment.csv` and `assessments.csv` (for assessment behavior and performance)
- `courses.csv` (course metadata)

Please see the Data Dictionary file (`DATA_DICTIONARY.md` in the repository root) and the 

### 5.2 Feature window (leakage-safe)
All engineered “behavior” and “performance” features must satisfy:

- **VLE features:** only events where `date <= 56`
- **Assessment features:** only assessments scheduled with `assessments.date <= 56` and any related submission/score data available up to that point

Examples of Week-8 feature families:
- total clicks, active days, mean/std daily clicks (consistency & stability)
- clicks by activity type (interpretability)
- number of assessments submitted by Day 56
- average score (where available) and weighted score summaries
- submission timing summaries (e.g., latest submission day ≤ 56)

### 5.3 Excluding “event already happened” cases
To preserve a realistic early-warning setup, enrolments that **unregistered on or before Day 56** are excluded, because the “non-completion pathway” has already occurred by prediction time.

> **Guarantee (no label leakage):** No features will be computed using events after Day 56, and enrolments already ended by Day 56 are removed.

---

## 6) Expected data challenges and planned handling

### 6.1 Class imbalance (likely)
`Withdrawn` is typically less frequent than `Pass/Distinction`, so we expect **class imbalance** (minority High Risk). This affects metric choice and may affect model training.

**Planned response:**
- prioritize **macro-averaged** evaluation (macro-F1) so minority classes matter
- report **balanced accuracy** and per-class metrics
- consider class-weighted models (e.g., `class_weight="balanced"`) as a default baseline
- optional: apply resampling only **inside CV folds** (never before splitting)

> **Guarantee (imbalance-aware evaluation):** We will not rely on accuracy alone; minority-class performance is explicitly measured and reported.

### 6.2 Missing values
Some engineered features may be missing (e.g., students with no early submissions). Missingness will be handled via a reproducible preprocessing pipeline:
- numeric imputation (median)
- categorical imputation (most frequent)

### 6.3 High-dimensional categorical features
Categorical variables (region, education, IMD band, etc.) require encoding:
- one-hot encoding (`handle_unknown="ignore"`) inside a pipeline

### 6.4 Potential proxies and fairness risks
Some variables may act as proxies for socioeconomic or demographic factors. This requires careful use and auditing (see Ethics section).

---

## 7) Model objective and success criteria (how we judge “good”)

### 7.1 Primary metric
- **Macro-F1** (primary): treats all classes equally, appropriate under imbalance

### 7.2 Secondary metrics
- **Balanced accuracy**
- **Per-class precision/recall/F1**, with emphasis on **High Risk (Withdrawn)** recall
- **Precision–Recall analysis (High Risk vs rest)** to support operational threshold decisions

### 7.3 Baseline requirement
- Compare against a **majority-class baseline** (DummyClassifier most_frequent) to ensure the model adds value.

**Success criteria (practical):**
- tuned models should meaningfully outperform the baseline on **macro-F1**
- demonstrate usable trade-offs for High Risk identification (PR curve) aligned with support capacity

---

## 8) Validation plan and experimental design (to avoid over-claiming)

- Use a **train/test split** with stratification to preserve class proportions
- Prefer **group-aware splitting by `id_student`** (so the same student does not appear in both train and test)
- Use **cross-validation on training only** for model selection and tuning
- Use the **test set once** for final reporting after selection

> **Guarantee (honest evaluation):** The test set is reserved for the final evaluation only.

---

## 9) Proposed modeling approach (high-level)

We will train and compare at least two model families:

1) **Logistic Regression (multinomial)**  
   - interpretable baseline  
   - supports class weights for imbalance

2) **Random Forest** (or other tree ensemble, if included)  
   - captures nonlinear patterns and feature interactions  
   - can handle mixed feature types after encoding

Hyperparameter tuning will be applied to **two models** using structured search (Grid/Randomized), and model selection will prioritize macro-F1 plus High Risk behavior.

---

## 10) Ethical considerations and mitigation plan

### 10.1 Risks
- **False negatives (High Risk predicted as Low/Medium):** students needing support may be missed  
- **False positives (Low/Medium predicted as High):** unnecessary outreach could burden staff and potentially stigmatize students  
- **Bias/fairness:** demographic/proxy variables could drive differential error rates across subgroups  
- **Misuse risk:** predictions could be used punitively rather than supportively

### 10.2 Mitigations
- Use the model for **support triage**, not punitive action
- Report per-class metrics and analyze High Risk PR trade-offs to set thresholds responsibly
- Conduct subgroup checks where possible (performance by demographic slices) and document limitations
- Consider excluding the most sensitive attributes from modeling if they dominate importance without clear justification
- Provide transparent interpretation artifacts (feature importances/coefficients)

> **Guarantee (responsible use):** The output is framed as *decision-support* with documented limitations and recommended safeguards.

---

## 11) Scope and non-goals

**In scope:**
- Week-8 early-warning prediction at the enrolment level
- 3-class risk tiering based on `final_result`
- leakage-safe feature engineering (≤ Day 56)
- model training, tuning, and evaluation with appropriate metrics

**Out of scope (for this capstone iteration):**
- real-time deployment, UI integration, or live intervention workflows
- causal claims (we do not claim features *cause* outcomes)
- personalized intervention recommendations (beyond risk triage)

---

## 12) How this deliverable connects to the rest of the solution

- **Deliverable 2 (Jupyter Notebooks):**
  - **Notebook 1:** data ingestion, leakage-safe Week-8 feature engineering, EDA (≥6 visuals + interpretation), preprocessing pipeline, train/test split artifacts
  - **Notebook 2:** baseline + 2 model families, CV evaluation, tuning for 2 models, final test evaluation, confusion matrix + PR/ROC + model interpretation artifacts

- **Deliverable 3 (Performance Report):**
  - non-technical summary referencing Notebook outputs (saved figures/tables), including ethical reflections and operational trade-offs

---
