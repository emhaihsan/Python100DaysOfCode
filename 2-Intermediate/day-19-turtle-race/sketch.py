import turtle

screen = turtle.Screen()
screen.title("Etch a Sketch")

t = turtle.Turtle()
t.speed(0)

def move_forward():
    t.forward(10)

def move_backward():
    t.backward(10)

def turn_left():
    t.left(10)

def turn_right():
    t.right(10)

def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

screen.onkey(move_forward, 'w')
screen.onkey(move_backward, 's')
screen.onkey(turn_left, 'a')
screen.onkey(turn_right, 'd')
screen.onkey(clear, 'c')

screen.listen()
screen.mainloop()