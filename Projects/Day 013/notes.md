# Day 13: Debugging

This day was different from the others. Instead of building a new project from scratch, the focus was on a crucial and practical skill for every developer: **debugging**. The goal was to take existing pieces of broken code, identify the errors, and fix them.

### Key Concepts Practiced

The entire day was an exercise in reading, understanding, and fixing code written by others. It teaches to look for common types of errors and think critically about program flow.

#### 1. Spotting Syntax vs. Logic Errors

The exercises covered different types of bugs🐞:

* **Odd or Even:** This was a classic **syntax error**. The code used a single equals sign (`=`), which is for assigning values, instead of a double equals sign (`==`), which is for checking equality. The Python interpreter can't even run the code correctly with this error.
* **Leap Year:** This was a **logical error**. The code ran without crashing, but it produced the wrong output because the logic was flawed (it checked for divisibility by 4000 instead of 400). These can be trickier to find because the program work but its not *logically correct*.

#### 2. Understanding Control Flow (`if` vs. `elif`)

The FizzBuzz problem was a great example of a **Control flow bug🐞**.

* The original code used a series of separate `if` statements. This meant that for a number like 15, it would print "FizzBuzz," then "Fizz," and then "Buzz," because it met all three conditions independently.
* The fix was to restructure the code into a proper `if/elif/else` chain. This ensures that only **one** block of code is executed for any given number, which is the correct logic for the game.

### Key Takeaways

* **Debugging is a core developer skill.** Writing code is only half the work; finding and fixing bugs is the other half.
* **Pay close attention to operators.** A single character, like the difference between `=` and `==`, can completely change how a program behaves.
* **The structure of your conditionals matters.** Using `if/elif/else` correctly is essential for creating logic that behaves as you expect and avoids unintended multiple outputs.