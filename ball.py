from turtle import Turtle
from random import randint


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.seth(randint(0, 360))

    def move(self):
        self.fd(2)

    def bounce(self):
        current_angle = self.heading()
        self.seth(360-current_angle)
