from re import S
import pygame
from colors import *
from config import *
from button import *
from icons import *


class Window:
    def __init__(self, actual_window):
        self.x=0
        self.y=0
        self.length=20
        self.height=4/5 * SCREEN_HEIGHT
        self.margin=100
        self.actual_window = actual_window
        
        # graphics staff
        self.triangle_size = 50
        
    
    def draw_me(self):
        if self.actual_window == 'sidebar':

            pygame.draw.polygon(WIN, MENU_GREEN, [
                (self.x, self.margin + self.y),
                (self.x, self.margin + self.y + self.triangle_size),
                (self.x + self.triangle_size, self.margin + self.y + self.triangle_size)
                ])

            pygame.draw.polygon(WIN, MENU_GREEN, [
                (self.x, SCREEN_HEIGHT - (self.margin + self.y)),
                (self.x, SCREEN_HEIGHT - (self.margin + self.y + self.triangle_size)),
                (self.x + self.triangle_size, SCREEN_HEIGHT - (self.margin + self.y + self.triangle_size))
                ])

            pygame.draw.rect(WIN, MENU_GREEN, pygame.Rect(
                self.x, 
                self.margin + self.y + self.triangle_size, 
                self.triangle_size + 1, SCREEN_HEIGHT - (2 * self.margin + 2 * self.triangle_size)))
            

        elif self.actual_window == 'side menu':

            pygame.draw.rect(WIN, MENU_GREEN, 
            pygame.Rect(
                self.x, 
                self.margin + self.y, 
                6 * self.triangle_size, 
            SCREEN_HEIGHT - (2 * self.margin )))

            pygame.draw.polygon(WIN, MENU_GREEN, [
                (self.x +  6 * self.triangle_size, self.margin + self.y),
                (self.x +  6 * self.triangle_size, self.margin + self.y + self.triangle_size),
                (self.x +  7 * self.triangle_size, self.margin + self.y + self.triangle_size)
            ])

            pygame.draw.polygon(WIN, MENU_GREEN, [
                (self.x +  6 * self.triangle_size, SCREEN_HEIGHT - (self.margin + self.y)),
                (self.x +  6 * self.triangle_size, SCREEN_HEIGHT - (self.margin + self.y + self.triangle_size)),
                (self.x +  7 * self.triangle_size, SCREEN_HEIGHT - (self.margin + self.y + self.triangle_size))
                ])

            pygame.draw.rect(WIN, MENU_GREEN, pygame.Rect(
                self.x +  6 * self.triangle_size, 
                self.margin + self.y + self.triangle_size, 
                self.triangle_size + 1, SCREEN_HEIGHT - (2 * self.margin + 2 * self.triangle_size)))


    def add_buttons(self):
        buttons = []
        
        if self.actual_window == 'sidebar':
           
            show_side_menu_button = Button(
                self.triangle_size / 2, (SCREEN_HEIGHT - (-0.5 * self.triangle_size + self.margin)) / 2,
                3* self.triangle_size // 7, 
                self.triangle_size, 'hehe', BLACK, SKY_BLUE, BLUE)

            show_side_menu_button_arrow_icon = Icon(
                [
                    (self.triangle_size/2 +self.triangle_size//10, (SCREEN_HEIGHT - (-0.5 * self.triangle_size + self.margin)) / 2 + 3 * self.triangle_size // 10), 
                    (self.triangle_size/2 + self.triangle_size//10 , (SCREEN_HEIGHT - (-0.5 * self.triangle_size + self.margin)) / 2 + 7 * self.triangle_size // 10), 
                    (self.triangle_size/2 + 3 * self.triangle_size // 10, (SCREEN_HEIGHT - (-0.5 * self.triangle_size + self.margin)) / 2 + self.triangle_size // 2)
            ],
            'triangle', 0, MENU_GREEN)
            buttons.append([show_side_menu_button, show_side_menu_button_arrow_icon, 'show_side_menu_button'])
            

        elif self.actual_window == 'side menu':
           
            hide_side_menu_button = Button(
                self.triangle_size / 2 +  6 * self.triangle_size, 
                (SCREEN_HEIGHT - (-0.5 * self.triangle_size + self.margin)) / 2, 
                3* self.triangle_size // 7 , self.triangle_size, 'hehe', BLACK, SKY_BLUE, BLUE)
            
            hide_side_menu_button_arrow_icon = Icon(
                [
                    (self.triangle_size/2 +3 *self.triangle_size//10  +  6 * self.triangle_size, (SCREEN_HEIGHT - (-0.5 * self.triangle_size + self.margin)) / 2 + 3 * self.triangle_size // 10), 
                    (self.triangle_size/2 + 3 *self.triangle_size//10  +  6 * self.triangle_size, (SCREEN_HEIGHT - (-0.5 * self.triangle_size + self.margin)) / 2 + 7 * self.triangle_size // 10), 
                    (self.triangle_size/2 +  self.triangle_size // 10  +  6 * self.triangle_size, (SCREEN_HEIGHT - (-0.5 * self.triangle_size + self.margin)) / 2 + self.triangle_size // 2)
            ],
            'triangle', 0, MENU_GREEN)
            
            buttons.append([hide_side_menu_button, hide_side_menu_button_arrow_icon, 'hide_side_menu_button'])
       
        return buttons




