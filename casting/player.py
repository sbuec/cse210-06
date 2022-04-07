import pyray as pr
from casting.paddle import Paddle
from structs import Window

class Player(Paddle):
    ''' 
    Description: The class that creates and manages player Actors.

    Args:
    - window (Window): The programs information about the Window
    - color (pr.Color): Color of Paddle
    - paddle_side (str): The side at which the paddle is created ('left' / 'right') 
    - key_dict (dict): The keys that control the player's movement
    '''
    def __init__(self, window: Window, texture: pr.Texture, paddle_side: str, key_dict: dict):
        super().__init__(window, texture, paddle_side)
        self._keys = key_dict
        self.set_initial_movement()
        self.window = Window
    
    def set_initial_movement(self):
        # Sets initial movements to False to create object without moving
        self._move = {
            'up': False,
            'down': False
            }

    def clamp(self, n, minn, maxn):
        if n < minn:
            return minn
        elif n > maxn:
            return maxn
        else:
            return n

    def updatePos(self):
        if (pr.is_key_down(pr.KEY_UP) or pr.is_key_down(pr.KEY_W)):
            self.position_y -= self.speed
        elif (pr.is_key_down(pr.KEY_DOWN) or pr.is_key_down(pr.KEY_S)):
            self.position_y += self.speed

        self.position_y = self.clamp(self.position_y, 5, 375)


    # self.position_x holds x position
    # self.position_y holds y position
    
    # Actor.image_load_texture(image_file) loads loads the image into a texture to use on the paddle
    # self.draw() draws the player paddle
    # self.set_initial_movement() sets player's initial movement - This is called when paddle is created