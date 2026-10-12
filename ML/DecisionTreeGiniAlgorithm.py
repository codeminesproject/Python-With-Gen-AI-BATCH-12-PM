
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

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

model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=4,
    random_state=42
)

model.fit(X, y)

print("=======================================================")

# Predict for a new situation
new_data = pd.DataFrame([{
    "Outlook": "Sunny",
    "Temperature": "Cool",
    "Humidity": "High",
    "Windy": "Yes",
    "Ground": "Dry"
}])

# Apply the same encoders used during training
for column in new_data.columns:
    new_data[column] = encoders[column].transform(
        new_data[column]
    )

prediction = model.predict(new_data)[0]
result = encoders["Play_Cricket"].inverse_transform(
    [prediction]
)[0]

print("Can we play outdoor cricket?", result)