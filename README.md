# ApexPlanet Data Analytics Internship — Task 1

**Project:** Data Immersion & Wrangling  
**Internship:** ApexPlanet Software Pvt. Ltd. — 60-Day Data Analytics Program  
**Author:** Hardik Kotawdekar

## Project Overview

This repository contains the Task 1 work for the ApexPlanet Data Analytics internship. The objective is to understand the supplied sales dataset, assess its quality, document its fields, clean and transform the data, and produce an analysis-ready dataset.

## Repository Structure

```text
Apex_Data_Analytics/
├── dataset/
│   └── ApexPlanet_DataAnalytics_Dataset.xlsx
├── documentation/
│   └── Data_Dictionary.xlsx
├── scripts/
│   ├── profile_data.py
│   └── data_cleaning.py
├── output/
│   └── cleaned_dataset.xlsx
└── README.md
```

## Dataset Overview

The supplied workbook contains a worksheet named `Sales_Dataset`, with 1,000 records and 12 fields:

- `Order_ID`, `Order_Date`
- `Customer_ID`, `Customer_Name`
- `Age`, `Gender`, `City`
- `Product`, `Category`
- `Quantity`, `Unit_Price`, `Total_Sales`

## Tools and Libraries

- Python
- Pandas
- OpenPyXL
- Visual Studio Code

Install the required libraries from the project root:

```bash
pip install pandas openpyxl matplotlib seaborn
```

## How to Run

Run the initial data profiling script:

```bash
python scripts/profile_data.py
```

Run the cleaning script:

```bash
python scripts/data_cleaning.py
```

The cleaning script reads the original workbook from `dataset/` and writes the result to `output/cleaned_dataset.xlsx`. It does not overwrite the original source file.

## Data Quality Assessment and Cleaning

Initial inspection identified:

- 20 missing values in `Age`
- 13 missing values in `City`
- 0 exact full-row duplicates
- `Order_Date` initially stored as text

The cleaning workflow:

1. Removes exact full-row duplicates only.
2. Trims leading and trailing whitespace in text fields.
3. Converts `Order_Date` to a datetime value.
4. Converts applicable numeric fields to numeric types.
5. Fills missing `Age` values with the median.
6. Fills missing `City` values with the most frequent city.
7. Exports cleaned data plus a cleaning summary and remaining-missing-values report.

**Important data-quality note:** repeated `Order_ID` values are not automatically treated as duplicate transactions. They require business-context review before any records are removed.

## Deliverables

- [Data Dictionary](documentation/Data_Dictionary.xlsx)
- [Data Profiling Script](scripts/profile_data.py)
- [Data Cleaning Script](scripts/data_cleaning.py)
- [Cleaned Dataset](output/cleaned_dataset.xlsx)

## Notes

The imputation choices are documented assumptions for this task. Review them against business rules before using the data for operational or financial decisions.

This repository is part of an internship learning project.
