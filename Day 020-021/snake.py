from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

DIRC = {
    'RIGHT' : 0,
    'LEFT': 180,
    'UP': 90,
    'DOWN': 270
}

class Snake:
    def __init__(self) -> None:
        self.snake = []
        for pos in STARTING_POSITIONS:
           self.create_obj(pos)
        self.head = self.snake[0]

    def create_obj(self, position):
        obj = Turtle(shape="square")
        obj.color("white")
        obj.penup()
        obj.speed("fastest")
        obj.setpos(position)
        self.snake.append(obj)

    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i].setpos(self.snake[i - 1].pos())
        self.head.forward(MOVE_DISTANCE)

    def left(self):
        if self.head.heading() != DIRC['RIGHT']:
            self.head.setheading(DIRC['LEFT'])

    def right(self):
        if self.head.heading() != DIRC['LEFT']:
            self.head.setheading(DIRC['RIGHT'])

    def up(self):
        if self.head.heading() != DIRC['DOWN']:
            self.head.setheading(DIRC['UP'])

    def down(self):
        if self.head.heading() != DIRC['UP']:
            self.head.setheading(DIRC['DOWN'])

    def stretch(self):
        self.create_obj(self.snake[-1].pos())
