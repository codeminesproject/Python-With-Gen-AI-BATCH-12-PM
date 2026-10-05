
import pandas as pd

df = pd.read_excel("C:\\CodeMines\\CodeMines Python\\DATA SCIENCE\\SANTTOSH\\Machine Learning\\Resources\\house_data.xlsx")

print("===============================================================")

# 1. find missing values

missing_values_count = df.isnull().sum()

print(missing_values_count)

print("===============================================================")

# 2. remove all empty value rows
# inplace=True: remove rows containing missing (NaN) values and update df itself.

df.dropna(inplace=True)

print("===============================================================")

missing_values_count = df.isnull().sum()

print(missing_values_count)

df.to_excel("updated_house_data.xlsx",index=False)