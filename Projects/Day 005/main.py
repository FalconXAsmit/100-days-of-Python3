# random module for creating randomised passwords
import random

# Characters usually accepted in any password on any website
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("A Basic yet Powerful Password Generator")
# user input for data like number of alphanumeric and symbol characters
pass_letters = int(input("How many letters do you like in your passwords\n"))
pass_numbers = int(input("How many numbers do you like in your passwords\n"))
pass_symbols = int(input("How many symbols do you like in your passwords\n"))

# Main Logic of this prroject
password_list = []

# Adding random characters to the password list
for i in range(pass_letters):
    password_list.append(random.choice(letters))
for i in range(pass_numbers):
    password_list.append(random.choice(numbers))
for i in range(pass_symbols):
    password_list.append(random.choice(symbols))
# Shuffeling the password list to make it even more random
random.shuffle(password_list)
# Making the list a string 
final_password = "".join(password_list)

# Displaying the final password
print(f"Your password can be:-{final_password}")
