import random

def get_valid_single_letter():
    """Get and validate user input for a single letter."""
    guess = input("Enter a single letter: ")
    if len(guess) == 1 and guess.isalpha():
        print("Good guess!")
        return guess
    else:
        print("Oops! That is not a valid input.")
        return None

# List of words
word_list = ["raspberry", "pineapple", "peach", "mango", "dragonfruit"]

# Get and validate user input
guess = get_valid_single_letter()

# Randomly select a word from the list
selected_word = random.choice(word_list)

print(selected_word)
