import pandas as pd
from sklearn.impute import KNNImputer
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("C:\\CodeMines\\CodeMines Python\\DATA SCIENCE\\SANTTOSH\\Machine Learning\\Resources\\house_data.xlsx")

print("===============================================================")

data = {
    "Area_sqft": [800, 1000, 1200, 1500, 1800, 2000, 2200, 2500],
    "BHK": [1, 2, 2, 3, 3, 4, 4, 5],
    "Bathrooms": [1, 1, 2, 2, 2, 3, 3, 4],
    "Age_Years": [15, 12, 10, 8, 6, 5, 3, 2],
    "Distance_Metro": [5.0, 4.5, 4.0, 3.0, 2.5, 2.0, 1.5, 1.0],
    "Price_Lakhs": [35, 45, 55, 70, 85, 105, 125, 150]
}

df = pd.DataFrame(data)

print(df)

# Correlation matrix
correlation_matrix = df.corr()

# Heatmap
plt.figure(figsize=(9, 7))

sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap - House Price")
plt.show()


