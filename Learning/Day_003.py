# Modulo Operator(%):- Gives the remainder of a division operation
# Example: 5 % 2 = 1, because 5 divided by 2
print("5 % 2 =", 5 % 2)

# A Problem
# Check Odd and Even
num = int(input("Enter the number:- "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# If/else statement, Nested if/else statement, Multipls if statements and Logical operator
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Child tickets are $5.")
        bill += 5
    elif 45 <=  age <= 55:
        print("You will get a free ticket.")
    elif age <= 18:
        print("Youth tickets are $7.")
        bill += 7
    else:
        print("Adult tickets are $12.")
        bill += 12
    wants_photo = input("Do you want to have a photo take? type y for Yes and n for No")
    if wants_photo.lower() == "y":
        bill += 3
    print(f"Your total bill is ${bill}")

else:
    print("You can not ride the rollercoaster!")

# Coding Exercise 5
# BMI Calculator with Interpretations
weight = 85
height = 1.85
bmi = weight / (height**2)
if bmi < 18.5:
    print("underweight")
elif bmi < 25:
    print("normal weight")
else:
    print("overweight")

# Write a pizza delivery program
print("Welcome to Pizza Deliveries!")
size = input("Enter the size of your pizza(S,M or L):- ")
pepperoni = input("Do you want pepperoni in your pizza?(Y for yes and N for No):- ")
extra_cheese = input(
    "Do you want extra cheese in your pizza?(Y for yes and N for No):- "
)
bill = 0

if size.upper() == "S":
    bill += 15
elif size.upper() == "M":
    bill += 20
elif size.upper() == "L":
    bill += 25
else:
    print("Enter a given size")
    exit()

if pepperoni.upper() == "Y":
    if size.upper() == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese.upper() == "Y":
    bill += 1

print(f"Your total bill is ${bill}")

# Logical Operators (and, or, not):- these operators are used to combine conditional statements
# Example: and operator returns True if both conditions are True, or operator returns True if at least one condition is True, not operator returns True if the condition is False
# Example: 5 > 3 and 2 < 4 returns True, 5 > 3 or 2 < 4 returns True, not(5 > 3) returns False