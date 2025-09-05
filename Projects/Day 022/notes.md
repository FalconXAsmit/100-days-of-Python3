# Day 22: Building the Pong Game

This project was a major milestone: building a complete, two-player version of the classic arcade game, Pong. The game features two paddles controlled by the players, a ball that bounces off walls and paddles, and a scoring system.

### Key Concepts Practiced

This project was a masterclass in Object-Oriented Programming and game design. It required creating multiple custom classes that interact with each other to form a cohesive game.

#### 1. Advanced OOP Structure

The entire game was broken down into four distinct, logical classes, each managing one component of the game. This separation of concerns is a core principle of good software design.

* **`Paddle` Class**: A blueprint for creating the player paddles. It handles their appearance, initial positioning, and up/down movement.
* **`Ball` Class**: Manages everything about the ball—its appearance, movement, bouncing logic, and what happens when it goes out of bounds.
* **`Scoreboard` Class**: Handles all on-screen text, including displaying the scores for both players and updating them.
* **`main.py`**: Acts as the "director," creating the objects from the classes and defining the main game loop where they all interact.

#### 2. Building Complex Interactions Between Objects

Unlike Snake where objects were part of a whole, Pong's objects are independent and need to be aware of each other.

* **Collision Detection**: The main game loop constantly checks for interactions. We used the `.distance()` method to see if the `ball` object was close to a `paddle` object.
* **Object Communication**: When a paddle missed the ball, the `main.py` script would tell the `ball` object to reset itself and the `scoreboard` object to update the score for the other player. This is a perfect example of how different objects "talk" to each other.

#### 3. Refining Game Feel and Physics

A key part of this project was making the game feel right to play.

* **Bouncing Logic**: The ball's `bounce_y()` and `bounce_x()` methods simply reverse its direction of travel, creating a realistic bounce effect.
* **Increasing Speed**: To make the game more challenging, the `ball.move_speed` attribute is decreased every time it hits a paddle, making the `time.sleep()` in the main loop shorter and thus speeding up the game.

### Key Takeaways

* **Complex applications are built from simple, single-purpose classes.** By creating separate classes for the paddle, ball, and scoreboard, we made a complex problem easy to manage.
* **Game development is about managing the interactions between objects.** The `main.py` file's primary job is to orchestrate how the different game objects behave and react to one another in the main game loop.
* **Small details can have a big impact on gameplay.** Adding a feature to increase the ball's speed over time makes the game more engaging and challenging.