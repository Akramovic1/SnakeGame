from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
snakes = []

for position in starting_positions:
    snake = Turtle("square")
    snake.color("white")
    snake.penup()
    snake.goto(position)
    snakes.append(snake)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for snake in range(len(snakes) - 1, 0, -1):
        snakes[snake].goto(snakes[snake - 1].xcor(), snakes[snake - 1].ycor())
    snakes[0].forward(20)


screen.exitonclick()
