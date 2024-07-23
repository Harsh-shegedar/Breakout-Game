from turtle import Turtle


class Stick(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(0.8, 6)
        self.up()
        self.goto(0, -260)

    def move_left(self):
        newx = self.xcor() - 39
        self.goto(newx, self.ycor())

    def move_right(self):
        newx = self.xcor() + 39
        self.goto(newx, self.ycor())

