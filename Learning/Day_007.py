# Day 7 about learning to make a hangman project
import random

stages = [
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
]

word_list = ["aardvark", "baboon", "camel"]

lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

# You created a string of underscores
placeholder = "".join("_" * len(chosen_word))
print(placeholder)

user_guessed_word = list(placeholder)

game_over = False

while not game_over:
    guess = input("Enter your guess:- ").lower()
    for letter in range(len(user_guessed_word)):
        if chosen_word[letter] == guess:
            user_guessed_word[letter] = guess

    display = "".join(user_guessed_word)
    print(display)

    if guess not in user_guessed_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose💀")

    if "_" not in display:
        game_over = True
        print("You win!")
    
    print(stages[lives])
