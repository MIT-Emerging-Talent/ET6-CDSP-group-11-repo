# Improved Data Modeling Slide Content

## Data Modeling Strategy

### What We Measured in the Real World

**Target Phenomenon:** Wage equity patterns in software engineering careers

- **Primary outcome:** Annual earnings across demographic groups
- **Key predictors:** Education level, gender, race/ethnicity, experience
- **Contextual factors:** Employment status, industry sector, career progression

### Data Sources Used

**Primary Dataset:** Software Engineers Employment Dataset (2019-2023)

- **Source:** Government employment surveys and industry reports
- **Sample size:** [Your actual sample size]
- **Coverage:** Software engineering roles across multiple companies/regions
- **Time period:** 2019-2021 and 2022-2023 employment data

### Data Modeling Limitations and Flaws

#### 1. **Cross-Sectional Design Limitations**

- **Issue:** No longitudinal tracking of individual career progression
- **Impact:** Cannot establish causal relationships, only associations
- **Example:** Can't determine if education directly causes higher wages
or if other factors mediate this relationship

#### 2. **Missing Contextual Variables**

- **Issue:** Key variables not captured in available data
- **Missing factors:**
  - Company size and industry subsector
  - Geographic location and cost of living
  - Specific job roles and responsibilities
  - Years of experience and career level
- **Impact:** Unmeasured confounding may bias results

#### 3. **Sample Representation Issues**

- **Issue:** Some demographic groups underrepresented
- **Specific concerns:**
  - Smaller sample sizes for certain race/ethnicity combinations
  - Potential selection bias in who responds to employment surveys
  - May not represent startup vs. large corporation differences
- **Impact:** Less reliable estimates for underrepresented groups

#### 4. **Temporal Validity**

- **Issue:** Rapid changes in tech industry compensation
- **Concerns:**
  - COVID-19 impact on remote work and compensation
  - Recent AI boom affecting certain roles disproportionately
  - Market volatility in tech sector 2019-2023
- **Impact:** Findings may not reflect current market conditions

#### 5. **Measurement Precision**

- **Issue:** Self-reported earnings data potential inaccuracies
- **Concerns:**
  - Total compensation vs. base salary differences
  - Stock options and equity compensation not captured
  - Benefits and non-monetary compensation excluded
- **Impact:** May underestimate true compensation disparities

### Sources of Uncertainty

#### Statistical Uncertainty

- **Confidence intervals:** All estimates include measurement error
- **Sample variability:** Results may vary with different samples
- **Model selection:** Different analytical approaches may yield different results

#### Methodological Uncertainty

- **Variable definitions:** How we categorize education, experience, etc.
- **Outlier handling:** Decisions about extreme values affect results
- **Interaction effects:** Complex relationships between variables may be oversimplified

#### External Validity

- **Generalizability:** Do findings apply to other time periods?
- **Industry evolution:** How do rapid tech changes affect applicability?
- **Geographic scope:** Do patterns hold across different regions/markets?

## How These Limitations Inform Our Analysis Strategy

Based on these modeling constraints, we designed our analysis to:

1. **Acknowledge uncertainty** through confidence intervals and sensitivity
testing
2. **Test robustness** by examining results with and without outliers
3. **Use multiple methods** (t-tests, ANOVA, regression) to triangulate
findings
4. **Focus on patterns** rather than precise causal claims
5. **Recommend pilot testing** before large-scale implementation

---

## Your Original Content (Now Belongs in Analysis Strategy)

### Analysis Strategy

- Using t-test, ANOVA to examine earnings differences
- Applied robust regression analysis to control for different factors  
- Conducted sensitivity analysis to validate findings with or without outliers
- Multiple analytical approaches to ensure robustness of findings

---

## Key Takeaway

**Data Modeling** = What you're trying to measure in the real world and how
well your data captures it
**Analysis Strategy** = What statistical methods you used to analyze that data
