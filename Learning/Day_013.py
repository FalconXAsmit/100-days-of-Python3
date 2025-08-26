# Debugging
import random

# Problem 1

# def my_function():
#     for i in range(1, 20):
#         if i == 20:
#             print("You got it")

def my_function():
    for i in range(1,21):
        if i == 20:
            print("You got it")
my_function()

# Problem 2 

# dice_number = [1,2,3,4,5,6]
# dice_num = random.randint(1,6)
# print(dice_number[dice_num])

dice_number = [1,2,3,4,5,6]
dice_num = random.randint(0,5)
print(dice_number[dice_num])

# Problem 3

# year = int(input("What's your birth year?: "))
# if year > 1980 and year < 1994:
#     print("You are a millennial.")
# elif year > 1994:
#     print("You are a Gen Z.")

year = int(input("What's your birth year?: "))
if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year >= 1994:
    print("You are a Gen Z.")

# Problem 4

# age = int(input("What is your age?: "))
# if age>18:
# print(f"You can drive at age {age}")

# try-except is a way of error handeling. It runs the try block of code and if it encounter some error we mentioned in except part it won't show error but show the code block we wrote inside it
try:
    age = int(input("What is your age?: "))
except ValueError:
    print("Invalid input. Try again with a numeric number like 18")

if age >= 18:
    print(f"You can drive at age {age}.")

# Problem 5

# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)


# Using Debugger and Problem 6

def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1,3)
        new_item += item
        b_list.append(new_item)
    print(b_list)
mutate([1,2,3,5,8,13])

