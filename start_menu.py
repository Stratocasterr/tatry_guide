from email.mime import image
from pickle import TRUE
from re import T
import pygame
from config import *

def starting_menu():
    
    start_btn_rect = pygame.Rect(756, 619, 146, 52)
    
    quit_btn_rect = pygame.Rect(769, 796, 130, 52)
    
    about_btn_rect = pygame.Rect(750, 709, 175, 52)
    run = True
    image = START_MENU
    while run:
        
        WIN.blit(image,(0,0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return [False, False]

            if start_btn_rect.collidepoint(pygame.mouse.get_pos()): 
                image = START_MENU_START
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    return [False, True]

            elif quit_btn_rect.collidepoint(pygame.mouse.get_pos()): 
                image = START_MENU_QUIT
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return [False, False]

            elif about_btn_rect.collidepoint(pygame.mouse.get_pos()): 
                image = START_MENU_ABOUT
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return [False, False]
            else: image = START_MENU
        pygame.display.update()
    return False