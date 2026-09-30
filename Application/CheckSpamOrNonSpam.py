
import pandas as pd
from LogisticRegressionProgram import LRClass
from sklearn.feature_extraction.text import TfidfVectorizer

file_location = "C:\\CodeMines\\CodeMines Python\\DATA SCIENCE\\SANTTOSH\\Machine Learning\\Resources\\email_spam_dataset.xlsx"
df = pd.read_excel(file_location)
print(df)

input_feature = df["email"]
target_feature = df["label"]
test_data = "100 percent free course"

ml_response = LRClass.predect_result(input_feature,target_feature,0.2,30)

model = ml_response[0]
vectorizer = ml_response[1]

test_vectorizer = vectorizer.transform([test_data])

prediction = model.predict(test_vectorizer)

if prediction[0]==0:
    print("Non Spam")
else:
    print("Spam")

probability = model.predict_proba(test_vectorizer)

print(probability)

print("Non Spam Propability:",probability[0][0]*100)
print("Spam Propability:",probability[0][1]*100)