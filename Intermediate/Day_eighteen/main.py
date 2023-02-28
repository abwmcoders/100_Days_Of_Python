from turtle import Turtle, Screen
import random

jk = Turtle()
#jk.shape('turtle')
#jk.color('red')
#for _ in range(15):
#    jk.forward(10)
#    jk.penup()
#    jk.forward(10)
#    jk.pendown()
#    

colors = ['red', 'blue', 'green', 'yellow']

def draw_shape(num_sides):  
    for _ in range(num_sides):
        angle = 360 / num_sides
        jk.forward(100)
        jk.right(angle)


for i in range(3, 15):
    jk.color(random.choice(colors))
    draw_shape(i)


screen = Screen()
screen.exitonclick()
