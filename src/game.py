"""Game module
"""

import pygame

class Game(object):
    """Game class
    """

    def __init__(self, width=640, height=480, fps=60):
        """Initialize the game, takes screenw width, height
        and max fps as parameters
        """
        self.width = width
        self.height = width
        self.fps = fps
        self.size = width, height

        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()

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
        pass
