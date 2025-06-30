# More details Data Cleaning and Preparation Process

## Step 1

I downloaded annual CSV files from the U.S. Bureau of Labor Statistics (BLS)
Quarterly Census of Employment and Wages (QCEW) program. Each file contained
nationwide data for NAICS 541511 (Custom Computer Programming Services),
representing the software engineering industry in the U.S.

## Step 2

I read each year’s CSV file into pandas and added a `year` column to keep track
of the calendar year for each row.

## Step 3

I concatenated all yearly DataFrames into a single `all_data` DataFrame
covering 2020–2024, making it easy to analyze employment and wage trends across
multiple years.

## Step 4

I verified the shape of the combined DataFrame, confirmed column names and data
types, and ensured the `year` column was included. We checked for missing
values and confirmed there were no nulls in our key columns.

## Step 5

I reduced the dataset to only the essential columns relevant to our research:

- `year`: The calendar year.
- `annual_avg_estabs`: Average number of establishments (companies) per year.
- `annual_avg_emplvl`: Average employment levels (number of workers) per year.
- `annual_avg_wkly_wage`: Average weekly wage per worker per year.

By dropping irrelevant metadata and advanced benchmarking columns,
i simplified the dataset for clearer analysis.

---

### Why This Data is Relevant**

The QCEW dataset provides authoritative, government-collected data on
employment and wages, making it one of the most reliable labor market datasets
available in the U.S. By focusing on NAICS 541511, we are zeroing in on the
software engineering and custom programming sector, directly aligning with our
research question about labor dynamics in the tech industry.

Covering 2020–2024 allows us to observe how the industry evolved before,
during, and after the COVID-19 pandemic, including booms, corrections, and the
effects of tech hiring slowdowns and layoffs. This period also captures trends
relevant to junior engineers’ hiring prospects and wage growth.

---

### Aim with this analysis

Analysis aims to:

- Understand employment trends: Did the overall number of software engineers
grow, plateau, or decline over these years in the usa?
- Analyze wage trajectories: Did salaries steadily increase, experience spikes,
or stagnate?
- Contextualize these trends with significant industry events, such as:
  - The 2020–2021 tech hiring boom,
  - The 2022–2023 waves of layoffs,
  - Shifting demands due to AI and automation.

These insights will help answer key questions, including:

- Are opportunities for junior engineers shrinking or expanding?
- Did the industry undergo a market correction after rapid growth?
- How resilient are wages in tech during economic uncertainty?

---

### What Do the Key Columns Mean**

- `year`: Calendar year the data represents (2020–2024).
- `annual_avg_estabs`: Average number of business establishments operating in
custom programming services that year.
- `annual_avg_emplvl`: Average number of employees working in these
establishments that year, serving as a proxy for total jobs.
- `annual_avg_wkly_wage`: Average gross weekly wage per employee in USD,
helping us track wage growth or stagnation.

---

### Why This Matters**

This cleaned and combined dataset provides a strong foundation for analyzing
labor economics trends in the U.S. software engineering sector, which is
directly tied to our research focus on wage trajectories, employment stability,
and structural shifts affecting job opportunities. By establishing clear
patterns in employment levels and wage trends across the industry, this dataset
creates a baseline that can help us investigate potential disparities between
native-born and immigrant software engineers as we incorporate additional data
sources or conduct supplementary research. It enables us to contextualize
barriers that may uniquely affect recent immigrants, such as challenges with
credential recognition, access to networks, or biases in hiring, and assess how
these factors might influence wage outcomes compared to their native-born peers.

For reference, the original data source is publicly available on the Bureau of
Labor Statistics website:
[Website](https://data.bls.gov/cew/apps/table_maker/v4/table_maker.htm#type=18&from=2020&to=2024&qtr=1&own=5&ind=541511&area=US000&supp=1)
