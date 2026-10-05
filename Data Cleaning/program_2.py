import pandas as pd

df = pd.read_excel("C:\\CodeMines\\CodeMines Python\\DATA SCIENCE\\SANTTOSH\\Machine Learning\\Resources\\house_data.xlsx")

print("===============================================================")

# 1. find missing values

missing_values_count = df.isnull().sum()

print(missing_values_count)

print("===============================================================")

# get all unique value from BHK column

print(df["BHK"].unique())

print("===============================================================")

# remove ' BHK' from BHK column

df["BHK"] = df["BHK"].astype(str).str.replace(" BHK","") 

# convert values into numeric form

df["BHK"] = pd.to_numeric(df["BHK"])

print(df["BHK"].unique())