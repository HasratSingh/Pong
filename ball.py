from turtle import Turtle
from random import randint, choice


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.reset_position()
        self.seth(randint(0, 360))  # Initially ball can go towards any side.

    def move(self):
        self.fd(10)

    def bounce_wall(self):
        current_angle = self.heading()
        self.seth(360-current_angle)

    def bounce_paddle(self):
        current_angle = self.heading()
        if 90 < current_angle < 100:  # Fixes bug in which case ball keeps bouncing between walls.
            self.seth(0)
        elif 80 < current_angle < 90: # Fixes bug in which case ball keeps bouncing between walls.
            self.seth(180)
        else:
            self.seth(180-current_angle)

    def reset_position(self, side="left"):  # If no side is given ball goes towards left
        self.penup()
        self.shape("circle")
        self.color("white")
        self.goto(0, 0)
        if side == "right":
            right_side_range = list(range(0, 90))+list(range(270, 360))  # Angle values for throwing ball to right side
            self.seth(choice(right_side_range))
        else:
            self.seth(randint(90, 270))
