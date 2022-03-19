'''
Classes to define objects such as players that use inputs
and NPCs that don't use inputs
'''

class Actor:
    def __init__(self):
        pass


# Class to create playable objects
class Player(Actor):
    ''' 
    Initializes actor
    Requires key dictionary to define which keys affect the player object
    '''
    def __init__(self, key_dict):
        super().__init__()
        self._keys = key_dict
        
        # Sets initial movements to False to create object without moving
        self._move = {
            'left': False,
            'right': False,
            'up': False,
            'down': False
            }

# Class to create objects that move on their own or stay still
class NPC(Actor):
    pass