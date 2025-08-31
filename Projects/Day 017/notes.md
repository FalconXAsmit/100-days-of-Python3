# Day 17 Project: The Quiz Game

This project is a command-line quiz game that pulls questions and answers from a ([data source](https://opentdb.com)). The game asks the user a series of true/false questions, keeps track of their score, and provides a final score at the end.

### Key Concepts Practiced

This project was the first real deep dive into creating custom classes from scratch. It is all about modeling the different parts of a problem (the questions, the quiz logic) as separate, interacting objects.

#### 1. Creating Classes From Scratch

The core of the project was building our own blueprints for the different parts of the quiz.

* **`Question` Class**: A simple class to model a single question. Its job was to have two attributes: `text` and `answer`. This is a great example of how a class can be used to create your own custom data type.
* **`QuizBrain` Class**: A more complex class designed to manage the logic of the quiz. It had attributes to track the `question_number` and `score`, and methods to run the game.

#### 2. Working with Attributes and Methods

We defined initial "factory settings" for our objects using the `__init__()` constructor.

* **Attributes**: The `QuizBrain` was initialized with a list of question objects and started the `question_number` and `score` at 0.
* **Methods**: We created methods to give our `QuizBrain` object abilities.
    * `next_question()`: Fetches the next question from the list.
    * `still_has_questions()`: Checks if the quiz is over.
    * `check_answer()`: Compares the user's answer to the correct one and updates the score.

#### 3. Modeling a Problem with OOP

This project showed how to take a real-world problem and break it down into logical objects. Instead of one giant script, we had:
* `data.py` (The raw information)
* `question_model.py` (The blueprint for a single question)
* `quiz_brain.py` (The engine that runs the quiz)
* `main.py` (The file that puts all the pieces together)

This separation makes the code incredibly clean and easy to understand.

### Key Takeaways

* **Classes let you create your own custom data types.** A "Question" is now a thing your program understands, just like a string or an integer.
* **Breaking a problem down into classes makes your code more organized.** Each class has one job, which makes debugging and adding new features much easier.
* **Attributes track an object's state, while methods define its behavior.** This is the fundamental concept that makes OOP so powerful.
* **Modularity** Object Oriented Programming provides modularity, I changed my dataset in `data.py` and just have to change 2 data in `main.py` for it to take the new data it makes writing complex problems easier. 