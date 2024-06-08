from typing import Any
import pygame, math
from pygame.math import Vector2
from board_map import *

class Hero(pygame.sprite.Sprite):

    def __init__(self, x, y, name):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        # pola dotyczące obrazu 
        self.image = pygame.Surface((20,20))
        self.image.fill((0,0,180))
        self.rect = self.image.get_rect()
        # pola dotyczące pozycji i pozycji docelowej
        self.speed = 2.
        self.row = x
        self.cell = y
        self.pose = self.get_position(x,y)
        self.rect.center = self.pose
        self.dest_pos = self.get_position(x,y)
        # pola dotyczące wyposarzenia i zachowania 
        self.coin = 0
        self.active_task = []
        self.equipment = []
        self.behavior = None

    def update(self, offset) -> None:
        self.pose += self.move_to()
        if offset.x != 0 or offset.y != 0:
            self.pose += offset
            self.dest_pos += offset
        self.rect.center = self.pose

    def move_to(self):
        dx = self.dest_pos.x - self.rect.centerx
        dy = self.dest_pos.y - self.rect.centery
        distance = math.sqrt(dx**2 + dy**2)
        if distance != 0:
            dx /= distance
            dy /= distance
            speed = 2
            return Vector2(dx * speed, dy * speed)
        return Vector2(0,0)
    
    def move(self, row, coll):
        # określenie pozycji pod względem kolumny i wiersza z mapy 
        if board_map[row, coll] == 2:
            print("umieszczam naszego gracza ")
            self.dest_pos.x = coll * TILE_SIZE[0] + int(TILE_SIZE[0]/2)
            self.dest_pos.y = row * TILE_SIZE[1] + int(TILE_SIZE[1]/2)
            self.dest_pos += global_offset
        else:
            print("nie dozowlone miejsce")

    def get_position(self, row, cell):
        temp_pos = pygame.math.Vector2([0,0])
        temp_pos.x = cell * TILE_SIZE[0] + int(TILE_SIZE[0]/2)
        temp_pos.y = row * TILE_SIZE[1] + int(TILE_SIZE[1]/2)
        temp_pos += global_offset
        return temp_pos