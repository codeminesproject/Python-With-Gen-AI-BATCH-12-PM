
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

df = pd.read_excel("C:\\CodeMines\\CodeMines Python\\DATA SCIENCE\\BATCH 12\\Resources\\cricket_data.xlsx")

print(df)

print("--------------------------------------------------")

encoders = {}
for column in df.columns:
    encoder = LabelEncoder()
    df[column] = encoder.fit_transform(df[column])
    encoders[column] = encoder

print(df)

print("--------------------------------------------------")

X = df[["Outlook","Temperature","Humidity","Windy","Ground"]]
y=df["Play_Cricket"]

print("--------------------------------------------------")

# 3. Create Random Forest with 5 trees
model = RandomForestClassifier(
    n_estimators=5,
    random_state=42
)

# 4. Train the model
model.fit(X, y)

print("--------------------------------------------------")

# Predict for a new situation
new_data = pd.DataFrame([{
    "Outlook": "Rainy",
    "Temperature": "Hot",
    "Humidity": "High",
    "Windy": "Yes",
    "Ground": "Dry"
}])

# Apply the same encoders used during training
for column in new_data.columns:
    new_data[column] = encoders[column].transform(
        new_data[column]
    )

# 6. Prediction by each tree
print("Individual Tree Predictions:")

print("Tree 1:", model.estimators_[0].predict(new_data)[0])
print("Tree 2:", model.estimators_[1].predict(new_data)[0])
print("Tree 3:", model.estimators_[2].predict(new_data)[0])
print("Tree 4:", model.estimators_[3].predict(new_data)[0])
print("Tree 5:", model.estimators_[4].predict(new_data)[0])

# 7. Final Random Forest prediction
result = model.predict(new_data)

print("\nFinal Prediction:", result[0])

# 8. Class probabilities
probability = model.predict_proba(new_data)[0]

print("\nClass Probabilities:")
print("No:", probability[0] * 100, "%")
print("Yes:", probability[1] * 100, "%")