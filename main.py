from turtle import Screen
import time

from day20.scoreboard import ScoreBoard
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
snake = Snake()
food= Food()
score_board =ScoreBoard()

screen.listen()
screen.onkey(fun=snake.up,key="Up")
screen.onkey(fun=snake.down,key="Down")
screen.onkey(fun=snake.left,key="Left")
screen.onkey(fun=snake.right,key="Right")

game_is_on=True



while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_move()
    #detect collision with food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        score_board.score_increase()
    #detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            game_is_on=False
            score_board.game_over()

    #detect collision with wall
    if snake.head.xcor()>285 or  snake.head.xcor()<-285 or  snake.head.ycor()>285 or  snake.head.ycor()<-285:
        game_is_on=False
        score_board.game_over()































screen.exitonclick()