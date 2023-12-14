import random

# Get user input for a single letter
guess = input("Enter a single letter: ")

# Check if the input is a valid single letter
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")

# List of words
word_list = ["raspberry", "pineapple", "peach", "mango", "dragonfruit"]

# Randomly select a word from the list
selected_word = random.choice(word_list)

print(selected_word)