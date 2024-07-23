from turtle import Turtle, Screen
from ball import Ball
from stick import Stick
#from blocks import Blocks
import random
from scoreboard import Scoreboard
from brick import Brick
import time



screen = Screen()
screen.title("Breakout game")
screen.setup(height=600, width=800)
screen.bgcolor("Black")
screen.tracer(0, 0)






stick = Stick()

scoreboard = Scoreboard()

ball = Ball()
ball.move()

bricks = []


for i in range(35):

    brick = Brick()
    brick.appear()
    bricks.append(brick)         ####################        LOOK HERE       #########################3



screen.listen()
screen.onkey(stick.move_left, key="c")
screen.onkeypress(stick.move_left, key="c")
screen.onkey(stick.move_right, key="v")
screen.onkeypress(stick.move_right, key="v")


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    for brick in bricks:
        if ball.distance(brick) < 30:
            ball.bounce_x()
            x_axis_difference = ball.distance(brick)
            y_axis_difference = ball.distance(brick)
            if x_axis_difference > y_axis_difference:
                # If the ball ditches at the side of the brick then ball's x-axis will be switched.
                ball.bounce_x()
            else:
                # If the ball ditches on the top or bottom of the brick then ball's y-axis will be switched.
                ball.bounce_x()
                ball.bounce_y()
            brick.disappear()
            bricks.remove(brick)
            scoreboard.increase_score()
            if scoreboard.get_score() % 8 == 0:
                ball.increase_speed()


    if ball.ycor() > 280:
        ball.bounce_y()

    if ball.xcor() > 365 or ball.xcor() < -365:
        ball.bounce_x()

    if ball.distance(stick) < 30 and ball.ycor() < 290:
        ball.bounce_y()

    if ball.ycor() < -295:
        scoreboard.game_over()
        game_is_on = False


    if not bricks:
        scoreboard.no_bricks()
        game_is_on = False















screen.mainloop()