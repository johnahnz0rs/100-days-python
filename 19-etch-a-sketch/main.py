from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def rotate_left():
    tim.left(5)

def rotate_right():
    tim.right(5)

def move_backwards():
    tim.backward(10)

def clear():
    tim.clear()


screen.listen()
screen.onkey(key="Up", fun=move_forwards)
screen.onkey(key="Left", fun=rotate_left)
screen.onkey(key="Right", fun=rotate_right)
screen.onkey(key="Down", fun=move_backwards)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
