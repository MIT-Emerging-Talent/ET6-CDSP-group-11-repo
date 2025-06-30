import pandas as pd

# Replace with your actual file path
file_path = "/Users/anna/Folder 1/CDSP/ET6-CDSP-group-11-repo/Data-6.csv"

# Read the first 1000 rows only
df = pd.read_csv(file_path, nrows=100)


df.drop(
    columns=[
        "Work activity during the reference year (4)",
        "UOM",
        "UOM_ID",
        "SCALAR_FACTOR",
        "SCALAR_ID",
        "VECTOR",
        "COORDINATE",
        "STATUS",
        "SYMBOL",
        "TERMINATED",
        "DECIMALS",
    ],
    inplace=True,
)

# Display basic info
print(df.head())
print(df.tail(10))

# print(df.columns)

df.to_csv(
    "/Users/anna/Folder 1/CDSP/ET6-CDSP-group-11-repo/cleaned_file.csv", index=False
)
