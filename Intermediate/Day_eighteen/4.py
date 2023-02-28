from turtle import Screen
import turtle as t
import random


tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    color = (r, g, b)
    return color

########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed",
           "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

directions = [0, 90, 180, 270]


for _ in range(200):
    tim.color(random_color())
    tim.pensize(10)
    tim.forward(30)
    tim.speed('fastest')
    tim.setheading(random.choice(directions))




screen = Screen()
screen.exitonclick()
