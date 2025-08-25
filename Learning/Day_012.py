# Scope

enemies = 1

# Can be done like this but not recomended
# def increase_enemies():
#     global enemies
#     enemies = "Zombies"
#     print(F"enemies inside function: {enemies}")

# Change any external variable with internal one easily with using return statement
def increase_enemies(enemy):
    print(f"enemies inside function: {enemies}")
    return enemy +1

enemies = increase_enemies(enemies)
print(f"enemies outside function: {enemies}")
