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




point1=Point(100,100,5,RED)
point2=Point(400,900,10,RED)
point3=Point(600,300,10,RED)

points=[
    Point(100,100,5,RED),  # SCHRONISKO MORSKIE OKO
    Point(200,200,5,RED),  # MOLO MORSKIE OKO
    Point(400,300,5,RED),  #
    Point(400,400,5,RED),  #
    Point(600,900,5,RED)   #
]

