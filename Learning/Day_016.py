# Day 16 Object Oriented Programming (OOPs)
from turtle import Turtle, Screen
from prettytable import PrettyTable

tommy = Turtle()
print(tommy)
tommy.shape("turtle")
tommy.color("coral")
tommy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()


table = PrettyTable()

table.add_column("Pokemon",["Pikachu", "Squirtle","Charmander"])
table.add_column("Types", ["Electric", "Water", "Fire"])
table.align = "l"

print(table)


