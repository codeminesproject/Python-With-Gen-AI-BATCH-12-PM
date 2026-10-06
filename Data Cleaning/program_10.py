import pandas as pd
from sklearn.impute import KNNImputer

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

# remove ' sq.ft' from Area_sqft column

df["Area_sqft"] = df["Area_sqft"].astype(str).str.replace(" sq.ft","") 

# convert values into numeric form

df["Area_sqft"] = pd.to_numeric(df["Area_sqft"])

print("===============================================================")

model = KNNImputer(n_neighbors=3)

df[["BHK","Area_sqft"]]= model.fit_transform(
    df[["BHK", "Area_sqft"]]
)

df.to_excel("new_house_data_knn.xlsx")
