
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

# 1. Original student dataset
df = pd.read_excel("Resources/svm_Data.xlsx")


# 2. Use Hours and Assignment for a 2D plot
X = df[["Hours", "Assignment"]]
y = df["Result"].map({"Fail": -1, "Pass": 1})

# 3. Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. Train a linear SVM
model = SVC(kernel="linear", C=1)
model.fit(X_scaled, y)

# 5. Create points for drawing the boundary
x_min = X_scaled[:, 0].min() - 0.5
x_max = X_scaled[:, 0].max() + 0.5

x_values = [
    x_min + i * (x_max - x_min) / 200
    for i in range(201)
]

# Decision boundary:
# w1*x + w2*y + b = 0
w1, w2 = model.coef_[0]
b = model.intercept_[0]

boundary = [-(w1 * x + b) / w2 for x in x_values]
margin_positive = [-(w1 * x + b - 1) / w2 for x in x_values]
margin_negative = [-(w1 * x + b + 1) / w2 for x in x_values]

# 6. Plot Pass and Fail students
fail = y == -1
passed = y == 1

plt.figure(figsize=(10, 6))

plt.scatter(
    X_scaled[fail, 0], X_scaled[fail, 1],
    label="Fail", marker="o", s=100
)

plt.scatter(
    X_scaled[passed, 0], X_scaled[passed, 1],
    label="Pass", marker="^", s=100
)

# 7. Highlight support vectors
support_vectors = model.support_vectors_

plt.scatter(
    support_vectors[:, 0],
    support_vectors[:, 1],
    s=250, facecolors="none", edgecolors="black",
    linewidths=2, label="Support Vectors"
)

# 8. Draw boundary and margins
plt.plot(x_values, boundary, label="Decision Boundary")
plt.plot(
    x_values, margin_positive,
    linestyle="--", label="Margin +1"
)
plt.plot(
    x_values, margin_negative,
    linestyle="--", label="Margin -1"
)

# 9. Label each student
for i, student in enumerate(df["Student"] if "Student" in df else
                            [f"S{j}" for j in range(1, 11)]):
    plt.annotate(
        student,
        (X_scaled[i, 0], X_scaled[i, 1]),
        xytext=(5, 5),
        textcoords="offset points"
    )

plt.xlabel("Standardized Hours Studied")
plt.ylabel("Standardized Assignment Completed")
plt.title("Linear SVM: Student Pass/Fail Prediction")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()



