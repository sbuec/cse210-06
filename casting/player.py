import pyray as pr
from casting.paddle import Paddle
from structs import Window

class Player(Paddle):
    ''' 
    Description: The class that creates and manages player Actors.

    Args:
    - window (Window): The programs information about the Window
    - width (int): Width of paddle
    - height (int): Height paddle
    - color (pr.Color): Color of Paddle
    - paddle_side (str): The side at which the paddle is created ('left' / 'right') 
    - key_dict (dict): The keys that control the player's movement
    '''
    def __init__(self, window: Window, width: int, height: int, texture: pr.Texture, paddle_side: str, key_dict: dict):
        super().__init__(window, width, height, texture, paddle_side)
        self._keys = key_dict
        self.set_initial_movement()
    
    def set_initial_movement(self):
        # Sets initial movements to False to create object without moving
        self._move = {
            'left': False,
            'right': False,
            'up': False,
            'down': False
            }
    
    # self.position_x holds x position
    # self.position_y holds y position
    
    # Actor.image_load_texture(image_file) loads loads the image into a texture to use on the paddle
    # self.draw() draws the player paddle
    # self.set_initial_movement() sets player's initial movement