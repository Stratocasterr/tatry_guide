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
        Point(647+offset_x,115+offset_y,5,RED),   # BESKID
        Point(715+offset_x,200+offset_y,5,RED),   # LILIOWE
        Point(847+offset_x,282+offset_y,5,RED),   # SKRAJNA PRZEŁĘCZ
        Point(882+offset_x,283+offset_y,5,RED),   # POŚREDNIA TURNIA
        Point(790+offset_x,245+offset_y,5,RED),   # SKRAJNA TURNIA
        Point(822+offset_x,272+offset_y,5,RED),   # SKRAJNA KOPA
        Point(818+offset_x,116+offset_y,5,RED),   # ZIELONY STAW
        Point(931+offset_x,313+offset_y,5,RED),   # ŚWINICKA PRZEŁĘCZ
        Point(814+offset_x,524+offset_y,5,RED),   # VALENTYNKOVA KOPA
        Point(975+offset_x,530+offset_y,5,RED),   # WALENTYNKOWY WIERCH
        Point(1010+offset_x,440+offset_y,5,RED),  # VALENTYNKOWY PRZEŁĘCZ
        Point(1023+offset_x,364+offset_y,5,RED),  # ŚWINICA
        Point(1040+offset_x,221+offset_y,5,RED),  # ZADNI STAW GĄSIENNICOWY
        Point(1012+offset_x,135+offset_y,5,RED),  # DŁUGI STAW
        Point(1110+offset_x,208+offset_y,5,RED),  # KOŚCIELEC
        Point(1118+offset_x,246+offset_y,5,RED),  # ZADNI KOŚCIELEC
        Point(1122+offset_x,345+offset_y,5,RED),  # ZAWRATOWA TURNIA
        Point(1128+offset_x,282+offset_y,5,RED),  # MYLNA PRZEŁĘCZ
        Point(1150+offset_x,359+offset_y,5,RED),  # ZAWRAT
        Point(1197+offset_x,367+offset_y,5,RED),  # MAŁY KOZI WIERCH
        Point(1257+offset_x,350+offset_y,5,RED),  # ZMARZŁA PRZEŁĘCZ
        Point(1276+offset_x,350+offset_y,5,RED),  # ZMARZŁA TURNIA
        Point(1292+offset_x,352+offset_y,5,RED),  # KOZIA PRZEŁĘCZ
        Point(1353+offset_x,393+offset_y,5,RED),  # KOZI WIERCH
        Point(1439+offset_x,327+offset_y,5,RED),  # PRZEŁĘCZ NAD BUCZYNOWĄ DOLINĄ
        Point(1430+offset_x,276+offset_y,5,RED),  # ZADNIA SIECZKOWA PRZEŁĘCZ
        Point(1415+offset_x,221+offset_y,5,RED),  # ZADNI GRANAT
        Point(1421+offset_x,189+offset_y,5,RED),  # POŚREDNI GRANAT
        Point(1434+offset_x,156+offset_y,5,RED),  # SKRAJNY GRANAT
        Point(1238+offset_x,244+offset_y,5,RED),  # ZMARZŁY STAW
        Point(1163+offset_x,108+offset_y,5,RED),  # CZARNY STAW GĄSIENNICOWY
        Point(1209+offset_x,472+offset_y,5,RED),  # KOŁOWA CZUBA
        Point(1084+offset_x,568+offset_y,5,RED),  # ZADNI STAW POLSKI
        Point(1117+offset_x,607+offset_y,5,RED),  # WOLE OKO
        Point(1339+offset_x,601+offset_y,5,RED),  # S.BRONIKOWSKIEGO
        Point(1080+offset_x,656+offset_y,5,RED),  # GŁADKA PRZEŁĘCZ
        Point(1090+offset_x,690+offset_y,5,RED),  # GŁADKI WIERCH
        Point(1174+offset_x,787+offset_y,5,RED),  # GŁADKA ŁAWKA

        Point(1359+offset_x,872+offset_y,5,RED),        # CZARNA ŁAWKA
        Point(1411+offset_x,870+offset_y,5,RED),        # NIŻNI LIPTOWSKI KOSTUR
        Point(1465+offset_x,915+offset_y,5,RED),        # WYŻNI LIPTOWSKI KOSTUR
        Point(1584+offset_x,850+168+offset_y,5,RED),    # SZPIGLASOWA PRZEŁĘCZ
        Point(1539+offset_x,850+197+offset_y,5,RED),    # SZPIGLASOWY WIERCH
        Point(1629+offset_x,335+850+offset_y,5,RED),        # WROTA CHAŁUBIŃSKIEGO
        Point(1362+offset_x,740+offset_y,5,RED),        # CZARNY STAW POLSKI

        Point(1579+offset_x,664+offset_y,5,RED),  # WIELKI STAW POLSKI
        Point(1682+offset_x,592+offset_y,5,RED),  # PRZEDNI STAW POLSKI
        Point(1609+offset_x,494+offset_y,5,RED),  # SIKLAWA
        Point(1635+offset_x,563+offset_y,5,RED),  # MAŁY STAW

        Point(1687+offset_x,506+offset_y,5,RED),  # SCHRONISKO W DOLINIE PIĘCIU STAWÓW POLSKICH
        Point(1400+offset_x,366+offset_y,5,RED),  # NIEDŹWIEDŹ
        Point(1400+offset_x,366+offset_y,5,RED),  # MIEDZIANE
        Point(1400+offset_x,366+offset_y,5,RED),  # MARCHWICZNA PRZEŁĘCZ
        Point(1400+offset_x,366+offset_y,5,RED),  # OPALONY WIERCH

        Point(1400+offset_x,366+offset_y,5,RED),  # ŚWISTOWA CZUBA
        Point(1400+offset_x,366+offset_y,5,RED),  # BUCZYNOWA SIKLAWA
        Point(1400+offset_x,366+offset_y,5,RED),  # BUCZYNOWY STAWEK




    ]
    return points
