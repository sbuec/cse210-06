class Window:
    '''
    struct

    Args:
    - width (int): Width of the window
    - height (int): height of the window
    - caption (str) caption of the window
    - fps_cap (int) fps of the window
    '''

    def __init__(self, width: int, height: int, caption: str, fps_cap: int) -> None:
        self.width = width
        self.height = height
        self.caption = caption
        self.fps_cap = fps_cap

    def pr_window_setup(self):
        return self.width, self.height, self.fps_cap, self.caption

    def __repr__(self) -> str:
        return f'Window({self.width}, {self.height}, "{self.caption}", {self.fps_cap})'

    def __str__(self) -> str:
        return f'({self.width}, {self.height}, "{self.caption}", {self.fps_cap})'