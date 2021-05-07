from turtle import Screen
from snake import Snake
from food import Food
from score_board import Scoreboard
import time

screen = Screen()

screen.setup(width=600, height=600)
screen.title("snakeGame")
screen.bgcolor("black")

screen.tracer(0)

snake = Snake()
food = Food()
sco = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        sco.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 277 or snake.head.ycor() < -280:
        sco.reset()
        snake.reset()

    for seg in snake.segment[1:]:
        if snake.head.distance(seg) < 10:
            sco.reset()
            snake.reset()

screen.exitonclick()
