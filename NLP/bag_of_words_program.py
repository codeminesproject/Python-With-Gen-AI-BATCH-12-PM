
from sklearn.feature_extraction.text import CountVectorizer

sentences = [
    "He is a good boy",
    "She is a good girl",
    "Boy and girl are good"
]

cv = CountVectorizer()
vocabulary = cv.fit_transform(sentences)

print("Vocabulary:")
print(cv.vocabulary_)

print("Feature Names:")
print(cv.get_feature_names_out())

print("Bag of Words Matrix:")
print(vocabulary.toarray())