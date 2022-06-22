import random
from turtle import Turtle, Screen

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("red")
        self.speed("fastest")
        self.screen=Screen()
        self.new_location()
    
    def new_location(self):
        self.x_random = random.randint(-int(self.screen.window_width() / 2 - 20), int(self.screen.window_width() / 2 - 25))
        self.y_random = random.randint(-int(self.screen.window_height() / 2 - 20), int(self.screen.window_height() / 2 - 25))
        self.goto(self.x_random, self.y_random)