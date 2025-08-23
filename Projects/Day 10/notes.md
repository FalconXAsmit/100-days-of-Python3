# Day 10 Project: Calculator

This project is a fully functional CLI calculator. It can perform addition, subtraction, multiplication, and division. A key feature is its ability to continue calculations using the previous result, allowing for chained operations like `5 * 2 + 8`.

### Key Concepts Practiced

This project was a deep dive into functions that return values, dictionaries, `while` loops, and recursion. It combined these concepts to create a stateful application that remembers the ongoing calculation.

#### 1. Functions with Outputs (`return`)

This was the first major project to heavily use functions that **return** a value.

* Each mathematical operation (`add`, `subtract`, etc.) was its own function that took two numbers as inputs and returned the result.
* This is a core programming concept that allows the output of one function to be used as the input for another, making complex logic possible.

#### 2. Dictionaries for Operations

A major highlight of this project was using a dictionary to map operation symbols (like `"+"`, `"-"`) to their corresponding functions (`add`, `subtract`).

* **`Keys`**: The dictionary keys were the string symbols (`"+"`, `"-"`, `"*"`, `"`/`"`).
* **`Values`**: The values were the actual function names themselves (e.g., `add`).
* This allowed the program to dynamically call the correct function based on the user's input, like this: `operations[operation_symbol](num1, num2)`. It's a clean and scalable way to manage operations.

#### 3. Recursion for a Fresh Start

To allow the user to start a new calculation without stopping and restarting the script, the program uses recursion.
* When the user chooses to start a new calculation, the `calculator()` function calls itself.
* This effectively restarts the entire program flow from the beginning, providing a seamless user experience.

### Key Takeaways

* **`return` is how functions give back results.** This is essential for building programs where different parts need to work together and pass data between them.
* **Dictionaries can store more than just data; they can store functions.** This is a powerful, advanced technique that makes code more flexible and easier to expand.
* **Recursion is a way for a function to call itself.** It's a powerful tool for solving problems that can be broken down into smaller, repeating versions of the same problem, like restarting a calculator.