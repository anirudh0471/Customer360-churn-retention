
from pathlib import Path
import pandas as pd

# Find the project folder
project_folder = Path(__file__).resolve().parent.parent

# File locations
input_file = project_folder / "data" / "Telco-Customer-Churn.csv"
output_file = project_folder / "data" / "Telco-Customer-Churn-Cleaned.csv"

# Load the original data
df = pd.read_csv(input_file)

print("\n--- STEP 1: ORIGINAL DATA ---")
print("Rows and columns:", df.shape)

# Check customer IDs
print("\n--- STEP 2: CUSTOMER ID CHECK ---")
print("Missing customer IDs:", df["customerID"].isna().sum())
print("Duplicate customer IDs:", df["customerID"].duplicated().sum())

# Check TotalCharges before cleaning
print("\n--- STEP 3: TOTAL CHARGES BEFORE CLEANING ---")
print("Original data type:", df["TotalCharges"].dtype)

blank_charges = df["TotalCharges"].astype(str).str.strip().eq("").sum()
print("Blank TotalCharges values:", blank_charges)

# Convert text to numbers; invalid or blank values become missing
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"].astype(str).str.strip(),
    errors="coerce"
)

print("\n--- STEP 4: AFTER CONVERSION ---")
print("New data type:", df["TotalCharges"].dtype)
print("Missing TotalCharges values:", df["TotalCharges"].isna().sum())

# Investigate affected customers
print("\n--- STEP 5: CUSTOMERS WITH MISSING TOTAL CHARGES ---")
print(
    df.loc[
        df["TotalCharges"].isna(),
        ["customerID", "tenure", "MonthlyCharges", "TotalCharges", "Churn"]
    ].head(10)
)

# Check duplicate full rows
print("\n--- STEP 6: DUPLICATE ROWS ---")
print("Duplicate rows:", df.duplicated().sum())

# Save a separate cleaned copy
df.to_csv(output_file, index=False)

print("\n--- STEP 7: FILE SAVED ---")
print(output_file)
print("Final rows and columns:", df.shape)
