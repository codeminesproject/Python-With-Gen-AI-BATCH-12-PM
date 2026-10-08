
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

data = {
    "study_hours": [2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
                    2, 4, 6, 8, 10, 3, 5, 7, 9, 12],

    "attendance": [60, 65, 70, 72, 75, 80, 85, 88, 92, 95,
                   62, 70, 78, 86, 94, 66, 74, 82, 90, 97],

    "previous_score": [45, 50, 55, 60, 65, 70, 75, 80, 85, 90,
                       48, 56, 66, 76, 88, 52, 62, 72, 82, 94],

    "assignments": [3, 4, 5, 6, 7, 7, 8, 9, 9, 10,
                    3, 5, 7, 8, 10, 4, 6, 8, 9, 10],

    "sleep_hours": [5, 5.5, 6, 6, 6.5, 7, 7, 7.5, 8, 8,
                    5, 6, 6.5, 7, 8, 5.5, 6, 7, 7.5, 8],

    "exam_score": [45, 50, 55, 61, 67, 72, 78, 83, 88, 94,
                   47, 56, 68, 79, 91, 51, 63, 74, 85, 96]
}

df = pd.DataFrame(data)

# 2. Features (X) and target (y)
X = df[
    [
        "study_hours",
        "attendance",
        "previous_score",
        "assignments",
        "sleep_hours"
    ]
]

y = df["exam_score"]

# 3. Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

scaler = StandardScaler()
# Fit ONLY on training data
X_train_scaled = scaler.fit_transform(X_train)

# Use the same learned mean/std on test data
X_test_scaled = scaler.transform(X_test)

# Use the same learned mean/std on test data
X_test_scaled = scaler.transform(X_test)

# 5. Train model
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# 6. Make predictions
y_pred = model.predict(X_test_scaled)

# 7. Evaluate
mae = mean_absolute_error(y_test, y_pred)

print(mae)
