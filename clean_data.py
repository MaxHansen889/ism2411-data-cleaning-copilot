import pandas as pd
# Load the raw data
raw_data = pd.read_csv("sales_raw_data.csv") 

#  Save cleaned version
raw_data.to_csv("processed_data.csv", index=False)

print("Cleaning complete.")
