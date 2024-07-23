from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.up()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.06

    def move(self):
        newx = self.xcor() + self.x_move
        newy = self.ycor() + self.y_move
        self.goto(newx, newy)

    def bounce_y(self):
        self.y_move *= -1


    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.move()                     #--------^LOOK HERE^^^^^^^&&&&&&&&&--------##############&&

    def increase_speed(self):
        self.move_speed *= 0.8

