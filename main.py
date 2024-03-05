from random import randint
from art import logo

EASY_LEVEL = 10
HARD_LEVEL = 5

#function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")

#function to set difficulty.
def set_difficulty():
   level = input("Choose a difficulty. Type 'easy' or 'hard': ")
   if level == "easy":
      return EASY_LEVEL
   else:
      return HARD_LEVEL

def game():
    print(logo)
    #choosing a random number between 1 and 100.
    print("\nWelcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    turns = set_difficulty()
    #repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"\nYou have {turns} attempts remaining to guess the number.")
        #let the user guess a number.
        guess = int(input("Make a guess: "))
        #track the number of turns and reduce by 1 if they get it wrong.
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")

game_start = input("Would you like to play the number guessing game? Type 'y' to start or 'n' to exit: ")
if game_start == 'y':
    game()
else:
    print("Goodbye! Have a nice day!")
    exit()

