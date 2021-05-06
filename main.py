from turtle import Screen
from paddle import Paddle, PADDLE_SIZE
from ball import Ball
from scoreboard import Scoreboard
from time import sleep

# Screen Setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(False)

# Setup Paddles,Ball and Scoreboard
paddle_right = Paddle(position=(380, 0))
paddle_left = Paddle(position=(-380, 0))
ball = Ball()
scoreboard = Scoreboard()
screen.update()

# Setup listeners
screen.listen()


def listener(fun, key):
    if key == "up":
        if fun.ycor() < 230:
            fun.move_up()
    else:
        if fun.ycor() > -230:
            fun.move_down()
    screen.update()


screen.onkeypress(fun=lambda: listener(paddle_left, 'up'), key="w")
screen.onkeypress(fun=lambda: listener(paddle_left, 'down'), key="s")
screen.onkeypress(fun=lambda: listener(paddle_right, 'up'), key="Up")
screen.onkeypress(fun=lambda: listener(paddle_right, 'down'), key="Down")

# Main game Loop
game_not_over = True
while game_not_over:
    ball.move()
    if ball.ycor() > 285 or ball.ycor() < -280:  # When ball hits top or bottom wall
        ball.bounce_wall()

    elif ball.xcor() > 360 and -PADDLE_SIZE/2 < (ball.ycor() - paddle_right.ycor()) < PADDLE_SIZE/2:
        if 0 < ball.heading() < 90 or 270 < ball.heading() < 360:  # So that ball changes direction only once
            ball.bounce_paddle()

    elif ball.xcor() < -360 and -PADDLE_SIZE/2 < (ball.ycor() - paddle_left.ycor()) < PADDLE_SIZE/2:
        if 90 < ball.heading() < 270:  # So that ball changes direction only once
            ball.bounce_paddle()

    elif ball.xcor() > 420:  # Ball crosses right boundary
        ball.reset_position("left")
        scoreboard.update_score_left()

    elif ball.xcor() < -420:  # Ball crosses left boundary
        ball.reset_position("right")
        scoreboard.update_score_right()

    if scoreboard.score_left == 10 or scoreboard.score_right == 10:
        scoreboard.final_result()
        ball.hideturtle()
        game_not_over = False
    sleep(0.01)
    screen.update()

# Screen does not close automatically
screen.exitonclick()
