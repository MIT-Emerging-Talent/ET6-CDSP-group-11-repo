import matplotlib.pyplot as plt
import pandas as pd

# Load dataset
file_path = "/Users/user/Documents/mit_stuff/CDSP_GROUP_11/ET6-CDSP-group-11-repo/1_datasets/olumide_data_collection_folder/USAforeignworkerssalarydata.xlsx"
df = pd.read_excel(file_path, sheet_name=0)

# Filter software engineers
se_df = df[
    df["JOB_TITLE_SUBGROUP"].str.contains("software engineer", case=False, na=False)
].copy()

# Prepare year
se_df["case_year"] = pd.to_datetime(
    se_df["CASE_RECEIVED_DATE"], errors="coerce"
).dt.year
se_df["dec_year"] = pd.to_datetime(se_df["DECISION_DATE"], errors="coerce").dt.year
se_df["year"] = se_df["case_year"].fillna(se_df["dec_year"])

# Median salary by year
median_salary_by_year = se_df.groupby("year")["PAID_WAGE_PER_YEAR"].median().dropna()

# Median salary by education level (only rows with both fields present)
edu_salary_df = se_df[["EDUCATION_LEVEL_REQUIRED", "PAID_WAGE_PER_YEAR"]].dropna()
edu_median = (
    edu_salary_df.groupby("EDUCATION_LEVEL_REQUIRED")["PAID_WAGE_PER_YEAR"]
    .median()
    .sort_values(ascending=False)
)
edu_median_df = edu_median.reset_index().rename(
    columns={"PAID_WAGE_PER_YEAR": "Median Salary ($)"}
)

# Plot median salary trajectory
plt.figure(figsize=(8, 5))
median_salary_by_year.sort_index().plot(marker="o")
plt.title("Median PAID_WAGE_PER_YEAR for Immigrant Software Engineers (2008-2015)")
plt.xlabel("Year")
plt.ylabel("Median Salary ($)")
plt.tight_layout()
plt.show()
