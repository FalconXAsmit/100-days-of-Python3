from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the colour: ")
colour = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colour[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-235,y=y_position[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 235:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f"You've won. {winning_colour} turtle won the race")
            else:
                print(f"You lose, {winning_colour} turtle won the race")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

    

screen.exitonclick()
