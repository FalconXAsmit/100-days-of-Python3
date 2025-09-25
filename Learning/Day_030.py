# FileNotFoundError
# with open("A_text.txt") as file:
#     file.read()

# KeyError
# a_dict = {"key":"value"}
# value = a_dict["non_existent_key"]

# IndexError
# fruits_list = ["Apple", "Banana", "Pear"]
# fruit = fruits_list[3]

# TypeError
# text = "abc"
# print(text + 5)

try:
    file = open("data.txt")
    a_dict = {"key":"value"}
    print(a_dict["key"])

except FileNotFoundError:
    file = open("data.txt", "w")
    file.write("Something")

except KeyError as error_messgae:
    print(f"Key {error_messgae} not found.")

else:
    content = file.read()
    print(content)

finally:
    raise TypeError("My Error. Yippie 🫠")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Are you even Human???")

bmi = weight / height ** 2
print(bmi)
