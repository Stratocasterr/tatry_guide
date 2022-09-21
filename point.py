from ctypes.wintypes import POINT
import pygame
from colors import *
from config import *

class Point:
    def __init__(self,x,y,radius,color,name):
        self.x=x
        self.y=y
        self.radius=radius
        self.color=color
        self.name=name
        
    
    
    def draw_me(self):
        pygame.draw.circle(WIN,self.color,(self.x,self.y),self.radius)




def add_point(offset_x, offset_y):
    points=[
        Point(133+offset_x,18+offset_y,5,RED,'GORYCZKOWA CZUBA'),                                 # GORYCZKOWA CZUBA
        Point(215+offset_x,44+offset_y,5,RED,'GORYCZKOWA PRZEŁĘCZ ŚWIŃSKA'),                      # GORYCZKOWA PRZEŁĘCZ ŚWIŃSKA
        Point(280+offset_x,47+offset_y,5,RED,'POŚREDNI WIERCH GORYCZKOWY'),                       # POŚREDNI WIERCH GORYCZKOWY
        Point(341+offset_x,69+offset_y,5,RED,'GORYCZKOWA PRZEŁĘCZ NAD ZAKOSY'),                              # GORYCZKOWA PRZEŁĘCZ NAD ZAKOSY
        Point(548+offset_x,33+offset_y,5,RED,'KASPROWY WIERCH'),                                  # KASPROWY WIERCH 
        
        Point(570+offset_x,60+offset_y,5,RED,'SUCHA PRZEŁĘCZ'),                                   # SUCHA PRZEŁĘCZ 
        Point(647+offset_x,115+offset_y,5,RED,'BESKID'),                                          # BESKID
        Point(715+offset_x,200+offset_y,5,RED,'LILIOWE'),                                         # LILIOWE


        
        Point(728+offset_x,66+offset_y,5,GREEN,'SZ1a'),
        Point(723+offset_x,102+offset_y,5,GREEN,'SZ1b'),
        Point(718+offset_x,126+offset_y,5,GREEN,'SZ1c'),
        Point(730+offset_x,154+offset_y,5,GREEN,'SZ1d'),
        Point(731+offset_x,200+offset_y,5,GREEN,'SZ1e'),


        Point(1104+offset_x,354+offset_y,5,RED,'NIEBIESKA PRZEŁĘCZ'),                             # NIEBIESKA PRZEŁĘCZ
        Point(801+offset_x,89+offset_y,5,RED,'KOTLINOWY STAWEK'),                                 # KOTLINOWY STAWEK
        
       
        
        Point(932+offset_x,94+offset_y,5,RED,'KURTKOWIEC'),                                       # KURTKOWIEC
        Point(939+offset_x,146+offset_y,5,RED,'CZERWONE STAWKI'),                                 # CZERWONE STAWKI
        Point(982+offset_x,756+offset_y,5,RED,'ZAWORY'),                                          # ZAWORY
        Point(1101+offset_x,364+500+offset_y,5,RED,'KOBYLI STAWEK'),                              # KOBYLI STAWEK
        Point(1110+offset_x,555+500+offset_y,5,RED,'SCHRONISKO POD CIEMNYMI SMERCZYNAMI'),        # SCHRONISKO POD CIEMNYMI SMERCZYNAMI
        Point(955+offset_x,345+500+offset_y,5,RED,'CICHY WIERCH'),                                # CICHY WIERCH
        Point(796+offset_x,377+500+offset_y,5,RED,'ZADNIA GRAJOWA KOPA'),                         # ZADNIA GRAJOWA KOPA
        Point(1289+offset_x,657+500+offset_y,5,RED,'POŚREDNIA CZUBA'),                            # POŚREDNIA CZUBA
        Point(1359+offset_x,719+500+offset_y,5,RED,'NIŻNA PRZYBYLIŃSKA PRZEŁĘCZ'),                # NIŻNA PRZYBYLIŃSKA PRZEŁĘCZ
        Point(1494+offset_x,782+500+offset_y,5,RED,'NIŻNI'),                                      # NIŻNI
        Point(1546+offset_x,792+500+offset_y,5,RED,'WYŻNI'),                                      # WYŻNI

        Point(1685+offset_x,830+500+offset_y,5,RED,'KOPROWY WIERCH'),                             # KOPROWY WIERCH    
        Point(1672+offset_x,618+500+offset_y,5,RED,'CIEMNOSMRECZYŃSKA TURNIA'),                   # CIEMNOSMRECZYŃSKA TURNIA
        Point(1591+offset_x,540+500+offset_y,5,RED,'GŁAŹNE WROTKA'),                              # GŁAŹNE WROTKA
        Point(1549+offset_x,475+500+offset_y,5,RED,'WYŻNIE SZPIGLASOWE WROTKA'),                  # WYŻNIE SZPIGLASOWE WROTKA
        Point(1528+offset_x,250+500+offset_y,5,RED,'SZPIGLASOWE STAWKI'),                         # SZPIGLASOWE STAWKI
        
        
        
        Point(847+offset_x,282+offset_y,5,RED,'SKRAJNA PRZEŁĘCZ'),                                # SKRAJNA PRZEŁĘCZ
        Point(882+offset_x,283+offset_y,5,RED,'POŚREDNIA TURNIA'),                                # POŚREDNIA TURNIA
        Point(790+offset_x,245+offset_y,5,RED,'SKRAJNA TURNIA'),                                  # SKRAJNA TURNIA
        Point(822+offset_x,272+offset_y,5,RED,'SKRAJNA KOPA'),                                    # SKRAJNA KOPA
        Point(818+offset_x,116+offset_y,5,RED,'ZIELONY STAW'),                                    # ZIELONY STAW
        Point(931+offset_x,313+offset_y,5,RED,'ŚWINICKA PRZEŁĘCZ'),                               # ŚWINICKA PRZEŁĘCZ
        Point(814+offset_x,524+offset_y,5,RED,'VALENTYNKOVA KOPA'),                               # VALENTYNKOVA KOPA
        Point(975+offset_x,530+offset_y,5,RED,'WALENTYNKOWY WIERCH'),                             # WALENTYNKOWY WIERCH
        Point(1010+offset_x,440+offset_y,5,RED,'VALENTYNKOWY PRZEŁĘCZ'),                          # VALENTYNKOWY PRZEŁĘCZ
        Point(1023+offset_x,364+offset_y,5,RED,'ŚWINICA'),                                        # ŚWINICA
        Point(1040+offset_x,221+offset_y,5,RED,'ZADNI STAW GĄSIENNICOWY'),                        # ZADNI STAW GĄSIENNICOWY
        Point(1012+offset_x,135+offset_y,5,RED,'DŁUGI STAW'),                                     # DŁUGI STAW
        Point(1110+offset_x,208+offset_y,5,RED,'KOŚCIELEC'),                                      # KOŚCIELEC
        Point(1118+offset_x,246+offset_y,5,RED,'ZADNI KOŚCIELEC'),                                # ZADNI KOŚCIELEC
        Point(1122+offset_x,345+offset_y,5,RED,'ZAWRATOWA TURNIA'),                               # ZAWRATOWA TURNIA
        Point(1128+offset_x,282+offset_y,5,RED,'MYLNA PRZEŁĘCZ'),                                 # MYLNA PRZEŁĘCZ
        Point(1150+offset_x,359+offset_y,5,RED,'ZAWRAT'),                                         # ZAWRAT
        Point(1197+offset_x,367+offset_y,5,RED,'MAŁY KOZI WIERCH'),                               # MAŁY KOZI WIERCH
        Point(1257+offset_x,350+offset_y,5,RED,'ZMARZŁA PRZEŁĘCZ'),                               # ZMARZŁA PRZEŁĘCZ
        Point(1276+offset_x,350+offset_y,5,RED,'ZMARZŁA TURNIA'),                                 # ZMARZŁA TURNIA
        Point(1292+offset_x,352+offset_y,5,RED,'KOZIA PRZEŁĘCZ'),                                 # KOZIA PRZEŁĘCZ
        Point(1353+offset_x,393+offset_y,5,RED,'KOZI WIERCH'),                                    # KOZI WIERCH
        Point(1439+offset_x,327+offset_y,5,RED,'PRZEŁĘCZ NAD BUCZYNOWĄ DOLINĄ'),                  # PRZEŁĘCZ NAD BUCZYNOWĄ DOLINĄ
        Point(1430+offset_x,276+offset_y,5,RED,'ZADNIA SIECZKOWA PRZEŁĘCZ'),                      # ZADNIA SIECZKOWA PRZEŁĘCZ
        Point(1415+offset_x,221+offset_y,5,RED,'ZADNI GRANAT'),                                   # ZADNI GRANAT
        Point(1421+offset_x,189+offset_y,5,RED,'POŚREDNI GRANAT'),                                # POŚREDNI GRANAT
        Point(1434+offset_x,156+offset_y,5,RED,'SKRAJNY GRANAT'),                                 # SKRAJNY GRANAT
        Point(1238+offset_x,244+offset_y,5,RED,'ZMARZŁY STAW'),                                   # ZMARZŁY STAW
        Point(1163+offset_x,108+offset_y,5,RED,'CZARNY STAW GĄSIENNICOWY'),                       # CZARNY STAW GĄSIENNICOWY
        
        
        
        Point(1209+offset_x,472+offset_y,5,RED,'KOŁOWA CZUBA'),                                   # KOŁOWA CZUBA
        Point(1084+offset_x,568+offset_y,5,RED,'ZADNI STAW POLSKI'),                              # ZADNI STAW POLSKI
        Point(1117+offset_x,607+offset_y,5,RED,'WOLE OKO'),                                       # WOLE OKO
        Point(1339+offset_x,601+offset_y,5,RED,'S.BRONIKOWSKIEGO'),                               # S.BRONIKOWSKIEGO
        Point(1080+offset_x,656+offset_y,5,RED,'GŁADKA PRZEŁĘCZ'),                                # GŁADKA PRZEŁĘCZ
        Point(1090+offset_x,690+offset_y,5,RED,'GŁADKI WIERCH'),                                  # GŁADKI WIERCH
        Point(1174+offset_x,787+offset_y,5,RED,'GŁADKA ŁAWKA'),                                   # GŁADKA ŁAWKA
        Point(1359+offset_x,872+offset_y,5,RED,'CZARNA ŁAWKA'),                                   # CZARNA ŁAWKA
        Point(1411+offset_x,870+offset_y,5,RED,'NIŻNI LIPTOWSKI KOSTUR'),                         # NIŻNI LIPTOWSKI KOSTUR
        Point(1465+offset_x,915+offset_y,5,RED,'WYŻNI LIPTOWSKI KOSTUR'),                         # WYŻNI LIPTOWSKI KOSTUR
        Point(1584+offset_x,750+168+offset_y,5,RED,'SZPIGLASOWA PRZEŁĘCZ'),                       # SZPIGLASOWA PRZEŁĘCZ
        Point(1539+offset_x,750+197+offset_y,5,RED,'SZPIGLASOWY WIERCH'),                         # SZPIGLASOWY WIERCH
        Point(1629+offset_x,750+335+offset_y,5,RED,'WROTA CHAŁUBIŃSKIEGO'),                       # WROTA CHAŁUBIŃSKIEGO
        Point(1362+offset_x,740+offset_y,5,RED,'CZARNY STAW POLSKI'),                             # CZARNY STAW POLSKI
        Point(1579+offset_x,664+offset_y,5,RED,'WIELKI STAW POLSKI'),                             # WIELKI STAW POLSKI
        Point(1682+offset_x,592+offset_y,5,RED,'PRZEDNI STAW POLSKI'),                            # PRZEDNI STAW POLSKI
        Point(1609+offset_x,494+offset_y,5,RED,'SIKLAWA'),                                        # SIKLAWA
        Point(1635+offset_x,563+offset_y,5,RED,'MAŁY STAW'),                                      # MAŁY STAW
        Point(1687+offset_x,506+offset_y,5,RED,'SCHRONISKO W DOLINIE PIĘCIU STAWÓW POLSKICH'),    # SCHRONISKO W DOLINIE PIĘCIU STAWÓW POLSKICH
        Point(1593+100+offset_x,679+offset_y,5,RED,'NIEDŹWIEDŹ'),                                 # NIEDŹWIEDŹ
        Point(1494+200+offset_x,830+offset_y,5,RED,'MIEDZIANE'),                                  # MIEDZIANE
        Point(1627+200+offset_x,708+offset_y,5,RED,'MARCHWICZNA PRZEŁĘCZ'),                       # MARCHWICZNA PRZEŁĘCZ
        Point(1673+200+offset_x,656+offset_y,5,RED,'OPALONY WIERCH'),                             # OPALONY WIERCH
        Point(1091+600+offset_x,542+600+offset_y,5,RED,'CIEMNOSMRECZYŃSKA TURNIA'),               # CIEMNOSMRECZYŃSKA TURNIA
        Point(1149+600+offset_x,510+600+offset_y,5,RED,'MNICHOWA KOPA'),                          # MNICHOWA KOPA
        Point(1176+600+offset_x,583+600+offset_y,5,RED,'CUBRYNA'),                                # CUBRYNA
        Point(1191+600+offset_x,586+600+offset_y,5,RED,'HIŃCZOWA PRZEŁĘCZ'),                      # HIŃCZOWA PRZEŁĘCZ
        Point(1283+600+offset_x,609+600+offset_y,5,RED,'MIĘGUSZOWIECKI SZCZYT'),                  # MIĘGUSZOWIECKI SZCZYT
        Point(1377+600+offset_x,699+600+offset_y,5,RED,'MIĘGUSZOWIECKA PRZEŁĘCZ POD CHŁOPKIEM'),  # MIĘGUSZOWIECKA PRZEŁĘCZ POD CHŁOPKIEM
        Point(1463+600+offset_x,679+600+offset_y,5,RED,'KAZALNICA'),                              # KAZALNICA
        Point(1509+600+offset_x,557+600+offset_y,5,RED,'CZARNY STAW POD RYSAMI'),                 # CZARNY STAW POD RYSAMI
        Point(1492+600+offset_x,480+600+offset_y,5,RED,'CZARNOSTAWIAŃSKA SIKLAWA'),               # CZARNOSTAWIAŃSKA SIKLAWA
        Point(1486+600+offset_x,237+600+offset_y,5,RED,'MORSKIE OKO'),                            # MORSKIE OKO
        Point(1367+600+offset_x,379+600+offset_y,5,RED,'DWOISTA SIKLAWA'),                        # DWOISTA SIKLAWA
        Point(1197+600+offset_x,311+600+offset_y,5,RED,'MNICHOWY POTOK'),                         # MNICHOWY POTOK
        Point(1192+600+offset_x,466+600+offset_y,5,RED,'MNICH'),                                  # MNICH
        Point(1050+600+offset_x,395+600+offset_y,5,RED,'STAWEK NA KOPKACH'),                      # STAWEK NA KOPKACH
        Point(1050+600+offset_x,395+600+offset_y,5,RED,'WYŻYNIE MNICHOWE STAWKI'),                # WYŻYNIE MNICHOWE STAWKI
        Point(1502+600+offset_x,177+600+offset_y,5,RED,'RYBIE STAWKI'),                           # RYBIE STAWKI
        Point(1539+600+offset_x,12+600+offset_y,5,RED,'WRZĄCE ŹRÓDŁO'),                           # WRZĄCE ŹRÓDŁO
        Point(1483+600+offset_x,181+600+offset_y,5,RED,'ŻABIE OKO'),                              # ŻABIE OKO
        Point(1321+600+offset_x,669+600+offset_y,5,RED,'POŚREDNI MIĘGUSZOWIECKI SZCZYT'),         # POŚREDNI MIĘGUSZOWIECKI SZCZYT
        Point(1410+600+offset_x,719+600+offset_y,5,RED,'MIĘGUSZOWIECKI SZCZYT'),                  # MIĘGUSZOWIECKI SZCZYT
        Point(1462+600+offset_x,793+600+offset_y,5,RED,'HIŃCZOWA TURNIA'),                        # HIŃCZOWA TURNIA
        Point(1528+600+offset_x,809+600+offset_y,5,RED,'WOŁOWA TURNIA'),                          # WOŁOWA TURNIA
        Point(1580+600+offset_x,829+600+offset_y,5,RED,'ŻABIA TURNIA'),                           # ŻABIA TURNIA
        Point(1658+600+offset_x,815+600+offset_y,5,RED,'ŻABIA PRZEŁĘCZ'),                         # ŻABIA PRZEŁĘCZ
        Point(1553+700+offset_x,746+600+offset_y,5,RED,'BULA POD RYSAMI'),                        # BULA POD RYSAMI
        Point(1665+700+offset_x,803+600+offset_y,5,RED,'RYSY'),                                   # RYSY
        Point(1670+700+offset_x,762+600+offset_y,5,RED,'PRZEŁĘCZ POD RYSAMI'),                    # PRZEŁĘCZ POD RYSAMI
        Point(1665+700+offset_x,699+600+offset_y,5,RED,'NIŻNIE RYSY'),                            # NIŻNIE RYSY
        Point(1651+700+offset_x,652+600+offset_y,5,RED,'SPADOWA KOPA'),                           # SPADOWA KOPA
        Point(1660+700+offset_x,629+600+offset_y,5,RED,'CIĘŻKA PRZEŁĄCZKA'),                      # CIĘŻKA PRZEŁĄCZKA
        Point(1684+700+offset_x,586+600+offset_y,5,RED,'WYŻNI ŻABI SZCZYT'),                      # WYŻNI ŻABI SZCZYT
        Point(1637+700+offset_x,550+600+offset_y,5,RED,'ŻABI MNICH'),                             # ŻABI MNICH
        Point(1619+700+offset_x,483+600+offset_y,5,RED,'BIAŁCZAŃSKA PRZEŁĘCZ'),                   # BIAŁCZAŃSKA PRZEŁĘCZ
        Point(1608+700+offset_x,413+600+offset_y,5,RED,'OWCZA PRZEŁĘCZ'),                         # OWCZA PRZEŁĘCZ
        Point(1615+700+offset_x,378+600+offset_y,5,RED,'NIŻNI ŻABI SZCZYT'),                      # NIŻNI ŻABI SZCZYT
        Point(1644+700+offset_x,309+600+offset_y,5,RED,'ŻABIA CZUBA'),                            # ŻABIA CZUBA
        Point(1360+700+offset_x,439+600+offset_y,5,RED,'DROGA CZERWONEGO SZLAKU OKA'),            # DROGA CZERWONEGO SZLAKU Z MORSKIEGO OKA
        Point(1645+700+offset_x,836+700+offset_y,5,RED,'CHATA POD RYSAMI'),                       # CHATA POD RYSAMI
        Point(883+500+offset_x,66+offset_y,5,RED,'ŻÓŁTA PRZEŁĘCZ'),                               # ŻÓŁTA PRZEŁĘCZ
        Point(911+500+offset_x,105+offset_y,5,RED,'WIERCH POD FAJKI'),                            # WIERCH POD FAJKI
        Point(918+500+offset_x,111+offset_y,5,RED,'PAŃSZCZYŃSKA PRZEŁĘCZ'),                       # PAŃSZCZYŃSKA PRZEŁĘCZ
        
        
        Point(958+500+offset_x,155+offset_y,5,RED,'GRANACKA PRZEŁĘCZ'),                              # SKRAJNY GRANAT
        Point(1022+500+offset_x,152+offset_y,5,RED,'KOŁOWA CZUBA'),                               # KOŁOWA CZUBA
        Point(1054+500+offset_x,149+offset_y,5,RED,'WIELKA BUCZYNOWA TURNIA'),                    # WIELKA BUCZYNOWA TURNIA
        Point(1100+500+offset_x,146+offset_y,5,RED,'MAŁA BUCZYNOWA'),                             # MAŁA BUCZYNOWA
        Point(1169+500+offset_x,109+offset_y,5,RED,'KRZYŻNE'),                                    # KRZYŻNE
        Point(1218+500+offset_x,117+offset_y,5,RED,'WIELKI WOŁOSZYN'),                            # WIELKI WOŁOSZYN
        Point(1265+500+offset_x,91+offset_y,5,RED,'WYŻYNA WOŁOSZYŃSKA'),                          # WYŻYNA WOŁOSZYŃSKA
        Point(1302+500+offset_x,70+offset_y,5,RED,'POŚREDNI WOŁOSZYN'),                           # POŚREDNI WOŁOSZYN
        Point(1369+500+offset_x,10+offset_y,5,RED,'NIŻNIA WOŁOSZYŃSKA PRZEŁĘCZ'),                 # NIŻNIA WOŁOSZYŃSKA PRZEŁĘCZ
        Point(1170+500+offset_x,30+offset_y,5,RED,'WAKSMUDZKI WIERCH'),                           # WAKSMUDZKI WIERCH
        Point(1189+500+offset_x,321+offset_y,5,RED,'BUCZYNOWA SIKLAWA'),                          # BUCZYNOWA SIKLAWA
        Point(1098+500+offset_x,322+offset_y,5,RED,'BUCZYNOWY STAWEK'),                           # BUCZYNOWY STAWEK
        Point(1340+500+offset_x,436+offset_y,5,RED,'ŚWISTOWA CZUBA'),                             # ŚWISTOWA CZUBA 
        Point(1548+500+offset_x,485+offset_y,5,RED,'KĘPA'),                                       # KĘPA
        Point(1663+500+offset_x,11+offset_y,5,RED,'TURNIA NAD SZCZOTAMI'),                        # TURNIA NAD SZCZOTAMI
        Point(1159+1000+offset_x,547+offset_y,5,RED,'POLE NAMIOTOWE PZA'),                        # POLE NAMIOTOWE PZA
        Point(1227+1000+offset_x,518+offset_y,5,RED,'WŁOSIENICA'),                                # WŁOSIENICA
        Point(1166+1000+offset_x,474+offset_y,5,RED,'LAS POD DZIADUŁĄ'),                          # LAS POD DZIADUŁĄ
        Point(1478+1000+offset_x,311+offset_y,5,RED,'LEŚNICZÓWKA MORSKIE OKO'),                   # LEŚNICZÓWKA MORSKIE OKO
        Point(1414+1000+offset_x,125+offset_y,5,RED,'ROZTOCKA CZUBA'),                            # ROZTOCKA CZUBA
        Point(1577+1000+offset_x,884+offset_y,5,RED,'MAŁY MŁYNAR'),                               # MAŁY MŁYNAR
        Point(1674+1000+offset_x,857+offset_y,5,RED,'JARZĄBKOWSKA TURNIA'),                       # JARZĄBKOWSKA TURNIA
        Point(1490+1000+offset_x,556+300+offset_y,5,RED,'NIŻNI ŻABI STAW BIAŁCZAŃSKI'),           # NIŻNI ŻABI STAW BIAŁCZAŃSKI
        Point(1475+1000+offset_x,672+300+offset_y,5,RED,'WYŻNI ŻABI STAW BIAŁCZAŃSKI'),           # WYŻNI ŻABI STAW BIAŁCZAŃSKI
        Point(1541+1000+offset_x,853+300+offset_y,5,RED,'MŁYNARŻOWA PRZEŁĘCZ'),                   # MŁYNARŻOWA PRZEŁĘCZ
        Point(1626+1000+offset_x,354+700+offset_y,5,RED,'MŁYNARZ'),                               # MŁYNARZ
        Point(1602+1000+offset_x,462+700+offset_y,5,RED,'MŁYNAROWA WIDŁA'),                       # MŁYNAROWA WIDŁA
        Point(1464+1000+offset_x,597+700+offset_y,5,RED,'CIĘŻKA TURNIA'),                         # CIĘŻKA TURNIA
        Point(1468+1000+offset_x,886+700+offset_y,5,RED,'WYSOKA'),                                # WYSOKA
        Point(1560+1000+offset_x,850+700+offset_y,5,RED,'RUMANOWA PRZEŁĘCZ'),                     # RUMANOWA PRZEŁĘCZ
        Point(1644+1000+offset_x,853+700+offset_y,5,RED,'GANEK'),                                 # GANEK
        Point(1652+1000+offset_x,753+700+offset_y,5,RED,'KACZA TURNIA'),                          # KACZA TURNIA
        Point(1622+1000+offset_x,665+700+offset_y,5,RED,'SKRAJNA PUSTA TURNIA'),                  # SKRAJNA PUSTA TURNIA
        Point(1635+1000+offset_x,843+700+offset_y,5,RED,'MAŁY GANEK'),                            # MAŁY GANEK
        Point(1434+1000+offset_x,867+700+offset_y,5,RED,'CIĘŻKI SZCZYT'),                         # CIĘŻKI SZCZYT
        Point(1405+1000+offset_x,799+700+offset_y,5,RED,'WAGA'),                                  # WAGA

        #SZLAK ZIELONY NA WSCHOD OD KASPROWEGO
        

        #SZLAK CZARNY NA WSCHOD OD KASPROWEGO
        Point(829+offset_x,70+offset_y,5,BLACK,'SCZ1a'),
        Point(863+offset_x,84+offset_y,5,BLACK,'SCZ1b'),
        Point(886+offset_x,115+offset_y,5,BLACK,'SCZ1c'),
        Point(909+offset_x,137+offset_y,5,BLACK,'SCZ1d'),
        Point(923+offset_x,159+offset_y,5,BLACK,'SCZ1e'),
        Point(942+offset_x,180+offset_y,5,BLACK,'SCZ1f'),
        Point(956+offset_x,236+offset_y,5,BLACK,'SCZ1g'),
        Point(921+offset_x,270+offset_y,5,BLACK,'SCZ1h'),
        
        #SZLAK NIEBIESKI NA WSCHOD OD KASPROWEGO

        Point(936+offset_x,124+offset_y,5,BLUE,'SNB1a'),
        Point(981+offset_x,108+offset_y,5,BLUE,'SNB1b'),
        Point(1008+offset_x,117+offset_y,5,BLUE,'SNB1c'),
        Point(1062+offset_x,108+offset_y,5,BLUE,'SNB1d'),
        
        #SZLAK CZARNY NA WSCHOD OD KASPROWEGO, DOJSCIE DO KOŚCIELCA I CZARNEGO STAWU
        
        Point(1089+offset_x,182+offset_y,5,BLACK,'SCZ2a'),
        Point(1078+offset_x,133+offset_y,5,BLACK,'SCZ2b'),
        Point(1048+offset_x,63+offset_y,5,BLACK,'SCZ2c'),
        Point(1073+offset_x,40+offset_y,5,BLACK,'SCZ2d'),
        Point(1107+offset_x,9+offset_y,5,BLACK,'SCZ2e'),
        
        #SZLAK NIEBIESKI PRZY CZARNYM STAWIE GĄSIENNICOWYM
        Point(1155+offset_x,5+offset_y,5,BLUE,'SNB1a'),
        Point(1192+offset_x,3+offset_y,5,BLUE,'SNB1b'),
        Point(1214+offset_x,65+offset_y,5,BLUE,'SNB1c'),
        Point(1257+offset_x,129+offset_y,5,BLUE,'SNB1d'),
        Point(1248+offset_x,195+offset_y,5,BLUE,'SNB1e'),
        Point(1220+offset_x,236+offset_y,5,BLUE,'SNB1f'),
        Point(1196+offset_x,273+offset_y,5,BLUE,'SNB1g'),
        Point(1164+offset_x,333+offset_y,5,BLUE,'SNB1h'),

        #SZLAK ZIELONY NA PÓŁNOC OD KOZIEGO WIERCHU

        Point(1281+offset_x,249+offset_y,5,GREEN,'SZ2a'),
        Point(1329+offset_x,287+offset_y,5,GREEN,'SZ2b'),
        Point(1364+offset_x,255+offset_y,5,GREEN,'SZ2c'),
        Point(1390+offset_x,217+offset_y,5,GREEN,'SZ2d'),

        # SZLAK CZARNY KOZIA DOLINKA
        Point(1359+offset_x,303+offset_y,5,BLACK,'SCZ3a'),
        Point(1416+offset_x,320+offset_y,5,BLACK,'SCZ3b'),

        #SZLAK ŻÓŁTY PRZY PAŃSZCZYŃSKIEJ PRZEŁĘCZY

        Point(1247+offset_x,60+offset_y,5,ORANGE,'SZO1a'),
        Point(1314+offset_x,98+offset_y,5,ORANGE,'SZO1b'),
        Point(1354+offset_x,111+offset_y,5,ORANGE,'SZO1c'),
        Point(1373+offset_x,137+offset_y,5,ORANGE,'SZO1d'),
        Point(1413+offset_x,144+offset_y,5,ORANGE,'SZO1e'),

        #SZLAK ŻÓŁTY PRZY ZMARZŁEJ PRZEŁĘCZY

        Point(1291+offset_x,322+offset_y,5,ORANGE,'SZO2a'),
        Point(1278+offset_x,272+offset_y,5,ORANGE,'SZO2b'),
        Point(1250+offset_x,204+offset_y,5,ORANGE,'SZO2c'),
        

    ]
    return points




def get_points_names(points):
    answer = []
    
    name = ''
    for point in points:
        if not (any(char.isdigit() for char in point.name)):
           
            for letter in point.name:
                if letter == "Ż": name += 'z'
                elif letter == "Ń": name += 'n'
                elif letter == "Ó": name += 'o'
                elif letter == "Ś": name += 's'
                elif letter == "Ć": name += 'c'
                elif letter == "Ą": name += 'a'
                elif letter == "Ę": name += 'e'
                elif letter == "Ł": name += 'l'
                elif letter == "Ź": name += 'z'
                else : name += letter
            name = name.lower()
            
            answer.append(name)
            name = ''
    return answer

def find_point(point_name, points):
    for point in points:
        if point.name == point_name:
            return [point.x, point.y]

# input for line to draw points = [(x1, y1), (x2, y2), ..., (xn, yn)]
def draw_the_line(points):
    for i in range(len(points)):
        if i < len(points) - 2:
            pygame.draw.line(WIN, RED, points[i], points[i+1], 8)


def find_name(points_names, input_name):
    suggestions = []
    if len(input_name) > 0:
        for point in points_names:
            if point[:len(input_name)] == input_name: suggestions.append(point)
    return suggestions


