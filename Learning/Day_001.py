# First line of python code
print("Hello world!")

# Coding Practice 1(Printing on Console)
print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.")
print("2. Knead the dough for 10 minutes.")
print("3. Add 3g of Salt.")
print("4. Leave to rise for 2 hours.")
print("5. Bake at 200 degrees C for 30 minutes.")

# String Manipulation and Code Intelligence
# # This line prints "Hello world!" twice, each on a new line. where \n is a newline character.
print("Hello world!\nHello world!\nHello world!")
# This line concatenates the strings "Hello" and "FalconX" to form "HelloFalconX". There is no space between the two strings.
print("Hello"+"FalconX")
# This line concatenates the strings "Hello", " ", and "FalconX" to form "Hello FalconX". The space is added between "Hello" and "FalconX".
print("Hello"+" "+"FalconX")
# This line concatenates the string "Hello " (with a space at the end) and "FalconX" to form "Hello FalconX". The space is included in the first string.
print("Hello "+"FalconX")

# Coding Practice 2(Debugging Practice)
# print(Notes from Day 1")
#  print("The print statement is used to output strings")
# print("Strings are strings of characters"
# priint("String Concatenation is done with the + sign")
# print(("New lines can be created with a \ and the letter n")
print("Notes from Day 1") # " marks at the start missing
print("The print statement is used to output strings") # Unnecessary space at the start of the line
print("Strings are strings of characters") # Missing closing paranthesis at the end of the string
print("String Concatenation is done with the + sign")
print("New lines can be created with a \ and the letter n")

# Input function
# This line prompts the user for their name and then prints "Hello " followed by the user's name and the exclamation mark.
print("Hello " + input("What is your name?: ") + "!") 

# Variables
# This line stores the user's input in the variable 'name'.
name = input("What is your name?: ") 
# This line prints the value stored in the variable 'name'.
print(name)
# This line prints the length of the string stored in 'name'.
print(len(input("What is your name?: ")))

# Do the same thing but split the values into different variables
username = input("What is your name?: ")
length = len(username)
print(length)

#Variable Naming Conventions
# 1. Make sure the variable name is descriptive and meaningful.
# 2. Don't have space in between.
# 3. Don't start with a number.
# 4. Don't use specific words like 'print', 'input', 'if', 'else', etc. as variable names.
# 5. Use underscores (_) to separate words in variable names.
# 6. Don't use special characters like @, #, $, %, etc. in variable names.
