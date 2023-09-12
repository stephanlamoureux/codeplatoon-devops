from guessing_game import GuessingGame

game = GuessingGame()
print("GUESSING GAME")
print("-------------")

while game.solved() == False:
    last_guess  = int(input("Enter your guess: "))
    print(game.guess(last_guess))
