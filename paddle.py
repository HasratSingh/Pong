from turtle import Turtle
PADDLE_SPEED = 20
PADDLE_SIZE = 100


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=PADDLE_SIZE/20, stretch_wid=1)
        self.seth(90)
        self.speed("fastest")
        self.color("white")
        self.penup()
        self.goto(position)

    def move_up(self):
        self.fd(PADDLE_SPEED)

    def move_down(self):
        self.back(PADDLE_SPEED)
