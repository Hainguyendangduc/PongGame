from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l = 0
        self.r = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-50, 250)
        self.write(self.l, move=False, align='left', font=('Arial', 24, 'normal'))
        self.goto(50, 250)
        self.write(self.r, move=False, align='left', font=('Arial', 24, 'normal'))

    def left_increase(self):
        self.l += 1
        self.update_score()

    def right_increase(self):
        self.r += 1
        self.update_score()



