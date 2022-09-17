
import imp
import colors
import pygame
from config import *
from point import *

CLOCK = pygame.time.Clock()



class GameView():
    def __init__(self):
        self.game_is_running = True
        self.points=points
        
        self.map_x=0
        self.map_y=0

       

    def game_loop(self):
        while self.game_is_running:
            self.game_draw()
            self.handle_events()
            self.sterowanie()
           

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
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT]:
            self.map_x+=1
        if pressed_keys[pygame.K_RIGHT]:
            self.map_x-=1
        if pressed_keys[pygame.K_UP]:
            self.map_y+=1
        if pressed_keys[pygame.K_DOWN]:
            self.map_y-=1

def main():
    GameView().game_loop()
    print(LT_MAP_SIZE)
    print(LB_MAP_SIZE)
    print(RT_MAP_SIZE)
    print(RB_MAP_SIZE)

if __name__ == "__main__":
    main()