"""Game module
"""

import pygame
import graphics
from sprite import Sprite

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

        self.sprite = Sprite("MyChar.bmp", 0, 0, self.tile_size, self.tile_size)

    def loop(self):
        """The main event loop
        """
        running = True
        while running:
            for event in pygame.event.get():
                if event.type is pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                elif event.type is pygame.QUIT:
                    running = False
            
            self.update()

            self.draw()

            self.clock.tick(self.fps)

    def update(self):
        """Update object postion
        """
        pass

    def draw(self):
        """Draw the objects
        """
        self.sprite.draw(self.graphics, 320, 240)
        self.graphics.flip()
