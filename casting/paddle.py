from casting.actor import Actor
from structs import Rectangle, Window
import pyray as pr

class Paddle(Actor):
    '''
    Description: Class for creating and managing the paddles.

    Args:
    - window (Window): The programs information about the Window
    - width (int): Width of paddle
    - height (int): Height paddle
    - color (pr.Color): Color of Paddle
    - paddle_side (str): The side at which the paddle is created ('left' / 'right') 
    '''

    def __init__(self, window: Window, width: int, height: int, texture: pr.Texture, paddle_side: str):
        super().__init__(window)
        self.width = width
        self.height = height
        self.texture = texture
        self.paddle_side = paddle_side
        self.set_start_position()

    def set_start_position(self):
        if self.paddle_side == 'left':
            self.position_x = self.window.width // 8

        if self.paddle_side == 'right':
            self.position_x = self.window.width // 8 * 7

        self.position_y = self.window.height // 2

    def draw(self):
        pr.draw_texture_rec(
            self.texture,
            pr.Rectangle(0,0, float(self.texture.width), float(self.texture.height)),
            pr.Vector2(self.position_x, self.position_y),
            pr.WHITE)