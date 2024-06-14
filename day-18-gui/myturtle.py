#####Turtle Intro######

import turtle as t
import random

timmy_the_turtle = t.Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")


######## Challenge 1 - Draw a Square ############

# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)


######## Challenge 2 - Draw a dashed line ############

# for _ in range(10):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()


######## Challenge 3 - Draw Shapes ############
# colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "black", "brown", "gray", "purple"]
# def draw_shape(num_sides):
#     timmy_the_turtle.color(random.choice(colors))
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(angle)

# for shape_side_n in range(3, 11):
#     draw_shape(shape_side_n)

######## Challenge 4 - Random Walk ############

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r / 255 , g / 255, b / 255)
    return random_color

# directions = [0, 90, 180, 270]
# timmy_the_turtle.pensize(15)
# timmy_the_turtle.pencolor(random_color())
# timmy_the_turtle.speed("fastest")

# move = True
# while move:
#     timmy_the_turtle.forward(30)
#     timmy_the_turtle.setheading(random.choice(directions))
#     timmy_the_turtle.color(random_color())

#     if timmy_the_turtle.xcor() > 300 or timmy_the_turtle.ycor() > 300 or timmy_the_turtle.xcor() < -300 or timmy_the_turtle.ycor() < -300:
#         move = False


######## Challenge 5 - Spirograph ############

timmy_the_turtle.speed("fastest")
timmy_the_turtle.hideturtle()

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.circle(100)
        timmy_the_turtle.setheading(timmy_the_turtle.heading() + size_of_gap)

draw_spirograph(5)
screen = t.Screen()
screen.exitonclick()