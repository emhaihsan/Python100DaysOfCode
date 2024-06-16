from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Game Ular")
screen.tracer(0)


snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.05)
    
    snake.move()

    

