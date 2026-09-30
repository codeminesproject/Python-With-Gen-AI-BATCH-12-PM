
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

file_location = "C:\\CodeMines\\CodeMines Python\\DATA SCIENCE\\SANTTOSH\\Machine Learning\\Resources\\email_spam_dataset.xlsx"

df = pd.read_excel(file_location)

print(df)

# ============================================================
# SEPARATE INPUT AND TARGET
# ============================================================

X = df["email"]
y = df["label"]


# ============================================================
# CONVERT TEXT INTO NUMERICAL FEATURES
# ============================================================

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(X)

# ============================================================
# SPLIT DATA INTO TRAINING AND TESTING
# ============================================================

X_train,X_test,y_train,y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=30,
    stratify=y
)

# ============================================================
# CREATE LOGISTIC REGRESSION MODEL AND TRAIN MODEL
# ============================================================

model = LogisticRegression()
model.fit(X_train,y_train)

# ============================================================
# PREDICT TEST DATA
# ============================================================

y_pred = model.predict(X_test)

# ============================================================
# MODEL EVALUATION
# ============================================================

accuracy = accuracy_score(y_test,y_pred)

print("accuracy:",accuracy)

# ============================================================
# Check Model
# ============================================================

email = input("Please enter email: ")

email_vectorizer = vectorizer.transform([email])

print(email_vectorizer)

prediction = model.predict(email_vectorizer)

if prediction[0]==0:
    print("Non Spam")
else:
    print("Spam")

probability = model.predict_proba(email_vectorizer)

print(probability)

print("Non Spam Propability:",probability[0][0]*100)
print("Spam Propability:",probability[0][1]*100)







