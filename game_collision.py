import pygame
from game_task import Task

class GameCollision:

    def __init__(self) -> None:
        pass

    def enemy_collision(self, player, enemies):
        collison = pygame.sprite.spritecollide(player, enemies, False)
        if len(collison) > 0:
            print(collison[0].behavior)