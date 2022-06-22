from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        
        #self.clear()
        self.color("white")
        self.goto(0, 275)
        self.update_score()
        self.hideturtle()
        #self.write((10,10), True)
    
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 16, "normal"))
    
    def increase_score(self):
        self.score += 1
        self.update_score()
        #self.write((10,10), True)
    
    def game_over(self):
        self.update_score()
        self.goto(0, 0)
        #self.clear()
        self.write("GAME OVER.", align="center", font=("Arial", 16, "normal"))
        self.hideturtle()
        #self.write((10,10), True)