from casting.actor import Actor
from structs import Circle, Window
import pyray as pr

class Ball(Actor):
    '''
    Description: The class for creating and managing ball Actors.
    
    Args:
    - window (Window): The programs information about the Window
    - radius (int): The radius of the ball
    - color (pr.Color): The color of the ball
    '''

    def __init__(self, window: Window, radius: int, color: pr.Color):
        super().__init__(window)
        self.radius = radius
        self.color = color
        self.set_start_position()

    def set_start_position(self):
        self.position_x = self.window.width // 2
        self.position_y = self.window.height // 2

    def draw(self):
        pr.draw_circle(self.position_x, self.position_y, self.radius, self.color)
    
    # self.position_x holds x position
    # self.position_y holds y position
    
    # self.draw() draws the player paddle