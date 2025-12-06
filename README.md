# Data Cleaning Pipeline

A Python-based data cleaning pipeline that processes raw sales data, standardizes formats, and outputs clean CSV files ready for analysis.

## Overview

This project takes messy raw sales data (`data/raw/sales_data_raw.csv`) and applies a series of cleaning transformations:
- Standardizes column names (lowercase, underscores)
- Removes quotes and extra whitespace from text fields
- Converts numeric and date columns to proper types
- Removes invalid rows (missing values, negative prices/quantities, duplicates)

The cleaned output is saved to `data/processed/sales_data_clean.csv`.

## Files

- `src/data_cleaning.py` — Main cleaning script with helper functions
- `data/raw/sales_data_raw.csv` — Raw input data
- `data/processed/sales_data_clean.csv` — Cleaned output data
- `README.md` — This file
- `reflection.md` — Project reflection and insights

## How to Run

1. Install dependencies (if needed):
```bash
pip install pandas
```

2. From the project root, run the cleaning pipeline:
```bash
python3 src/data_cleaning.py
```

3. The cleaned data will be written to `data/processed/sales_data_clean.csv`

## Output

The script prints:
- Number of rows loaded
- Cleaned column names
- Rows removed at each validation step
- First few rows of clean data
- Data types and summary statistics
