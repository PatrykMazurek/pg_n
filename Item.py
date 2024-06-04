import pygame
from board_map import *

class Item(pygame.surface.Surface):

    def __init__(self, row, cell, type, value=0 ) -> None:
        # typ i nazwa obiektu
        self.type = type
        self.name = None
        # pozycja i grafika obiektu
        self.row = row
        self.cell = cell
        self.image = self.cut_image(type)
        self.rect = self.image.get_rect()
        self.pose = pygame.math.Vector2(self.set_position(row, cell))
        self.rect.center = self.pose
        # dodakiwe własnści obiektu
        self.task = None
        self.coin_value = value
        self.equpment = []

    def update(self, offset) -> None:
        self.rect.x += offset.x
        self.rect.y += offset.y

    def set_position(self, row, cell):
        temp_pos = pygame.math.Vector2([0,0])
        temp_pos.x = cell * TILE_SIZE[0] + int(TILE_SIZE[0]/2)
        temp_pos.y = row * TILE_SIZE[1] + int(TILE_SIZE[1]/2)
        return temp_pos
    
    def cut_image(self, type):
        item_pos = {"coin": [[3,3], [3,4], [4,3]],
                    "box" : [[2,4], [2,5], [2,6], [4,4], [4,5], [4,6]],
                    "task": [[2,11], [3,11], [4,11]],
                    "key" : [[4,8],[4,9]]}
        
        sheet = pygame.image.load(os.path.join("assets", "objects", "Dungeon_item_props_v2.png"))
        img = pygame.Surface((16,16))
        pos = random.choice(item_pos[type])
        pos = [pos[0] * 16, pos[1] * 16, 16, 16]
        img.blit(sheet, (0,0), pos)
        return img