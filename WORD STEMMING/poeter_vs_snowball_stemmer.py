
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

print("------------------ Porter Stemmer Result --------------------")

# create object of PorterStemmer

porterstemmer = PorterStemmer()
print(porterstemmer.stem("fairly"))
print(porterstemmer.stem("sportingly"))
print(porterstemmer.stem("goes"))

print("------------------ Snowball Stemmer Result --------------------")

# create object of SnowballStemmer

snowballsstemmer = SnowballStemmer('english')
print(snowballsstemmer.stem("fairly"))
print(snowballsstemmer.stem("sportingly"))
print(snowballsstemmer.stem("goes"))

print("------------------ lemmatization Result --------------------")

# create object of SnowballStemmer

wordnetlemmatizer = WordNetLemmatizer()
print(wordnetlemmatizer.lemmatize("fairly",pos="a"))
print(wordnetlemmatizer.lemmatize("sportingly",pos="a"))
print(wordnetlemmatizer.lemmatize("goes",pos="v"))