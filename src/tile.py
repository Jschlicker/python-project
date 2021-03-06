from lib2to3.pytree import convert
import pygame
from settings import *

class Tile(pygame.sprite.Sprite):

    # Initialize tile
    def __init__(self,pos,groups,sprite_type,surface = pygame.Surface((TILESIZE,TILESIZE))):
        super().__init__(groups)
        self.sprite_typye = sprite_type
        self.image = surface
        if sprite_type =='object':
            # do an offset
            self.rect = self.image.get_rect(topleft = (pos[0],pos[1] - TILESIZE))
            self.hitbox = self.rect.inflate(0,-40)
        else:
            self.rect = self.image.get_rect(topleft = pos)
            self.hitbox = self.rect.inflate(0,-20)