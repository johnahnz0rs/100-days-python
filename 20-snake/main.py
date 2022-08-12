from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.turn_up, "Up")
screen.onkey(snake.turn_down, "Down")
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.14)
    snake.move()

    # detect collision w food
    if snake.head.distance(food) < 15:
        food.new_food()
        scoreboard.increase_score()
        snake.grow_snake()

    
    # detect collision w wall
    if snake.head.xcor() > 299 or snake.head.xcor() < -299 or snake.head.ycor() > 299 or snake.head.ycor() < -299:
        # game_is_on = False
        # scoreboard.game_over()
        scoreboard.reset()
        snake.reset()


    # detect collision w tail
    for s in snake.segments[1:]:
        if snake.head.distance(s) < 10:
            # game_is_on = False
            # scoreboard.game_over()
            scoreboard.reset()
            snake.reset()



screen.exitonclick()
