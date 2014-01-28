"""Player module
"""

import pygame
import sprite
import game

class Player(object):
    """Player class
    """

    walking_acceleration = 0.0012   # pixels / ms / ms
    max_speed_x = 0.325             # pixels / ms
    slowdown_factor = 0.8

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.acceleration_x = 0.0
        self.velocity_x = 0
        self.sprite = sprite.AnimatedSprite(
                "content/MyChar.bmp", 0, 0,
                game.Game.tile_size, game.Game.tile_size,
                15, 3
        )

    def update(self, elapsed_time_ms):
        self.sprite.update(elapsed_time_ms)

        self.x += round(self.velocity_x * elapsed_time_ms)
        self.velocity_x += self.acceleration_x * elapsed_time_ms
        if self.acceleration_x < 0:
            self.velocity_x = max(self.velocity_x, -self.max_speed_x)
        elif self.acceleration_x > 0:
            self.velocity_x = min(self.velocity_x, self.max_speed_x)
        else:
            self.velocity_x *= self.slowdown_factor

    def draw(self, graphics):
        self.sprite.draw(graphics, self.x, self.y)

    def start_moving_left(self):
        self.acceleration_x -= self.walking_acceleration
    
    def start_moving_right(self):
        self.acceleration_x += self.walking_acceleration
    
    def stop_moving(self):
        self.acceleration_x = 0.0
