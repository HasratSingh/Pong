from turtle import Screen
import paddle
import ball
from time import sleep

# Screen Setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(False)

# Setup Paddles and Ball
paddle_right = paddle.Paddle(position=(380, 0))
paddle_left = paddle.Paddle(position=(-380, 0))
ball = ball.Ball()
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
    if ball.xcor() > 360 and -50 < ball.ycor()-paddle_right.ycor() < 50:
        ball.bounce_paddle()
    elif ball.xcor() < -360 and -50 < ball.ycor()-paddle_left.ycor() < 50:
        ball.bounce_paddle()
    sleep(0.01)
    screen.update()

# Screen does not close automatically
screen.exitonclick()
