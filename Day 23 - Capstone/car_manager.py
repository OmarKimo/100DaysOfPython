from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
LEFT = 180

class CarManager:
    def __init__(self):
        self.fd_distance = STARTING_MOVE_DISTANCE
        self.cars = []

    def accelerate(self):
        self.fd_distance += MOVE_INCREMENT

    def add_car(self):
        car = Turtle(shape="square", visible=False)
        car.penup()
        car.color(random.choice(COLORS))
        car.goto(x=300, y=random.randint(-245, 245))
        car.shapesize(stretch_len=1.8, stretch_wid=0.8)
        car.setheading(LEFT)
        car.showturtle()
        self.cars.append(car)

    def generate(self, player):
        if random.randint(1,10) == 7:
            self.add_car()
        rem = []
        for car in self.cars:
            car.fd(self.fd_distance)
            if car.xcor() < -290:
                rem.append(car)
            else:
                if player.distance(car) < 15:
                    return True
        for car in rem:
            car.hideturtle()
            self.cars.remove(car)
        return False
    