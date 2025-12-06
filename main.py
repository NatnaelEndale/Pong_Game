from turtle import Screen, Turtle
from ball import Ball
from paddle import Paddel
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.screensize(800, 600)
screen.title("Pong Game")
screen.tracer(0)

ball = Ball()

l_paddle = Paddel((-350, 0))
r_paddle = Paddel((350, 0))

l_score = Scoreboard((-150, 220))
r_score = Scoreboard((150, 220))

screen.listen()
screen.onkey(l_paddle.go_up, "Up")
screen.onkey(l_paddle.go_down, "Down")
screen.onkey(r_paddle.go_up, "w")
screen.onkey(r_paddle.go_down, "s")

move_speed = 0.1

game_is_on = True

x_speed = 10
y_speed = 10
while game_is_on:
    r_score.update_scoreboard()
    l_score.update_scoreboard()
    time.sleep(move_speed)
    screen.update()

    # Detecet collision with wall
    if -340 <= ball.xcor() <= 340:
        if ball.ycor() >= 250:
            y_speed = -10
        elif ball.ycor() <= -250:
            y_speed = 10
        move_speed *= 0.99

    # Detect collision with paddles
    if ball.xcor() == 330 and ball.distance(r_paddle) < 50:
        x_speed *= -1
    elif ball.xcor() == -330 and ball.distance(l_paddle) < 50:
        x_speed *= -1

    # Detect if the ball goes out of bounds
    if ball.xcor() >= 380:
        l_score.increase_score()
        ball.home()
        x_speed *= -1
        move_speed = 0.1

    if ball.xcor() <= -380:
        r_score.increase_score()
        ball.home()
        x_speed *= -1
        move_speed = 0.1

    ball.move(x_speed, y_speed)

screen.exitonclick()
