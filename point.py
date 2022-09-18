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
        Point(548+offset_x,33+offset_y,5,RED),  # KASPROWY WIERCH 
        Point(570+offset_x,60+offset_y,5,RED),  # SUCHA PRZEŁĘCZ 
        Point(647+offset_x,115+offset_y,5,RED),  # BESKID
        Point(715+offset_x,200+offset_y,5,RED),  # LILIOWE
        Point(847+offset_x,282+offset_y,5,RED),  # SKRAJNA PRZEŁĘCZ
        Point(882+offset_x,283+offset_y,5,RED),  # POŚREDNIA TURNIA
        Point(790+offset_x,245+offset_y,5,RED),  # SKRAJNA TURNIA
        Point(822+offset_x,272+offset_y,5,RED),  # SKRAJNA KOPA
        Point(818+offset_x,116+offset_y,5,RED),  # ZIELONY STAW
        Point(931+offset_x,313+offset_y,5,RED),  # ŚWINICKA PRZEŁĘCZ
        Point(814+offset_x,524+offset_y,5,RED),  # VALENTYNKOVA KOPA
        Point(975+offset_x,530+offset_y,5,RED),  # WALENTYNKOWY WIERCH
        Point(1010+offset_x,440+offset_y,5,RED),  # VALENTYNKOWY PRZEŁĘCZ
        Point(1023+offset_x,364+offset_y,5,RED),  # ŚWINICA
        Point(1040+offset_x,221+offset_y,5,RED),  # ZADNI STAW GĄSIENNICOWY
        Point(1012+offset_x,135+offset_y,5,RED),  # DŁUGI STAW
        Point(1110+offset_x,208+offset_y,5,RED),  # KOŚCIELEC
        Point(1118+offset_x,246+offset_y,5,RED),  # ZADNI KOŚCIELEC
        Point(1122+offset_x,345+offset_y,5,RED),  # ZAWRATOWA TURNIA
        Point(1128+offset_x,282+offset_y,5,RED),  # MYLNA PRZEŁĘCZ
        Point(1150+offset_x,359+offset_y,5,RED),  # ZAWRAT




    ]
    return points
