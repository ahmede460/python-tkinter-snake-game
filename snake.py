from turtle import Turtle

MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        '''Creates a snake'''
        self.segments = []
        self.endxpos = 0
        
        for _ in range (3):
            snake = Turtle("square")  
            snake.color("white")
            snake.penup()
            snake.setposition(x=self.endxpos, y= 0)
            self.endxpos -= 20
            self.segments.append(snake)

        self.pos = self.segments[0].pos()    

    def move(self):
        '''Starts the snake movement'''
        for snk in range (len(self.segments) - 1 , 0 ,-1):
            snake_last_position = self.segments[snk - 1].pos()
            self.segments[snk].setpos(snake_last_position) 
        self.segments[0].forward(MOVE_DISTANCE)


    def up(self):
        if self.segments[0].heading() == 0:   
            self.segments[0].left(90) 
        elif self.segments[0].heading() == 180:
            self.segments[0].right(90)

    def down(self):
        if self.segments[0].heading() == 0:   
            self.segments[0].right(90) 
        elif self.segments[0].heading() == 180:
            self.segments[0].left(90)

    
    def right(self):
        if self.segments[0].heading() == 270:   
            self.segments[0].left(90)
        elif self.segments[0].heading() == 90:
            self.segments[0].right(90)
          
    
    def left(self):
        if self.segments[0].heading() == 270:   
            self.segments[0].right(90)
        elif self.segments[0].heading() == 90:
            self.segments[0].left(90)

    def extend(self):

        snake = Turtle("square")  
        snake.color("white")
        snake.penup()
        snake.setposition(self.segments[-1].position())
        self.segments.append(snake)

    # def collison_check(self):
    #      for possible_segment in self.segments[1:]:
    #          if self.segments[0].distance(possible_segment) < 15:
    #              pass
    #          else:
    #              print("2")