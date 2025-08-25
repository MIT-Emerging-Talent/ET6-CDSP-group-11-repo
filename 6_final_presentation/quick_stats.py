import pandas as pd

# Load data
df = pd.read_csv('../data/wage_equity/wage_equity_data_20250820_151048.csv')

# Calculate key statistics
print("\nKey Statistics for Presentation:")
print("-" * 40)

# Gender statistics
gender_means = df.groupby('gender')['salary'].mean()
print("\nAverage Salary by Gender:")
for gender, salary in gender_means.items():
    print(f"{gender}: ${salary:,.2f}")

# Education statistics
edu_means = df.groupby('education_level')['salary'].mean().sort_values(ascending=False)
print("\nAverage Salary by Education (Top 3):")
for edu, salary in edu_means.head(3).items():
    print(f"{edu}: ${salary:,.2f}")

# Location statistics
loc_means = df.groupby('location')['salary'].mean().sort_values(ascending=False)
print("\nAverage Salary by Location:")
for loc, salary in loc_means.items():
    print(f"{loc}: ${salary:,.2f}")

print("\nSample Size:", len(df))
