import pygame

class Box(pygame.sprite.Sprite):

    def __init__(self, x, y) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((x,y))
        self.rect = self.image.get_rect()
        self.image.fill((70,120,56))


