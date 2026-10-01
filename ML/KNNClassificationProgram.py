
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

df = pd.read_excel("C:\\CodeMines\\CodeMines Python\\DATA SCIENCE\\BATCH 12\\Resources\\knn_student_pass_or_fail.xlsx")

print(df)

print("================================================================")

# input feature
X = df[["Hours_Studied"]]

#target feature
y = df["Result"]



X_train,X_test,y_train,y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=30
)

# create model of KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=3)

# train model with input feature and result
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test,y_pred)

print("Accuracy Score:",accuracy)

print("=============================================================")

no_of_hour_study = [[2.2]]

prediction = model.predict(no_of_hour_study)

print(prediction)
