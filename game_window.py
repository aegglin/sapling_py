import pygame 
from sys import exit
from beetle import Beetle
from map_tile_handler import MapTileHandler

import constants


class GameWindow:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
        pygame.display.set_caption('Sapling by Aiden Egglin')
        self.clock = pygame.time.Clock()

        self.beetle = Beetle(constants.STARTING_X, constants.STARTING_Y, 4, self)
        pygame.display.set_icon(self.beetle.down1)
        self.map_tile_handler = MapTileHandler('assets/maps/map1.txt', self)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            self.map_tile_handler.draw_all()
            self.beetle.update()
            self.beetle.draw()

            pygame.display.update()
            self.clock.tick(constants.FPS) # 60 fps

 

