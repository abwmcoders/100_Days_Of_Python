from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


RIGHT_POSITION = (350, 0)
LEFT_POSITION = (-350, 0)

screen = Screen()
scoreboard = Scoreboard()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Berry Pong Game')
screen.tracer(0)


right_paddle = Paddle(RIGHT_POSITION)
left_paddle = Paddle(LEFT_POSITION)
ball = Ball()
screen.listen()
screen.onkey(key="Up", fun=right_paddle.up)
screen.onkey(key="Down", fun=right_paddle.down)
screen.onkey(key="w", fun=left_paddle.up)
screen.onkey(key="s", fun=left_paddle.down)



game_is_on = True

while game_is_on:

    time.sleep(ball.moving_speed)
    screen.update()
    ball.move()

    # Detecting collission with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


    # Detect collision with paddle
    if ball.distance(right_paddle) < 50 or ball.xcor() > 320 or ball.distance(left_paddle) < 50 or ball.xcor() < -320:
        ball.bounce_x()


    # Detect when R paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()


    # Detect when L paddle misses the ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()









screen.exitonclick()

