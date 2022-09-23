from itertools import count
from venv import create
from start_menu import *
from operator import concat
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
        self.chosen_points = []
        

        # path
        self.create_path = False
        self.path = []
        self.start = ''
        self.destination = ''

        # tools
        self.enter = False
        self.counter = 0
        self.click_mode = False

       
        
        
        
       
    def generate_tools(self):
        if self.append_tools:
            self.buttons = Window(self.actual_window).add_buttons()
            self.points = add_point()
            self.points_names = get_points_names(self.points)
            self.destination = ''
            self.start = ''

        self.append_tools = False

    def create_path_for_me(self):
 
            if self.path and self.start and self.destination: 
                
                draw_the_line(self.path, self.points, self.points_names, self.map_x, self.map_y)

        
    def game_loop(self):

        while self.game_is_running:
            
            self.game_draw()
            self.handle_events()
            self.sterowanie()
            self.generate_tools()
            
            

    def game_draw(self):
        # draw map
       
        WIN.blit(LT_MAP,(self.map_x,self.map_y))
        WIN.blit(LB_MAP,(self.map_x,self.map_y+LT_MAP_SIZE[1]))
        WIN.blit(RT_MAP,(self.map_x+LT_MAP_SIZE[0],self.map_y))
        WIN.blit(RB_MAP,(self.map_x+LT_MAP_SIZE[0],self.map_y+RT_MAP_SIZE[1]))
        
        
        

        # draw and check points
        if self.click_mode: 
            self.chosen_points = check_points(self.points, self.map_x, self.map_y, self.chosen_points)
            if len(self.chosen_points)  == 2 : self.start, self.destination = self.chosen_points[0], self.chosen_points[1]

        # draw path
        self.create_path_for_me()

        # draw actual window
        window =  Window(self.actual_window)
        window.draw_me()

        # animate arrow
        if self.start and self.destination: self.counter = animate_arrow(self.counter)
        
        # draw actual window's buttons
        
        for button in self.buttons:
            
            if button[0].active_button:
                
                if button[1] == 'show_side_menu_button':
                    self.actual_window = 'side menu'
                    self.append_tools = True
                    
                elif button[1] == 'hide_side_menu_button':
                    self.actual_window = 'sidebar'
                    self.append_tools = True
                    
                elif button[1] == 'from_button': 
                    button[0].allow = True
                    self.start = ''

                elif button[1] == 'help_button':
                    pass
                    

                elif button[1] == 'to_button': 
                    button[0].allow = True
                    self.destination = ''
    
                elif button[1] == 'draw_path_button':  button[0].allow = True 
                    
            
                elif button[1] == 'point_button': 
                    if not self.click_mode : self.click_mode = True
                    else:  self.click_mode = False



            if button[0].allow:
                # entering points

                if button[1] == 'search_button' or button[1] == 'from_button' or button[1] == 'to_button':
                    if not self.click_mode:
                        self.path = ''
                        button[0].text = self.keyboard_input
                        button[0].text_backing_color = SKY_BLUE

                        
                        if self.keyboard_input: 
                            suggestions = find_name(mp_graph[2], self.keyboard_input)
                            if suggestions: draw_suggestions(suggestions)

                        if self.enter:
                            if self.keyboard_input in mp_graph[2]: 
                                button[0].text_backing_color = LIGHT_GREEN
                                if button[1] == 'from_button' : self.start = self.keyboard_input
                                elif button[1] == 'to_button' : self.destination = self.keyboard_input
                            else : button[0].text_backing_color = RED
                            
                            self.keyboard_input = ''
                            button[0].allow = False
                            self.enter = False
            
                elif button[1] == 'draw_path_button':
                    button[0].allow = False
                    
                    if self.start and self.destination: 
                        self.path = algorithm.the_shortest_path(self.start, self.destination, mp_graph)
                   
                
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

                elif event.key == pygame.K_RETURN:
                    self.enter = True

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
    answer = [True, True]
    start_menu = False

    while start_menu:
        answer = starting_menu()
        start_menu = answer[0]
    
    if answer[1]: GameView().game_loop()
    

if __name__ == "__main__":
    main()