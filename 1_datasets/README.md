# Datasets

## Olumide Data Collection

### QCEW Data Preparation Summary

[QCEW Annual Avg Wage Cleaning Folder](./Users/user/Documents/mit_stuff/CDSP_GROUP_11/ET6-CDSP-group-11-repo/1_datasets/olumide_data_collection_folder/annual_avg_wage)

I collected annual data for 2020–2024 from the U.S. Bureau of Labor Statistics
Quarterly Census of Employment and Wages (QCEW). The dataset focuses on NAICS
541511, representing custom computer programming services in the U.S., which
broadly covers software engineering jobs. We downloaded separate CSV files for
each year from 2020 to 2024.

For each file, we added a `year` column to identify the calendar year, then
combined all annual files into a single DataFrame. After combining, we checked
the data's shape, columns, and missing values to ensure data integrity. We
found no missing values in our key columns, which confirmed the data was
reliable for analysis.

We then cleaned the dataset by removing irrelevant metadata columns.
We kept only these relevant columns: `year`, `annual_avg_estabs`
(the average number of establishments each year), `annual_avg_emplvl`
(average number of employees each year), and `annual_avg_wkly_wage`
(average weekly wage for employees each year). This simplified the dataset and
made it directly aligned with our research goals.

This data is relevant because it provides authoritative information on
employment levels and wage trends in the software engineering sector. It lets
us observe how employment and wages evolved from before the pandemic through
the post-pandemic tech boom and recent corrections. By tracking these variables
across multiple years, we can identify trends that may reveal how the software
engineering labor market has changed.

This matters to our research question because it allows us to analyze whether
structural barriers, hiring trends, or broader economic cycles might affect
early-career engineers, including recent immigrants. Our cleaned dataset
provides a concrete basis for answering questions like whether there has been a
slowdown in hiring, whether wages have stagnated or grown, and how industry
dynamics may impact opportunities for junior engineers.

You can explore the original data source at the Bureau of Labor Statistics
[QCEW Data Viewer](https://data.bls.gov/cew/apps/table_maker/v4/table_maker.htm#type=18&from=2020&to=2024&qtr=1&own=5&ind=541511&area=US000&supp=1)
