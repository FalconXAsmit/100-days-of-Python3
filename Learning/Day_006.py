# Function - A function is a reusable block of code that performs a specific, named task.
# There are two types of fucntion:-
# Build-in :- they are already in python and we can use directly like print(), len(), int(), etc
print("Hello World!")
len("Hello World!")
# Programmer Defined :- they are defined by the programmer to be able to call further in code rather than to type whole logic again and again
def my_func():
    print("Hello")
    print("Bye")

my_func()

# While Loops
number = 5

print("Starting countdown...")

# The loop will continue as long as 'number' is greater than 0.
while number > 0:
    print(number)
    # We decrease the number by 1 in each loop.
    # Without this, the loop would run forever (an infinite loop).
    number -= 1

# This code runs only AFTER the loop's condition becomes False.
print("Blast off! 🚀")
