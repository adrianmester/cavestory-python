"""Graphics module
"""

import pygame

class Graphics(object):
    """Graphics class
    """

    def __init__(self, size):
        """Create a screen of the specified size
        """
        self._screen = pygame.display.set_mode(size)

    def blit(self, source, dest, area=None, special_flags=0):
        """Draw an image to the screen
        """
        self._screen.blit(source, dest, area, special_flags)

    def flip(self):
        """Flip the display 
        """
        pygame.display.flip()
