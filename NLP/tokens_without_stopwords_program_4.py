from nltk import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
import re


description = "At our institution, we are committed ● to delivering high-quality education in programming and technology at our institute. Our courses are designed to provide comprehensive commit knowledge and practical skills in various programming languages and technologies. We pride ourselves on offering a supportive learning environment where students can thrive and reach their full potential."

print(description)

print("-----------------------------------------------------------")

# convert paragraph into sentences
sentences = sent_tokenize(description.lower())

print("-----------------------------------------------------------")

# get all stopwords from stopword library
stop_words = stopwords.words('english')

# convert sentence into words
for sentence in sentences:
    sentence_without_special_characters = re.sub(r"[^a-zA-Z0-9\s]","",sentence)
    words = word_tokenize(sentence_without_special_characters)
    tokens = []
    for word in words:
        if word not in stop_words:
            # add only unique tokens
            if word not in tokens:
                tokens.append(word)
    print(tokens)