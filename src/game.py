"""Game module
"""

import pygame
import graphics
from player import Player

class Game(object):
    """Game class
    """

    tile_size = 32

    def __init__(self, width=640, height=480, fps=60):
        """Initialize the game, takes screenw width, height
        and max fps as parameters
        """
        self.width = width
        self.height = width
        self.fps = fps
        self.size = width, height

        self.graphics = graphics.Graphics(self.size)
        self.clock = pygame.time.Clock()

        self.player = Player(self.graphics, 320, 240)

    def loop(self):
        """The main event loop
        """
        running = True
        while running:
            key_input = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type is pygame.QUIT:
                    running = False
            if key_input[pygame.K_ESCAPE]:
                running = False

            # Player horizonal
            if key_input[pygame.K_LEFT] and key_input[pygame.K_RIGHT]:
                self.player.stop_moving()
            elif key_input[pygame.K_LEFT]:
                self.player.start_moving_left()
            elif key_input[pygame.K_RIGHT]:
                self.player.start_moving_right()
            else:
                self.player.stop_moving()

            # Player jump
            if key_input[pygame.K_z]:
                self.player.start_jump()
            else:
                # released?
                self.player.stop_jump()

            self.clock.tick(self.fps)
            
            self.update(self.clock.get_time())

            self.draw()

    def update(self, elapsed_time_ms):
        """Update object postion
        """
        self.player.update(elapsed_time_ms)

    def draw(self):
        """Draw the objects
        """
        self.graphics.clear()
        self.player.draw(self.graphics)
        self.graphics.flip()
