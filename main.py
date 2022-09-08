from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.listen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.back(10)


def rotate_left():
    tim.left(10)


def rotate_right():
    tim.right(10)


def reset():
    tim.reset()


screen.onkey(fun=move_forward, key='w')
screen.onkey(fun=move_backward, key='s')
screen.onkey(fun=rotate_right, key='d')
screen.onkey(fun=rotate_left, key='a')
screen.onkey(fun=reset, key='c')

screen.exitonclick()
