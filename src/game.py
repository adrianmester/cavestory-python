"""Game module
"""

import pygame
import graphics
from sprite import AnimatedSprite

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

        self.sprite = AnimatedSprite("MyChar.bmp", 0, 0, self.tile_size,
                                     self.tile_size, 15, 3)

    def loop(self):
        """The main event loop
        """
        running = True
        while running:
            key_input = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type is pygame.QUIT:
                    running = False
            if key_pressed[pygame.K_ESCAPE]:
                running = False
            
            self.clock.tick(self.fps)
            
            self.update(self.clock.get_time())

            self.draw()

    def update(self, elapsed_time_ms):
        """Update object postion
        """
        self.sprite.update(elapsed_time_ms)

    def draw(self):
        """Draw the objects
        """
        self.sprite.draw(self.graphics, 320, 240)
        self.graphics.flip()
