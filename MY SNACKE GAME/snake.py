from turtle import Turtle
STARTING_POSITION=[(0,0) ,(-20 ,0),(-40,0)]
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT =0
SPEED = 5
class Snake:

    def __init__(self ):
        self.postion=[]
        self.creat_snake()

    def creat_snake(self):
        for position in STARTING_POSITION:
            turtle = Turtle("square")
            turtle.shapesize(0.5 ,0.5)
            turtle.penup()
            turtle.color('yellow')
            turtle.goto(position)
            turtle.speed(SPEED)
            self.postion.append(turtle)
    def new_snack(self , position):
        turtle = Turtle("square")
        turtle.shapesize(0.5, 0.5)
        turtle.penup()
        turtle.color('yellow')
        turtle.goto(position)
        turtle.speed(SPEED)
        self.postion.append(turtle)
    def move(self):
        for seg_num in range(len(self.postion) - 1, 0, -1):
            new_x = self.postion[seg_num - 1].xcor()
            new_y = self.postion[seg_num - 1].ycor()
            self.postion[seg_num].goto(new_x, new_y)
        self.postion[0].forward(DISTANCE)

    def up(self):
        if self.postion[0].heading() != DOWN:
            self.postion[0].setheading(UP)

    def Down(self):
        if self.postion[0].heading() != UP:
            self.postion[0].setheading(DOWN)

    def left(self):
        if self.postion[0].heading() != RIGHT:
            self.postion[0].setheading(LEFT)

    def right(self):
        if self.postion[0].heading() != LEFT:
            self.postion[0].setheading(RIGHT)


    def getting_longer(self):
        self.new_snack(self.postion[-1].position())

