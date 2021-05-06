from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.seth(90)
        self.speed("fastest")
        self.color("white")
        self.penup()
        self.goto(position)

    def move_up(self):
        self.fd(20)

    def move_down(self):
        self.back(20)
