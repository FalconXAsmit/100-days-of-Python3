from turtle import Screen, Turtle, colormode
import random

tommy = Turtle()
# Challenge 1 Draw a Square
# tommy.shape("turtle")
# tommy.color("pink")
# for _ in range(4):
#     tommy.forward(100)
#     tommy.left(90)

# Challlenge 2 Draw a Dashed Line
# for _ in range(15):
#     tommy.forward(10)
#     tommy.penup()
#     tommy.forward(10)
#     tommy.pendown()

# Challenge 3 Draw different shapes
# def draw_shape(num_sides):
#     for _ in range(num_sides):
#         angle = 360 / num_sides
#         tommy.forward(100)
#         tommy.right(angle)

# colours = ["royal blue", "lime", "yellow", "firebrick", "maroon", "plum", "deep pink", "indigo", "blue violet", "medium slate blue"]

# for shape_side_n in range(3,11):
#     tommy.color(colours[shape_side_n-3])
#     draw_shape(shape_side_n)

# Challenge 4 Draw a Random walk
# directions = [0, 90, 180, 270]
colormode(255)

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

tommy.speed(0)

# for _ in range(200):
#     tommy.color(random_colour())
#     tommy.forward(30)
#     tommy.setheading(random.choice(directions))

# Challenge 5 Draw a Spirograph
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tommy.color(random_colour())
        tommy.circle(100)
        tommy.setheading(tommy.heading() + size_of_gap)

draw_spirograph(15)

screen = Screen()
screen.exitonclick()
