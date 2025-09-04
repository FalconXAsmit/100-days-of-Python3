# Day 20: Build the Snake Game Part 1

This is the start of another milestone project: building the classic Snake game from scratch. Day 20 focused on creating the foundational components of the game: setting up the screen, creating the snake, and controlling its movement.

### Key Concepts Practiced

This project was a deep dive into OOP, focusing on how to create a custom class to manage a complex game object. It also introduced professional techniques for handling game animations.

#### 1. Creating a Custom Class

The core of the project was building the `Snake` class from scratch. This class is responsible for everything related to the snake itself.

* **Attributes**: The class was initialized with a `segments` attribute (a list to hold the turtle objects that make up the snake's body) and a `head` attribute for easy access to the front of the snake.
* **Methods**: We created methods to give our `Snake` object its abilities, like `create_snake()`, `move()`, and the directional controls (`up()`, `down()`, etc.). This bundles all the snake's logic into one clean, reusable blueprint.

#### 2. Managing Multiple Objects as a Single Entity

The snake isn't one turtle; it's a collection of turtle objects that need to move together seamlessly.

* The `move()` method contained the most complex logic. It uses a `for` loop that iterates backward, moving each segment to the position of the one in front of it before finally moving the head. This creates the classic "follow-the-leader" snake movement.

#### 3. Professional Animation Control

To avoid the choppy, instant movement of the turtle, we took manual control of the game's animation.

* **`screen.tracer(0)`**: This method turns off the automatic screen updates, allowing us to draw everything in the background.
* **`screen.update()`**: This method manually refreshes the screen, showing the new frame.
* By placing `screen.update()` inside the main `while` loop, we create a smooth, controlled animation, essentially building our own game engine.

### Key Takeaways

* **OOP is essential for building games.** Creating a `Snake` class to manage all the snake's properties and behaviors is far cleaner than trying to handle a list of segments with separate functions.
* **Complex movement can be created with simple, clever logic.** The backward-iterating `for` loop is a powerful and efficient solution for making the snake's body follow its head.
* **Controlling the animation loop is key to a smooth game.** Using `tracer(0)` and `update()` gives you full control over the "framerate" of your game, making it look and feel professional.