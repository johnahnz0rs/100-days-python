from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)


l_paddle = Paddle(-350,0)
r_paddle = Paddle(350,0)
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")




game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision w top or bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision w either paddle
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_x()

    #detect miss by r_paddle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    #detect miss by l_paddle
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        





screen.exitonclick()
