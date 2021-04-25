from turtle import Turtle

FONT = ("Arial", 40, "bold")
ALIGN = "center"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()

        self.score = [0, 0]
        self.shape("blank")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.update()

    def increase_score1(self):
        self.score[0] += 1
        self.update()

    def increase_score2(self):
        self.score[1] += 1
        self.update()

    def update(self):
        self.clear()
        self.goto(x=-60, y=240)
        self.write(f"{self.score[0]}", align=ALIGN, font=FONT)
        self.goto(x=60, y=240)
        self.write(f"{self.score[1]}", align=ALIGN, font=FONT)
