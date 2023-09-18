import random
import string


class WordGuess:
    tries = {"e": 10, "m": 6, "h": 4}

    def __init__(self, debug=True):
        # are we in debug mode?
        self.debug = debug

        # possible words, selected at random
        self.words = {
            "e": [
                "dog",
                "cat",
                "bug",
                "hat",
                "cap",
                "lit",
                "kin",
                "fan",
                "fin",
                "fun",
                "tan",
                "ten",
                "tin",
                "ton",
            ],
            "m": [
                "plain",
                "claim",
                "brine",
                "crime",
                "alive",
                "bride",
                "skine",
                "drive",
                "slime",
                "stein",
                "jumpy",
            ],
            "h": [
                "machiavellian",
                "prestidigitation",
                "plenipotentiary",
                "quattuordecillion",
                "magnanimous",
                "unencumbered",
                "bioluminescent",
                "circumlocution",
            ],
        }

        # ask the user to set the game mode
        self.mode = self.set_mode()

        self.word = random.choice(
            self.words[self.mode]
        )  # chosen word; players try to guess this
        self.guesses = self.tries[self.mode]  # how many tries the player gets
        self.user_word = list("•" * len(self.word))  # a "blank word" for user output
        self.guessed = []  # keep track of letters that have been guessed

        # debugging?
        if self.debug:
            print(f"Your word is { self.word }.")

            # user messages
            print(f"You have { self.guesses } guesses.")
            print(f"Guess the word: { self.joined_user_word() }")

        # start the first turn
        self.play_turn()

    def joined_user_word(self):
        return "".join(self.user_word)

    def play_turn(self):
        # a turn begins by asking a player for their guess
        letter = self.ask_for_letter()

        # update the word with the letter, maybe
        self.update_user_word(letter)

        # decrement the available guesses
        # unless the letter matches and it's not already in the @guessed array
        self.lose_a_turn(letter)

        # push the letter into the guessed array, if we need to
        self.add_to_guessed(letter)

        # debugging
        print(f"Previous guesses: { ''.join(self.guessed)}")
        print(f"You guessed { letter }. The word is now { self.joined_user_word() }.")
        print(f"You have { self.guesses } guesses left.")

        # determine if the player has won or lost
        if self.won():
            self.end_game(True)
        elif self.lost():
            self.end_game(False)
        else:  # play another turn if we haven't won or lost
            self.play_turn()

    def set_mode(self):
        mode = ""
        while mode not in ["e", "m", "h"]:
            mode = input(
                "\nThis can be (e)asy, (m)edium or really (h)ard. The choice is yours: "
            )
        return mode

    def add_to_guessed(self, letter):
        if letter not in self.guessed:
            self.guessed.append(letter)

    def end_game(self, won):
        if won:
            print("You win the game! Yay! ^␣^")
        else:
            print("You did not win the game :(\nMaybe next time! <3")
        return

    def won(self):
        # we win when the user has guessed all the letters to the word
        return self.word == self.joined_user_word()

    def lost(self):
        # we lose when the user is out of guesses and has not guessed the word
        return not self.won() and self.guesses <= 0

    def lose_a_turn(self, letter):
        # if the guessed letter isn't part of the word and
        # the guessed letter isn't already in the list of guesses
        if letter not in self.word and letter not in self.guessed:
            self.guesses -= 1

    def update_user_word(self, letter):
        for i, l in enumerate(self.word):
            if self.word[i] == letter:
                self.user_word[i] = letter

    def ask_for_letter(self):
        letter = ""
        # we import the string module to give us access to an easy way to create a list of the entire alphabet
        while letter not in list(string.ascii_lowercase):
            letter = input("\nPlease guess a letter! (a..z): ").lower()
        return letter


WordGuess()
