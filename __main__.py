import pyray as pr

from services.keyboardservice import KeyboardService
from services.videoservice import VideoService

from directing.director import Director

from casting.actor import Actor
from casting.actor import Player
from casting.actor import NPC

# Screen values
screen_width = 900
screen_height = 600
screen_fps = 60
screen_caption = 'Pong Renewed'

def main():
    # Creates service objects
    ks = KeyboardService()
    vs = VideoService(screen_width, screen_height, screen_fps, screen_caption)

    # Creates an array for the cast
    cast = []

    # Player setup values
    # Dictionary to define which keys are assigned to player
    player_keys = {
        'left': pr.KEY_A,
        'right': pr.KEY_D,
        'up': pr.KEY_W,
        'down': pr.KEY_S
        }

    cast.append(Player(player_keys))

    # Officially starts the game
    director = Director(ks, vs)
    director.start_game(cast)

if __name__ == "__main__":
    main()