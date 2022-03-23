from structs import Window, Character
import pyray as pr
from casting.Load import Load

class Actor:
    '''
    Description: Base class for all Actors.

    Args:
    - window (Window): The programs information about the Window
    '''
    
    def __init__(self, window: Window):
        self.window = window

    def update_position(self, x_pos, y_pos):
        '''
        Description: updates x/y coords for actors.

        Args:
        x_pos (int): x position
        y_pos (int): y position        
        '''
        self.position_x = x_pos
        self.position_y = y_pos
    
    def image_load_texture(image_file: str) -> pr.Texture:
        '''
        Description: Loads a pr.Texture from an image file.

        Args:
        - image_file (str): The file of the image to load

        Returns:
        - pr.Texture
        '''
        return Load.image_file_to_texture(image_file)

    def set_start_position(self):
        '''
        Description: Default behavior for setting actor's default position.
        '''
        raise NotImplementedError

    def draw(self):
        '''
        Description: Default behavior for drawing an actor. 
        '''
        raise NotImplementedError