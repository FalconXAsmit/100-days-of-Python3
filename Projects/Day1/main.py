# This is a simple band name generator script.
# It prompts the user for their city of origin and their pet's name,

# Text to tell the user what is this about.
print("Welcome to the Band Name Generator.")
# Input the user's city and pet name.
city_name = input("What's the name of the city you grew up in?\n")
pet_name = input("What's the name of your pet?\n")
# Combine the city name and pet name and a empty space in between to create a band name.
band_name = city_name + " " + pet_name
# Output the generated band name to the user.
# It then combines these inputs to create a band name and displays it.
print("Your band name could be " + band_name)