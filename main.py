from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("The Famous Arcade Game!")

screen.tracer(0)  # stops screen
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()

player_1 = Scoreboard()
player_2 = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

is_on = True

while is_on:
    screen.update()  # updates screen after the work is done
    time.sleep(0.1)  # (move_speed)
    ball.move()

    # COLLISION WITH WALL
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # COLLISION WITH PADDLES
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_back()

    if player_1.score > 1:
        ball.goto(800, 600)  # Out of screen
        player_1.goto(0, 0)
        player_1.write(f'Player 1 Won!', align="center", font=("Courier", 10, "normal"))
        is_on = False

    elif player_2.score > 1:
        ball.goto(800, 600)  # Out of screen
        player_2.goto(0, 0)
        player_2.write(f'Player 2 Won!', align="center", font=("Courier", 10, "normal"))
        is_on = False

    else:
        # MISSES THE PADDLE AND GOES OUT OF SCREEN (Player 2 Misses)
        if ball.xcor() > 380:
            player_1.increase_score()
            player_1.goto(-370, 270)
            player_1.write(f'Player 1 Score:{player_1.score} ', align="left", font=("Courier", 10, "normal"))
            ball.reset_ball()

        # (Player 1 Misses)
        if ball.xcor() < -380:
            player_2.increase_score()
            player_2.goto(370, 270)
            player_2.write(f'Player 2 Score:{player_2.score} ', align="right", font=("Courier", 10, "normal"))
            ball.reset_ball()

screen.exitonclick()

