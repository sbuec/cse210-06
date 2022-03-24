from structs import Window

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
        self.position_x += x_pos
        self.position_y += y_pos

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