import pygame
from sys import exit
import random

WIDTH , HEIGHT = 1200 , 700

block_lst = []

counter = 0

class Block:
    def __init__(self , x , y , side):
        self.x = x
        self.y = y
        
        self.side = side
        
        self.width = 100
        if side == "top":
            self.surface = pygame.Surface( (self.width , self.y) )
        else:
            self.surface = pygame.Surface( (self.width , HEIGHT - self.y) )
        self.surface.fill("green")
    def update(self):
        self.x -= 2
    
    def draw(self):
        if self.side == "top":
            self.surface_rect = self.surface.get_rect(bottomleft = (self.x , self.y))
        else:
            self.surface_rect = self.surface.get_rect(topleft = (self.x , self.y))
        screen.blit(self.surface , self.surface_rect)
def create_block():
    mid = random.randint(150 , 550)
    top = mid - 125
    bottom = mid + 125
    
    block_lst.append(Block(WIDTH , top , "top"))
    block_lst.append(Block(WIDTH , bottom , "bottom"))
    
    
def draw():
    for block in block_lst:
        block.update()
        block.draw()

pygame.init()
screen = pygame.display.set_mode( (WIDTH , HEIGHT) )

clock = pygame.time.Clock()


while True:
    screen.fill("white")
    pygame.display.set_caption(f"Flappy Bird FPS : {round(clock.get_fps())}")
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if counter % 150 == 0:
        create_block()
    draw()
    counter += 1    
    pygame.display.update()
    clock.tick(60)
