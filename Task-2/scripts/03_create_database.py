
import pandas as pd
import sqlite3
import os

# Load cleaned dataset
df = pd.read_excel("Task-1/output/cleaned_dataset.xlsx")

# Create database folder
os.makedirs("Task-2/data", exist_ok=True)

# Connect to SQLite database
connection = sqlite3.connect("Task-2/data/sales.db")

# Import dataset into SQL table
df.to_sql("sales", connection, if_exists="replace", index=False)

# Verify database
result = pd.read_sql_query(
    "SELECT COUNT(*) AS total_records FROM sales",
    connection
)

print("Database created successfully!")
print(result)

connection.close()
