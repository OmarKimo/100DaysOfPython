from turtle import Turtle

LENGTH = 12

def DashedLine(height):
    height -= 40
    cnt = int((height / 2) / LENGTH) + 1
    y_cor = height / 2
    for _ in range(cnt):
        t = Turtle(shape="square", visible=False)
        t.penup()
        t.resizemode("user")
        t.shapesize(stretch_wid=0.7, stretch_len=0.2)
        t.speed("fastest")
        t.color("white")
        t.goto(x=0, y=y_cor)
        t.showturtle()
        y_cor -= 2*LENGTH

