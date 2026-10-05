import pandas as pd

df = pd.read_excel("C:\\CodeMines\\CodeMines Python\\DATA SCIENCE\\SANTTOSH\\Machine Learning\\Resources\\house_data.xlsx")

print("===============================================================")

# 1. find missing values

missing_values_count = df.isnull().sum()

print(missing_values_count)

print("===============================================================")

df["City"] = df["City"].str.upper()
df["City"]= df["City"].str.strip()

# get all unique value from City column

print(df["City"].unique())

print("===============================================================")

# fill missing values using mode method

df["City"] = df["City"].fillna(
    df["City"].mode()[0]
)

print(df["City"].unique())

df.to_excel("updated_house_city_mode.xlsx",index=False)