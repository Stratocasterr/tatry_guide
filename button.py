import pygame
import numpy as np
from colors import *
from config import *
import text

class Button:
    def __init__(self, x, y, length, height, text, text_front_color, text_backing_color, activate_color):
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.text = text
        self.text_front_color = text_front_color
        self.text_backing_color = text_backing_color
        self.activate_color = activate_color
        self.active_button = False
        self.rect = pygame.Rect(self.x, self.y, self.length, self.height)

        self.allow = False
        

    def draw_the_button(self):
        self.active_button = False
        color = self.button_press()

        pygame.draw.rect(WIN, color,
                         pygame.Rect(self.x, self.y, self.length, self.height))

        text.text_rendering(self.text, self.text_front_color, color,
                            (self.x + self.length / 2, self.y + self.height / 2), BASIC_FONT)

        

    def button_press(self):
        collide_color = WHITE
        color = self.text_backing_color
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if not pygame.mouse.get_pressed()[0]:
                if self.text_backing_color == WHITE: collide_color = SKY_BLUE
                pygame.draw.rect(WIN, collide_color,
                                 pygame.Rect(self.x + 2, self.y + 2, self.length, self.height), 2)

            else:
                color = self.activate_color
                self.active_button = True

        return color

    def change_color(self, new_color):
        self.text_backing_color = new_color

    

    