from turtle import Screen
import paddle

# Screen Setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(False)

# Setup Paddles
paddle_left = paddle.Paddle(position=(350, 0))
paddle_right = paddle.Paddle(position=(-350, 0))
screen.update()

# Setup listeners
screen.listen()
screen.onkey(paddle_left.move_up, "w")
screen.onkey(paddle_left.move_down, "s")
screen.onkey(paddle_right.move_up, "Up")
screen.onkey(paddle_right.move_down, "Down")

# Screen does not close automatically
screen.exitonclick()
