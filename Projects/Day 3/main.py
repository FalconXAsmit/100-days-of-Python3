print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************
''')
print("Welcome to Treasure Island")
print("Your Mission is to find the treasure.")
print("You are at a crossroad where will you go?")
road = input("\tType \"left\" or \"right\"\n").lower()

if road == "right":
    print("You fell into a hole. Game Over")

elif road == "left":
    print("You have come to a lake. There is an island in the middle of the lake.")

    action = input("\tType \"wait\" to wait for a boat or type \"swim\" to swim across\n").lower()
    if action == "swim":
        print("You became food for Piranas in the lake.")
    elif action == "wait":
        print("You arrived at the island unharmed. There are a house with 3 coloured door.")
        door = input("\tOne red, one yellow and one blue. Which colour to choose?\n").lower()
        if door == "red":
            print("Its a room full of fire. GAMEOVER")
        elif door == "yellow":
            print("Its the room full of gold and different treasue. YOU WON")
        elif door == "blue":
            print("Its a room full of beasts. GAMEOVER")
        else:
            print("GAME OVER YOU TYPED WRONG")
    else:
        print("GAME OVER YOU TYPED WRONG")
else:
    print("GAME OVER YOU TYPED WRONG")
