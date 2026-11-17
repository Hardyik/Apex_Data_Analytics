"""
ApexPlanet Data Analytics Internship - Task 1
Data cleaning script for ApexPlanet_DataAnalytics_Dataset.xlsx

Expected project structure:
ApexPlanet-Data-Analytics/
    dataset/ApexPlanet_DataAnalytics_Dataset.xlsx
    scripts/data_cleaning.py
    output/cleaned_dataset.xlsx

Run from the project root:
    python scripts/data_cleaning.py
"""

from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
INPUT_FILE = PROJECT_ROOT / "dataset" / "ApexPlanet_DataAnalytics_Dataset.xlsx"
OUTPUT_DIR = PROJECT_ROOT / "output"
OUTPUT_FILE = OUTPUT_DIR / "cleaned_dataset.xlsx"

def main():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"Could not find input file: {INPUT_FILE}\n"
            "Place the original Excel file in the project's dataset folder."
        )

    # 1. Load the original data (the source file is never overwritten).
    df = pd.read_excel(INPUT_FILE, sheet_name="Sales_Dataset")
    original_rows = len(df)

    print("========== BEFORE CLEANING ==========")
    print("Rows:", len(df))
    print("Columns:", len(df.columns))
    print("\\nMissing values by column:")
    print(df.isna().sum())
    print("\\nExact duplicate rows:", df.duplicated().sum())

    # 2. Remove exact full-row duplicates only.
    exact_duplicates = int(df.duplicated().sum())
    df = df.drop_duplicates().copy()

    # 3. Trim leading/trailing spaces from text columns.
    text_columns = df.select_dtypes(include=["object"]).columns
    for column in text_columns:
        df[column] = df[column].apply(
            lambda value: value.strip() if isinstance(value, str) else value
        )

    # 4. Convert Order_Date from text to a proper date.
    # Invalid/unparseable dates become missing and are reported below.
    df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")

    # 5. Convert numeric columns safely.
    numeric_columns = ["Age", "Quantity", "Unit_Price", "Total_Sales"]
    for column in numeric_columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    # 6. Fill missing Age values with the median.
    age_missing_before = int(df["Age"].isna().sum())
    age_median = df["Age"].median()
    if pd.notna(age_median):
        df["Age"] = df["Age"].fillna(age_median)

    # 7. Fill missing City values with the most frequent city.
    city_missing_before = int(df["City"].isna().sum())
    city_modes = df["City"].mode(dropna=True)
    if not city_modes.empty:
        df["City"] = df["City"].fillna(city_modes.iloc[0])

    # 8. Create a cleaning summary and identify unresolved missing values.
    remaining_missing = df.isna().sum()
    summary = pd.DataFrame({
        "Metric": [
            "Original row count",
            "Rows after exact-duplicate removal",
            "Exact duplicate rows removed",
            "Missing Age values filled",
            "Missing City values filled",
            "Repeated Order_ID rows (not automatically removed)",
            "Remaining missing cells"
        ],
        "Value": [
            original_rows,
            len(df),
            exact_duplicates,
            age_missing_before,
            city_missing_before,
            int(df["Order_ID"].duplicated().sum()),
            int(remaining_missing.sum())
        ]
    })

    # 9. Export cleaned data and a summary sheet to Excel.
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with pd.ExcelWriter(OUTPUT_FILE, engine="openpyxl", datetime_format="yyyy-mm-dd") as writer:
        df.to_excel(writer, sheet_name="Cleaned_Data", index=False)
        summary.to_excel(writer, sheet_name="Cleaning_Summary", index=False)
        remaining_missing.rename("Remaining Missing Values").to_frame().to_excel(
            writer, sheet_name="Remaining_Missing"
        )

        for ws in writer.book.worksheets:
            ws.freeze_panes = "A2"
            ws.auto_filter.ref = ws.dimensions
            for col_cells in ws.columns:
                max_len = max(len(str(c.value)) if c.value is not None else 0 for c in col_cells)
                ws.column_dimensions[col_cells[0].column_letter].width = min(max(max_len + 2, 14), 42)

    print("\\n========== AFTER CLEANING ==========")
    print("Rows:", len(df))
    print("Columns:", len(df.columns))
    print("\\nRemaining missing values:")
    print(remaining_missing)
    print("\\nExact duplicate rows:", df.duplicated().sum())
    print("\\nRepeated Order_ID values:", df["Order_ID"].duplicated().sum())
    print("\\nSaved cleaned workbook to:", OUTPUT_FILE)

if __name__ == "__main__":
    main()
