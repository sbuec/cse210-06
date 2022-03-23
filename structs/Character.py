import pyray as pr

class Character:
    '''
    struct

    Args:
    - character (str): Single Character
    - font_size (int): Font size of character
    - color (pr.Color): Color of character
    '''

    def __init__(self, character: str, font_size: int, color: pr.Color) -> None:
        self.character = character
        self.font_size = font_size
        self.color = color

    def return_vars(self):
        return self.character, self.font_size, self.color

    def __repr__(self) -> str:
        return f'String("{self.character}", {self.font_size}, Color{self.color})'

    def __str__(self) -> str:
        return f'("{self.character}", {self.font_size}, {self.color})'