from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Which colour will win the race?")
colours = ["red", "orange", "yellow", "purple", "green", "blue"]
turtles = []
y = -100

for i in range(6):
    timmy = Turtle(shape="turtle")
    timmy.color(colours[i])
    timmy.penup()
    timmy.goto(-230,y)
    y += 40
    turtles.append(timmy)

if user_bet:
    is_race_on = True

winner = ""
while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f"You've won! The {winning_colour} turtle won the race.")
            else:
                print(f"You've lost! The {winning_colour} turtle won the race.")
        dist = random.randint(0, 10)
        turtle.forward(dist)
        



screen.exitonclick()