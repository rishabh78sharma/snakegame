from turtle import Turtle

START_PS = [(0, 0), (-20, 0), (-40, 0)]
MOV = 20
RIGHT = 0
LEFT = 180
UP = 90
DOWN = 270


class Snake:
    def __init__(self):
        self.segment = []
        self.creates_snake()
        self.head = self.segment[0]

    def creates_snake(self):
        for seg in START_PS:
            self.add(seg)

    def add(self, seg):
        turtle = Turtle("square")
        turtle.color("white")
        turtle.penup()
        turtle.goto(seg)
        self.segment.append(turtle)

    def reset(self):
        for seg in self.segment:
            seg.goto(1000, 1000)
        self.segment.clear()
        self.creates_snake()
        self.head = self.segment[0]

    def extend(self):
        self.add(self.segment[-1].position())

    def move(self):
        for i in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[i - 1].xcor()
            new_y = self.segment[i - 1].ycor()
            self.segment[i].goto(new_x, new_y)
        self.head.fd(MOV)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
