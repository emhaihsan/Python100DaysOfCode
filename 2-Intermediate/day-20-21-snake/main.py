from turtle import Screen
from snake import Snake
from food import Food
from score import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Game Ular")
screen.tracer(0)


snake = Snake()
food = Food()
score = ScoreBoard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    score.update_scoreboard()
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.getFood()
        score.increase_score()

    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        game_on = False
        score.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()

screen.exitonclick()

    

