from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 80, "bold")

class Scoreboard(Turtle):

    def __init__(self, postion):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(postion)


    def update_scoreboard(self):
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
