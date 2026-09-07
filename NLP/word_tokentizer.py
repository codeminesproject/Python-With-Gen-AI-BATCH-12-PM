"""
install nltk

pip install nltk

nltk - natural language tool kit
"""

from nltk import word_tokenize


description = "There are now 1,301 confirmed dead and 5,339 still missing in Nepal and Tibet following the deadly flash flooding nine days ago. That figure includes 1,280 dead and 4,798 missing in Nepal, in the latest update from the country's police service. On the Tibet side, officials confirmed at a press conference yesterday that the death toll has increased to 21, with 541 still unaccounted for. Hundreds of foreigners are believed to be among those missing, from at least 34 countries. Rescue operations are taking place at half a dozen hydropower tunnels in Nepal in which more than 150 people are feared trapped."

print(description)

print("-----------------------------------------------------------")

words = word_tokenize(description)

print("no of words in paragraph:",len(words))

for word in words:
    print(word)