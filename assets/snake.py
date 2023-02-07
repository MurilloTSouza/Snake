from assets import display
from assets import direction


class Segment:
    x = 0
    y = 0

    def __init__(self, color):
        self._pixel = display.Pixel(color)

    def color(self, color):
        self._pixel.color(color)

    def position(self, x, y):
        self.x = x
        self.y = y
        self._pixel.position(x, y)

    def destroy(self):
        self._pixel.destroy()
        del self

    def is_collided_with(self, pixel):
        return self._pixel.is_collided_with(pixel)


class Snake:
    _x = 0
    _y = 0
    _direction = direction.LEFT
    _segments = []
    _color = "white"

    _collision_listeners = []

    def __init__(self, size):
        for _ in range(size):
            self._add_head()

    def _add_head(self):
        segment = Segment(self._color)
        self._x = self._x + self._direction["x"]
        self._y = self._y + self._direction["y"]
        segment.position(x=self._x, y=self._y)
        self._segments.insert(0, segment)

    def _add_tail(self):
        last_pixel = self._segments[-1]
        tail = Segment(self._color)
        tail.position(last_pixel.x, last_pixel.y)
        self._segments.append(tail)

    def _remove_tail(self):
        last_pixel = self._segments.pop()
        last_pixel.destroy()

    def _trigger_collisions(self):
        for i, listener in enumerate(self._collision_listeners):
            if self.is_collided_with(listener["pixel"]):
                listener["callback"]()

    def forward(self):
        self._add_head()
        self._remove_tail()
        self._trigger_collisions()

    def turn_left(self):
        self._direction = direction.counter_clockwise(self._direction)

    def turn_right(self):
        self._direction = direction.clockwise(self._direction)

    def head(self):
        return self._segments[0]

    def increase_size(self, size):
        for _ in range(size):
            self._add_tail()

    def is_collided_with(self, pixel):
        for i, segment in enumerate(self._segments):
            if segment.is_collided_with(pixel):
                return True
        return False

    def on_collision_with(self, pixel, callback):
        listener = {
            "pixel": pixel,
            "callback": callback
        }
        self._collision_listeners.append(listener)
