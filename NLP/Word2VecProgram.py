
from gensim.models import Word2Vec

# ---------------------------------------------------------
# Step 2: Create Training Dataset
# ---------------------------------------------------------

sentences = [
    ["the", "king", "is", "a", "strong", "man"],
    ["the", "queen", "is", "a", "wise", "woman"],
    ["the", "boy", "is", "a", "young", "man"],
    ["the", "girl", "is", "a", "young", "woman"],
    ["prince", "is", "a", "young", "king"],
    ["princess", "is", "a", "young", "queen"],
    ["man", "is", "strong"],
    ["woman", "is", "beautiful"]
]

print("===========================================================")
print("Training Dataset")
print("===========================================================")

for sentence in sentences:
    print(" ".join(sentence))

# ---------------------------------------------------------
# Step 3: Train Word2Vec Model
# ---------------------------------------------------------

model = Word2Vec(
    sentences=sentences,
    vector_size=5,     # Size of each word vector
    window=5,            # Context window size
    min_count=1,         # Keep every word
    workers=4,           # Number of CPU cores
    sg=1                 # 0 = CBOW, 1 = Skip-Gram
)

print("\nModel Training Completed Successfully.")

# ---------------------------------------------------------
# Step 4: Display Vocabulary
# ---------------------------------------------------------

print("===========================================================")
print("Vocabulary")
print("===========================================================")

print(model.wv.index_to_key)

# ---------------------------------------------------------
# Step 5: Display Word Vector
# ---------------------------------------------------------

print("===========================================================")
print("Word Vector of 'king'")
print("===========================================================")

print(model.wv["king"])

print("===========================================================")
print("Word Vector of 'Queen'")
print("===========================================================")

print(model.wv["queen"])

# ---------------------------------------------------------
# Step 7: Similarity Between Two Words
# ---------------------------------------------------------

print("===========================================================")
print("Similarity Between 'king' and 'queen'")
print("===========================================================")

similarity = model.wv.similarity("king", "queen")

print(similarity)

# ---------------------------------------------------------
# Step 8: Find Similar Words
# ---------------------------------------------------------

print("===========================================================")
print("Most Similar Words to 'king'")
print("===========================================================")

similar_words = model.wv.most_similar("boy")

for word, score in similar_words:
    print(f"{word:12} {score:.4f}")

# ---------------------------------------------------------
# Step 10: Word Analogy
# ---------------------------------------------------------

print("\n" + "=" * 60)
print("Word Analogy")
print("=" * 60)

result = model.wv.most_similar(
    positive=["queen", "man"],
    negative=["woman"],
    topn=1
)

print(result)