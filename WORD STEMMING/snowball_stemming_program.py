
from nltk.stem import SnowballStemmer
from nltk import word_tokenize


description = "At our institution, we are committed ● to delivering high-quality education in programming and technology at our institute. Our courses are designed to provide comprehensive commit knowledge and practical skills in various programming languages and technologies. We pride ourselves on offering a supportive learning environment where students can thrive and reach their full potential."

print(description)

print("-----------------------------------------------------------")

# create object of SnowballStemmer

snowball_stemmer = SnowballStemmer('english')

words = word_tokenize(description)

for word in words:
    print(word ," -----> ", snowball_stemmer.stem(word))
