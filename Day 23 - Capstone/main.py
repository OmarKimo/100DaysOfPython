import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)


player = Player()

scoreboard = Scoreboard()

cars = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    collision = cars.generate(player)

    if collision:
        scoreboard.game_over()
        game_is_on = False

    if player.check_pass():
        scoreboard.increase_level()
        cars.accelerate()

    screen.listen()
    screen.onkeypress(key="Up", fun=player.move)

screen.exitonclick()