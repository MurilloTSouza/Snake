from turtle import Turtle

SCALE = 20


class Pixel:

    def __init__(self, color):
        turtle = Turtle("square")
        turtle.color(color)
        turtle.penup()
        self._turtle = turtle

    def position(self, x, y):
        self._turtle.goto(x*SCALE, y*SCALE)

    def color(self, color):
        self._turtle.color(color)

    def destroy(self):
        self._turtle.hideturtle()
        del self
