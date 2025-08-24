# Day 11 Capstone Project: Blackjack

This is the first capstone project, a complete command-line Blackjack game. The player competes against an automated dealer (the computer). The game follows standard Blackjack rules, including handling Aces as 1 or 11, and the dealer hitting until their score is 17 or higher.

### Key Concepts Practiced

This project was a major milestone, combining all previously learned concepts—functions, loops, conditionals, and data structures—to build a complex, interactive game from the ground up.

#### 1. Functions with Outputs (`return`)

The entire program was built around functions that return values, allowing for clean, modular, and reusable code.

* **`deal_card()`**: Returns a single random card.
* **`calculate_score()`**: Takes a list of cards as input and returns the calculated score. This function contained complex logic to handle Blackjacks and the dual value of an Ace.
* **`compare()`**: Takes the final scores of the user and computer, and returns a string declaring the winner.

#### 2. Complex Conditional Logic

The project required intricate `if/elif/else` chains to handle the many rules and outcomes of Blackjack.

* The `calculate_score` function had to check for a Blackjack (a score of 21 with two cards), and also check if an Ace should be counted as 1 or 11.
* The `compare` function was a large set of conditionals that covered every possible win, loss, or draw scenario.

#### 3. Game State Management with Loops

A `while` loop was used to manage the "state" of the game, continuing the player's turn as long as they chose to "hit" and their score was under 21.

* A boolean flag (`is_game_over`) controlled the main game loop, ensuring the game continued until a win condition or a bust was met.

### Key Takeaways

* **Capstone projects integrate all your skills.** This wasn't about learning one new thing, but about proving me that I can combine everything I've learned to build something substantial.
* **Breaking down a complex problem into smaller functions is essential.** Trying to build the whole game in one block of code would be nearly impossible. Functions like `deal_card` and `calculate_score` make the problem manageable.
* **Careful planning of logic is crucial.** A game like Blackjack has many specific rules. Mapping out all the possible outcomes and conditions *before* coding is a key step to success.
