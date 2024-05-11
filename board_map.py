import pygame
from pygame.math import Vector2
import numpy as np

board_map = np.array([
    [1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,2,2,2,2,2,2,1,2,2,1,1,1,1,1,1,1,2,2,2,2,1,1,2,2,2,1,1,1],
    [1,2,2,2,2,2,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,1,1],
    [1,2,2,2,2,2,2,1,2,2,1,1,1,1,1,1,1,2,2,2,2,2,1,2,2,2,2,2,1],
    [1,2,2,2,2,2,2,2,2,2,1,0,0,0,0,0,1,2,2,2,2,2,2,2,2,2,2,2,1],
    [1,2,2,2,2,2,2,2,2,2,1,0,0,0,0,0,1,2,2,2,2,2,2,2,2,2,2,2,1],
    [1,2,2,2,2,2,2,2,2,2,1,0,0,0,0,0,1,2,2,2,2,2,2,2,2,2,2,2,1],
    [1,2,2,2,2,2,2,2,2,2,1,0,0,0,0,0,1,2,2,2,2,2,2,2,2,2,2,2,1],
    [1,2,2,2,2,2,2,2,2,2,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,2,2,2,2,2,2,2,2,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,2,2,2,2,2,2,2,2,2,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,2,2,2,2,2,2,2,2,2,1,0,0,0,0,0,1,2,2,2,2,2,2,2,2,2,2,2,1],
    [1,2,2,2,2,2,2,2,2,2,1,0,0,0,0,0,1,2,2,2,2,2,2,2,2,2,2,2,1],
    [1,2,2,2,2,2,2,2,2,2,1,0,0,0,0,0,1,2,2,2,2,2,2,2,2,2,2,2,1],
    [1,2,2,2,1,1,2,2,2,2,1,1,1,1,1,1,1,2,2,2,2,2,1,1,2,2,2,2,1],
    [1,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,1],
    [1,1,1,1,1,1,2,2,2,2,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,1],
    [0,0,0,0,0,1,2,2,2,2,1,0,0,0,0,0,1,2,2,2,2,2,2,2,2,2,2,2,1],
    [0,0,0,0,0,1,2,2,2,2,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])

class BoardMap:

    def determine_offset(self, mouse_pose, width, height):
        if mouse_pose[0] > 50 and mouse_pose[0] < (width - 50) and mouse_pose[1] > 0 and mouse_pose[1] < 50:
            return  Vector2(0,1) # górę
        if mouse_pose[0] > (width - 50) and mouse_pose[0] < width and mouse_pose[1] > 0 and mouse_pose[1] < 50:
            return  Vector2(-1,1) # prawo góra
        if mouse_pose[0] > (width - 50) and mouse_pose[0] < width and mouse_pose[1] > 50 and mouse_pose[1] < (height - 50):
            return  Vector2(-1,0) # prawo
        if mouse_pose[0] > (width - 50) and mouse_pose[0] < width and mouse_pose[1] > (height - 50) and mouse_pose[1] < height:
            return  Vector2(-1,-1) # prawo dół
        if mouse_pose[0] > 50 and mouse_pose[0] < (width-50) and mouse_pose[1] > (height - 50) and mouse_pose[1] < height:
            return  Vector2(0,-1) # dół
        if mouse_pose[0] > 0 and mouse_pose[0] < 50 and mouse_pose[1] > (height - 50) and mouse_pose[1] < height:
            return  Vector2(1,-1) # lewo dół
        if mouse_pose[0] > 0 and mouse_pose[0] < 50 and mouse_pose[1] > 50 and mouse_pose[1] < (height-50):
            return  Vector2(1,0) # lewo
        if mouse_pose[0] > 0 and mouse_pose[0] < 50 and mouse_pose[1] > 0 and mouse_pose[1] < 50:
            return  Vector2(1,1) # lewo góra
        return Vector2(0,0)
    
    def get_element_from_table(self, pos):
        temp_x = int(pos.x /30)
        temp_y = int(pos.y /30)
        size = board_map.shape * 30
        if pos.x > -1 and pos.y > -1:
            print(" {} {} {} ".format(temp_y, temp_x, board_map[temp_y,temp_x]))
            return temp_y, temp_x, board_map[temp_y,temp_x]
        else:
            print(" poza obszarem")
            return None