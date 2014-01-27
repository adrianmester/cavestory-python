"""Sprite module
"""

import pygame
import game

class Sprite(object):
    """Sprite class
    """

    def __init__(self, path, left, top, width, height):
        """Creates a sprite from the image
        """
        self._image = pygame.image.load(path).convert()
        self._source_rect = pygame.Rect(left, top, width, height)

    def draw(self, graphics, x, y):
        """Draw the sprite to the specified graphics object
        """
        graphics.blit(self._image, (x, y), area=self._source_rect)


class AnimatedSprite(Sprite):
    """Animated sprite class, ingerits Sprite
    """

    def __init__(self, path, left, top, width, height, fps, num_frames):
        """Created the animated sprite
        """
        super(AnimatedSprite, self).__init__(path, left, top, width, height)
        self.frame_time = 1000.0 / fps
        self.num_frames = num_frames
        self.current_frame = 0
        self.elapsed_time = 0

    def update(self, elapsed_time_ms):
        """Updates the sprite based on elapsed ms
        """
        self.elapsed_time += elapsed_time_ms
        if (self.elapsed_time > self.frame_time):
            self.current_frame += 1
            self.elapsed_time = 0

            if self.current_frame < self.num_frames:
                self._source_rect.x += game.Game.tile_size
            else:
                # we're at the end, go back to the first frame
                self._source_rect.x -= game.Game.tile_size * (self.num_frames - 1)
                self.current_frame = 0
