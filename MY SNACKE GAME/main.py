from turtle import  Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.title("My Snake Game")
screen.setup(height=600 , width= 600)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up , 'Up')
screen.onkey(snake.Down , 'Down')
screen.onkey(snake.left , 'Left')
screen.onkey(snake.right , 'Right')

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
# now we have to make the relation between snake and food
    if snake.postion[0].distance(food) < 15:
        food.refresh()
        snake.getting_longer()
        scoreboard.increase_score()
    if snake.postion[0].xcor() > 280 or snake.postion[0].xcor()< -280 or snake.postion[0].ycor()> 280 or snake.postion[0].ycor()< -280:
        game_on =False
        scoreboard.game_over()

    for position in snake.postion:
        if snake.postion[0] == position:
            pass
        elif snake.postion[0].distance(position) <10 :
            game_on= False
            scoreboard.game_over()


screen.exitonclick()