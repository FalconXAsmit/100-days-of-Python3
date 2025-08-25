# Day 3 Project: Treasure Island

This project is a classic "Choose Your Own Adventure" game that runs in the terminal. The player makes a series of choices that determine the outcome of the story, leading to either treasure or a game over. The awesome ASCII art at the start sets the mood for an adventure!

---

### Key Concepts Practiced

This project was a deep dive into using conditional logic to control the flow of a program and create a dynamic, interactive experience.

#### 1. Conditional Logic (`if`/`elif`/`else`)

The entire game is built on a foundation of `if`, `elif`, and `else` statements. The very first choice the player makes splits the path of the game into two main branches.

```python
# The first choice in the game
road = input("\tType \"left\" or \"right\"\n").lower()

if road == "right":
    print("You fell into a hole. Game Over")
elif road == "left":
  # The adventure continues down this path....
```

#### 2. Nested `if/else` Statements

To create the branching narrative with multiple steps, we use **nested conditionals**. This means putting an `if/elif/else` block inside another `if` block. This allows for a sequence of choices, where each choice depends on the one made before it.

```python
# This is a nested conditional block
elif road == "left":
    action = input("\tType \"wait\" or type \"swim\"...\n").lower()
    if action == "wait":
        # The story continues to the next level of nesting...
        door = input("\tWhich colour to choose?\n").lower()
        if door == "yellow":
            print("...YOU WON")
        else:
            print("...GAMEOVER")
```

#### 3. Handling User Input with `.lower()`

When dealing with user input, you can't predict if they will type "Left", "left", or "LEFT". To make the game work regardless of capitalization, the `.lower()` string method was used. This method converts the user's input to all lowercase letters before it's checked, making the code more robust.

```python
# .lower() ensures "Left", "LEFT", and "left" are all treated the same
road = input("\tType \"left\" or \"right\"\n").lower()
```

#### 4. Catching Invalid Input

The final `else` statements in each nested block act as a safety net. They catch any input that doesn't match the expected choices ("left", "right", "wait", "swim", etc.) and end the game, preventing errors.

```python
# This else block catches any door color that isn't red, yellow, or blue
else:
    print("GAME OVER YOU TYPED WRONG")
```

---

### Key Takeaways

* **Conditional logic is the core of interactivity.** `if/else` statements are the primary tool for making a program respond to different user choices.
* **Nesting creates depth.** By placing `if` statements inside other `if` statements, you can build complex, branching paths in a story or program.
* **Always sanitize user input.** Using methods like `.lower()` makes your code more reliable and prevents errors caused by unexpected capitalization.
* **Plan for the unexpected.** Using a final `else` to handle invalid inputs is a key part of writing robust programs.