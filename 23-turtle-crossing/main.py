import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager(20)
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.move_cars()

    # detect win
    if player.ycor() > 280:
        player.player_win()
        scoreboard.increase_level()

    # collision w/ car
    for c in cars.all_cars:
        if player.distance(c) < 20 and abs(player.ycor() - c.ycor()) < 5:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()