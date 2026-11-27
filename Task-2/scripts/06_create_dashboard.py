
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load dataset
df = pd.read_excel("Task-1/output/cleaned_dataset.xlsx")

# Create dashboard folder
os.makedirs("Task-2/dashboard", exist_ok=True)

# Prepare dashboard data
total_revenue = df["Total_Sales"].sum()
total_quantity = df["Quantity"].sum()
total_customers = df["Customer_ID"].nunique()
total_products = df["Product"].nunique()

category_sales = (
    df.groupby("Category")["Total_Sales"]
    .sum().sort_values(ascending=False)
)

monthly_sales = (
    df.assign(Month=pd.to_datetime(df["Order_Date"]).dt.to_period("M").astype(str))
    .groupby("Month")["Total_Sales"].sum()
)

product_sales = (
    df.groupby("Product")["Total_Sales"]
    .sum().sort_values(ascending=False).head(5)
)

# Dashboard layout
sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(2, 2, figsize=(16, 10))
fig.suptitle("APEXPLANET SALES PERFORMANCE DASHBOARD",
             fontsize=19, fontweight="bold")

# KPI summary
kpi_text = (
    f"TOTAL REVENUE\n{total_revenue:,.2f}\n\n"
    f"QUANTITY SOLD\n{total_quantity:,}\n\n"
    f"UNIQUE CUSTOMERS\n{total_customers:,}\n\n"
    f"UNIQUE PRODUCTS\n{total_products:,}"
)

axes[0, 0].axis("off")
axes[0, 0].text(
    0.5, 0.5, kpi_text,
    ha="center", va="center",
    fontsize=17, fontweight="bold"
)

# Revenue by category
category_sales.plot(kind="bar", ax=axes[0, 1])
axes[0, 1].set_title("Revenue by Category")
axes[0, 1].set_xlabel("Category")
axes[0, 1].set_ylabel("Revenue")
axes[0, 1].tick_params(axis="x", rotation=25)

# Monthly revenue
monthly_sales.plot(kind="line", marker="o", ax=axes[1, 0])
axes[1, 0].set_title("Monthly Revenue Trend")
axes[1, 0].set_xlabel("Month")
axes[1, 0].set_ylabel("Revenue")
axes[1, 0].tick_params(axis="x", rotation=30)

# Top products
product_sales.plot(kind="bar", ax=axes[1, 1])
axes[1, 1].set_title("Top 5 Products by Revenue")
axes[1, 1].set_xlabel("Product")
axes[1, 1].set_ylabel("Revenue")
axes[1, 1].tick_params(axis="x", rotation=25)

plt.tight_layout(rect=[0, 0, 1, 0.94])

# Save dashboard
plt.savefig(
    "Task-2/dashboard/sales_dashboard.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Dashboard created successfully!")
print("Saved: Task-2/dashboard/sales_dashboard.png")
