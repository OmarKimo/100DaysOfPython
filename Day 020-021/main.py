from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from time import sleep

screen = Screen()

screen.setup(600, 600)
screen.title("Snake Game")
screen.bgcolor("black")

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()

screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_over = False

while not game_over:
    screen.update()
    sleep(0.1)
    snake.move()

    # eat food
    if snake.head.distance(food) < 15:
        snake.stretch()
        food.move()
        scoreboard.increase_score()

    # collision with tail
    for obj in snake.snake[1:]:
        if snake.head.distance(obj) < 15:
            scoreboard.game_over()
            game_over = True
            break

    # collision with wall
    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280
    ):
        scoreboard.game_over()
        game_over = True

screen.exitonclick()
