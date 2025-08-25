import random
from art import logo

EASY_LIVES = 10
HARD_LIVES = 5

turns = 0

def check_answer(user_input, actual_answer, turns):
    if user_input > actual_answer:
        print("Too High")
        return turns - 1
    elif user_input < actual_answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"You guessed it correctly with {turns} attempts left. The number is {actual_answer}")
        return turns

def set_difficulty():
    difficulty = input("Choose a difficulty. 'easy' or 'hard': ").lower()
    if difficulty == 'easy':
        return EASY_LIVES
    elif difficulty == 'hard':
        return HARD_LIVES
    else:
        print("You typed it wrong. Giving you the Hardest Version Guess in 3 turns")
        return 3

def game():
    print(logo)
    print("Welcome to Guess the Number!")
    print("I am thinking of a number between 1 to 100")
    answer = random.randint(1, 100)

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"you have {turns} attempts left to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You ran out of turns. GAME OVER")
            return False
        elif guess != answer:
            print("Guess Again")

game()
