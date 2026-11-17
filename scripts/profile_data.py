
import pandas as pd

# Step 1: Load the dataset
file_path = "File_Path"

df = pd.read_excel(file_path)

# Step 2: Display basic information
print("\n========== DATASET OVERVIEW ==========")

print("Total Rows:", df.shape[0])
print("Total Columns:", df.shape[1])

# Step 3: Display column names
print("\n========== COLUMN NAMES ==========")
print(df.columns.tolist())

# Step 4: Display data types
print("\n========== DATA TYPES ==========")
print(df.dtypes)

# Step 5: Check missing values
print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# Step 6: Check duplicate records
print("\n========== DUPLICATE RECORDS ==========")
print("Duplicates:", df.duplicated().sum())

# Step 7: Numerical statistics
print("\n========== NUMERICAL STATISTICS ==========")
print(df.describe())

# Step 8: Check unique values
print("\n========== UNIQUE VALUES ==========")

for column in df.select_dtypes(include="object").columns:
    print(column, ":", df[column].nunique())

print("\n========== PROFILING COMPLETED ==========")
