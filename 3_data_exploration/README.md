# Data Exploration

This folder contains exploratory data analysis (EDA) notebooks and visual
outputs used to understand the cleaned dataset of U.S.-based software
engineers. This step is critical for uncovering basic patterns, identifying
anomalies, and guiding the next phase of analysis — without jumping into
predictive modeling or inferential statistics.

---

## Dataset Explored

- **Source**: `/1_datasets/software_engineers_employment_dataset_cleaned.csv`
- **Origin**: Cleaned extract from IPUMS USA (ACS microdata)
- **Content**: Individual-level demographic, employment, and wage data for
software engineers in tech industries.

---

## Notebook

### `/ET6-CDSP-group-11-repo/3_data_exploration/explore_software_engineers_dataset.ipynb`

This notebook is structured to:

1. **Load** the cleaned dataset
2. **Visualize** distributions and summary statistics
3. **Explore** demographic factors and their relationship with weekly earnings
4. **Document** all reasoning, insights, and open questions

No machine learning or statistical testing is performed in this notebook.

---

## Variables Explored

| Variable         | Description |
|------------------|-------------|
| `AGE`            | Age of respondent |
| `SEX`            | Gender (1 = Male, 2 = Female) |
| `RACE`           | Coded race categories |
| `EDUC`           | Education level (coded) |
| `OCC2010`        | Occupation code (filtered to 1020) |
| `IND`            | Industry (filtered to tech sectors) |
| `UHRSWORK`       | Hours worked per week |
| `INCWAGE`        | Annual wage income |
| `weekly_earnings`| Derived income per week: `INCWAGE / 52` |

---

## Visualizations Generated

1. **Distribution of Weekly Earnings**
   - Histogram with KDE overlay
   - Reveals earnings clustering and outliers

2. **Box Plot: Weekly Earnings by Gender**
   - Visual check for wage disparity between males and females

3. **Box Plot: Weekly Earnings by Education Level**
   - Helps examine how earnings relate to educational attainment

4. **Box Plot: Weekly Earnings by Race**
   - Initial view of potential disparities across race codes

---

## Key Insights from EDA

- **Weekly earnings** generally range from ~$600 to ~$2,500, with some
outliers above.
- **Gender gaps** in weekly earnings appear present in median and IQR values.
- **Education level** strongly correlates with earnings, but variance remains
within levels.
- **Racial disparities** exist, but deeper analysis is needed to interpret
them responsibly.
- No major missing data issues were found in this cleaned dataset.

---

## Ideas for Further Exploration

- Group-wise summary tables: mean/median weekly earnings
by `SEX`, `RACE`, `EDUC`
- Explore potential interaction effects (e.g., gender × education)
- Normalize weekly earnings by hours worked to derive a "true hourly wage"
- Encode and map categorical variables to meaningful labels
- Visualize multi-variable patterns using violin plots or swarm plots

---
