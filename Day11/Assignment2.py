text = "python is easy and python is powerful"

# Split the sentence into a list of words
words = text.split()

# Create an empty dictionary to store frequencies
word_freq = {}

# Iterate through the words and count them
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

print(word_freq)