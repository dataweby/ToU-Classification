# Deliverable 1:<br>**Problem Definition**

## 1. Background

Online and blended courses often have limited capacity for proactive support for learners who are struggling with the learning experience in the course. By the time a learner(student) has clearly disengaged, withdrew from the course, or fails a major assessment, it may be too late to intervene effectively. This project proposes an **early-warning classification model** that uses *early-course signals* (engagement + assessment behavior) to predict end-of-course risk tiers at **Week 8** which is a typical mid point for higher-education course offerings globally (about 50% of a semester).

In a previous project (*The Regression Challenge Capstone*), a regression solution based on the same dataset did not work as well as expected for identifying "at risk" students by predicting the final score and had some analytical gaps in the reporting.

**Intended Impact:**  
The model is designed to support *early supportive interventions*, such as:
- Targeted outreach (check-ins, guidance, and offering recommendations)
- Tutoring referrals
- Study planning support
- Resource recommendations
- Escalation to advisors for high-risk cases

> **Important Note:** <br>Predictions are framed for support, not evaluation or penalization. The model is decision-support only and must be paired with human review and appropriate student services.

## 2. Classification Problem Statement

### 2.1. Framing (UNIT / EVENT / HORIZON / PREDICTION TIME)

Predict whether a **student in a given course** will fall into **Low / Medium / High risk** of course outcome **by end of course**, using data recorded up to **a cutoff date (Day 98)**, so that course staff can **prioritize early supportive interventions** for learners most likely to need help.

### 2.2. The "Risk" Definition

This project defines risk as the **risk of not successfully completing the course**, to create a system of risk tiers. The risk will be mapped as a **3-class label** derived from `final_result` creating three tiers:

1. **Low risk:** `Pass` or `Distinction` (which would be no risk) 
2. **Medium risk:** `Fail`  
3.  **High risk:** `Withdrawn`

This mapping creates a **risk severity ladder** where `Withdrawn` represents the highest risk outcome in terms of course non-completion.

### 2.3. Concerns

The "Withdrawn" outcome for a student may be less predictable than assumed since there are many possible reasons for that that go beyond performance or the basic demographics that are captured in the dataset.

## 3. Hypothesis

Early-course behavioral and performance signals available by a given day of the course (the models will use day 98 since it's 14 weeks and less than half the duration for all courses in the dataset), especially VLE engagement patterns and assessment performance, should contain enough signals to predict the 3-class risk tier better than a majority-class baseline.

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

### 5.2. Range

All relevant features must satisfy:

- **VLE features:** only events where the date is before the cutoff (number of days)
- **Assessment features:** only assessments scheduled where the date is before the cutoff (number of days) and any related submission data available up to that point
- To preserve a realistic early-warning setup, enrolment that unregistered before the cutoff are excluded, because the “non-completion pathway” has already occurred by prediction time.

## 6. Data Handling

### 6.1. Class Imbalance
It is likley that some outcomes are less frequent than others. This should be identifed and addressed.

### 6.2. Missing values
Some features may be missing. Missing values will be handled via a reproducible preprocessing pipeline:
- numeric imputation (median)
- categorical imputation (most frequent)

An initial exploration revealed over 80% of the records in the virtual learning environment are missing values for the *week_from* and *week_from* columns.

### 6.3. Use of Categorical features
Categorical variables (region, education, IMD band, etc.) require encoding:
- one-hot encoding (`handle_unknown="ignore"`) inside a pipeline

## 7. Success Criteria

### 7.1 Primary
- **Macro-F1** since it treats all classes equally and can be a good fit when there is a class imbalance.

### 7.2 Secondary
- **Per-class precision/recall/F1**, with emphasis on **High Risk (Withdrawn)** recall
- **Precision–Recall analysis (High Risk vs rest)** to support operational threshold decisions

## 8. Validation Plan

- Use a **train/test split** with stratification to preserve class proportions
- Use **cross-validation on training only** for model selection and tuning
- Use the **test set once** for final reporting after selection

## 9. Approach

Train and compare at least two model families:

1. **Logistic Regression** <br>
   Since it is interpretable baseline and supports class weights for imbalance

2. **Random Forest**
   Since it should be able to handle mixed feature types after encoding.

Hyperparameter tuning will be applied.

## 10. Ethical Considerations

- **False negatives (High Risk predicted as Low/Medium):** will lead to students needing support may be missed.
- **False positives (Low/Medium predicted as High):** will lead to unnecessary outreach and trust erosion (in the solution and organization).  
- **Bias:** demographic/proxy variables could drive differential error rates across subgroups. 