import pygame 
import utils
from sys import exit
from beetle import Beetle

# Game variables
GAME_WIDTH = 768
GAME_HEIGHT = 576


pygame.init()
window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption('Sapling by Aiden Egglin')
clock = pygame.time.Clock()


# left(x), top(y), width, height
player = pygame.Rect(150, 150, 50, 50)

STARTING_X = GAME_WIDTH / 2
STARTING_Y = GAME_HEIGHT / 2

beetle = Beetle(STARTING_X, STARTING_Y, 4)
pygame.display.set_icon(beetle.down1)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # TODO: what should be in these? 
        beetle.update()
        beetle.draw()

        window.fill((20, 18, 167, 167))
        
        window.blit(beetle.curr_sprite, (beetle.x, beetle.y))
        pygame.display.update()
        clock.tick(60) # 60 fps