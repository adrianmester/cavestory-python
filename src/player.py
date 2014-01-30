"""Player module
"""

import sprite
import game


class SpriteState(object):
    """Sprite State class"""

    class MotionType(object):
        """Motion type enum, possible values: STANDING, WALKING"""
        STANDING, WALKING = range(2)

    class HorizontalFacing(object):
        """Horizontal facing enum, possible values: LEFT, RIGHT"""
        LEFT, RIGHT = range(2)

    def __init__(self, motion_type=MotionType.WALKING,
                 horizontal_facing=HorizontalFacing.LEFT):
        """Sprite state initializer"""
        self.motion_type = motion_type
        self.horizontal_facing = horizontal_facing

    def __cmp__(self, other):
        """Define the comparisson operator, first check motion type.
        If the motion type is the same, compare the horizontal facing"""
        if self.motion_type != other.motion_type:
            return self.motion_type.__cmp__(other.motion_type)
        return self.horizontal_facing.__cmp__(other.horizontal_facing)

    def __hash__(self):
        """Object hash based on its member values"""
        return self.motion_type * 10 + self.horizontal_facing


class Jump(object):
    jump_time = 275

    def __init__(self):
        self.time_remaining = 0
        self.active = False

    def reset(self):
        self.time_remaining = self.jump_time
        self.reactivate()

    def reactivate(self):
        self.active = self.time_remaining > 0

    def deactivate(self):
        self.active = False

    def update(self, elapsed_time_ms):
        if self.active:
            self.time_remaining -= elapsed_time_ms
            if self.time_remaining <= 0:
                # Can't we just call reactivate here?
                self.active = False


class Player(object):
    """Player class
    """

    walking_acceleration = 0.0012   # pixels / ms / ms
    max_speed_x = 0.325             # pixels / ms
    slowdown_factor = 0.8
    jump_speed = 0.325
    gravity = walking_acceleration
    max_speed_y = 0.325


    def __init__(self, graphics, x, y):
        """Create the player at the specified position"""
        self.x = x
        self.y = y
        self.acceleration_x = 0.0
        self.velocity_x = 0
        self.velocity_y = 0
        self.sprites = {}
        self.initialize_sprites(graphics)
        self.horizontal_facing = SpriteState.HorizontalFacing.LEFT
        self.jump = Jump()

    def get_sprite_state(self):
        """Get the current sprite state"""
        if self.acceleration_x == 0:
            motion_type = SpriteState.MotionType.STANDING
        else:
            motion_type = SpriteState.MotionType.WALKING
        return SpriteState(motion_type, self.horizontal_facing)


    def initialize_sprites(self, graphics):
        """Create sprites for each state"""
        # Walking Left
        self.sprites[SpriteState(
            SpriteState.MotionType.WALKING,
            SpriteState.HorizontalFacing.LEFT
        )] = sprite.AnimatedSprite(
                graphics,
                "content/MyChar.bmp", 0, 0,
                game.Game.tile_size, game.Game.tile_size,
                15, 3
        )

        # Standing Left
        self.sprites[SpriteState(
            SpriteState.MotionType.STANDING,
            SpriteState.HorizontalFacing.LEFT
        )] = sprite.Sprite(
                graphics,
                "content/MyChar.bmp", 0, 0,
                game.Game.tile_size, game.Game.tile_size
        )

        # Walking Right
        self.sprites[SpriteState(
            SpriteState.MotionType.WALKING,
            SpriteState.HorizontalFacing.RIGHT
        )] = sprite.AnimatedSprite(
                graphics,
                "content/MyChar.bmp", 0, game.Game.tile_size,
                game.Game.tile_size, game.Game.tile_size,
                15, 3
        )

        # Standing Right
        self.sprites[SpriteState(
            SpriteState.MotionType.STANDING,
            SpriteState.HorizontalFacing.RIGHT
        )] = sprite.Sprite(
                graphics,
                "content/MyChar.bmp", 0, game.Game.tile_size,
                game.Game.tile_size, game.Game.tile_size
        )

    def update(self, elapsed_time_ms):
        """Update the player position and animation frame"""
        self.jump.update(elapsed_time_ms)

        self.sprites[self.get_sprite_state()].update(elapsed_time_ms)

        self.x += round(self.velocity_x * elapsed_time_ms)
        self.velocity_x += self.acceleration_x * elapsed_time_ms
        if self.acceleration_x < 0:
            self.velocity_x = max(self.velocity_x, -self.max_speed_x)
        elif self.acceleration_x > 0:
            self.velocity_x = min(self.velocity_x, self.max_speed_x)
        elif self.on_ground():
            self.velocity_x *= self.slowdown_factor

        self.y += round(self.velocity_y * elapsed_time_ms)
        if not self.jump.active:
            self.velocity_y = min(
                self.velocity_y + self.gravity * elapsed_time_ms,
                self.max_speed_y
            )

        # TODO: remove this hack
        if self.y >= 320:
            self.y = 320
            self.velocity_y = 0

    def draw(self, graphics):
        """Draw the player on the screen"""
        self.sprites[self.get_sprite_state()].draw(graphics, self.x, self.y)

    def start_moving_left(self):
        """Start moving the player to the left"""
        self.acceleration_x = -self.walking_acceleration
        self.horizontal_facing = SpriteState.HorizontalFacing.LEFT

    def start_moving_right(self):
        """Start moving the player to the right"""
        self.acceleration_x = self.walking_acceleration
        self.horizontal_facing = SpriteState.HorizontalFacing.RIGHT

    def stop_moving(self):
        """Stop the player"""
        self.acceleration_x = 0.0

    def start_jump(self):
        if self.on_ground():
            self.jump.reset()
            self.velocity_y = -self.jump_speed
        elif self.velocity_y < 0:
            self.jump.reactivate()

    def stop_jump(self):
        self.jump.deactivate()

    def on_ground(self):
        return self.y >= 320
