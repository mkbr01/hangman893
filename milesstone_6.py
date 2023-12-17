import random
import datetime

class Hangman:
    def __init__(self, word_pool, max_lives):
        self.word_pool = word_pool
        self.max_lives = max_lives
        self.selected_word = self.choose_random_word()
        self.word_guessed = ['_' for _ in self.selected_word]
        self.remaining_letters = len(set(self.selected_word))
        self.guessed_letters = []
        self.start_date = datetime.date(2023, 12, 14)

#Choose a random word from the word
    def choose_random_word(self):
        return random.choice(self.word_pool)

    def display_repeated_letter_message(self, guessed_letter):
        """Display a message for a repeated letter."""
        print(f"You already tried that one '{guessed_letter}'. Try another.")

    def check_guess(self, guessed_letter):
        """
        Check the guessed letter and update the game state.

        Parameters:
        - guessed_letter (str): The guessed letter.
        """
        guessed_letter = guessed_letter.lower()

        if guessed_letter in self.guessed_letters:
            self.display_repeated_letter_message(guessed_letter)
            return

        self.guessed_letters.append(guessed_letter)

        if guessed_letter in self.selected_word:
            self.handle_correct_guess(guessed_letter)
        else:
            self.handle_incorrect_guess(guessed_letter)

        self.display_word_status()

    def handle_correct_guess(self, correct_letter):
        """
        Handle a correct guess.

        Parameters:
        - correct_letter (str): The correctly guessed letter.
        """
        print(f"Good guess! '{correct_letter}' is in the word.")
        for i in range(len(self.selected_word)):
            if self.selected_word[i] == correct_letter:
                self.word_guessed[i] = correct_letter
                self.remaining_letters -= 1

    def handle_incorrect_guess(self, incorrect_letter):
        """
        Handle an incorrect guess.

        Parameters:
        - incorrect_letter (str): The incorrectly guessed letter.
        """
        self.max_lives -= 1
        print(f"Sorry, '{incorrect_letter}' is not in the word. You have {self.max_lives} lives left.")

    def display_word_status(self):
        """Display the current word status."""
        print("Word Guessed:", ' '.join(self.word_guessed))

# Asks user to input a character
    def ask_for_input(self):
        while True:
            guessed_letter = input("Guess a letter: ")

            if len(guessed_letter) == 1 and guessed_letter.isalpha():
                self.check_guess(guessed_letter)
                break
            elif len(guessed_letter) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guessed_letter in self.guessed_letters:
                print(f"You already tried the letter '{guessed_letter}'. Try a different one.")

    def display_status(self):
        """Display the current game status."""
        print(f"Word: {' '.join(self.word_guessed)}")
        print(f"Lives left: {self.max_lives}")
        print(f"Letters guessed: {', '.join(self.guessed_letters)}")


def play_game(word_pool):
    """
    Play the Hangman game.

    Parameters:
    - word_pool (list): A list of words to choose from.
    """
    max_lives = 5
    game = Hangman(word_pool, max_lives)

    while True:
        if game.max_lives == 0:
            print("You lost!")
            break
        elif game.remaining_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations! You won the game!")
            break

# list of fruit names
word_pool = ["raspberry", "pineapple", "peach", "mango", "dragonfruit"]
# play the game
play_game(word_pool)
