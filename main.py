
import imp
import colors
import pygame
from config import *
from point import *

CLOCK = pygame.time.Clock()



class GameView():
    def __init__(self):
        self.game_is_running = True
        self.points=[]
        
        self.map_x=0
        self.map_y=0

       

    def game_loop(self):
        while self.game_is_running:
            self.game_draw()
            self.handle_events()
            self.sterowanie()
            self.points=add_point(self.map_x, self.map_y)
           

    def game_draw(self):
        WIN.blit(LT_MAP,(self.map_x,self.map_y))
        WIN.blit(LB_MAP,(self.map_x,self.map_y+LT_MAP_SIZE[1]))
        WIN.blit(RT_MAP,(self.map_x+LT_MAP_SIZE[0],self.map_y))
        WIN.blit(RB_MAP,(self.map_x+LT_MAP_SIZE[0],self.map_y+RT_MAP_SIZE[1]))
        
       
        for point in self.points:
            point.draw_me()


        pygame.display.update()


    def handle_events(self):
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                self.game_is_running = False


    def sterowanie(self):
        print(self.map_y)
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