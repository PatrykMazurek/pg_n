import pygame, os
import numpy as np
from board_map import *
from player import Player
from enemy import Enemy
# from object_map import ObjectMap
from sprite_animation import SpriteAnimation
from item import Item

WIDTH, HEIGHT = 800, 650
FPS = 60

pygame.display.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("game")
clock = pygame.time.Clock()

run = True

def draw_window(win, board_group, player, enemies_group, coin_group, animation):
    win.fill((30,30,30))
    board_group.draw(win)
    enemies_group.draw(win)
    coin_group.draw(win)
    win.blit(player.image, player.rect)
    animation.draw(win)
    pygame.display.update()

def check_collision(player, enemies):
    collison = pygame.sprite.spritecollide(player, enemies, False)
    if len(collison) > 0:
        print(collison[0].behavior)

maps = BoardMap()

board_wall = pygame.sprite.Group()
cell, row = board_map.shape
for r in range(row):
    for c in range(cell):
        if board_map[c,r] != 0:
            board_wall.add(BoardTile(board_map[c,r], r, c))

player = Player(1,1, "bohater")
all_enemies = pygame.sprite.Group()
all_enemies.add(Enemy(4, 5, player, "boch_1"))
all_enemies.add(Enemy(9, 8, player, "boch_1"))

coins = pygame.sprite.Group()
# coins.add(ObjectMap(5,7, "coin",player))
# coins.add(Item(3, 5, "coin", value=10))

sprite_img = pygame.image.load(os.path.join("assets", "objects", "torch.png"))
animation_step = 6
light_animation = SpriteAnimation(sprite_img, 5,7, animation_step, 16,28)

countdown = 120
last_update = pygame.time.get_ticks()

while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                current_cursor_pos = pygame.mouse.get_pos() - global_offset
                row, cell, _ = maps.get_element_from_table(pygame.math.Vector2(current_cursor_pos))
                player.move(row, cell)
            if event.button == 3:
                print(pygame.mouse.get_pos()[0])

    current_time = pygame.time.get_ticks()
    if (current_time - last_update) >= countdown:
        last_update = current_time
        light_animation.frame += 1
        if light_animation.frame >= animation_step:
            light_animation.frame = 0

    check_collision(player, all_enemies)
    offset = maps.determine_offset(pygame.mouse.get_pos(), WIDTH, HEIGHT)
    global_offset += offset
    board_wall.update(offset)
    player.update(offset)
    all_enemies.update(offset)
    light_animation.update(offset)
    # coins.update(offset)

    draw_window(win, board_wall, player, all_enemies, coins, light_animation)

pygame.quit()
    