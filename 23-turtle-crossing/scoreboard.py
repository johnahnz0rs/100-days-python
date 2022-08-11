from turtle import Turtle
FONT = ("Courier", 24, "normal")
# level = 1


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)
        self.write(f"Level: {self.level}", font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)

    def game_over(self):
        self.goto(0,260)
        self.clear()
        self.write("GAME OVER", align="center", font=FONT)
