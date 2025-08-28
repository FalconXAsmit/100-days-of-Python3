# Day 15 Project: The Coffee Machine

This project is a complete simulation of a coin-operated coffee machine. The program manages a set of resources (water, milk, coffee), processes coin payments, checks for sufficient resources and payment, and serves one of three different coffee drinks.

### Key Concepts Practiced

This project was a major step up in complexity, requiring the management of state, data, and money. It was a practical exercise in structuring a larger program with multiple interacting functions.

#### 1. Program Decomposition into Functions

The entire program was broken down into smaller, single-responsibility functions, which is a core concept of professional software development.

* **`is_resource_sufficient()`**: Checks if the machine has enough ingredients.
* **`process_coins()`**: Handles user input for coins and calculates the total value.
* **`is_transaction_successful()`**: Verifies if the user paid enough and handles change.
* **`make_coffee()`**: Deducts the used ingredients from the resources.

#### 2. Managing State with Dictionaries

Dictionaries were the backbone of this project, used to store and modify the machine's state.

* A nested dictionary (`MENU`) was used to store the recipes and costs for each drink.
* A simple dictionary (`resources`) was used to track the current inventory of ingredients. This dictionary was modified throughout the program's execution.

#### 3. Using a Global Variable

To keep track of the money earned, a **global variable** (`profit`) was used.

* The `global` keyword was used inside the `is_transaction_successful()` function to modify the `profit` variable that was defined in the global scope. While not always ideal, this was a practical introduction to the concept.

### Key Takeaways

* **Complex problems are solved by breaking them into small, simple functions.** Each function should do one thing and do it well. This makes the code easier to write, read, and debug.
* **Dictionaries are incredibly powerful for managing program state.** They allow you to store and update related pieces of data (like ingredients or money) in a clean and organized way.
* **Be careful with loop logic and `return` statements.** A misplaced `return` inside a loop can cause the function to exit prematurely, leading to subtle and hard-to-find bugs. This happened while I was running the main project in `is_resource_sufficient` function