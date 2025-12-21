
## Deliverables

 - **Deliverable 1: Problem Definition** <br>Available as a markdown file report in `reports/01_problem_definition.md`.

 - **Deliverable 2: Jupyter Notebook** <br>Split across two Jupyter notebooks in the `/notebooks` folder. The first notebook `/notebooks/01_dataset_preprocessing.ipynb` handles the preprocessing of the data and inital steps for the model whereas the second notebook `/notebooks/02_models.ipynb` contains the solution implementation.

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

