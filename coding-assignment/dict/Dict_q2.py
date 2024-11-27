#Count Word Frequency in a String
text = "python is fun and learning python is easy"
word_count = {}

for word in text.split():
    word_count[word] = word_count.get(word, 0) + 1

print("Word Frequency:", word_count)
