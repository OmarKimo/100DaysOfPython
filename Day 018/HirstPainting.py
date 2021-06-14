import colorgram
from turtle import Turtle, Screen, colormode
from random import choice

t = Turtle()
colormode(255)

rgb_colors = []
colors = colorgram.extract("Day 018/image.jpg", 30)
for color in colors:
    rgb_colors.append(color.rgb)

t.pu()
t.left(180)
t.fd(180)
t.right(90)
t.fd(180)
t.right(90)

for i in range(10):
    for j in range(10):
        if j:
            t.pu()
            t.fd(50)
        t.color(choice(rgb_colors))
        t.dot(20)
    t.pu()
    if i%2 == 0: 
        t.right(90)
        t.fd(50)
        t.right(90)
    else: 
        t.left(90)
        t.fd(50)
        t.left(90)
    
        
s = Screen()
s.exitonclick()