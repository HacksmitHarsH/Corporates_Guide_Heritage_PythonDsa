#  sentence as input from the user
sentence = input()

#  sentence into a list of individual words
words = sentence.split()

# empty dictionary to store the word counts
word_counts = {}

#  Loop through each word in the list
for word in words:
    #  word is already in our dictionary, increase its count by 1
    if word in word_counts:
        word_counts[word] += 1
    # new word, add it to the dictionary with a starting count of 1
    else:
        word_counts[word] = 1


for word in word_counts:
    print(word, word_counts[word])