from turtle import Turtle
from random import randint

MOVE_DISTANCE = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.mode = 1  # initial direction toward myself

    def start(self):
        if self.mode:
            self.setheading(randint(100, 260))
        else:
            self.setheading(randint(-80, 80))

    def invert_mode(self):
        self.mode = 1 - self.mode

    def set_mode(self, mode):
        self.mode = mode

    def move(self):
        self.check_wall()
        self.forward(MOVE_DISTANCE)

    def check_wall(self):
        if self.ycor() > 290 or self.ycor() < -290:
            self.setheading(-self.heading())

    def check_kill(self):
        if self.xcor() > 490:
            return 1
        elif self.xcor() < -490:
            return 0
        else:
            return -1

    def check_player(self):
        self.setheading(self.heading() + 180)

