import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")
image = "Projects/Day 025/blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("Projects/Day 025/50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(
        f"{len(guessed_states)}/50 States Guessed", "What's Another State"
    ).title()
    if answer_state == "Exit":
        missing_states = []
        for states in all_states:
            if states not in guessed_states:
                missing_states.append(states)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("Missing_States.csv")
        break
    elif answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.speed(0)
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x.item()), int(state_data.y.item()))
        t.write(state_data.state.item())

screen.exitonclick()
