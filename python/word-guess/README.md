# Exercise: Word Guess CSV

The goal of this exercise is to refactor the included `word_guess.py` to get its words from the included `words.csv`.

## Playing the Game

Run `$ python3 word_guess.py` to start the game. Choose a difficulty level and then try to guess the word one letter at a time. You win when you complete the word, and lose if you run out of guesses.

### Debug mode

The `WordGuess` initializer accepts an optional boolean. Pass `True` to put the game in _debug_ mode, which will reveal the chosen word at the beginning of the game.

## Requirements

- Alter the game to get its words from the provided `words.csv`.
- The CSV has three lines. The first entry on each line is the difficulty and every other entry is a word for that difficulty.
  - __Example__: `e,cat,hat,bat,rat,sat,wat,nat,mat....`
  - The `e` is the difficulty (easy mode).
  - Everything else is a word for the easy difficulty
- __The updated program should read the csv and select a random word from the appropriate difficulty.__
- No other game play changes are required.

Adapted from Ada Developer Academy
