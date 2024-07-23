from turtle import Turtle
import random

color = ["green", "red", "yellow"]
yposition = [90, 110, 140,170, 200, 230]
xpositions = [-320, -260, -200, -150, -100, 0, 60, 120, 180, 240, 280]


class Brick(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(color))
        self.shapesize(1, 3)
        self.up()


    def appear(self):
        self.goto(x=random.choice(xpositions), y=random.choice(yposition))

    def disappear(self):
        self.hideturtle()