from button import *
import imp
import colors
import pygame
from config import *
from point import *
from navigation_window import *

CLOCK = pygame.time.Clock()

class GameView():
    def __init__(self):
        self.game_is_running = True
        self.points = []
        self.map_x = 0
        self.map_y = 0
        self.append_tools = True

        # windows 
        self.buttons = []
        self.actual_window = 'sidebar'
       
    def generate_tools(self):
        if self.append_tools:
           self.buttons = Window(self.actual_window).add_buttons()
        self.append_tools = False


    def game_loop(self):
        while self.game_is_running:
            self.game_draw()
            self.handle_events()
            self.sterowanie()
            self.points = add_point(self.map_x, self.map_y)
            self.generate_tools()
            
           

    def game_draw(self):
        WIN.blit(LT_MAP,(self.map_x,self.map_y))
        WIN.blit(LB_MAP,(self.map_x,self.map_y+LT_MAP_SIZE[1]))
        WIN.blit(RT_MAP,(self.map_x+LT_MAP_SIZE[0],self.map_y))
        WIN.blit(RB_MAP,(self.map_x+LT_MAP_SIZE[0],self.map_y+RT_MAP_SIZE[1]))

        for point in self.points:
            point.draw_me()

        
        
        Window(self.actual_window).draw_me()

        
        print(self.buttons)
        for button in self.buttons:
            
            if button[0].active_button:
                
                
                if button[2] == 'show_side_menu_button':
                    print("ss")
                    self.actual_window = 'side menu'
                    self.append_tools = True
                elif button[2] == 'hide_side_menu_button':
                    self.actual_window = 'sidebar'
                    self.append_tools = True
                    print("bb")
                
            if len(button) == 2: button[0].draw_the_button()
            else:  
                button[0].draw_the_button()
                button[1].draw_me()

        
        pygame.display.update()


    def handle_events(self):
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                self.game_is_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
                #print(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])

            ''' 
            if event.type==pygame.KEYDOWN:
                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[pygame.K_LEFT]:
                    if self.map_x<0: self.map_x+=100

                if pressed_keys[pygame.K_RIGHT]:
                    if self.map_x>(-LT_MAP_SIZE[0]-RT_MAP_SIZE[0]+SCREEN_LENGTH): self.map_x-=100


                if pressed_keys[pygame.K_UP]:
                    if self.map_y<0: self.map_y+=100

                if pressed_keys[pygame.K_DOWN]:
                    if self.map_y>(-LT_MAP_SIZE[1]-LB_MAP_SIZE[1]+SCREEN_HEIGHT): self.map_y-=100
            '''


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