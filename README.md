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

