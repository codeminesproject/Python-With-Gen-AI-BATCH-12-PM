
from sklearn.feature_extraction.text import CountVectorizer

# input sentences

sentences = [
    "food good",
    "Food not bad"
]

# STEP 1: Apply unigram
cv = CountVectorizer(ngram_range=(1,1))
vocabulary = cv.fit_transform(sentences)

print("Vocabulary:")
print(cv.vocabulary_)

print("Feature Names:")
print(cv.get_feature_names_out())

print("n gram Matrix:")
print(vocabulary.toarray())

print("-------------------------------------------------------------------------")

# STEP 2: Apply biagram
cv = CountVectorizer(ngram_range=(1,2))
vocabulary = cv.fit_transform(sentences)

print("Vocabulary:")
print(cv.vocabulary_)

print("Feature Names:")
print(cv.get_feature_names_out())

print("n gram Matrix:")
print(vocabulary.toarray())

print("-------------------------------------------------------------------------")

# STEP 3: Apply trigram
cv = CountVectorizer(ngram_range=(1,3))
vocabulary = cv.fit_transform(sentences)

print("Vocabulary:")
print(cv.vocabulary_)

print("Feature Names:")
print(cv.get_feature_names_out())

print("n gram Matrix:")
print(vocabulary.toarray())