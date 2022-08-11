from hashlib import new
from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, xcor, ycor):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(xcor,ycor)

    def move_up(self):
        new_y = self.ycor() + 20
        new_y = new_y if new_y < 250 else 250 
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        new_y = new_y if new_y > -250 else -250
        self.goto(self.xcor(), new_y)

