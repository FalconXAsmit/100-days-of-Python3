# Function with Input
# A normal function
def greet():
    print("Hello")
    print("How do you do?")
    print("Isn't the weather nice?")

greet()

# Function that allow input
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
    print("Isn't the weather nice?")

greet_with_name("Asmit")

# Coding exercise 7
def life_in_weeks(age):
    total_weeks = 90*52
    weeks_lived = age*52
    weeks_left = total_weeks - weeks_lived
    print(f"You have {weeks_left} weeks left")

life_in_weeks(12)

# Function with more than one input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"How's life in {location}")

# Positional Argument where position of the values is the same as in the definiton of function and put the values of variable respectively.
# Here "Asmit" goes to name and "Delhi" goes to loaction
greet_with("Asmit","Delhi")

# With positional arguments, the values are assigned to the function's parameters based on their order, so reversing the arguments will change which parameter receives which value.
# greet_with("Delhi","Asmit")

# Keyword argument, here we specify which variable we want to put the value of and it can be anywhere inside ()
greet_with(location="Delhi", name="Asmit")
