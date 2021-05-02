from ball import Ball
from player import Player
from scoreboard import ScoreBoard
from dashedline import DashedLine
from turtle import Screen
from time import sleep

screen = Screen()

screen.setup(width=1000, height=600)
screen.title("Pong The Game")
screen.bgcolor("black")

DashedLine(screen.window_height())

scoreboard = ScoreBoard()

ball = Ball()

player1 = Player((-480, 0))
player2 = Player((480, 0))


def rest():
    ball.home()
    player1.go_home()
    player2.go_home()
    #sleep(3)
    #ball.start()
    

def play():
    ball.start()
    while True:
        screen.update()
        sleep(0.01)
        ball.move()

        if ball.distance(player1) < 20:
            ball.check_player()

        if ball.distance(player2) < 20:
            ball.check_player()
        
        iskill = ball.check_kill()
        if not iskill:
            scoreboard.increase_score2()
            ball.set_mode(0)
            rest()
            break
        elif iskill == 1:
            scoreboard.increase_score1()
            ball.set_mode(1)
            rest()
            break


screen.listen()

screen.onkeypress(key="Up", fun=player1.up)
screen.onkeypress(key="Down", fun=player1.down)
screen.onkeypress(key="w", fun=player2.up)
screen.onkeypress(key="s", fun=player2.down)
screen.onkey(key="space", fun=play)

screen.exitonclick()