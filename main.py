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


is_game_on = True


def game_over():
    global is_game_on
    is_game_on = False


snake.on_collision_with_self(game_over)


def on_update():
    game.on_key("Left", snake.turn_left)
    game.on_key("Right", snake.turn_right)
    snake.forward()
    return is_game_on


game.run(on_update)
