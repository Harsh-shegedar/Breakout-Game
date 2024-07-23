from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 250)
        self.write(f"Score: {self.score}", align="center", font=("Courier", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def get_score(self):
        return self.score

    def no_bricks(self):
        self.goto(0, 0)
        self.write("YOU WIN", align="center", font=("Courier", 20, "normal"))

    def game_over(self):
        self.goto(0, -100)
        self.write(f"Try again\n\n Your final score: {self.score}", align="center", font=("italic (sans)", 20, "bold"))