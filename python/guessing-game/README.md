# Build a Simple Guessing Game

## This challenge will help you to:

- Break down problems into implementable pseudocode
- Implement a basic Python class and identify when to use instance variables
- Use flow control and iteration where appropriate
- Explain how instance variables and methods represent the characteristics and actions of an object

## Summary

Let's create a simple guessing game. Think in terms of when you were 7 and asked your friends to identify the number you were thinking.

Your `GuessingGame` class should be initialized with an integer called something like `answer` or `answer_number`.

Define an instance method `GuessingGame#guess` (hashtags in documentation generally means it is a method. In our case, `GuessingGame` has a method called `guess`) which takes an integer called `user_guess` as its input. `#guess` should return the string `high` if the `user_guess` is larger than the `answer`, `correct` if the `user_guess` is equal to the `answer`, and `low` if the `user_guess` is lower than the `answer`.

Define an instance method `GuessingGame#solved` which returns `True` if the most recent `user_guess` was correct and `False` otherwise.

For example:

```python
game = GuessingGame(10)

game.solved()   # => False

game.guess(5)  # => 'low'
game.guess(20) # => 'high'
game.solved()   # => False

game.guess(10) # => 'correct'
game.solved()   # => True
```

Or:

```python
import random

game = GuessingGame(random.randint(1,100))
last_guess  = None
last_result = None

While game.solved == False:
  if last_guess not None:
    print(f"Oops! Your last guess ({last_guess}) was {last_result}.")
    print("")

  last_guess  = input("Enter your guess: ")
  last_result = game.guess(last_guess)


print(f"{last_guess} was correct!")
```

