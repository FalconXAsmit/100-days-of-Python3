# Importing required modules and our art and word list
import random
from hangman_art import stages, logo
from hangman_words import word_list

# Printing the hangman logo
print(logo)

# Specifying the lives
lives = 6

# Selecting a word our of the random words
chosen_word = random.choice(word_list)

# Creating a list of the number of underscores the chosen word have
placeholder = ["_"] * len(chosen_word)
print(f"The given word is{' '.join(placeholder)}")


# To prevent repeated guess of same letter
guessed_letters = []

# Main logic
game_over = False
while not game_over:
    # Printing the number of lives user have
    print(
        f"***************************************************{lives}/6 LIVES LEFT******************************************************"
    )

    # Taking the guess from the user
    guess = input("Enter your guess:- ").lower()

    # Checking if user have already guessed it
    if guess in guessed_letters:
        print("Letter already guessed, try another letter")
        continue
    else:
        guessed_letters.append(guess)

    # Checking the guess if its in the word or not
    for letter in range(len(placeholder)):
        if chosen_word[letter] == guess:
            placeholder[letter] = guess

    # Making the display string seperately
    display = "".join(placeholder)
    print(display)

    # ASCII ART of the stages of the game
    print(stages[lives])

    # Lives deducting if not guessed the right letter
    if guess not in chosen_word:
        print(f"The letter '{guess}' is not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_over = True
            print(
                "**************************************************You lose💀**************************************************"
            )

    # Winning condition of the user
    if "_" not in display:
        game_over = True
        print(
            "**************************************************You win!🎉**************************************************"
        )

print(f"The word was {chosen_word}")
