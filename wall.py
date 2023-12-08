from turtle import Turtle

WALL_POSITIONS = [
    (40, 50),
    (20, 50),
    (0, 50),
    (-20, 50),
    (-40, 50),
    (60, 50),
    (80, 50),
    (-200, 80),
    (-200, 60),
    (-200, 40),
    (-200, 20),
    (-200, 0),
    (-200, -20),
    (-200, -40),
]


class Wall:
    """A class to represent the walls in the snake game"""

    def __init__(self):
        """Initialize the wall attributes"""
        self.segments = []
        self.build_wall()
        self.head = self.segments[0]

    def build_wall(self):
        """Build the wall using predefined positions"""
        for position in WALL_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Add a segment to the wall"""
        new_segment = Turtle(shape="square")
        new_segment.color("yellow")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
