###########
# Hangman #
###########



import random
import datetime

class Hangman:
    def __init__(self, word_list, num_lives):
        self.word_list = word_list
        self.num_lives = num_lives
        self.selected_word = self.choose_random_word()
        self.word_guessed = ['_' for _ in self.selected_word]
        self.remaining_letters = len(set(self.selected_word))
        self.list_of_guesses = []
        self.start_date = datetime.date(2023, 12, 14)

    def choose_random_word(self):
        return random.choice(self.word_list)

    def check_guess(self, guessed_letter):
        guessed_letter = guessed_letter.lower()

        if guessed_letter in self.list_of_guesses:
            print(f"You already tried the letter '{guessed_letter}'. Try a different one.")
            return

        self.list_of_guesses.append(guessed_letter)

        if guessed_letter in self.selected_word:
            self.handle_correct_guess(guessed_letter)
        else:
            self.handle_incorrect_guess(guessed_letter)

        self.display_word_status()

    def handle_correct_guess(self, correct_letter):
        print(f"Good guess! '{correct_letter}' is in the word.")
        for i in range(len(self.selected_word)):
            if self.selected_word[i] == correct_letter:
                self.word_guessed[i] = correct_letter
                self.remaining_letters -= 1

    def handle_incorrect_guess(self, incorrect_letter):
        self.num_lives -= 1
        print(f"Sorry, '{incorrect_letter}' is not in the word. You have {self.num_lives} lives left.")

    def display_word_status(self):
        print("Word Guessed:", ' '.join(self.word_guessed))

    def ask_for_input(self):
        while True:
            guessed_letter = input("Guess a letter: ")

            if len(guessed_letter) == 1 and guessed_letter.isalpha():
                self.check_guess(guessed_letter)
                break
            elif len(guessed_letter) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guessed_letter in self.list_of_guesses:
                print(f"You already tried the letter '{guessed_letter}'. Try a different one.")

    def display_status(self):
        print(f"Word: {' '.join(self.word_guessed)}")
        print(f"Lives left: {self.num_lives}")
        print(f"Letters guessed: {', '.join(self.list_of_guesses)}")


def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.remaining_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations! You won the game!")
            break

# list of fruit names
word_list = ["raspberry", "pineapple", "peach", "mango", "dragonfruit"]
# play the game
play_game(word_list)


