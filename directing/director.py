'''
Starts the game

'''

class Director:
    def __init__(self, keyboardservice, videoservice):
        self._ks = keyboardservice
        self._vs = videoservice

    
    # Runs through the different stages: inputs, updates, and outputs/display
    def run_game(self, cast):
        self._vs.open_window()

    # Runs game until window is closed
        while self._vs.check_window():
            self.get_inputs(cast)
            self.do_updates(cast)
            self.do_outputs(cast)
        self._vs.close_window()

    # Receives inputs from players
    def get_inputs(self, cast):
        pass

    # Updates object values (location, speed, etc.)
    def do_updates(self, cast):
        pass

    # Puts all the changes together and draws next frame
    def do_outputs(self, cast):
        
        # Clears screen to prepare for next frame
        self._vs.clear_buffer()

        # Draws cast
        self._vs.draw_all_actors(cast)
        self._vs.flush_buffer()