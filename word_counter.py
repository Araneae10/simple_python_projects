# enter the words to count
words = input("enter the words:")

# sentence ko words haru lai '' le split handincha
words_split = words.split(' ')

# words haru count gare ra word_count ma save hancha
word_count = len(words_split)

# prints the results
print(f"Number of words: {words_split}")

    