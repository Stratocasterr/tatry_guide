from ctypes.wintypes import POINT
import pygame
from colors import *
from config import *

class Point:
    def __init__(self,x,y,radius,color):
        self.x=x
        self.y=y
        self.radius=radius
        self.color=color
        
    
    
    def draw_me(self):
        
        pygame.draw.circle(WIN,self.color,(self.x,self.y),self.radius)




def add_point(offset_x, offset_y):
    points=[
        #Point(300+offset_x,100+offset_y,5,RED),  # SCHRONISKO MORSKIE OKO
        Point(548+offset_x,32+offset_y,5,RED),  # KASPROWY WIERCH 
        Point(570+offset_x,60+offset_y,5,RED),  # SUCHA PRZEŁĘCZ 
        Point(647+offset_x,115+offset_y,5,RED),  # BESKID
        Point(715+offset_x,200+offset_y,5,RED),  # LILIOWE
        Point(847+offset_x,284+offset_y,5,RED),  # SKRAJNA PRZEŁĘCZ
       
    ]
    return points
