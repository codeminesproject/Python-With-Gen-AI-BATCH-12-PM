
import nltk

sentence="Santtosh Upadhyay is a trainer in CodeMines Computer"

words = nltk.word_tokenize(sentence)

print(words)

words_tags = nltk.pos_tag(words)

print(words_tags)