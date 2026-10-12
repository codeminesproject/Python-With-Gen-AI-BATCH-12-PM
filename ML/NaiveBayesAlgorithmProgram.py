
import pandas as pd
from sklearn.naive_bayes import CategoricalNB

df = pd.read_excel("Resources/NB_student_pass_fail.xlsx")
print(df)

# Convert text into numbers
df["Assignment"] = df["Assignment"].map({"No": 0, "Yes": 1})
df["Previous"] = df["Previous"].map({"Fail": 0, "Pass": 1})

# Input and output
X = df[["Hours", "Assignment", "Previous"]]
y = df["Result"]

k_list = [X["Hours"].max(),X["Assignment"].nunique(),X["Previous"].nunique()]

print(k_list)

# Train model
model = CategoricalNB(alpha=1,min_categories=k_list)
model.fit(X,y)

# Predict new student
student = [[5, 1, 1]]  # 5 hours, Assignment Yes, Previous Pass

prediction = model.predict(student)

print("Student Result:", prediction[0])