import pygame
import numpy as np
from colors import *
from config import *

class Icon:
    def __init__(self, points, shape, size, color):
        self.points = points
        self.shape = shape
        self.size = size
        self.color = color

    def draw_me(self):
        if self.shape == 'triangle':
            pygame.draw.polygon(WIN, self.color, [self.points[0], self.points[1], self.points[2]])