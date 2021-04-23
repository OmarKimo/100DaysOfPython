from turtle import Turtle

FONT = ("Courier", 20, "bold")
ALIGN = "center"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0
        self.shape("blank")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.goto(x=0, y=270)
        self.update()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()

    def update(self):
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGN, font=FONT)