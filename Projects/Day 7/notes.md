# Day 7 Project: Hangman

This project is a complete, text-based implementation of the classic word-guessing game, Hangman. The program selects a random word, and the player must guess letters to reveal it. The game tracks the player's lives, displaying the state of the hangman using ASCII art with each incorrect guess.

### Key Concepts Practiced

This project was a major step up, combining loops, lists, conditional logic, and modular programming to create an interactive and replayable game.

#### 1. Modular Programming (`import`)

A key professional practice introduced in this project was splitting the code into logical files.

* **`hangman_words.py`**: This file exclusively holds the game's data (the `word_list`).
* **`hangman_art.py`**: This file contains the visual assets, like the `logo` and `stages` list.
* **`main.py`**: This file contains the core game logic and imports the necessary variables from the other modules to bring the game to life.

This separation of concerns makes the code cleaner, more organized, and easier to maintain.

#### 2. The `while` Loop for Game State

Unlike previous projects that ran once, Hangman required a game loop that continues as long as a certain condition is met. The `while not game_over:` loop was used to keep the game running, allowing the player to guess letters turn after turn until they either won or lost.

#### 3. Managing State with Lists

A list was the primary tool for managing the "state" of the game board.

* A `placeholder` list was created with one underscore for each letter in the `chosen_word`.
* When a correct letter was guessed, a `for` loop was used to iterate through the list and replace the underscores at the correct positions. This method is efficient because it directly modifies the game state rather than rebuilding it on every turn.

#### 4. Checking User Input

The program checks if a letter has already been guessed, preventing the player from losing a life for a repeated guess. This was handled by maintaining a `guessed_letters` list and checking if the new `guess` was already in it.

### Key Takeaways

* **Separating data and logic is a core programming principle.** Keeping your word lists and art in separate files makes your main game file cleaner and more focused.
* **`while` loops are essential for creating games** and any other program that needs to run until a specific end condition is met.
* **Lists are powerful tools for managing state.** Using a list to represent the displayed word is an efficient way to track and update the game's progress.
* **Anticipating user behavior** (like guessing the same letter twice) is a key part of building a user-friendly application.