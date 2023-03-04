from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen  = Screen()
food = Food()
scoreboard = Scoreboard()

screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Berry Snack Game')
screen.tracer(0)
game_is_on = True
snake = Snake()
screen.listen()
screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='Right', fun=snake.right)
screen.onkey(key='Left', fun=snake.left)

 



while game_is_on:
    screen.update()
    time.sleep(.1)

    snake.move()


    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
      

    # Detect ollision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() <  -280:
        scoreboard.reset()
        snake.reset()

    # Detect ollision with tail
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()








screen.exitonclick()