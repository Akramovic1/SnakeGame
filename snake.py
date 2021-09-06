from turtle import Screen, Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVED_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            snake = Turtle("square")
            snake.color("white")
            snake.penup()
            snake.goto(position)
            self.segments.append(snake)

    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            self.segments[segment].goto(self.segments[segment - 1].xcor(), self.segments[segment - 1].ycor())
        self.segments[0].forward(MOVED_DISTANCE)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)