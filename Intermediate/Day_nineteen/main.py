from turtle import Turtle, Screen
import random



is_race_on = False
screen = Screen()
all_turtle = []
color = ["red", "orange", "blue", "yellow", "purple", "green"]
y_positions = [-50, -20, 10, 40, 70, 100]
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turyle will win the race? enter a color: ")


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    new_turtle.color(color[turtle_index])
    all_turtle.append(new_turtle)



if user_bet:
    is_race_on = True


while is_race_on:
    for one_turtle in all_turtle:
        if one_turtle.xcor() > 230:
            is_race_on = False
            winning_color = one_turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! the {winning_color} turtle is the winner")
            else:
                print(f"You lose! the {winning_color} turtle is the winner")

        rand_distance = random.randint(0, 10)
        one_turtle.forward(rand_distance)






screen.exitonclick()