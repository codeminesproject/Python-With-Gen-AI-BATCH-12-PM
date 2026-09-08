
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

description = "At our institution, we are committed ● to delivering high-quality education in programming and technology at our institute. Our courses are designed to provide comprehensive commit knowledge and practical skills in various programming languages and technologies. We pride ourselves on offering a supportive learning environment where students can thrive and reach their full potential."

print(description)

print("===================================================")

# convert into words

words = word_tokenize(description)

lemmatizer = WordNetLemmatizer()
for word in words:
    print(word ," ----> ", lemmatizer.lemmatize(word,pos="v"))

