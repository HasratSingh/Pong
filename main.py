from turtle import Screen
import paddle

# Screen Setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(False)

# Setup Paddles
paddle_right = paddle.Paddle(position=(350, 0))
paddle_left = paddle.Paddle(position=(-350, 0))
screen.update()

# Setup listeners
screen.listen()


def listener(fun, key):
    if key == "up":
        fun.move_up()
    else:
        fun.move_down()
    screen.update()


screen.onkeypress(fun=lambda: listener(paddle_left, 'up'), key="w")
screen.onkeypress(fun=lambda: listener(paddle_left, 'down'), key="s")
screen.onkeypress(fun=lambda: listener(paddle_right, 'up'), key="Up")
screen.onkeypress(fun=lambda: listener(paddle_right, 'down'), key="Down")

# Screen does not close automatically
screen.exitonclick()
