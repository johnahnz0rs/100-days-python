from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    
    def __init__(self, how_many):
        self.all_cars = []
        for _ in range(how_many):
            self.create_car()
        
        

    def create_car(self):
        c = Turtle()
        c.penup()
        c.color(random.choice(COLORS))
        c.shape("square")
        c.shapesize(stretch_wid=1, stretch_len=2)
        c.setheading(180)
        x_cor = random.randint(-299, 300)
        y_cor = random.randint(-250, 250)
        c.goto(x_cor, y_cor)
        self.all_cars.append(c)

    def move_cars(self):
        for c in self.all_cars:
            if c.xcor() < -299:
                new_x = c.xcor() + 600
                same_y = c.ycor()
                c.goto(new_x, same_y)
            c.forward(MOVE_INCREMENT)
    

