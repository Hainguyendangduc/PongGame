import time
from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.tracer(0)

ball = Ball()
paddle_l = Paddle((-480, 0))
paddle_r = Paddle((480, 0))

scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_r.move_up, "Up")
screen.onkey(paddle_r.move_down, "Down")
screen.onkey(paddle_l.move_up, "u")
screen.onkey(paddle_l.move_down, "d")

is_going_on = True
while is_going_on:
    screen.update()
    time.sleep(0.3)
    ball.move()

    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y()

    if ball.xcor() >= 465 and ball.distance(paddle_r) < 50 or ball.xcor() <= -465 and ball.distance(paddle_l) < 50:
        ball.bounce_x()

    if ball.xcor() >= 500:
        scoreboard.left_increase()
        ball.goto(0, 0)
        ball.bounce_x()

    if ball.xcor() <= -500:
        scoreboard.right_increase()
        ball.goto(0, 0)
        ball.bounce_x()

screen.exitonclick()
