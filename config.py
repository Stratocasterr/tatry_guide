from tkinter import font
import pygame
SCREEN_HEIGHT = 900
SCREEN_LENGTH = 1700

# text staff
pygame.font.init()
BASIC_FONT = pygame.font.Font('fonts/freesansbold.ttf', 10)

CRAZY_FONT = pygame.font.Font('fonts/FlappyBirdy.ttf',20)
WIN = pygame.display.set_mode((SCREEN_LENGTH, SCREEN_HEIGHT))


# images 

# map images
LT_MAP=pygame.image.load('images/mapLT.jpg')
LT_MAP_SIZE=[LT_MAP.get_width(),LT_MAP.get_height()]

LB_MAP=pygame.image.load('images/mapLB.jpg')
LB_MAP_SIZE=[LB_MAP.get_width(),LB_MAP.get_height()]

RT_MAP=pygame.image.load('images/mapRT.jpg')
RT_MAP_SIZE=[RT_MAP.get_width(),RT_MAP.get_height()]

RB_MAP=pygame.image.load('images/mapRB.jpg')
RB_MAP_SIZE=[RB_MAP.get_width(),RB_MAP.get_height()]

# side menu images
TATRY_GUIDE_LOGO = pygame.image.load('images/tatryguide_logo.jpg')
TATRY_GUIDE_LOGO = pygame.transform.scale(TATRY_GUIDE_LOGO, (257, 177))

SAVE_TATRY = pygame.image.load('images/savetatry.png')
SAVE_TATRY = pygame.transform.scale(SAVE_TATRY,(101, 20))

FIND_YOUR_WAY = pygame.image.load('images/findyourway.png')
FROM = pygame.image.load('images/from.png')
TO = pygame.image.load('images/to.png')

SEARCH = pygame.image.load('images/search.png')
SEARCH = pygame.transform.scale(SEARCH, (70, 30))


# start menu images
START_MENU = pygame.image.load('images/start_menu.png')
START_MENU_START = pygame.image.load('images/start_menu_start.png')
START_MENU_QUIT = pygame.image.load('images/start_menu_quit.png')
START_MENU_ABOUT = pygame.image.load('images/start_menu_about.png')