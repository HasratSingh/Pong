from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.hideturtle()
        self.score_left = 0
        self.score_right = 0
        self.update_scoreboard()

    def update_score_left(self):
        self.score_left += 1
        self.update_scoreboard()

    def update_score_right(self):
        self.score_right += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Left:{self.score_left} Right:{self.score_right}", align=ALIGN, font=FONT)

    def final_result(self):
        if self.score_right > self.score_left:
            winner = "Right"
        else:
            winner = "Left"
        self.goto(0, 0)
        self.write(f"Game Over. {winner} is Winner.", align=ALIGN, font=FONT)
