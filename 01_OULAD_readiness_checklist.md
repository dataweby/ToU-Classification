# OULAD Dataset Readiness Checklist

| Check | What to Look For? | OULAD notes |
|---|---|---|
| 1. Alignment | Do the classes match your framed problem? | Yes.<br>OULAD includes `studentInfo.final_result` (a final outcome per student–module–presentation), which the 3-tier “risk of not successfully completing the course” label can be derived from it.
| 2. Label veracity | Who labelled the data? Experts, crowd, or automated scripts? | Labels are institutional/administrative outcomes from the Open University data warehouse (not crowdsourced). |
| 3. Scale | Enough examples per class? (≥50 per class is a pilot minimum) | OULAD is large overall (tens of thousands of student-module-presentation records), so it meets the scale with a large enouhg cutoff date (a period reviewed for early assessments). |
| 4. Class balance | Are labels skewed? Will you need to re-sample? | Expecting imbalance (assming most students pass). |
| 5. File integrity | Sample 1% through previews; check for broken or corrupted files | No issues identified. |
| 6. Documentation | Is there a README, data dictionary, and license? | Source documentation exists (table schemas/column descriptions) and OULAD is distributed with a clear open license (CC BY 4.0). Details are copied into the `README.md` file and the features listed in the `DATA_DICTIONARY.md` file. |
| 7. Ethics | Any sensitive content? Faces, personal info, endangered species locations? | No faces/media, but there are some potentially sensitive attributes (e.g., gender, age band, region, disability, deprivation band). Those are regarded as sensitive. |
| 8. Access hurdles | IRB approval, API key, or license restrictions (e.g. non-commercial use)? | Public download and open license with from Kaggle. |