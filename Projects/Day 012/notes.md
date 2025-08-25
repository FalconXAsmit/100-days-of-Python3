# Day 12 Project: Guess the Number

This project is a classic number guessing game where the computer thinks of a number between 1 and 100, and the player has to guess it. The game includes two difficulty levels, which determine the number of guesses the player gets.

### Key Concepts Practiced

The main focus of this project was understanding **variable scope** in Python. It also reinforced the use of functions and constants to write clean, organized code.

#### 1. Scope and Global Constants

This was the first project to really dive into the concept of scope.

* **Local vs. Global Scope**: We learned that variables created inside a function are **local** to that function and can't be accessed outside of it.
* **Global Constants**: Variables that are meant to be used globally and never change (like `EASY_LIVES` and `HARD_LIVES`) are defined at the top level of the script. The convention is to name them in all capital letters to make it clear they are constants.

#### 2. Functions Returning Values

The program was structured around functions that return values to pass information between different parts of the code.

* The `set_difficulty()` function returns the number of turns based on the user's choice.
* The `check_answer()` function takes the user's guess and the current turns, and returns the updated number of turns. This is a clean way to manage the game's state without using global variables.

#### 3. The Secret Difficulty (Easter Egg)

A fun addition to the project was a hidden feature for handling incorrect user input.

* In the `set_difficulty()` function, if the user types anything other than 'easy' or 'hard', the game defaults to a secret, ultra-hard mode with only 3 turns. This is a fun way to handle user input errors and make it my own code.

### Key Takeaways

* **Avoid modifying global variables from within a local scope.** It's generally bad practice and can lead to confusing bugs. It's better to use `return` to pass values out of a function.
* **Use global constants for values that never change.** This makes your code more readable and prevents you from accidentally changing a value that should remain fixed.
* **Thinking about user input errors can lead to creative features.** Adding a "secret" hard mode is a fun way to handle invalid input instead of just showing an error message.
* **No 'const' keyword???** We just capitalize all the letters of the variable we need to use as a const we can change that but don't change those it will be a lot of confusion for you and other as well. Example - `EASY_LIVES` and `HARD_LIVES` 