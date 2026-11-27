
import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.chart import BarChart, LineChart, Reference
from openpyxl.utils import get_column_letter
import os

df = pd.read_excel("Task-1/output/cleaned_dataset.xlsx")

os.makedirs("Task-2/dashboard", exist_ok=True)

# Prepare dashboard data
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

kpis = [
    ["KPI", "Value"],
    ["Total Revenue", df["Total_Sales"].sum()],
    ["Total Quantity Sold", df["Quantity"].sum()],
    ["Unique Customers", df["Customer_ID"].nunique()],
    ["Unique Products", df["Product"].nunique()]
]

category = df.groupby("Category", as_index=False)["Total_Sales"].sum()
category.columns = ["Category", "Revenue"]
category = category.sort_values("Revenue", ascending=False)

product = df.groupby("Product", as_index=False)["Total_Sales"].sum()
product.columns = ["Product", "Revenue"]
product = product.sort_values("Revenue", ascending=False)

df["Month"] = df["Order_Date"].dt.to_period("M").astype(str)
monthly = df.groupby("Month", as_index=False)["Total_Sales"].sum()
monthly.columns = ["Month", "Revenue"]

# Create workbook
wb = Workbook()
ws = wb.active
ws.title = "Dashboard"

ws["A1"] = "APEXPLANET SALES PERFORMANCE DASHBOARD"
ws["A1"].font = Font(size=18, bold=True, color="FFFFFF")
ws["A1"].fill = PatternFill("solid", fgColor="17365D")
ws.merge_cells("A1:D1")

# KPI section
for row in kpis:
    ws.append(row)

# Category data
start = 9
ws.cell(start, 1, "Revenue by Category")
ws.cell(start + 1, 1, "Category")
ws.cell(start + 1, 2, "Revenue")

for i, row in enumerate(category.itertuples(index=False), start + 2):
    ws.cell(i, 1, row[0])
    ws.cell(i, 2, float(row[1]))

# Product data
product_start = 9
ws.cell(product_start, 4, "Revenue by Product")
ws.cell(product_start + 1, 4, "Product")
ws.cell(product_start + 1, 5, "Revenue")

for i, row in enumerate(product.itertuples(index=False), product_start + 2):
    ws.cell(i, 4, row[0])
    ws.cell(i, 5, float(row[1]))

# Monthly data
month_start = 20
ws.cell(month_start, 1, "Monthly Revenue")
ws.cell(month_start + 1, 1, "Month")
ws.cell(month_start + 1, 2, "Revenue")

for i, row in enumerate(monthly.itertuples(index=False), month_start + 2):
    ws.cell(i, 1, row[0])
    ws.cell(i, 2, float(row[1]))

# Category chart
bar = BarChart()
bar.title = "Revenue by Category"
bar.y_axis.title = "Revenue"
bar.x_axis.title = "Category"
data = Reference(ws, min_col=2, min_row=10, max_row=10 + len(category))
cats = Reference(ws, min_col=1, min_row=11, max_row=10 + len(category))
bar.add_data(data, titles_from_data=True)
bar.set_categories(cats)
ws.add_chart(bar, "G3")

# Monthly chart
line = LineChart()
line.title = "Monthly Revenue Trend"
line.y_axis.title = "Revenue"
data = Reference(ws, min_col=2, min_row=21, max_row=21 + len(monthly))
cats = Reference(ws, min_col=1, min_row=22, max_row=21 + len(monthly))
line.add_data(data, titles_from_data=True)
line.set_categories(cats)
ws.add_chart(line, "G20")

# Format columns
for col in range(1, 6):
    ws.column_dimensions[get_column_letter(col)].width = 22

for row in ws.iter_rows():
    for cell in row:
        cell.alignment = Alignment(vertical="center")

for cell in ws[2]:
    cell.font = Font(bold=True, color="FFFFFF")
    cell.fill = PatternFill("solid", fgColor="4472C4")

# Save workbook
output = "Task-2/dashboard/sales_dashboard.xlsx"
wb.save(output)

print("Excel dashboard created successfully!")
print("Saved:", output)
