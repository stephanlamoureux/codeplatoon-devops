from random import randrange


class GuessingGame:
    def __init__(self):
        self.answer = randrange(5)
        self.is_correct = False

    def guess(self, user_guess):
        self.user_guess = user_guess

        if self.user_guess == self.answer:
            self.is_correct = True
            return "Correct!"
        elif self.user_guess < self.answer:
            return "Too Low!"
        elif self.user_guess > self.answer:
            return "Too High!"
        else:
            return "Invalid Input!"

    def solved(self):
        return True if self.is_correct == True else False

# tests
if __name__ == "__main__":
	game = GuessingGame()
	print(game.guess(1))
	print(game.guess(2))
	print(game.guess(3))
	print(game.guess(4))
	print(game.guess(5))
	print(game.solved())
