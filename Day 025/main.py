from turtle import Turtle, Screen
import pandas

ALIGN = "center"

data = pandas.read_csv("Day 025/50_states.csv")

cnt_states = len(data)
cnt_ans = 0
answered = {}

screen = Screen()
screen.setup(width=730, height=500)
screen.bgpic("Day 025/blank_states_img.gif")

while cnt_ans < cnt_states:
    ans = screen.textinput(
        title=f"{cnt_ans}/{cnt_states} States Correct",
        prompt="What's another state name?",
    ).title()
    if not ans:
        screen.bye()
    if ans in set(data.state) and not answered.get(ans, 0):
        found = data[data.state == ans]
        x = int(found.x)
        y = int(found.y)
        print(ans, x, y)
        text = Turtle(shape="blank", visible=False)
        text.color("black")
        text.penup()
        text.goto(x=x, y=y)
        text.write(ans)
        text.showturtle()
        cnt_ans += 1
        answered[ans] = 1

game_over = Turtle(shape="blank")
game_over.color("black")
game_over.write(
    "Congratulations, you get all states correct. ^_^",
    align=ALIGN,
    font=("Courier", 24, "normal"),
)

screen.exitonclick()
