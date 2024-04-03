import pygame

from scripts.settings import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, sprite_type, surface=pygame.Surface((TILESIZE, TILESIZE))):
        super().__init__(groups)
        self.sprite_type = sprite_type
        y_offset = HITBOX_OFFSET[sprite_type]
        self.image = surface

        self.rect = self.image.get_rect(
            topleft=pos - pygame.math.Vector2(0, TILESIZE) if sprite_type == 'object' else pos)
        self.hitbox = self.rect.inflate(0, y_offset)
