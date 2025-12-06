

"""
Data Cleaning Pipeline for Sales Data

Loads raw sales data, applies cleaning transformations (standardize column names,
remove whitespace, handle missing values, remove invalid rows), and outputs clean CSV.
"""

import pandas as pd
from pathlib import Path


def load_data(file_path: str) -> pd.DataFrame:
    """Load sales data from CSV file."""
    df = pd.read_csv(file_path)
    print(f"Loaded {len(df)} rows from {file_path}")
    return df


def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Standardize column names: strip whitespace, lowercase, replace spaces with underscores."""
    # Strip whitespace, lowercase, replace spaces with underscores for consistency
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(r"\s+", "_", regex=True)
    )
    print(f"Cleaned column names: {df.columns.tolist()}")
    return df


def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """Remove quotes and whitespace from text; convert numeric/date columns to proper types."""
    # Clean product name: remove quotes, strip whitespace, lowercase
    if "prodname" in df.columns:
        df["prodname"] = (
            df["prodname"]
            .fillna("")
            .astype(str)
            .str.replace('"', "")
            .str.strip()
            .str.lower()
        )
    
    # Clean category: remove quotes, strip whitespace, lowercase
    if "category" in df.columns:
        df["category"] = (
            df["category"]
            .fillna("")
            .astype(str)
            .str.replace('"', "")
            .str.strip()
            .str.lower()
        )
    
    # Convert price and qty to numeric (coerce invalid values to NaN)
    if "price" in df.columns:
        df["price"] = pd.to_numeric(df["price"].astype(str).str.strip(), errors="coerce")
    
    if "qty" in df.columns:
        df["qty"] = pd.to_numeric(df["qty"].astype(str).str.strip(), errors="coerce")
    
    # Convert date_sold to datetime
    if "date_sold" in df.columns:
        df["date_sold"] = pd.to_datetime(df["date_sold"], errors="coerce")
    
    print(f"After handling missing values: {len(df)} rows")
    return df


def remove_invalid_rows(df: pd.DataFrame) -> pd.DataFrame:
    """Remove rows with missing/invalid values: NaN prices/qty, non-positive prices/qty, duplicates."""
    initial_rows = len(df)
    
    # Drop rows with missing price or qty
    df = df.dropna(subset=["price", "qty"])
    after_missing = len(df)
    print(f"Dropped {initial_rows - after_missing} rows with missing price/qty")
    
    # Drop rows with non-positive price
    df = df[df["price"] > 0]
    after_price = len(df)
    print(f"Dropped {after_missing - after_price} rows with non-positive price")
    
    # Drop rows with non-positive qty
    df = df[df["qty"] > 0]
    after_qty = len(df)
    print(f"Dropped {after_price - after_qty} rows with non-positive qty")
    
    # Drop duplicate rows
    df = df.drop_duplicates(keep="first")
    after_dup = len(df)
    print(f"Dropped {after_qty - after_dup} duplicate rows")
    
    print(f"Final clean dataset: {len(df)} rows (removed {initial_rows - len(df)} total)")
    return df


if __name__ == "__main__":
    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"

    print("=" * 60)
    print("Data Cleaning Pipeline")
    print("=" * 60)
    
    df_raw = load_data(raw_path)
    df_clean = clean_column_names(df_raw)
    df_clean = handle_missing_values(df_clean)
    df_clean = remove_invalid_rows(df_clean)
    
    df_clean.to_csv(cleaned_path, index=False)
    print(f"\nCleaned data written to {cleaned_path}")
    
    print("\nFirst few rows:")
    print(df_clean.head())
    
    print("\nData types:")
    print(df_clean.dtypes)
    
    print("\nSummary statistics:")
    print(df_clean.describe())
