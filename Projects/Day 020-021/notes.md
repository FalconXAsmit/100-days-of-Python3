# Days 20 & 21: Building the Complete Snake Game

This two-day project was dedicated to building the classic Snake game from scratch using OOPs. The final product is a complete, playable game with scoring, collision detection, and a game-over state.

### Key Concepts Practiced

This project was a deep dive into OOP, focusing on how to structure a complex game by breaking it down into logical, interacting classes. It also introduced key game development concepts like inheritance, animation control, and collision detection.

#### 1. Structuring a Game with OOP

The entire game was built around three custom classes, each with a single, clear responsibility. This is the core of good OOP design.

* **`Snake` Class**: Manages everything related to the snake itself—creating the segments, handling movement, extending the body, and responding to key presses.

* **`Food` Class**: Responsible for the food pellet, including its appearance and repositioning itself randomly.

* **`Scoreboard` Class**: Handles all on-screen text, such as displaying the current score and the "GAME OVER" message.

#### 2. Class Inheritance

A major new OOP concept was **inheritance**. This allows a new class (child) to take on all the attributes and methods of an existing class (parent).

* Both the `Food` and `Scoreboard` classes inherited from the `Turtle` class (e.g., `class Food(Turtle):`).

* This is incredibly powerful because it means our objects are instantly equipped with all of Turtle's abilities (like `.goto()`, `.color()`, etc.), while still having their own specialized methods like `food.refresh()` or `scoreboard.increase_score()`.

#### 3. Professional Animation Control

To create a smooth visual experience, we took manual control of the game's animation loop.

* **`screen.tracer(0)`**: This turns off the default automatic animations.

* **`screen.update()`**: This manually refreshes the screen.

* By putting `screen.update()` and a `time.sleep()` inside the main `while` loop, we created a stable "game engine" that runs at a consistent frame rate, making the game look and feel professional.

#### 4. Collision Detection & Slicing

The game's logic is driven by detecting collisions between objects.

* **With Food**: The `.distance()` method was used to check if the snake's head was close enough to the food to "eat" it.

* **With the Wall**: A simple `if` statement checked if the snake's head `xcor()` or `ycor()` went beyond the screen boundaries.

* **With the Tail**: A `for` loop checked the distance between the snake's head and every other segment in its body. A crucial technique here was **list slicing** (`snake.segment[1:]`) to ensure we didn't check the head against itself, which would cause an instant game over.

### Key Takeaways

* **OOP is essential for building complex games.** Breaking the problem down into self-contained classes (`Snake`, `Food`, `Scoreboard`) makes the code infinitely more organized and easier to manage.

* **Inheritance prevents you from reinventing the wheel.** By inheriting from `Turtle`, we got a huge amount of functionality for free.

* **A controlled game loop is the heart of any game.** Manually updating the screen with `tracer()` gives you full control over the timing and feel of your game.

* **Slicing is a powerful tool for avoiding common bugs.** Using it to exclude the snake's head during tail collision detection is a perfect example of thinking ahead to prevent logical errors.