import pandas as pd

df = pd.read_excel("C:\\CodeMines\\CodeMines Python\\DATA SCIENCE\\SANTTOSH\\Machine Learning\\Resources\\house_data.xlsx")

print("===============================================================")

# 1. find missing values

missing_values_count = df.isnull().sum()

print(missing_values_count)

print("===============================================================")

df["BHK"] = df["BHK"].astype(str).str.replace(" BHK","") 

# convert values into numeric form

df["BHK"] = pd.to_numeric(df["BHK"])

print("===============================================================")

# fill missing values with default value

df["City"] = df["City"].fillna("Unknown")

print("===============================================================")

# remove ' sq.ft' from Area_sqft column

df["Area_sqft"] = df["Area_sqft"].astype(str).str.replace(" sq.ft","") 

# convert values into numeric form

df["Area_sqft"] = pd.to_numeric(df["Area_sqft"])

df["Area_sqft"] = df["Area_sqft"].fillna(
    df.groupby(["City","BHK"])["Area_sqft"].transform("median")
    )

df.to_excel("new_house_data.xlsx")
