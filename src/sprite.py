"""Sprite module
"""

import pygame

class Sprite(object):
    """Sprite class
    """

    def __init__(self, path, left, top, width, height):
        """Creates a sprite from the image
        """
        self._image = pygame.image.load(path).convert()
        self._source_rect = pygame.Rect(left, top, width, height)

    def draw(self, graphics, x, y):
        graphics.blit(self._image, (x, y), area=self._source_rect)
