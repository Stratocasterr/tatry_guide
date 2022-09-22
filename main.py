from button import *
import pygame
from config import *
from point import *
from navigation_window import *
from basic_functions import *

from turtle import window_height
import numpy as np
import sys

sys.path.append("C:/Users/kacpe/Visual Studio Projects/tatry_guide/Dijkstra's algorithm")
import algorithm

from graph_map import map_graph as mp_graph

CLOCK = pygame.time.Clock()

class GameView():
    def __init__(self):
        self.game_is_running = True
        
        self.map_x = 0
        self.map_y = 0
        self.append_tools = True

        # windows 
        self.buttons = []
        self.actual_window = 'sidebar'
        self.keyboard_input = ''

        # points
        self.points = []
        self.points_names = []
        self.points_namesPL = []
        self.suggesting = False
       
    def generate_tools(self):
        if self.append_tools:
            self.buttons = Window(self.actual_window).add_buttons()
            self.points_names = get_points_names(self.points)
            
            print(algorithm.the_shortest_path('GORYCZKOWA CZUBA','GORYCZKOWA PRZEŁĘCZ NAD ZAKOSY',mp_graph))

        self.append_tools = False


    def game_loop(self):

        while self.game_is_running:
            self.game_draw()
            self.handle_events()
            self.sterowanie()
            self.points = add_point(self.map_x, self.map_y)
            self.generate_tools()

            # print(find_name(self.points_names, self.keyboard_input))
           

    def game_draw(self):
        # draw map
       
        WIN.blit(LT_MAP,(self.map_x,self.map_y))
        WIN.blit(LB_MAP,(self.map_x,self.map_y+LT_MAP_SIZE[1]))
        WIN.blit(RT_MAP,(self.map_x+LT_MAP_SIZE[0],self.map_y))
        WIN.blit(RB_MAP,(self.map_x+LT_MAP_SIZE[0],self.map_y+RT_MAP_SIZE[1]))
       
        

        # draw points

        for point in self.points:
            
            point.draw_me()

        # draw actual window
        
        Window(self.actual_window).draw_me()

        # draw actual window's buttons
        
        for button in self.buttons:
           
            if button[0].active_button:
                
                if button[1] == 'show_side_menu_button':
                    self.actual_window = 'side menu'
                    self.append_tools = True

                elif button[1] == 'hide_side_menu_button':
                    self.actual_window = 'sidebar'
                    self.append_tools = True

                elif button[1] == 'search_button':
                    button[0].allow = True
                    
            
            if button[0].allow:
                button[0].text = self.keyboard_input
            

                   
                
            if len(button) == 2: button[0].draw_the_button()
            else:  
                button[0].draw_the_button()
                button[2].draw_me()

        
        pygame.display.update()


    def handle_events(self):
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                self.game_is_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
                print(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_0:
                    self.keyboard_input += "0"
                elif event.key == pygame.K_1:
                    self.keyboard_input += "1"
                elif event.key == pygame.K_2:
                    self.keyboard_input += "2"
                elif event.key == pygame.K_3:
                    self.keyboard_input += "3"
                elif event.key == pygame.K_4:
                    self.keyboard_input += "4"
                elif event.key == pygame.K_5:
                    self.keyboard_input += "5"
                elif event.key == pygame.K_6:
                    self.keyboard_input += "6"
                elif event.key == pygame.K_7:
                    self.keyboard_input += "7"
                elif event.key == pygame.K_8:
                    self.keyboard_input += "8"
                elif event.key == pygame.K_9:
                    self.keyboard_input += "9"

                elif event.key == pygame.K_a:
                    self.keyboard_input += "a"
                elif event.key == pygame.K_b:
                    self.keyboard_input += "b"
                elif event.key == pygame.K_c:
                    self.keyboard_input += "c"
                elif event.key == pygame.K_d:
                    self.keyboard_input += "d"
                elif event.key == pygame.K_e:
                    self.keyboard_input += "e"
                elif event.key == pygame.K_f:
                    self.keyboard_input += "f"
                elif event.key == pygame.K_g:
                    self.keyboard_input += "g"
                elif event.key == pygame.K_h:
                    self.keyboard_input += "h"
                elif event.key == pygame.K_i:
                    self.keyboard_input += "i"
                elif event.key == pygame.K_j:
                    self.keyboard_input += "j"
                elif event.key == pygame.K_k:
                    self.keyboard_input += "k"
                elif event.key == pygame.K_l:
                    self.keyboard_input += "l"
                elif event.key == pygame.K_m:
                    self.keyboard_input += "m"
                elif event.key == pygame.K_n:
                    self.keyboard_input += "n"
                elif event.key == pygame.K_o:
                    self.keyboard_input += "o"
                elif event.key == pygame.K_u:
                    self.keyboard_input += "u"
                elif event.key == pygame.K_u:
                    self.keyboard_input += "u"
                elif event.key == pygame.K_p:
                    self.keyboard_input += "p"
                elif event.key == pygame.K_r:
                    self.keyboard_input += "r"
                elif event.key == pygame.K_s:
                    self.keyboard_input += "s"
                elif event.key == pygame.K_t:
                    self.keyboard_input += "t"
                elif event.key == pygame.K_w:
                    self.keyboard_input += "w"
                elif event.key == pygame.K_z:
                    self.keyboard_input += "z"
                elif event.key == pygame.K_x:
                    self.keyboard_input += "x"
                elif event.key == pygame.K_y:
                    self.keyboard_input += "y"
                elif event.key == pygame.K_q:
                    self.keyboard_input += "q"

                elif event.key == pygame.K_SPACE:
                    self.keyboard_input += " "

                elif event.key == pygame.K_BACKSPACE:
                    self.keyboard_input = self.keyboard_input[:-1]

    def sterowanie(self):
        
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT]:
            if self.map_x<0: self.map_x+=1

        if pressed_keys[pygame.K_RIGHT]:
            if self.map_x>(-LT_MAP_SIZE[0]-RT_MAP_SIZE[0]+SCREEN_LENGTH): self.map_x-=1


        if pressed_keys[pygame.K_UP]:
            if self.map_y<0: self.map_y+=1

        if pressed_keys[pygame.K_DOWN]:
            if self.map_y>(-LT_MAP_SIZE[1]-LB_MAP_SIZE[1]+SCREEN_HEIGHT): self.map_y-=1

def main():
    GameView().game_loop()
    

if __name__ == "__main__":
    main()