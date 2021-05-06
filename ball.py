from turtle import Turtle
from random import randint


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.reset()

    def move(self):
        self.fd(3)

    def bounce_wall(self):
        current_angle = self.heading()
        self.seth(360-current_angle)

    def bounce_paddle(self):
        current_angle = self.heading()
        self.seth(180-current_angle)

    def reset(self):
        self.penup()
        self.shape("circle")
        self.color("white")
        self.seth(randint(0, 360))
        self.goto(0, 0)
