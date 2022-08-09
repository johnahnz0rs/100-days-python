from turtle import Turtle, Screen
import time
t = Turtle()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
starting_positions = [(0,0), (-20,0), (-40,0)]
segments = []
game_is_on = True


for p in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(p)
    segments.append(new_segment)

screen.update()
# while game_is_on:
for _ in range(0,10):
    
    for n in range(len(segments)-1, 0, -1):
        new_x = segments[n-1].xcor()
        new_y = segments[n-1].ycor()
        segments[n].goto(new_x, new_y)
    segments[0].forward(20)
    segments[0].left(90)

    screen.update()
    time.sleep(.5)










# screen.tracer(8, 25)
# dist = 2
# for i in range(200):
#     t.fd(dist)
#     t.rt(90)
#     dist += 2

screen.exitonclick()
