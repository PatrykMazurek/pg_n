import pygame
import numpy as np
from box import Box

WIDTH, HEIGHT = 800, 650
FPS = 60

pygame.display.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("game")
clock = pygame.time.Clock()

run = True

def draw_window(win, box):
    win.fill((30,30,30))
    # box.draw(win)
    win.blit(box.image, box.rect)
    pygame.display.update()

# box = pygame.surface.Surface((50,50))
# box.fill((240, 45, 39))
# box_rect = box.get_rect()
# box_rect.center = pygame.math.Vector2(int(WIDTH/2), int(HEIGHT/2) )

box = Box(int(WIDTH/2), int(HEIGHT/2))
move = False

while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # print(pygame.mouse.get_pos())
                move = True
            if event.button == 3:
                print(pygame.mouse.get_pos()[0])
        
        if event.type == pygame.MOUSEBUTTONUP:
            move = False

    #     if event.type == pygame.MOUSEMOTION:
    #         if move:
    #             box_rect.center = pygame.mouse.get_pos()


    # key = pygame.key.get_pressed()
    # if key[pygame.K_d] and box_rect.right < WIDTH:
    #     box_rect.x += 3
    # if key[pygame.K_a] and box_rect.x > 0 :
    #     box_rect.x -= 3
    # if key[pygame.K_w] and box_rect.y > 0:
    #     box_rect.y -= 3
    # if key[pygame.K_s] and box_rect.bottomright[1] < HEIGHT:
    #     box_rect.y += 3



    draw_window(win, box)

pygame.quit()
    