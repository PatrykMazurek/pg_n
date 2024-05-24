import pygame
from board_map import *


class Item(pygame.surface.Surface):

    def __init__(self, row, cell, type) -> None:
        self.type = type
        self.row = row
        self.cell = cell
        self.image = pygame.Surface((30,30))
        self.rect = self.image.get_rect()
        self.pose = pygame.math.Vector2(self.set_position(row, cell))
        self.rect.center = self.pose

    def update(self, offset) -> None:
        self.rect.x += offset.x
        self.rect.y += offset.y

    def set_position(self, row, cell):
        temp_pos = pygame.math.Vector2([0,0])
        temp_pos.x = cell * TILE_SIZE[0] + int(TILE_SIZE[0]/2)
        temp_pos.y = row * TILE_SIZE[1] + int(TILE_SIZE[1]/2)
        return temp_pos