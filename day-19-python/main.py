from turtle import Turtle, Screen
import random

colours = ['red', 'blue', 'green', 'purple', 'yellow', 'orange']

is_race_on = False

screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a colour: ")
print(user_bet)

y_positions = [-100, -80, -60, -40, -20, 0]

all_turtles = []

for turt in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colours[turt])
    new_turtle.goto(x=-230, y=y_positions[turt])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You won! {winner} is the winner!")
            else:
                print(f"Tough luck! {winner} is the winner!")
        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)





screen.exitonclick()