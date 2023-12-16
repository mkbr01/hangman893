# Hangman game #
################

import random

import datetime

class Hangman:
    def __init__(self, word_list):
        self.word_list = word_list
        self.num_lives = 5
        self.selected_word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.selected_word]
        self.num_letters = len(set(self.selected_word))
        self.list_of_guesses = []
        self.start_date = datetime.date(2023, 12, 14)

    def check_guess(self, guess):
        guess = guess.lower()

        if guess in self.list_of_guesses:
            print(f"You already tried that letter! Try a different one.")
            return

        self.list_of_guesses.append(guess)

        if guess in self.selected_word:
            print(f"Good guess! '{guess}' is in the word.")
            for i in range(len(self.selected_word)):
                if self.selected_word[i] == guess:
                    self.word_guessed[i] = guess

            # Reduce the variable num_letters by 1
            self.num_letters = len(set(self.selected_word)) - self.word_guessed.count('_')
        else:
            self.num_lives -= 1
            print(f"Sorry, '{guess}' is not in the word. You have {self.num_lives} lives left.")

        # Display the updated word_guessed
        print("Word Guessed:", ' '.join(self.word_guessed))

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")

            if len(guess) == 1 and guess.isalpha():
                self.check_guess(guess)
                break
            elif len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter! Try a different one.")

    def display_status(self):
        print(f"Word: {' '.join(self.word_guessed)}")
        print(f"Lives left: {self.num_lives}")
        print(f"Letters guessed: {', '.join(self.list_of_guesses)}")

# Create an instance of the Hangman class
hangman_game = Hangman(["raspberry", "pineapple", "peach", "mango", "dragonfruit"])

# Game loop
while hangman_game.num_lives > 0 and hangman_game.num_letters > 0:
    hangman_game.ask_for_input()
    hangman_game.display_status()

# Display the result
if '_' not in hangman_game.word_guessed:
    print("Congratulations! You guessed the word.")
else:
    print(f"Sorry, you ran out of lives. The word was: {hangman_game.selected_word}")

# Display project information
print("\nProject Information:")
print("Project started on:", hangman_game.start_date)

