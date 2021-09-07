from turtle import Turtle



class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.counter = -1
        self.update()

    def update(self):
        self.clear()
        self.counter += 1
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=260)
        self.write(f"Score:{self.counter} ", align="center", font= ("Arial", 24, "normal"))


