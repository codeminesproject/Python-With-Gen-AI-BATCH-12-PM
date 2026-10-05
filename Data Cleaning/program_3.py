import pandas as pd

df = pd.read_excel("C:\\CodeMines\\CodeMines Python\\DATA SCIENCE\\SANTTOSH\\Machine Learning\\Resources\\house_data.xlsx")

print("===============================================================")

# 1. find missing values

missing_values_count = df.isnull().sum()

print(missing_values_count)

print("===============================================================")

# get all unique value from Area_sqft column

print(df["Area_sqft"].unique())

print("===============================================================")

# remove ' sq.ft' from Area_sqft column

df["Area_sqft"] = df["Area_sqft"].astype(str).str.replace(" sq.ft","") 

# convert values into numeric form

df["Area_sqft"] = pd.to_numeric(df["Area_sqft"])

print(df["Area_sqft"].unique())

print("===============================================================")

# remove nan with mean value of Area_sqft

df["Area_sqft"] = df["Area_sqft"].fillna(
    df["Area_sqft"].mean()
)

print(df["Area_sqft"].unique())

print("===============================================================")


missing_values_count = df["Area_sqft"].isnull().sum()

print(missing_values_count)