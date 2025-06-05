import pygame 
from sys import exit 

# Game variables
GAME_WIDTH = 768
GAME_HEIGHT = 576

pygame.init()
window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption('Sapling by Aiden Egglin')
clock = pygame.time.Clock()


# left(x), top(y), width, height
player = pygame.Rect(150, 150, 50, 50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            player.y -= 5
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            player.y += 5
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player.x -= 5
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player.x += 5

        window.fill((20, 18, 167, 167))
        pygame.draw.rect(window, (2, 239, 238), player)
        pygame.display.update()
        clock.tick(60) # 60 fps