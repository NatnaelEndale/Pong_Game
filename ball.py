from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(0.8, 0.8)
        self.penup()

    def move(self, x_direction, y_direction):
        new_x = self.xcor() + x_direction
        new_y = self.ycor() + y_direction
        self.goto(new_x, new_y)

