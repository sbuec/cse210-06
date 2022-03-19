'''
Service provided to receive input and change associated values
'''
import pyray as pr

class KeyboardService:

    '''
    Receives the actor and its previously defined key associations
    Checks if actor's keys are pressed
    Changes move value to true while associated key is pressed 
    or false while associated key isn't pressed
    '''
    def check_keys_pressed(self, actor, dict):
        for key in dict:
            if pr.is_key_down(dict[key]):
                actor._move[key] = True
            else:
                actor._move[key] = False