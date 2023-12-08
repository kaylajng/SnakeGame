from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


# test snake class
screen = Screen()
snake = Snake()

# ensure snake segments are created properly
assert len(snake.segments) == 3

# test food class
food = Food()

# ensure food is initialized correctly
assert food.shape() == "circle"

# test food refresh method
previous_position = food.position()
food.refresh()
assert previous_position != food.position()

# test scoreboard class
scoreboard = Scoreboard()

# ensure scoreboard initializes with zero score
assert scoreboard.score == 0

# test scoreboard update methods
scoreboard.increase_score()
assert scoreboard.score == 1

print("All tests passed!")
