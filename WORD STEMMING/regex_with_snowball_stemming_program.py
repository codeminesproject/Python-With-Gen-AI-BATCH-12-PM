
from nltk.stem import RegexpStemmer,SnowballStemmer
from nltk import word_tokenize


description = "At our institution, we are committed ● to delivering high-quality education in programming and technology at our institute. Our courses are designed to provide comprehensive commit knowledge and practical skills in various programming languages and technologies. We pride ourselves on offering a supportive learning environment where students can thrive and reach their full potential."

print(description)

print("-----------------------------------------------------------")

# create object of RegexpStemmer

regex_stemmer = RegexpStemmer('ing$|s$|e$|able$', min=4)


words = word_tokenize(description)

regex_stemmer_words = []

for word in words:
    regex_stemmer_words.append(regex_stemmer.stem(word))

# apply snowball stemmer

snowball_stemmer = SnowballStemmer('english')

for word in regex_stemmer_words:
    print(word," ----> ",snowball_stemmer.stem(word))
