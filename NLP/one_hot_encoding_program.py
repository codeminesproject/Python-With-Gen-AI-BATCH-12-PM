
from nltk import word_tokenize
from sklearn.preprocessing import OneHotEncoder
import numpy as np

sentence = "I love Python"

words = word_tokenize(sentence)

print(words)

# convert list into 2D array 
words_array = np.array(words).reshape(-1,1)

print(words_array)

# convert 2D array into vector

encoding = OneHotEncoder(categories=[words],sparse_output=False,
    handle_unknown='ignore')
encoded = encoding.fit_transform(words_array)

print(encoded)
