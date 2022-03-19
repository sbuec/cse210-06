'''
VideoService is a class designed to hold the things needed to display things
on the computer screen in a window.
'''

import pyray as pr

class VideoService:
    # Creates object using window dimensions, frame rate, and window caption
    def __init__(self, width, height, fps, caption):
        self._width = width
        self._height = height
        self._fps = fps
        self._caption = caption

    # Opens the window
    def open_window(self):
        pr.init_window(self._width, self._height, self._caption)
        pr.set_target_fps(self._fps)

    # Closes the window
    def close_window(self):
        pr.close_window()

    # Clears the window and prepares it for next frame
    # Use at beginning of draw phase
    def clear_buffer(self):
        pr.begin_drawing()
        pr.clear_background(pr.BLACK)

    # Copies buffer to screen
    # Use at end of draw phase
    def flush_buffer(self):
        pr.end_drawing()

    # Checks if wndow is still open
    def check_window(self):
        return not pr.window_should_close()


    # Draws a single actor
    def draw_actor(self, actor):
        pass

    # Draws all actors from a specific group
    def draw_group(self, group):
        pass

    # Draws all actors from all groups
    def draw_all_actors(self, cast):
        pass


