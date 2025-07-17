# Domain Study: Wage Disparities in U.S. Software Engineering

## Research Question

**What demographic factors influence median weekly earnings for software
engineers in the U.S. tech industry?**

This project aims to explore how characteristics like gender, age, education,
and race affect pay within a high-growth occupation like software engineering
using publicly available U.S. Census data.

---

## Why This Question?

Our initial goal was to explore wage disparities between **immigrant** and
**native-born** software engineers. However, after examining data sources such
as the Bureau of Labor Statistics (BLS) and the American Community Survey (ACS)
we found that
**immigration status is not directly reported at the occupation level in most datasets**.

To make the project feasible within our timeline and toolset, we revised our
research question to focus on
**demographics that are more readily available and still meaningful**,
while keeping the core theme of pay equity in tech.

---

## Data Source and Feasibility

We are using **IPUMS USA**, which provides harmonized ACS microdata suitable
for individual-level wage analysis. It allows us to filter for:

- **Software Engineers** using *OCC2010* codes
- **Tech industry roles** using *IND* codes
- **Earnings** via *INCWAGE*
- **Demographics** like *SEX*, *RACE*, *AGE*, *EDUC*

These variables are sufficient to explore our research question using Python
for data science with straightforward filtering and cleaning processes.

---

## Key Concepts Covered in This Domain

- **Occupational wage gaps**
- **Workforce equity in STEM**
- **Demographic trends in tech employment**
- **Public microdata usage (ACS/IPUMS)**
- **Measuring labor market outcomes**

---

## How This Can Scale

If time and resources allow, this research can be extended by:

- Including **foreign-born status** using *BPL* and *CITIZEN*
- Comparing wage growth **over multiple years** using pooled ACS data (e.g., 2018–2023)
- Adding geographic analysis (e.g., by region or metro area)
- Conducting regression analysis to identify **statistical significance** of
observed gaps

These extensions would provide deeper insight into structural inequities in
tech and inform policy or hiring practices.

---

## Useful Resources and Notes

This folder contains:

- Summaries of ACS and IPUMS variable definitions
- Links to IPUMS documentation
- Notes on industry codes relevant to tech
- Definitions of *OCC2010* codes related to software development
- Any external PDFs or articles that contextualize wage equity in tech

For further exploration, see [IPUMS USA](https://usa.ipums.org/usa/) and [ACS PUMS](https://www.census.gov/programs-surveys/acs/microdata.html).
