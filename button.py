import pygame
import numpy as np
from colors import *
from config import *


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

    def draw_the_button(self):
        self.active_button = False
        color = self.button_press()

        pygame.draw.rect(WIN, color,
                         pygame.Rect(self.x, self.y, self.length, self.height))

        

    def button_press(self):

        color = self.text_backing_color
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if not pygame.mouse.get_pressed()[0]:
                pygame.draw.rect(WIN, WHITE,
                                 pygame.Rect(self.x + 2, self.y + 2, self.length, self.height), 2)

            else:
                color = self.activate_color
                self.active_button = True

        return color

    def change_color(self, new_color):
        self.text_backing_color = new_color


    

    