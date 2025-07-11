import pygame 
from sys import exit
from beetle import Beetle
from map_tile_handler import MapTileHandler

import constants


class GameWindow:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((constants.GAME_WIDTH, constants.GAME_HEIGHT))
        pygame.display.set_caption('Sapling by Aiden Egglin')
        self.clock = pygame.time.Clock()

        self.beetle = Beetle(constants.STARTING_X, constants.STARTING_Y, 4, self)
        pygame.display.set_icon(self.beetle.down1)
        self.map_tile_handler = MapTileHandler('assets/maps/map1.txt')

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.beetle.update()
            self.beetle.draw()

            self.window.fill((255, 255, 255, 0))
            self.window.blit(self.beetle.curr_sprite, (self.beetle.x, self.beetle.y))
            pygame.display.update()
            self.clock.tick(constants.FPS) # 60 fps

 

