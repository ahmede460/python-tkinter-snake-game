from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()

screen.title("My Snake Game")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()

snake.segments[0].setheading(90)
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True


while is_game_on == True :
    time.sleep(0.1)
    screen.update()

    snake.move()
    if snake.segments[0].distance(food.pos()) < 15:
        food.eaten()
        snake.extend()
        scoreboard.score_increase()

    if snake.segments[0].xcor() > 300 or snake.segments[0].xcor() < -300 or snake.segments[0].ycor() > 300 or snake.segments[0].ycor() < -300: 

        scoreboard.game_over()
        scoreboard.reset()
        is_game_on = False
    
    for possible_segment in snake.segments[1:]:
        if snake.segments[0].distance(possible_segment) < 15:
            scoreboard.reset()
            is_game_on = False 
    

    

screen.exitonclick()