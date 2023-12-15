import random

# List of words
word_list = ["raspberry", "pineapple", "peach", "mango", "dragonfruit"]

selected_word = random.choice(word_list)

# Function to check if a guess is in the word
def check_guess(guess):
    guess = guess.lower()

    if guess in selected_word:
        print(f"Good guess! '{guess}' is in the word.")
    else:
        print(f"Sorry, '{guess}' is not in the word. Try again.")

# Function to handle user input
def ask_for_input():
    while True:
        guess = input("Guess a letter: ")
        if (len(guess) == 1 and guess.isalpha()):
            check_guess(guess)
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

# Call the ask_for_input function to start the game
ask_for_input()

# Print the selected word
print(f"The selected word was: {selected_word}")

