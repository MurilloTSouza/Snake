UP = {"x": 0, "y": 1}
RIGHT = {"x": 1, "y": 0}
DOWN = {"x": 0, "y": -1}
LEFT = {"x": -1, "y": 0}
CLOCKWISE_DIRECTIONS = [UP, RIGHT, DOWN, LEFT]


def clockwise(direction):
    index = CLOCKWISE_DIRECTIONS.index(direction)
    new_index = (index+1) % 4
    return CLOCKWISE_DIRECTIONS[new_index]


def counter_clockwise(direction):
    index = CLOCKWISE_DIRECTIONS.index(direction)
    new_index = (index-1) % 4
    return CLOCKWISE_DIRECTIONS[new_index]
