
import sqlite3
import pandas as pd
import os

# Database connection
db_path = "Task-2/data/sales.db"
connection = sqlite3.connect(db_path)

# Create reports folder
os.makedirs("Task-2/reports", exist_ok=True)

# Seven business questions
queries = {
    "Total Revenue": """
        SELECT ROUND(SUM(Total_Sales), 2) AS total_revenue
        FROM sales;
    """,

    "Revenue by Category": """
        SELECT Category,
               ROUND(SUM(Total_Sales), 2) AS revenue
        FROM sales
        GROUP BY Category
        ORDER BY revenue DESC;
    """,

    "Revenue by City": """
        SELECT City,
               ROUND(SUM(Total_Sales), 2) AS revenue
        FROM sales
        GROUP BY City
        ORDER BY revenue DESC;
    """,

    "Top Products": """
        SELECT Product,
               SUM(Quantity) AS total_quantity
        FROM sales
        GROUP BY Product
        ORDER BY total_quantity DESC
        LIMIT 5;
    """,

    "Monthly Revenue": """
        SELECT strftime('%Y-%m', Order_Date) AS sales_month,
               ROUND(SUM(Total_Sales), 2) AS monthly_revenue
        FROM sales
        GROUP BY sales_month
        ORDER BY sales_month;
    """,

    "Top Customers": """
        SELECT Customer_ID,
               Customer_Name,
               ROUND(SUM(Total_Sales), 2) AS customer_revenue
        FROM sales
        GROUP BY Customer_ID, Customer_Name
        ORDER BY customer_revenue DESC
        LIMIT 10;
    """,

    "Average Order Value": """
        SELECT ROUND(AVG(order_revenue), 2) AS average_order_value
        FROM (
            SELECT Order_ID, SUM(Total_Sales) AS order_revenue
            FROM sales
            GROUP BY Order_ID
        );
    """
}

# Execute queries and save results
output_file = "Task-2/reports/sql_business_results.xlsx"

with pd.ExcelWriter(output_file) as writer:
    for question, query in queries.items():
        result = pd.read_sql_query(query, connection)

        # Print results
        print(f"\n========== {question} ==========")
        print(result.to_string(index=False))

        # Save each result in a separate Excel sheet
        sheet_name = question[:31]
        result.to_excel(writer, sheet_name=sheet_name, index=False)

connection.close()

print("\nAll SQL queries executed successfully!")
print("Results saved to:", output_file)
