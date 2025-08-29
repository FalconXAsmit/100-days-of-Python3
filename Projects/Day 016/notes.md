# Day 16: Object-Oriented Programming (OOP)

Today marks the beginning of intermediate Python with the introduction of a new programming paradigm: Object-Oriented Programming (OOP). Instead of just writing functions, we now model real-world things as Objects, which have their own data (attributes) and functions (methods).

### Key Concepts Practiced

The entire Coffee Machine project from Day 15 was refactored from procedural code into an OOP structure. This demonstrates how OOP can be used to organize complex projects into clean, logical, and reusable components.

#### 1. Classes and Objects

The core of OOP is the Class, which acts as a blueprint, and the Object, which is the actual instance created from that blueprint.

* **Classes**: We created several classes, each with a specific responsibility: `CoffeeMaker`, `MoneyMachine`, `Menu`, and `MenuItem`.
* **Objects**: In `main.py`, we created objects from these classes (e.g., `coffee_maker = CoffeeMaker()`). Each object is an independent instance with its own data.

#### 2. Attributes and Methods

Objects hold their own data and have their own functions.

* **Attributes**: These are the variables associated with an object (e.g., the `CoffeeMaker` object has a `resources` attribute, which is a dictionary).
* **Methods**: These are the functions that an object can perform (e.g., the `MoneyMachine` object has a `report()` method and a `make_payment()` method).

#### 3. Modular Code with Classes

OOP takes the idea of modular programming to the next level. Instead of just separating data into different files, we separated entire chunks of functionality into self-contained classes.

* The `CoffeeMaker` class handles everything related to ingredients.
* The `MoneyMachine` class handles everything related to payments.
* The `Menu` class handles everything related to the available drinks.
* This makes the `main.py` file incredibly simple and easy to read, as it only needs to call methods on the created objects.

### Key Takeaways

* **OOP helps organize complex code.** By modeling a problem as a set of interacting objects, you can manage complexity and make your code easier to understand and maintain.
* **Classes are blueprints for creating consistent objects.** Every object created from the `CoffeeMaker` class will start with the same resources, ensuring predictable behavior.
* **Objects bundle data and functionality together.** An object doesn't just hold data (attributes); it knows what it can do with that data (methods).