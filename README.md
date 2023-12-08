# Final Project Report

* Student Name: Kayla Jiang
* Github Username: kaylajng
* Semester: Fall 2023
* Course: 5001



## Description 
General overview of the project, what you did, why you did it, etc. 

I created a snake game because it was one of my favorite games during my childhood. The game is very simple, the player needs to control the snake to eat food through the keyboard. Every time the snake eats the food, it will add one point. However, if the snake accidentally collides with a wall, it's game over. To make the game more challenging, I added two more walls in the middle of the game interface. 


## Key Features
Highlight some key features of this project that you want to show off/talk about/focus on. 

- simple controls: intuitive arrow key controls for easy navigation of the snake across the screen
- scoreboard: tracks and displays the player's score in real-time
- collision detection: recognizes collisions with both walls and the snake's own body
- dynamic food generation: randomized appearance of food to challenge the player's strategy and movement

## Guide
How do we run your project? What should we do to see it in action? - Note this isn't installing, this is actual use of the project.. If it is a website, you can point towards the gui, use screenshots, etc talking about features. 

- Download the code
- Open the terminal
- Run the game - execute the **python main.py** file 
- After running the file, a window displaying the snake game interface will appear
- Use the arrow keys on your keyboard to move the snake around the screen. Aim to eat the food to increase your score. Hitting the walls or the snake's body will end the game


## Installation Instructions
If we wanted to run this project locally, what would we need to do?  If we need to get API key's include that information, and also command line startup commands to execute the project. If you have a lot of dependencies, you can also include a requirements.txt file, but make sure to include that we need to run `pip install -r requirements.txt` or something similar.

1. clone the project from Github with running **git clone https://github.com/kaylajng/SnakeGame.git** in terminal, then you can see downloaded project on your local directory
2. ensure you have Python installed on your system
3. open terminal and run the game: run the main.py file 
4. once the game is running, use the arrow keys to move the snake
5. try not to collide with a wall

## Code Review
Go over key aspects of code in this section. Both link to the file, include snippets in this report (make sure to use the [coding blocks](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#code)).  Grading wise, we are looking for that you understand your code and what you did. 

1. Food class refresh method: In this method, the food position on the screen is refreshed when it is eaten by the snake. However, it prevents food from being positioned on the wall. 

```python
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
```

2. Snake movement methods: In this method, the player can control the snake's movement and direction based on arrow key inputs.

   ```python
   def up(self):
       self.head.setheading(UP)
   
   def down(self):
       self.head.setheading(DOWN)
   
   def left(self):
       self.head.setheading(LEFT)
   
   def right(self):
       self.head.setheading(RIGHT)
   ```

3. Wall class: This class constructs the walls in the game by creating segments at specific positions listed in wall_positions

   ```python
   class Wall:
       def __init__(self):
           self.segments = []
           self.build_wall()
           self.head = self.segments[0]
   
       def build_wall(self):
           for position in WALL_POSITIONS:
               self.add_segment(position)
   
       def add_segment(self, position):
           new_segment = Turtle(shape="square")
           new_segment.color("yellow")
           new_segment.penup()
           new_segment.goto(position)
           self.segments.append(new_segment)
   
   ```

   4. Collision detection: it exist to end the game when the snake touches the wall or its own tail. These consitions are checked within the main game loop

   ```python
   if (
       snake.head.xcor() > 280
       or snake.head.xcor() < -280
       or snake.head.ycor() > 280
       or snake.head.ycor() < -280
       or snake.hit_wall(snake.head, WALL_POSITIONS)
   ):
       game_is_on = False
       scoreboard.game_over()
   
   for segment in snake.segments:
       if segment == snake.head:
           pass
       elif snake.head.distance(segment) < 10:
           game_is_on = False
           scoreboard.game_over()
   
   ```

   

### Major Challenges
Key aspects could include pieces that your struggled on and/or pieces that you are proud of and want to show off.

One of the major challenges I faced was ensuring that the snake's body moved seamlessly and coherently. Initially, there were issues where the segments of the snake moved independently. Another challenge is about OOD that was applied in this project, without much experience on that part before taking this class, how to design the system with multiple classes for different purpose was a bit challenging to me. It took a while for me to think through OOD design.


## Example Runs
Explain how you documented running the project, and what we need to look for in your repository (text output from the project, small videos, links to videos on youtube of you running it, etc)

![image-20231208182332855](/Users/kayla/Library/Application Support/typora-user-images/image-20231208182332855.png)

## Testing

How did you test your code? What did you do to make sure your code was correct? If you wrote unit tests, you can link to them here. If you did run tests, make sure you document them as text files, and include them in your submission. 

> _Make it easy for us to know you *ran the project* and *tested the project* before you submitted this report!_

I did a series of manual tests. I used assertions to verify specific functionalities of various game components such as snake class, food class, food refresh method and scoreboard class. 

## Missing Features / What's Next

Focus on what you didn't get to do, and what you would do if you had more time, or things you would implement in the future. 

If I had more time, I'd explore enriching the game experience by introducing a two-player mode, allowing each player to take turns navigating the snake and competing for the highest score. Additionally, implementing various difficulty modes would provide players with options suited to their skill levels—easy mode with two walls, medium mode with four walls, and hard mode with six walls, for instance. Each difficulty mode could correspond to different snake speeds, with harder modes leading to faster snake movements, adding an extra layer of challenge and excitement to the gameplay.

## Final Reflection
Write at least a paragraph about your experience in this course. What did you learn? What do you need to do to learn more? Key takeaways? etc.

This course has been a foundational experience in my journal through computer science. I've gained a solid understanding of Python fundamentals and programming concepts, enabling me to create programs like the snake game. However, I recognize there's a lot of knowledge awaiting exploration, such as data structures and algorithms. To deepen my expertise, I'd like to delve into more advanced topics, seeking to grasp complex data structures and algorithms to solve complex problems. 