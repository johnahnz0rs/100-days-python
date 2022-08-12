from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    
    def __init__(self):
        self.all_cars = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            c = Turtle("square")
            c.penup()
            c.color(random.choice(COLORS))
            c.shapesize(stretch_wid=1, stretch_len=2)
            y_cor = random.randint(-250, 250)
            c.goto(300, y_cor)
            self.all_cars.append(c)

    def move_cars(self):
        for c in self.all_cars:
            c.backward(self.move_speed)
            
    def level_up(self):
        self.move_speed += MOVE_INCREMENT
    

