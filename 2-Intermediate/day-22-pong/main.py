# main.py
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import ScoreBoard
import time
# Set up the screen
screen = Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(90)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
r_score = ScoreBoard((50, 250))
l_score = ScoreBoard((-50, 250))
ball = Ball()
ball.move()
screen.listen()

screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")

game_on = True

while game_on:  
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.position()[1] > 280 or ball.position()[1] < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.reset_position()
        l_score.increase_score()
    if ball.xcor() < -380:
        ball.reset_position()
        r_score.increase_score()
