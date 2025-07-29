# Data Analysis README

## Goal of This Folder

This folder contains the scripts and notebooks used to derive **insights**
from our cleaned dataset of U.S. software engineers, with a focus on
understanding **the relationship between education and weekly earnings**.
The goal is to support our research question with **statistical evidence**,
making use of appropriate **inferential methods** to move beyond
surface-level trends.

---

## Research Question

**How does educational attainment affect weekly earnings among software
engineers in the United States?**

This research question seeks to evaluate whether increased education
(measured via the `EDUC` code) corresponds to a **statistically significant**
increase in earnings (`weekly_earnings`). This has practical implications for
career planning, policy-making, and economic mobility within the software
engineering profession.

---

## Dataset Used

- **Name:** `/ET6-CDSP-group-11-repo/1_datasets/software_engineers_employment_dataset_cleaned.csv`
- **Source:** IPUMS-USA (ACS microdata)
- **Fields Used for Analysis:**
  - `EDUC` – Educational attainment (ordinal categorical variable)
  - `weekly_earnings` – Computed as income divided by usual hours worked
  - `AGE`, `SEX`, `RACE`, `OCC2010`, `IND`, `EMPSTAT`, etc.
  (used for control or subgroup analysis)

---

## Analysis Strategy

We explore the central relationship between education and earnings using
multiple techniques to build confidence in our findings:

### 1. **Descriptive Analysis**

- **What we did**: Computed group-level statistics such as **mean**,
**median**, and **standard deviation** of `weekly_earnings` for each
`EDUC` level.
- **Why**: This gives an overview of the **earning trajectory** across
education levels, identifying any initial signal of correlation.
- **Limitations**: Descriptive stats do not establish causality or control
for confounding variables like age or industry.

### 2. **Group-wise Boxplots**

- **What we did**: Plotted `weekly_earnings` distribution for each education
level using boxplots.
- **Why**: Boxplots reveal **median trends**, **outliers**, and
**earning dispersion** within groups.
- **Technical note**: Since `EDUC` is ordinal, visualizing it on the x-axis
helps us observe increasing or plateauing patterns.
- **Non-technical takeaway**: We’re asking: “Does higher education usually mean
more pay—and how much more?”

### 3. **Analysis of Variance (ANOVA)**

- **What we did**: Ran a one-way ANOVA to test if
**at least one education group** differs significantly in mean weekly earnings.
- **Why**: ANOVA is the right test when comparing means across more than
two groups.
- **Interpretation**: A significant p-value supports the hypothesis that
**education level affects earnings**.
- **Limitations**: Assumes normally distributed groups with equal variances.

### 4. **Linear Regression**

- **What we did**: Attempted a basic linear regression model with
`weekly_earnings ~ EDUC`.
- **Why**: To test if the effect of education on earnings is **predictable**
and **linear**.
- **Issue**: `statsmodels` library had system issues. We decided not to rely on
this and instead leaned on visual + ANOVA.
- **Alternative approach**: Grouped averages + confidence intervals to sketch a
manual trendline.

---

## Key Findings (So Far)

- **Earnings generally increase with education**, but the jump from bachelor’s
to master’s or PhD shows **diminishing returns**.
- The **spread of earnings widens** at higher education levels, suggesting
**greater earning potential** but also more variability.
- Early education levels (e.g., high school or some college) show more
**consistency** but lower ceilings.

## Additional Gender & Race Wage Findings

### Gender Wage Differences (No Education Control)

- Men earn **on average $499 more per week** than women (**p < 0.001**).  
- This represents roughly **23% higher earnings** for men compared to women.  
- Gender alone explains **~1% of earnings variation (R² = 0.011)**, indicating
that other factors (education, experience, location, industry) also strongly
influence wages.

### Gender Wage Differences by Education

- **Gender wage gaps persist at most education levels**, with men generally
earning more than women.  
- At **Bachelor** and **Graduate+** levels, men’s earnings are substantially
higher, while some lower education levels (e.g., Grade 9) show unexpected
patterns likely due to small sample sizes.  
- The interaction between **education and gender** is statistically significant,
indicating that **returns to education differ by gender**.

### Race and Education Interactions

- Education raises earnings across all race groups, but **returns vary by race**.
- Some groups (e.g., “Other race”, “Three+ races”) show unusually high earnings
in specific categories, likely due to **small sample sizes or outliers**.  
- No strong statistical evidence was found that race alone changes the effect
of education dramatically, but outlier patterns suggest further investigation
is needed.

---

## Interpretation and Relevance

This analysis is **highly relevant** to our broader study of
**career mobility and wage equity** in software engineering:

- If education has **strong influence**, then policies promoting access to
education may **narrow wage gaps**.
- If the influence is **limited**, then other factors like
**skills, location, or experience** might matter more—and should be
explored next.
- For immigrants or underrepresented groups, this insight can guide
**career decisions** and inform the **ROI of further education**.

---

## Next Steps

- Explore **interaction effects** between education and other variables
(like race or gender).
- Investigate **non-linear models** or **multivariate regression**
if library issues are resolved.
- Continue building toward a comprehensive answer that can
**stand up to scrutiny** and inform **policy or career advice**.

---

## Scripts and Notebooks

`/ET6-CDSP-group-11-repo/4_data_analysis/software_engineering_dataset_analysis.ipynb`
`/ET6-CDSP-group-11-repo/4_data_analysis/educ_gender_analysis.ipynb`  
`/ET6-CDSP-group-11-repo/4_data_analysis/gender_analysis.ipynb`
