import pygame, math, random
from board_map import *

class Enemy(pygame.sprite.Sprite):

    def __init__(self, player, row, cell) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30,30))
        self.image.fill((140,190,130))
        self.rect = self.image.get_rect()
        self.player = player
        self.row = row
        self.cell = cell
        self.pose = pygame.math.Vector2(self.set_position(row, cell))
        self.dest_pos = pygame.math.Vector2(self.set_position(row, cell))
        self.rect.center = self.pose
        self.speed = 1.5
        self.behavior = random.choice(["agressive","neutral","passive"])
        self.asction = None

    def update(self, offset) -> None:
        self.interaction()
        self.pose += self.move_to()
        if offset.x != 0 or offset.y != 0:
            self.pose += offset
            self.dest_pos += offset
        self.rect.center = self.pose


    def set_position(self, row, cell):
        temp_pos = pygame.math.Vector2([0,0])
        temp_pos.x = cell * 30 + 15
        temp_pos.y = row * 30 + 15
        temp_pos += self.player.global_offset
        return temp_pos

    def move(self, type):
        if type != None:
            if type == "attac":
                dx = self.player.pose.x - self.rect.centerx
                dy = self.player.pose.y - self.rect.centery
                distance = math.sqrt(dx**2 + dy**2)
                if distance < 50:
                    self.speed = 2
                else:
                    self.speed = 0
                if distance != 0:
                    dx /= distance
                    dy /= distance
                self.rect.centerx += dx * self.speed
                self.rect.centery += dy * self.speed
            elif type == "run":
                if self.dest_pos.distance_to(self.pose) < 0.5:
                    # założenie że przeciwnik ucieka w  losowym kierunku
                    self.action = random.randint(0,8)
                    match self.action:
                        case 0:
                            if board_map[self.row-1, self.cell-1] == 2:
                                self.dest_pos = self.set_position(self.row-1, self.cell-1)
                        case 1:
                            if board_map[self.row-1, self.cell] == 2:
                                self.dest_pos = self.set_position(self.row-1, self.cell)
                        case 2:
                            if board_map[self.row-1, self.cell+1] == 2:
                                self.dest_pos = self.set_position(self.row-1, self.cell+1)
                        case 3:
                            if board_map[self.row, self.cell+1] == 2:
                                self.dest_pos = self.set_position(self.row, self.cell+1)
                        case 4:
                            if board_map[self.row+1, self.cell+1] == 2:
                                self.dest_pos = self.set_position(self.row+1, self.cell+1)
                        case 5:
                            if board_map[self.row+1, self.cell] == 2:
                                self.dest_pos = self.set_position(self.row+1, self.cell)
                        case 6:
                            if board_map[self.row+1, self.cell] == 2:
                                self.dest_pos = self.set_position(self.row+1, self.cell-1)
                        case 7:
                            if board_map[self.row+1, self.cell] == 2:
                                self.dest_pos = self.set_position(self.row, self.cell)


    def move_to(self):
        dx = self.dest_pos.x - self.rect.centerx
        dy = self.dest_pos.y - self.rect.centery
        distance = math.sqrt(dx**2 + dy**2)
        if distance != 0:
            dx /= distance
            dy /= distance
            return Vector2(dx * self.speed, dy * self.speed)
        return Vector2(0,0)

    def check_distance(self):
        dx = self.player.pose.x - self.rect.centerx
        dy = self.player.pose.y - self.rect.centery
        return math.sqrt(dx**2 + dy**2)
    
    def interaction(self):
        distance = self.check_distance()
        if distance < 50:
            match self.behavior:
                case "agressive":
                    self.move("attac")
                case "passive":
                    self.move("run")
        else:
            self.move(None)