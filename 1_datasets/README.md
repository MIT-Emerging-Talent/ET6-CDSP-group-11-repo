# Datasets: Software Engineer Earnings Analysis

This folder contains the **raw and processed datasets** used for our research:  
**“What demographic factors influence median weekly earnings for software
engineers in the U.S. tech industry?”**

Our goal is to explore how demographic variables such as age, gender, race,
and education correlate with wage outcomes for software engineers working in
tech-focused industries across the U.S.

---

## Dataset Summary

Upcoming..

## Source

- **Source**: [IPUMS USA](https://usa.ipums.org/usa/)
- **Data**: American Community Survey (ACS) Public Use Microdata
Sample (PUMS), 2020–2023
- **Extraction Tool**: IPUMS online extract system
- **License**: Public-use data provided by the U.S. Census Bureau and
harmonized by the Minnesota Population Center

---

## Variables Included

The following variables were selected to support our analysis:

- **OCC2010** – Occupation (filtered for code 1106: Software Developers)
- **IND** – Industry (limited to tech-related codes: 7270, 7370, 7380, etc.)
- **INCWAGE** – Annual income from wages
- **UHRSWORK** – Usual hours worked per week
- **WKSWORK1** – Weeks worked last year
- **SEX**, **AGE**, **RACE**, **EDUC** – Demographic indicators
- **EMPSTAT** – Employment status (filtered for employed individuals)
- **CLASSWKR** – Class of worker (optional for public/private sector
comparisons)

---

## Data Types

- **Quantitative (Continuous)**: Weekly earnings, age
- **Quantitative (Discrete)**: Weeks worked, hours worked
- **Qualitative (Categorical)**: Gender, race, education level, industry,
occupation
- **Structured format**: Tabular data (CSV files)

---

## Data Collection Method

- **Secondary observational data**
- Collected through the U.S. Census Bureau’s ACS annual surveys
- Individuals self-report employment and income information
- Harmonized by IPUMS for longitudinal and cross-sectional analysis

---

## Ethical Use

This dataset contains **no personally identifiable information (PII)**.
It is safe for public research. All analysis is conducted in line with the
data use agreement from IPUMS USA.

---

## Future Use

If time permits, we plan to expand the dataset by:

- Incorporating more ACS years (e.g., 2015–2023) for trend analysis
- Adding birthplace and citizenship fields to analyze immigrant status
- Linking geographic indicators to explore regional wage variation
