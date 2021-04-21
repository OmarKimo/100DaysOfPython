from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)

in_color = screen.textinput(
    title="Make your bet", prompt="Who will win the race? Enter a color:"
)

objects = [Turtle(shape="turtle") for _ in range(6)]
rainbow = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(6):
    objects[i].speed(1)
    objects[i].color(rainbow[i])

for i in range(6):
    objects[i].pu()
    objects[i].goto(-235, -80 + i * 30)

flag = False
winner = ""
while not flag:
    for i in range(6):
        objects[i].forward(randint(0, 10))
        if objects[i].pos()[0] >= 250:
            winner = objects[i].color()[0]
            flag = True
            break

out = ["win. ^_^", "lose. ;_;"]
print(
    f"You {out[0] if winner == in_color else out[1]} The {winner} turtle is the winner not the {in_color}."
)

screen.bye()