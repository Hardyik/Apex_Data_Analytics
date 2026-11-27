
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load cleaned dataset
df = pd.read_excel("Task-1/output/cleaned_dataset.xlsx")

# Create visualization folder
os.makedirs("Task-2/visualization", exist_ok=True)

sns.set_theme(style="whitegrid")

# 1. Sales distribution
plt.figure(figsize=(9, 5))
sns.histplot(df["Total_Sales"], bins=30, kde=True)
plt.title("Distribution of Total Sales")
plt.xlabel("Total Sales")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("Task-2/visualization/sales_distribution.png")
plt.close()

# 2. Revenue by category
category_sales = df.groupby("Category")["Total_Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(9, 5))
sns.barplot(x=category_sales.index, y=category_sales.values)
plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("Task-2/visualization/sales_by_category.png")
plt.close()

# 3. Revenue by product
product_sales = df.groupby("Product")["Total_Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 5))
sns.barplot(x=product_sales.index, y=product_sales.values)
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("Task-2/visualization/sales_by_product.png")
plt.close()

# 4. Customer age distribution
plt.figure(figsize=(9, 5))
sns.histplot(df["Age"], bins=15, kde=True)
plt.title("Customer Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("Task-2/visualization/customer_age_distribution.png")
plt.close()

# 5. Sales by gender
gender_sales = df.groupby("Gender")["Total_Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(7, 5))
sns.barplot(x=gender_sales.index, y=gender_sales.values)
plt.title("Total Sales by Gender")
plt.xlabel("Gender")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("Task-2/visualization/sales_by_gender.png")
plt.close()

print("All 5 visualizations generated successfully!")

print("\nRevenue by Category:")
print(category_sales)

print("\nRevenue by Product:")
print(product_sales)
