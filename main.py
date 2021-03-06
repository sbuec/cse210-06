import pyray as pr
from casting.player import Player
from casting.npc import npc
from casting.ball import Ball
from casting.Load import Load
from structs import Window

screen_width = 900
screen_height = 600
screen_fps = 60
screen_caption = 'Pong Renewed'

# player key dictionary
key_dict = {
    'up': pr.is_key_down(pr.KEY_UP) or pr.is_key_down(pr.KEY_W),
    'down': pr.is_key_down(pr.KEY_DOWN) or pr.is_key_down(pr.KEY_S)
}

# holds window information
window = Window(screen_width, screen_height, screen_caption, screen_fps)

def main():

    pr.init_window(*window.pr_window_setup())
    pr.set_target_fps(window.fps_cap)

    # creates ball (window informantion, radius of ball, color of ball)
    ball = Ball(window, 5, pr.WHITE)

    # created a paddle texture (image to make texture from)
    # NOTE: The image can only be a png
    paddle_texture = Load.image_file_to_texture('Paddle.png')

    # creates player and npc paddles (window information, paddle texture, side of screen paddle appears, keys|ball)
    paddle1 = Player(window, paddle_texture, 'left', key_dict)
    paddle2 = npc(window, paddle_texture, 'right', ball)
    bv = [-3, 2]

    while not pr.window_should_close():

        # updated balls position
        ball.update_position(bv[0], bv[1])
        

        # checks to see if ball has collided with paddles
        collided2 = ball.check_collision(paddle2)
        collided1 = ball.check_collision(paddle1)

        pr.begin_drawing()
        pr.clear_background(pr.BLACK)

        # draws paddle
        paddle1.draw()
        paddle2.draw()

        #Update paddle positions
        paddle1.updatePos()
        paddle2.updatePos()

        # draws ball
        ball.draw()

        pr.end_drawing()

        # does something when ball hits paddles
        if collided2:
            ball.calculateBV(paddle2)
        if collided1:
            ball.calculateBV(paddle1)

        if (ball.position_x <= 0):
            paddle2.score += 1
            print(f"You: {paddle1.score} Bot: {paddle2.score}")
            ball.set_start_position()
        elif (ball.position_x >= 900):
            paddle1.score += 1
            print(f"You: {paddle1.score} Bot: {paddle2.score}")
            ball.set_start_position()

        print(paddle1.position_y)
    
    pr.close_window()

if __name__ == "__main__":
    main()