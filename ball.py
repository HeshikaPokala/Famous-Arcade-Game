from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.move_dist_x = 10
        self.move_dist_y = 10
        # self.move_speed = 0

    def move(self):
        new_x = self.xcor() + self.move_dist_x
        new_y = self.ycor() + self.move_dist_y
        self.goto(new_x, new_y)

    def bounce(self):
        self.move_dist_y *= -1

    def bounce_back(self):
        self.move_dist_x *= -1
        # self.move_speed *= 0.9  # INCREASES SPEED EVERYTIME IT HITS THE PADDLE

    def reset_ball(self):
        self.goto(0, 0)
        self.bounce_back()
        # self.move_speed = 0.1  # SETS BACK SPEED WHEN A PLAYER MISSES AND STARTS OVER
