import pygame
from sys import exit
import random

WIDTH , HEIGHT = 1200 , 700

block_lst = []

counter = 0

score = 0

WIDTH_OF_BLOCK = 250

gameover = False
class Bird:
    def __init__(self):
        self.x = 300
        self.y = 200
        
        self.gravity = 1
        self.velocity = -10
    
        self.surface = pygame.Surface( (40 , 40) )
        self.surface.fill("red")
    def jump(self):
        self.velocity = -15
        self.y -= 25
    
    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity
        
    def draw(self):
        self.surface_rect = self.surface.get_rect(center = (self.x , self.y))
        screen.blit(self.surface , self.surface_rect)


bird = Bird()
class Block:
    def __init__(self , x , y , side):
        self.x = x
        self.y = y
        self.marked = False
        self.side = side
        
        self.width = 100
        if side == "top":
            self.surface = pygame.Surface( (self.width , self.y) )
            self.surface_rect = self.surface.get_rect(bottomleft = (self.x , self.y))
            
        else:
            self.surface = pygame.Surface( (self.width , HEIGHT - self.y) )
            self.surface_rect = self.surface.get_rect(topleft = (self.x , self.y))
            
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
    top = mid - WIDTH_OF_BLOCK / 2
    bottom = mid + WIDTH_OF_BLOCK / 2
    
    block_lst.append(Block(WIDTH , top , "top"))
    block_lst.append(Block(WIDTH , bottom , "bottom"))
    
def check():
    global gameover , score
    if bird.y - 20 > HEIGHT:
        gameover = True
    for block in block_lst:
        if block.surface_rect.colliderect(bird.surface_rect):
            gameover = True
        if block.x + block.width < bird.x and not block.marked:
            score += 5
            block.marked = True

def draw(score_text):

    if not gameover:
        bird.update()
    bird.draw()
    
    for block in block_lst:
        if not gameover:
            block.update()
        block.draw()
        if block.x < 0 - block.width:
            block_lst.remove(block)
    score1_text = score_text.render(f"Score : {score}" , True , "black")
    score_text_rect = score1_text.get_rect(center = (50 , 30))
    screen.blit(score1_text , score_text_rect)

pygame.init()
screen = pygame.display.set_mode( (WIDTH , HEIGHT) )
clock = pygame.time.Clock()

score_text = pygame.font.Font(None , 30)

while True:
    screen.fill("white")
    pygame.display.set_caption(f"Flappy Bird FPS : {round(clock.get_fps())}")
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN and not gameover:
            if event.key == pygame.K_SPACE:
                bird.jump()
    draw(score_text)
    if not gameover:
        check()
        if counter % 150 == 0:
            create_block()
    counter += 1    
    pygame.display.update()
    clock.tick(60)
