
# TreebankWordTokenizer is a class inside nltk.tokentizer module
# It is used to generate token from corpus

from nltk.tokenize import TreebankWordTokenizer
from nltk import sent_tokenize

description = "At our institution, we are committed to delivering high-quality education in programming and technology. Our courses are designed to provide comprehensive knowledge and practical skills in various programming languages and technologies. We pride ourselves on offering a supportive learning environment where students can thrive and reach their full potential."

print(description)
print("-----------------------------------------------------------")

# step 1 : create object of TreebankWordTokenizer
tokenizer = TreebankWordTokenizer()

# step 2: generate document from corpus
sentences = sent_tokenize(description)

# step 2 : generate token from documents
for sentence in sentences:
    tokens = tokenizer.tokenize(sentence)
    print(tokens)