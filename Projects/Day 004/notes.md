# Day 4 Project: Rock, Paper, Scissors

This project is a classic game of Rock, Paper, Scissors played against the computer. The program randomly selects a move, compares it to the player's choice, and determines the winner based on the game's rules.

---

### Key Concepts Practiced

This project combined randomization, data storage in lists, and conditional logic to create a fully functional game.

#### 1. Randomization with the `random` Module

To make the computer's choice unpredictable, we used Python's built-in `random` module.

* `import random`: This line at the top of the script makes the functions from the `random` module available to use.
* `random.randint(a, b)`: This function generates a random integer between `a` and `b` (inclusive). We used `random.randint(0, 2)` to get a random index for our choices list.

```python
# Generate a random integer: 0 for Rock, 1 for Paper, or 2 for Scissors
computer_choice = random.randint(0, 2)
```

#### 2. Using Lists to Store Data

A list was the perfect way to store the ASCII art for the game's choices. This allows us to easily access and display the correct image based on the player's or computer's numerical choice (index).

```python
# The list of ASCII art choices
choices = [rock, paper, scissor]

# Display the human's choice using its index
print("Human choice is:-\n" + choices[human_choice])
```

#### 3. Complex Conditional Logic (`if`/`elif`/`else`)

The core of the game is a chain of `if`, `elif`, and `else` statements that checks all possible outcomes. The logic explicitly defines the conditions for a draw and each of the three ways the player can win.

```python
# Check for a draw first
if human_choice == computer_choice:
    print("It's a draw")
# Check all winning conditions
elif human_choice == 0 and computer_choice == 2: # Rock vs Scissors
    print("You win!")
elif human_choice == 1 and computer_choice == 0: # Paper vs Rock
    print("You won!")
elif human_choice == 2 and computer_choice == 1: # Scissors vs Paper
    print("You won!")
# If it's not a draw and you didn't win, you must have lost
else:
    print("You lose!")
```

#### 4. Input Validation

A key feature of this code is the initial `if` statement that checks if the user's input is valid. By checking for `human_choice >= 3 or human_choice < 0`, the program handles incorrect inputs gracefully instead of crashing, making it more robust.

---

### Key Takeaways

* **Randomisation.** The `random` module is essential for creating unpredictable and replayable games.
* **Lists can store more than just simple data.** Using a list to hold multi-line string art is a great way to organize complex data.
* **Explicit logic is better than clever tricks.** Writing out each winning condition clearly makes the code easier to read, understand, and debug.
* **Always validate user input.** Checking for invalid inputs at the beginning is a best practice that prevents errors and makes your programs more professional. It is a good practice but if you can't, just gloss over it it will be completely explained in the topic exception handeling.