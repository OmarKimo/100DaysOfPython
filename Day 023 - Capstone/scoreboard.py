from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGN = "left"

WRITE_POSITION = (-270, 250)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.level = 1
        self.shape("blank")
        self.color("black")
        self.penup()
        self.speed("fastest")
        self.goto(WRITE_POSITION)
        self.update()

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update()

    def update(self):
        self.write(f"Level: {self.level}", align=ALIGN, font=FONT)

    def game_over(self):
        self.home()
        self.write(f"GAME OVER", align="center", font=FONT)