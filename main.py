import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
turtle_object = Turtle()
turtle_object.shape("turtle")
screen.colormode(255)
color_list = [(184, 147, 94), (151, 104, 46), (178, 150, 22), (83, 34, 27), (12, 57, 73), (31, 100, 120), (101, 41, 47)]

# hide turtle image
turtle_object.hideturtle()
# take turtle to top left position
turtle_object.penup()
turtle_object.left(153)
turtle_object.forward(800)
turtle_object.setheading(0)
turtle_object.pendown()
turtle_object.speed(100)

# draw spots
for i in range(10):
    for _ in range(10):
        turtle_object.dot(20, random.choice(color_list))
        turtle_object.penup()
        turtle_object.forward(50)

    # set turtle back to starting position
    turtle_object.setheading(270)
    turtle_object.forward(50)
    turtle_object.setheading(180)
    turtle_object.forward(500)
    turtle_object.setheading(0)


screen.exitonclick()
