from assets import game
from assets.snake import Snake

snake = Snake(size=3)


def on_update():
    game.on_key("Left", snake.turn_left)
    game.on_key("Right", snake.turn_right)
    snake.forward()
    return True


game.run(on_update)
