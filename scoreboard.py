from turtle import Turtle


class Scoreboard(Turtle):
    """A class to manage the scoreboard in the snake game

    Attributes:
        score(int): The current score of the player
    """

    def __init__(self):
        """Initialize the scoreboard attributes"""
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """Update the displayed score on the scoreboard"""
        self.write(f"Score:{self.score}", align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        """Display 'GAME OVER' at the center of the screen"""
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        """Increase the score and update the scoreboard"""
        self.score += 1
        self.clear()
        self.update_scoreboard()
