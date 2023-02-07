from turtle import Screen
import time

FPS = 10

SCALE = 20
X_UNITS = 30
Y_UNITS = 30


screen = Screen()
screen.setup(width=(X_UNITS+2)*SCALE, height=(Y_UNITS+2)*SCALE)
screen.bgcolor("black")
screen.title("snakeee")
screen.tracer(0)
screen.listen()


def on_key(key, callback):
    screen.onkey(key=key, fun=callback)


def run(on_update):
    is_running = True
    while is_running:
        should_continue = on_update()
        screen.update()
        time.sleep(1/FPS)
        if not should_continue:
            is_running = False


