
from pathlib import Path
import pandas as pd

# Locate the project folder and CSV file
project_folder = Path(__file__).resolve().parent.parent
file_path = project_folder / "data" / "Telco-Customer-Churn.csv"

# Check that the file exists
if not file_path.exists():
    raise FileNotFoundError(
        f"CSV not found at: {file_path}\n"
        "Check the filename and data folder."
    )

# Load the dataset
df = pd.read_csv(file_path)

# Display basic information
print("\n--- FIRST 5 CUSTOMERS ---")
print(df.head())

print("\n--- DATASET SIZE ---")
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

print("\n--- COLUMN NAMES ---")
print(df.columns.tolist())

print("\n--- DATA TYPES ---")
print(df.dtypes)

print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

print("\n--- CHURN COUNTS ---")
print(df["Churn"].value_counts(dropna=False))

print("\n--- DUPLICATE ROWS ---")
print(df.duplicated().sum())

churned = (df["Churn"] == "Yes").sum()
total = len(df)
churn_rate = (churned / total) * 100

print("\n--- OVERALL CHURN RATE ---")
print(f"Churned customers: {churned}")
print(f"Total customers: {total}")
print(f"Churn rate: {churn_rate:.2f}%")
