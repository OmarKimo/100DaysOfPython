from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
UP = 90

class Player(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.shape("turtle")
        self.color("black")
        self.penup()
        #self.speed("fastest")
        self.goto(STARTING_POSITION)
        self.setheading(UP)
        self.showturtle()

    def move(self):
        self.fd(MOVE_DISTANCE)

    def check_pass(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.hideturtle()
            self.goto(STARTING_POSITION)
            self.setheading(UP)
            self.showturtle()
            return True
        return False