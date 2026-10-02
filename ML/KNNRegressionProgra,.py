
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error

df = pd.read_excel("C:\\CodeMines\\CodeMines Python\\DATA SCIENCE\\BATCH 12\\Resources\\house_price.xlsx")

print(df)

print("*"*60)

# assign input and target features

X = df[["area_sqft","Bedrooms"]]
y= df["Price_Lakhs"] 

print("*"*60)

X_train,X_test,y_train,y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=30
)

print("*"*60)

model = KNeighborsRegressor(n_neighbors=3)
model.fit(X_train,y_train)

print("*"*60)

y_pred = model.predict(X_test)

absolute_error = mean_absolute_error(y_test,y_pred)

print("Absolute Error:",absolute_error)

print("----------------------------------------------------------")

house_data = pd.DataFrame(
    {
        "area_sqft":[1700],
        "Bedrooms":[3]
    }
)

prediction = model.predict(house_data)

print("House Area:", 1700, "sqft")
print("Bedrooms:", 3)
print("Predicted Price:", round(prediction[0], 2), "Lakhs")