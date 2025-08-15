# Day 2 for 100 days of code challenge
# Subscripting
# Prints the first character of the string "FalconX". Which is 'F'
print("FalconX"[0]) 
# Print the last character of the string "FalconX". Which is 'X'
print("FalconX"[-1])

# Strings
# Concatenates the strings "123" and "345" to form "123345".
print("123"+"345")

# Integers = Whole numbers + Negative numbers
# Adds the integers 123 and 345 to get 468.
print(123 + 345)

# Large Integers
# This is a large integer with underscores for readability.
print(123_456_789)

# Floats = Decimal numbers
# Adds the float 123.456 and the integer 345 to get 468.456
print(3.14159)

# Booleans = True or False
# This line prints the boolean value True.
print(True)
print(False)

# Write 4 diffrent variables with different data types and check it using type function
# String
s = "FalconX"
# Integer
i = 18
# Float
f = 3.14
# Boolean
b = True

print(type(s)) # This will print <class 'str'>
print(type(i)) # This will print <class 'int'>
print(type(f)) # This will print <class 'float'>
print(type(b)) # This will print <class 'bool'>

# Type Conversion
# Concatenates the strings "123" and "345" to form "123345".
print("123"+"345")
# Converts strings to integers and adds them
print(int("123") + int("345")) 

# Converts the length of the name to a string for concatenation
print("Number of letters in your name is: " + str(len(input("What is your name?: "))))


# Mathematical Operations
print(123+456) # Addition
print(7-3) # Subtraction
print(3*2) # Multiplication
print(6/3) # Division will return a float
print(6//3) # Floor Division will return an integer. This will truncate the decimal part.
print(2**3) # Exponentiation

# PEMDAS
# Paranthesis ()
# Exponents **
# Multiplication * and Division / (from left to right)
# Addition + and Subtraction - (from left to right)

print(3 * 3 + 3 / 3 - 3)


# Coding Exercise 4 - BMI Calculator
height = 1.65 
weight = 84

# Write your code here.
# Calculate the bmi using weight and height.
bmi = weight / height**2

print(bmi)

# Number Manipulation and F-Strings
# Flooring a float number to get the largest integer less than or equal to the number.
print(int(bmi))  # This will print the integer part of the bmi.

print(round(bmi, 2))  # This will round the bmi to 2 decimal places.

# Assignment Operators
score = 0

# User input to increase the score
score += int(input("Enter your score: ")) # This will add the user input to the score.
print(score)

# F-Strings
print(f"Your score is {score}")  # This will print the score using f-strings.
