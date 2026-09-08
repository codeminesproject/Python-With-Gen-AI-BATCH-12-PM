
from nltk.stem import PorterStemmer
from nltk import word_tokenize


description = "At our institution, we are committed ● to delivering high-quality education in programming and technology at our institute. Our courses are designed to provide comprehensive commit knowledge and practical skills in various programming languages and technologies. We pride ourselves on offering a supportive learning environment where students can thrive and reach their full potential."

print(description)

print("-----------------------------------------------------------")

# create object of PorterStemmer

porter_stemmer = PorterStemmer()

words = word_tokenize(description)

for word in words:
    print(word ," -----> ", porter_stemmer.stem(word))
