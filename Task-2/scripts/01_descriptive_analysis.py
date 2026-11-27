
import pandas as pd
import os

# Dataset path
file_path = os.path.join(
    "Task-1", "output", "cleaned_dataset.xlsx"
)

# Load dataset
df = pd.read_excel(file_path)

# Create Task 2 reports folder if needed
os.makedirs("Task-2/reports", exist_ok=True)

# Dataset overview
print("\n========== DATASET OVERVIEW ==========")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
print("\nColumn Names:")
print(df.columns.tolist())

# Data types
print("\n========== DATA TYPES ==========")
print(df.dtypes)

# Statistical summary
print("\n========== DESCRIPTIVE STATISTICS ==========")
print(df.describe(include="all"))

# Missing values
print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# Business KPIs
print("\n========== SALES KPIs ==========")
print("Total Sales:", df["Total_Sales"].sum())
print("Total Quantity Sold:", df["Quantity"].sum())
print("Average Sales per Row:", df["Total_Sales"].mean())
print("Unique Customers:", df["Customer_ID"].nunique())
print("Unique Products:", df["Product"].nunique())

# Save descriptive statistics
df.describe(include="all").to_excel(
    "Task-2/reports/descriptive_statistics.xlsx"
)

# Save missing value report
df.isnull().sum().to_csv(
    "Task-2/reports/missing_values_report.csv"
)

print("\nReports saved successfully!")
