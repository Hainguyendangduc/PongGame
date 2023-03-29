from turtle import Turtle
MOVE_DISTANCE = 20


class Paddle(Turtle):

    def __init__(self, positions):
        super().__init__()
        self.positions = positions
        self.shape("square")
        self.color("white")
        self.penup()
        self.setheading(90)
        self.shapesize(stretch_wid=0.5, stretch_len=4)
        self.goto(positions)

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.backward(20)



