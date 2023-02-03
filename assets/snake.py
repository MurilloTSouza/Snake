from assets import display
from assets import direction


class Segment:
    _x = 0
    _y = 0

    def __init__(self, color):
        self._pixel = display.Pixel(color)

    def color(self, color):
        self._pixel.color(color)

    def position(self, x, y):
        self._x = x
        self._y = y
        self._pixel.position(x, y)

    def destroy(self):
        self._pixel.destroy()
        del self


class Snake:
    _x = 0
    _y = 0
    _direction = direction.LEFT
    _segments = []
    _color = "white"

    def __init__(self, size):
        for _ in range(size):
            self._add_head()

    def _add_head(self):
        segment = Segment(self._color)
        self._x = self._x + self._direction["x"]
        self._y = self._y + self._direction["y"]
        segment.position(x=self._x, y=self._y)
        self._segments.insert(0, segment)

    def _remove_tail(self):
        last_pixel = self._segments.pop()
        last_pixel.destroy()

    def forward(self):
        self._add_head()
        self._remove_tail()

    def turn_left(self):
        self._direction = direction.counter_clockwise(self._direction)

    def turn_right(self):
        self._direction = direction.clockwise(self._direction)