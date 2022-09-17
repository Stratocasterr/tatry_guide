import pygame
SCREEN_HEIGHT = 900
SCREEN_LENGTH = 1700


WIN = pygame.display.set_mode((SCREEN_LENGTH, SCREEN_HEIGHT))

LT_MAP=pygame.image.load('images/mapLT.jpg')
LT_MAP_SIZE=[LT_MAP.get_width(),LT_MAP.get_height()]

LB_MAP=pygame.image.load('images/mapLB.jpg')
LB_MAP_SIZE=[LB_MAP.get_width(),LB_MAP.get_height()]

RT_MAP=pygame.image.load('images/mapRT.jpg')
RT_MAP_SIZE=[RT_MAP.get_width(),RT_MAP.get_height()]

RB_MAP=pygame.image.load('images/mapRB.jpg')
RB_MAP_SIZE=[RB_MAP.get_width(),RB_MAP.get_height()]