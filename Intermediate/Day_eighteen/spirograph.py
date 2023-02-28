from turtle import Screen
import turtle as t
import random


tim = t.Turtle()
t.colormode(255)

def draw_spiragraph(size):
    for _ in range(int(360 / size)):
        tim.color(random_color())
        tim.circle(100)
        current_heading = tim.heading()
        tim.setheading(current_heading + size)
        tim.circle(100)


def random_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    color = (r, g, b)
    return color


tim.speed('fastest')
draw_spiragraph(5)



screen = Screen()
screen.exitonclick()
