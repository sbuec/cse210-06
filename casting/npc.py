from casting.paddle import Paddle
from structs import Window
import pyray as pr
from casting.ball import Ball

class npc(Paddle):
    ''' 
    Description: The class that creates and manages player Actors.

    Args:
    - window (Window): The programs information about the Window
    - color (pr.Color): Color of Paddle
    - paddle_side (str): The side at which the paddle is created ('left' / 'right')
    - ball (Ball): The ball Actor currently on screen
    '''

    def __init__(self, window: Window, texture: pr.Texture, paddle_side: str, ball: Ball):
        super().__init__(window, texture, paddle_side)
        self.ball = ball

    def locate_ball_y(self):
        '''
        Description: Locates Ball actor's y position.
        '''
        self.ball_y = self.ball.position_y

    def set_location(self):
        self.position_y = self.ball_y

    # self.position_x holds x position
    # self.position_y holds y position
    
    # Actor.image_load_texture(image_file) loads loads the image into a texture to use on the paddle
    # self.draw() draws the npc paddle
    # self.locate_ball_y() finds the ball actor's y position so that it can position it's self on the y axis.
    # self.set_location() sets npc's y position to ball actor's y position.