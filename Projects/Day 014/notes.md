# Day 14 Project: Higher Lower Game

This project is a fully interactive "Higher Lower" guessing game. The program presents the player with two options from a dataset, and the player must guess which one has more Instagram followers. The game continues with the winner of the previous round until the player guesses incorrectly.

### Key Concepts Practiced

This was the first project built entirely from scratch without any given TODOs for what problem to tackle first then second and third. The focus was on problem decomposition: breaking a large problem down into smaller, manageable steps.

#### 1. Decomposing the Problem

Instead of following instructions, this project required thinking like a developer. The problem was broken down into logical steps:

* Fetch two random accounts from the data.
* Format and display the accounts to the user.
* Ask the user for their guess.
* Check if the user's guess is correct by comparing follower counts.
* Update the score and continue the game with the winner.
* End the game when the user is wrong.

#### 2. Working with Nested Data Structures

The game's data was stored in a list of dictionaries. This required accessing nested data by using multiple keys.

* To get a person's name, the syntax was `account['name']`.
* To get their follower count, it was `account['follower_count']`.

#### 3. Writing Robust Logic

A key part of building from scratch is anticipating potential issues.

* To prevent the game from picking the same account for both options, a **`while` loop** was used. This is more robust than a simple `if` statement because it guarantees the two choices will be different, even if the random choice is the same multiple times in a row.

#### 4. Managing Game State

The flow of the game was controlled by a main `while` loop and a few key variables.

* A `score` variable was used to keep track of the player's progress.
* A boolean flag, `game_over`, controlled the main game loop, ensuring it continued as long as the player was guessing correctly.

### Key Takeaways

* **Breaking down complex program into simple TODOs and then completing one at a time.** Breaking a big project into small, logical steps is the key to solving any complex problem.
* **Thinking about edge cases makes your code stronger.** Using a `while` loop to prevent duplicate choices is a perfect example of writing reliable, bug-resistant code.
* **Clear variable names are crucial.** Using names like `account_a`, `a_followers`, and `is_correct` makes the code self-explanatory and easier to debug.