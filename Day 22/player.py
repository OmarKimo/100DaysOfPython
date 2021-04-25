from turtle import Turtle

MOVE_DISTANCE = 10


class Player(Turtle):
    def __init__(self, position):
        super().__init__(visible=False)
        self.position = position
        self.shape("square")
        self.color("white")
        self.penup()
        self.resizemode("user")
        self.shapesize(stretch_len=4, stretch_wid=0.8)
        self.speed("fastest")
        self.go_home()

    def move(self):
        if not (
            (self.heading() == 90 and self.ycor() > 250)
            or (self.heading() == 270 and self.ycor() < -250)
        ):
            self.forward(MOVE_DISTANCE)

    def go_home(self):
        self.hideturtle()
        self.goto(self.position)
        self.up()
        self.showturtle()

    def up(self):
        self.setheading(90)
        self.move()

    def down(self):
        self.setheading(270)
        self.move()