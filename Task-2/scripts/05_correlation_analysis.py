
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load dataset
df = pd.read_excel("Task-1/output/cleaned_dataset.xlsx")

# Create visualization folder
os.makedirs("Task-2/visualization", exist_ok=True)

sns.set_theme(style="whitegrid")

# Select numeric columns
numeric_columns = [
    "Age",
    "Quantity",
    "Unit_Price",
    "Total_Sales"
]

numeric_df = df[numeric_columns]

# 1. Correlation matrix
correlation = numeric_df.corr()

print("\n========== CORRELATION MATRIX ==========")
print(correlation.round(2))

# Save correlation matrix
correlation.to_excel(
    "Task-2/reports/correlation_matrix.xlsx"
)

# 2. Correlation heatmap
plt.figure(figsize=(9, 6))
sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    linewidths=0.5
)
plt.title("Sales Dataset Correlation Heatmap")
plt.tight_layout()
plt.savefig("Task-2/visualization/correlation_heatmap.png")
plt.close()

# 3. Quantity vs Total Sales
plt.figure(figsize=(9, 5))
sns.scatterplot(
    data=df,
    x="Quantity",
    y="Total_Sales"
)
plt.title("Quantity vs Total Sales")
plt.tight_layout()
plt.savefig("Task-2/visualization/quantity_vs_sales.png")
plt.close()

# 4. Unit Price vs Total Sales
plt.figure(figsize=(9, 5))
sns.scatterplot(
    data=df,
    x="Unit_Price",
    y="Total_Sales"
)
plt.title("Unit Price vs Total Sales")
plt.tight_layout()
plt.savefig("Task-2/visualization/unit_price_vs_sales.png")
plt.close()

# 5. Pair plot
sns.pairplot(numeric_df)
plt.savefig("Task-2/visualization/pairplot.png")
plt.close()

print("\nCorrelation analysis completed successfully!")
