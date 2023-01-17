import turtle
from turtle import Turtle,Screen
screen = Screen()
screen.bgcolor("black")
tim= Turtle()
import random
turtle.colormode(255)
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color = (r, g, b)
    return random_color
R=True
while R:
    tim.width(2)
    tim.color(random_color())
    tim.speed(12)
    tim.circle(20,150)
    tim.left(90)
    tim.circle(20,150)
    tim.right(90)
    tim.forward(60)
    tim.circle(100)
    tim.right(2)
    tim.left(10)
screen.exitonclick()
