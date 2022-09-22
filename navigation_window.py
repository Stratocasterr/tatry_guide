from re import S, search
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

            # main menu area
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

            # put images

            WIN.blit(TATRY_GUIDE_LOGO,(0.75 * self.triangle_size, (SCREEN_HEIGHT - 3 * self.margin) ))
            # WIN.blit(SAVE_TATRY,(2.3 * self.triangle_size, (SCREEN_HEIGHT  - 5 * self.margin // 4 )))
            WIN.blit(FIND_YOUR_WAY,(0.9 * self.triangle_size, self.margin + 0.5 * self.triangle_size))
            WIN.blit(FROM,(0.2 * self.triangle_size, 4 * self.triangle_size))
            WIN.blit(TO,(0.45 * self.triangle_size, 5.2 * self.triangle_size))
            WIN.blit(SEARCH,(0.45 * self.triangle_size, 6.2 * self.triangle_size))


    def add_buttons(self):
        buttons = []
        
        if self.actual_window == 'sidebar':
           
            show_side_menu_button = Button(
                self.triangle_size / 2, (SCREEN_HEIGHT - (-0.5 * self.triangle_size + self.margin)) / 2,
                3* self.triangle_size // 7, 
                self.triangle_size, '', BLACK, SKY_BLUE, BLUE)

            show_side_menu_button_arrow_icon = Icon(
                [
                    (self.triangle_size/2 +self.triangle_size//10, (SCREEN_HEIGHT - (-0.5 * self.triangle_size + self.margin)) / 2 + 3 * self.triangle_size // 10), 
                    (self.triangle_size/2 + self.triangle_size//10 , (SCREEN_HEIGHT - (-0.5 * self.triangle_size + self.margin)) / 2 + 7 * self.triangle_size // 10), 
                    (self.triangle_size/2 + 3 * self.triangle_size // 10, (SCREEN_HEIGHT - (-0.5 * self.triangle_size + self.margin)) / 2 + self.triangle_size // 2)
            ],
            'triangle', 0, MENU_GREEN)
            buttons.append([show_side_menu_button,'show_side_menu_button', show_side_menu_button_arrow_icon])
            

        elif self.actual_window == 'side menu':

            # hide menu
           
            hide_side_menu_button = Button(
                self.triangle_size / 2 +  6 * self.triangle_size, 
                (SCREEN_HEIGHT - (-0.5 * self.triangle_size + self.margin)) / 2, 
                3* self.triangle_size // 7 , self.triangle_size, '', BLACK, SKY_BLUE, BLUE)
            
            hide_side_menu_button_arrow_icon = Icon(
                [
                    (self.triangle_size/2 +3 *self.triangle_size//10  +  6 * self.triangle_size, (SCREEN_HEIGHT - (-0.5 * self.triangle_size + self.margin)) / 2 + 3 * self.triangle_size // 10), 
                    (self.triangle_size/2 + 3 *self.triangle_size//10  +  6 * self.triangle_size, (SCREEN_HEIGHT - (-0.5 * self.triangle_size + self.margin)) / 2 + 7 * self.triangle_size // 10), 
                    (self.triangle_size/2 +  self.triangle_size // 10  +  6 * self.triangle_size, (SCREEN_HEIGHT - (-0.5 * self.triangle_size + self.margin)) / 2 + self.triangle_size // 2)
            ],
            'triangle', 0, MENU_GREEN)
            
            buttons.append([hide_side_menu_button, 'hide_side_menu_button', hide_side_menu_button_arrow_icon])

            # from

            from_button = Button(
                2.2 * self.triangle_size,
                self.margin + 2.3* self.triangle_size,
                2.5 * self.triangle_size,
                0.5 * self.triangle_size,
                '...',
                MENU_GREEN,
                WHITE,
                SKY_BLUE
                
            )

            buttons.append([from_button,'from_button'])

            # clear from

            clear_from_button = Button(
                4.8 * self.triangle_size,
                self.margin + 2.3* self.triangle_size,
                0.5 * self.triangle_size,
                0.5 * self.triangle_size,
                'X',
                WHITE,
                RED,
                SKY_BLUE
                
            )

            buttons.append([clear_from_button,'clear_from_button'])

            help_from_button = Button(
                5.4 * self.triangle_size,
                self.margin + 2.3* self.triangle_size,
                0.5 * self.triangle_size,
                0.5 * self.triangle_size,
                '?',
                WHITE,
                SKY_BLUE,
                SKY_BLUE
                
            )

            buttons.append([help_from_button,'help_from_button'])

            # to
            to_button = Button(
                2.2 * self.triangle_size,
                self.margin + 3.3* self.triangle_size,
                2.5 * self.triangle_size,
                0.5 * self.triangle_size,
                '...',
                MENU_GREEN,
                WHITE,
                SKY_BLUE
                
            )

            buttons.append([to_button,'to_button'])

            # clear to

            clear_to_button = Button(
                4.8 * self.triangle_size,
                self.margin + 3.3* self.triangle_size,
                0.5 * self.triangle_size,
                0.5 * self.triangle_size,
                'X',
                WHITE,
                RED,
                SKY_BLUE
                
            )

            buttons.append([clear_to_button,'clear_to_button'])

            help_to_button = Button(
                5.4 * self.triangle_size,
                self.margin + 3.3* self.triangle_size,
                0.5 * self.triangle_size,
                0.5 * self.triangle_size,
                '?',
                WHITE,
                SKY_BLUE,
                SKY_BLUE
                
            )

            buttons.append([help_to_button,'help_to_button'])

            # search
            search_button = Button(
                2.2 * self.triangle_size,
                self.margin + 4.3* self.triangle_size,
                2.5 * self.triangle_size,
                0.5 * self.triangle_size,
                'type your place...',
                MENU_GREEN,
                WHITE,
                SKY_BLUE
                
            )

            buttons.append([search_button,'search_button'])


            draw_path_button = Button(
                4.8 * self.triangle_size,
                self.margin + 4.3* self.triangle_size,
                1.1 * self.triangle_size,
                0.5 * self.triangle_size,
                'Draw path',
                WHITE,
                SKY_BLUE,
                SKY_BLUE
            
            )

            buttons.append([draw_path_button,'draw_path_button'])
       
        return buttons




