
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

df = pd.read_excel("Resources/svm_Data.xlsx")

print(df)

print("-----------------------------------------------------------")

df["Result"] = df["Result"].map({"Fail": -1, "Pass": 1})

print(df)

print("-----------------------------------------------------------")

X = df[["Hours","Assignment","Previous_Result"]]
y = df["Result"]

# 3. Standardize the input features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("-----------------------------------------------------------")

model = SVC(kernel="linear",C=1)
model.fit(X_scaled, y)

# Individual feature weights
weights = model.coef_[0]

print("Individual Feature Weights:")
print("Hours Studied Weight:", weights[0])
print("Assignment Completed Weight:", weights[1])
print("Previous Result Weight:", weights[2])
print("Bias:", model.intercept_[0])

print("-----------------------------------------------------------")

# 8. Predict for a new student
new_student = pd.DataFrame({
    "Hours": [2],
    "Assignment": [1],
    "Previous_Result": [0]
})

new_student_scaled = scaler.transform(new_student)
prediction = model.predict(new_student_scaled)[0]

if prediction==1:
    print("Pass")
else:
    print("Fail")