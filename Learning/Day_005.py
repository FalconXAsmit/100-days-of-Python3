# Loops with Python lists
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")

# Problem Solving
student_score = [150,142,185,120,171,184,149,24,59,68,199,78,65,89,55,91,64,89]

# max_score = max(student_score)
# To replicate this function

max_score = 0
for score in student_score:
    if max_score < score:
        max_score = score

print(max_score)

# For loops with range() function

sum_of_1_to_100 = 0
for num in range(1,101):
    sum_of_1_to_100 += num
print(sum_of_1_to_100)

# Coding Exercise 6
for num in range(1,101):
    if num %3 ==0 and num % 5 ==0:
        print("FizzBuzz")
    elif num %3 == 0:
        print("Fizz")
    elif num %5 == 0:
        print("Buzz")
    else:
        print(num)
