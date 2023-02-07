import random
from turtle import Turtle
from assets import game


class Pixel:

    x = 0
    y = 0

    def __init__(self, color):
        turtle = Turtle("square")
        turtle.color(color)
        turtle.penup()
        self._turtle = turtle

    def position(self, x, y):
        self.x = x
        self.y = y
        self._turtle.goto(x*game.SCALE, y*game.SCALE)

    def color(self, color):
        self._turtle.color(color)

    def is_collided_with(self, pixel):
        return self.x == pixel.x and self.y == pixel.y

    def destroy(self):
        self._turtle.hideturtle()
        del self


class Food(Pixel):

    def __init__(self):
        super().__init__("blue")
        self._turtle.shape("circle")
        self._turtle.shapesize(stretch_len=0.5, stretch_wid=0.5)

    def random_position(self):
        random_x = random.randint(-game.X_UNITS / 2, game.X_UNITS / 2)
        random_y = random.randint(-game.Y_UNITS / 2, game.Y_UNITS / 2)
        self.position(random_x, random_y)
