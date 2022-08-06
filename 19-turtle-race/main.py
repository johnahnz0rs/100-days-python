# heading - E = 0, N = 90, W=180, S = 270
from turtle import Turtle, Screen
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

screen = Screen()
screen.setup(width=500, height=400)

# create 6 turtles: shape, color, position
for i in range(0,6):
    t = Turtle(shape="turtle")
    t.color(colors[i])
    t.penup()
    t.goto(x=-230, y=y_positions[i])
    



bet = screen.textinput(title="Place your bet", prompt="Which turtle will win? Enter a color (r, o, y, g, b, v): ")





screen.exitonclick()