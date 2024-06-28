## Create turtle race

import turtle
import random

def setup_screen():
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.title("Turtle Race")
    screen.bgcolor("white")

    guess = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: red, orange, yellow, green, blue, indigo, or violet")

    return screen, guess

def create_turtle(color, y_position):
    t = turtle.Turtle(shape="turtle")
    t.color(color)
    t.penup()
    t.goto(-350, y=y_position)
    return t

def start_race(turtles):
    race_on = True
    while race_on:
        for turtle in turtles:
            turtle.forward(random.randint(0, 10))
            if turtle.xcor() >= 380:
                race_on = False
                return turtle

# Turtle colors
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
y_positions = [-150, -100, -50, 0, 50, 100, 150]

screen, player_guess = setup_screen()

turtles = [create_turtle(color, y_position) for color, y_position in zip(colors, y_positions)]

winning_turtle = start_race(turtles)

if player_guess == winning_turtle.color()[0]:
    print(f"You won! The {winning_turtle.color()[0]} turtle is the winner!")
else:
    print(f"You lost! The {winning_turtle.color()[0]} turtle is the winner!")

screen.exitonclick()