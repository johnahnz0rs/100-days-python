# heading - E = 0, N = 90, W=180, S = 270
from turtle import Turtle, Screen
import random

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
    all_turtles.append(t)
    




bet = screen.textinput(title="Place your bet", prompt="Which turtle will win? Enter a color: ").lower()


if bet:
    is_race_on = True
    # is_race_on = False

while is_race_on:
# for _ in range(0,10):
    # for i in range(0,6):
    for t in all_turtles:
        random_number = random.randint(1,10)
        t.forward(random_number)

        if t.xcor() > 200:
            is_race_on = False
            winner = t.pencolor()
            if winner == bet:
                print(f"You win! The {winner} turtle is the winner!")
            else:
                print(f"You lost. The {winner} turtle is the winner.")






screen.exitonclick()