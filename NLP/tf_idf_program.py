
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

sentences = [
    "Boy is Good",
    "Girl is Good",
    "Boy and Girl are Good"
]

# create object of TfidfVectorizer
vectorizer = TfidfVectorizer(use_idf=True)

# Fit and Transform
tfidf_matrix = vectorizer.fit_transform(sentences)

df = pd.DataFrame(
    tfidf_matrix.toarray(),
    columns=vectorizer.get_feature_names_out(),
    index=["S1", "S2", "S3"]
)

print(df)