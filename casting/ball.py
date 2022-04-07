from casting.actor import Actor
from structs import Window
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
        '''
        Description: Sets the start position of the ball.
        '''
        self.position_x = self.window.width // 2
        self.position_y = self.window.height // 2

    def draw(self):
        '''
        Description: Draws the ball onto the screen.
        '''
        pr.draw_circle(self.position_x, self.position_y, self.radius, self.color)

    def check_collision(self, paddle):
        '''
        Description: Checks for a collision with the player or the npc.

        Args:
        - paddle (npc or Player): Either the Player instance or npc instance

        Returns:
        - bool: True - Ball has collided | False - Ball has not collided
        '''
        return pr.check_collision_circle_rec(
            pr.Vector2(self.position_x, self.position_y),
            self.radius,
            pr.Rectangle(paddle.position_x, paddle.position_y, paddle.texture.width, paddle.texture.height)
        )
    
    def calculateBV(self, paddle):
        pass

    # self.position_x holds x position
    # self.position_y holds y position
    
    # self.set_start_position() sets the start position of the ball - Called automatically on ball creation
    # self.draw() draws the player paddle
    # self.check_collision(paddle) checks for paddle collisions