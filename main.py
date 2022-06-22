from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Python Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        #snake.segments.append(len(snake.head))
        score.increase_score()
        print(f"feed me more, score: {score.score}")
        snake.extend()
        food.new_location()
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        score.game_over()
        game_is_on = False
    for segment in snake.segments[1::]:
        #if segment == snake.head:
        #    pass
        if snake.head.distance(segment) < 10:
            score.game_over()
            game_is_on = False
            
            
            


screen.exitonclick()