
from pathlib import Path
import pandas as pd

# Locate the project folder
project_folder = Path(__file__).resolve().parent.parent

# Load the cleaned dataset
file_path = project_folder / "data" / "Telco-Customer-Churn-Cleaned.csv"
df = pd.read_csv(file_path)

# Convert Churn into a numeric indicator
df["ChurnFlag"] = (df["Churn"] == "Yes").astype(int)

# 1. Overall churn rate
print("\n--- OVERALL CHURN ---")
print(f"Total customers: {len(df)}")
print(f"Churned customers: {df['ChurnFlag'].sum()}")
print(f"Overall churn rate: {df['ChurnFlag'].mean() * 100:.2f}%")

# 2. Churn by contract type
print("\n--- CHURN BY CONTRACT TYPE ---")
contract_analysis = (
    df.groupby("Contract")
    .agg(
        Customers=("ChurnFlag", "size"),
        Churned=("ChurnFlag", "sum"),
        ChurnRate=("ChurnFlag", "mean")
    )
    .reset_index()
)
contract_analysis["ChurnRate"] *= 100
print(contract_analysis.round(2).to_string(index=False))

# 3. Churn by payment method
print("\n--- CHURN BY PAYMENT METHOD ---")
payment_analysis = (
    df.groupby("PaymentMethod")
    .agg(
        Customers=("ChurnFlag", "size"),
        Churned=("ChurnFlag", "sum"),
        ChurnRate=("ChurnFlag", "mean")
    )
    .reset_index()
)
payment_analysis["ChurnRate"] *= 100
print(payment_analysis.round(2).to_string(index=False))

# 4. Save the results
reports_folder = project_folder / "reports"
reports_folder.mkdir(exist_ok=True)

contract_analysis.to_csv(
    reports_folder / "churn_by_contract.csv", index=False
)
payment_analysis.to_csv(
    reports_folder / "churn_by_payment.csv", index=False
)

print("\nAnalysis complete. Results saved in the reports folder.")
