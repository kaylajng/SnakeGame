from turtle import Turtle
from wall import WALL_POSITIONS
import random


class Food(Turtle):
    wall_pos = []
    """A class to represent the food in the snake game
    
    Attributes:
        shape(str): The shape of the food, a circle
        color(str): The color of the food, red
    """

    def __init__(self):
        """Initialize the food attributes"""
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Move the food to a random position on the screen"""
        while True:
            in_wall = False
            random_x = random.randint(-275, 275)
            random_y = random.randint(-275, 275)
            food_pos = (random_x, random_y)
            if food_pos in WALL_POSITIONS:
                in_wall = True
                break

            if not in_wall:
                break

        self.goto(random_x, random_y)
