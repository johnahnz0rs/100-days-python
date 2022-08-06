from turtle import Turtle, Screen
t = Turtle()
screen = Screen()
starting_positions = [(0,0), (-20,0), (-40,0)]
segments = []
game_is_on = True

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")


for p in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(p)
    segments.append(new_segment)


while game_is_on:
    game_is_on = False










# screen.tracer(8, 25)
# dist = 2
# for i in range(200):
#     t.fd(dist)
#     t.rt(90)
#     dist += 2

screen.exitonclick()
