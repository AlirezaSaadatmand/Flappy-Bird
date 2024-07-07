import pygame
from sys import exit
import random

WIDTH , HEIGHT = 1200 , 700

class Block:
    def __init__(self , x , y):
        self.x = x
        self.y = y
        


pygame.init()
screen = pygame.display.set_mode( (WIDTH , HEIGHT) )
clock = pygame.time.Clock()



while True:
    pygame.display.set_caption(f"Flappy Bird FPS : {round(clock.get_fps())}")
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
    pygame.display.update()
    clock.tick(60)
