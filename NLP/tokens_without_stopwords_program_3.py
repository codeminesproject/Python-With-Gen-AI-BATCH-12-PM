from nltk import sent_tokenize,word_tokenize
from nltk.corpus import stopwords


description = "At our institution, we are committed ● to delivering high-quality education in programming and technology. Our courses are designed to provide comprehensive knowledge and practical skills in various programming languages and technologies. We pride ourselves on offering a supportive learning environment where students can thrive and reach their full potential."

print(description)

print("-----------------------------------------------------------")

# convert paragraph into sentences
sentences = sent_tokenize(description.lower())

print("-----------------------------------------------------------")

# get all stopwords from stopword library
stop_words = stopwords.words('english')

# get all list of special symbols
special_symbols = [
    "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", 
    "-", "_", "+", "=", "{", "}", "[", "]", "|", "\\",
    ":", ";", "\"", "'", "<", ">", ",", ".", "?", "/",
    "`", "~"
]

# convert sentence into words
for sentence in sentences:
    words = word_tokenize(sentence)
    tokens = []
    for word in words:
        if word not in stop_words:
            if word not in special_symbols:
                tokens.append(word)
    print(tokens)