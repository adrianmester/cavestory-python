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
        self._image_cache = {}

    def load_image(self, file_path):
        if file_path not in self._image_cache:
            self._image_cache[file_path] =\
                    pygame.image.load(file_path).convert()
        for k, v in self._image_cache.iteritems():
            print k, id(v)
        return self._image_cache[file_path]

    def blit(self, source, dest, area=None, special_flags=0):
        """Draw an image to the screen
        """
        self._screen.blit(source, dest, area, special_flags)

    def flip(self):
        """Flip the display 
        """
        pygame.display.flip()

    def clear(self):
        """Clear the screen with black
        """
        self._screen.fill(0)    # black
