from assets import game
from assets.snake import Snake
from assets.display import Food

snake = Snake(size=3)
food = Food()
food.random_position()


def eat_food():
    snake.increase_size(1)
    food.random_position()


snake.on_collision_with(food, eat_food)


def on_update():
    game.on_key("Left", snake.turn_left)
    game.on_key("Right", snake.turn_right)
    snake.forward()
    return True


game.run(on_update)
