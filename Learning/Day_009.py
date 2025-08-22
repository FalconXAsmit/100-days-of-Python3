# Python Dictionary and Nesting
# Dictionary is a data structure that store data as a collection of key-value pairs instead of numerical index like in list
# {key:value}

colour = {
    "apple": "red",
    "pear": "green",
    "banana": "yellow"
}
print(colour["apple"])

colour["blueberry"] = "black"
print(colour)

colour["blueberry"] = "blue"

for fruit in colour:
    print(fruit)
    print(colour[fruit])

# Nested Dictionary

capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

travel_log = {
    "France" : ["Paris", "Lille", "Dijon"],
    "Germany" : ["Stuttgart", "Berlin"]
}

print(travel_log["France"][1])
