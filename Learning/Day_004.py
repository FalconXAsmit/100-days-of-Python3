# Randomisation
import random

random_integer = random.randint(1, 10)
print(random_integer)

random_number_0_to_1 = random.random() * 7
print(random_number_0_to_1)

random_float = random.uniform(1, 10)
print(random_float)

# A Coin Flip Simulation (Heads or Tails)

flip_value = random.randint(0, 1)
if flip_value == 1:
    print("HEADS")
else:
    print("TAILS")

# Lists in Python :- It is an ordered, mutable (changeable) collection of items, which allows duplicate values and is accessed by index.
states_in_india = [
    "Andhra Pradesh",
    "Assam",
    "Bihar",
    "Karnataka",
    "Kerala",
    "Madhya Pradesh",
    "Odisha",
    "Punjab",
    "Rajasthan",
    "Tamil Nadu",
    "Uttar Pradesh",
    "West Bengal",
    "Andaman and Nicobar Islands",
    "Delhi",
    "Lakshadweep",
    "Gujarat",
    "Maharashtra",
    "Puducherry",
    "Nagaland",
    "HaryanaChandigarh",
    "Himachal Pradesh",
    "Manipur",
    "Meghalaya",
    "Tripura",
    "Sikkim",
    "Arunachal Pradesh",
    "Goa",
    "Mizoram",
    "Chhattisgarh",
    "Jharkhand",
    "Uttarakhand",
    "Telangana",
    "Jammu and Kashmir",
    "Ladakh",
]

print(states_in_india[0])
# Number of states
print(len(states_in_india))
# Adding a new state
states_in_india.append("Dadra and Nagar Haveli and Daman and Diu")
# Removing a state
states_in_india.remove("Lakshadweep")
# Sorting the list
states_in_india.sort()
# Reversing the list
states_in_india.reverse()
# Printing the modified list
print(states_in_india)

# Problem Solving Exercise: Randomly select a person who will pay the bill from a group of friends.
friends = ["Alice", "Bob", "Charlie", "David", "Eve"]
who_pays = random.choice(friends)
print(f"{who_pays} will pay the bill")

# Nested Lists
tic_tac_toe_board = [
    ["X", "O", "X"],
    ["O", "X", "O"], 
    [" ", "O", "X"]
]
middle_square = tic_tac_toe_board[1][1]
print(f"The middle square {middle_square}")
