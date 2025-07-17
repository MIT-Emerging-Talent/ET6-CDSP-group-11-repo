# Data Preparation

This folder contains the Jupyter notebook used to clean and process the raw
IPUMS USA dataset for our research question:

**What demographic factors influence median weekly earnings for software engineers
in the U.S. tech industry?**

---

## Notebook Included

### `/ET6-CDSP-group-11-repo/2_data_preparation/employment_dataset_cleaning_script.ipynb`

This notebook:

- Reads in the raw dataset `employment_dataset.csv` from `/1_datasets`
- Filters the data to include only:
  - **Software engineers** (OCC2010 == `1020`)
  - **Currently employed individuals** (EMPSTAT == `1`)
  - **Workers in tech-related industries**:
    - 7270 = Computer systems design
    - 7370 = Data processing & hosting
    - 7380 = Internet publishing/web portals
    - 7390 = Other information services
- Drops invalid or missing earnings/work hour entries
- Computes a derived `weekly_earnings` column using the formula:
This assumes full-year employment and provides a consistent earnings comparison.

- Selects relevant demographic and occupational fields for analysis
- Saves the cleaned output to `/1_datasets/software_engineers_cleaned.csv`

---

## Input & Output

- **Input file**:  
`/1_datasets/employment_dataset.csv`  
(Raw IPUMS extract)

- **Output file**:  
`/ET6-CDSP-group-11-repo/1_datasets/software_engineers_employment_dataset_cleaned.csv`
(Cleaned, analysis-ready dataset)

---

## Columns in Final Dataset

| Column           | Description |
|------------------|-------------|
| `AGE`            | Age of respondent |
| `SEX`            | 1 = Male, 2 = Female |
| `RACE`           | Race category (coded) |
| `EDUC`           | Educational attainment (coded) |
| `OCC2010`        | Occupation code (filtered to 1020) |
| `IND`            | Industry code (filtered to tech) |
| `EMPSTAT`        | Employment status (filtered to 1 = Employed) |
| `UHRSWORK`       | Usual hours worked per week |
| `INCWAGE`        | Annual wage income |
| `weekly_earnings`| Derived average weekly earnings (INCWAGE ÷ 52) |

---

## Notes

- The raw data is **not modified**; we write a new clean file.
- Weekly earnings are estimated — further accuracy can be added in future
iterations by including `WKSWORK1` if available.
- All processing steps are documented with Markdown cells in the notebook for
clarity and reproducibility.
