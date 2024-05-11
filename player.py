from typing import Any
import pygame, math
from pygame.math import Vector2
from board_map import board_map

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20,20))
        self.image.fill((0,0,180))
        self.rect = self.image.get_rect()
        self.pose = pygame.math.Vector2(x,y)
        self.rect.center = self.pose
        self.dest_pos = pygame.math.Vector2(x,y)
        self.global_offset = pygame.math.Vector2(0,0)

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
            self.dest_pos.x = coll * 30 + 15
            self.dest_pos.y = row * 30 + 15
            self.dest_pos += self.global_offset
        else:
            print("nie dozowlone miejsce")
