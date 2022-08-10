from turtle import Turtle
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20



class Snake:
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for p in STARTING_POSITIONS:
            new_seg = Turtle("square")
            new_seg.color("white")
            new_seg.penup()
            new_seg.goto(p)
            self.segments.append(new_seg)

    def move(self):
        for n in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[n-1].xcor()
            new_y = self.segments[n-1].ycor()
            self.segments[n].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)




    
    def turn_up(self):
        if self.head.heading() not in [-90, 270]:
            self.head.setheading(90)

    def turn_down(self):
        if self.head.heading() not in [90, -270]:
            self.head.setheading(270)
        

    def turn_left(self):
        if self.head.heading() not in [0, -360]:
            self.head.setheading(180)

    def turn_right(self):
        if self.head.heading() not in [180, -180]:
            self.head.setheading(0)

    def check_for_collision(self):
        pass


    def eat_grow(self):
        pass




# t = Turtle()



