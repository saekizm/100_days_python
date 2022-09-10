from turtle import Screen, Turtle, Screen, back, forward, left, right
import random
import turtle

turtle.colormode(255)

colors = [ (237, 224, 80), (205, 4, 73), (236, 50, 130), (198, 164, 8), (111, 179, 218), (204, 75, 12), (219, 161, 103), (234, 224, 4), (11, 23, 63), (29, 189, 111), (22, 107, 174), (16, 28, 177), (216, 134, 179), (8, 186, 216), (229, 167, 200), (210, 25, 148)]

timmy = Turtle()
timmy.hideturtle()
timmy.speed(0)
timmy.setheading(225)
timmy.penup()
timmy.forward(400)


num_dots = 100

for dot_count in range(1, num_dots + 1):
    timmy.setheading(0)
    timmy.dot(20, random.choice(colors))
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)



screen = Screen()
screen.exitonclick()
