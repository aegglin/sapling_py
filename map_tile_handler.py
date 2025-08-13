import pygame

from tile import Tile

import constants

class MapTileHandler:

    def __init__(self, map_file, game_window):
        self.map_file = map_file
        self.map_tile_numbers = []
        self.map_tiles = []
        self.load_images()
        self.load_map(map_file)
        self.game_window = game_window

    def load_map(self, map_file):
        with open(map_file, 'r') as f:
            lines = f.readlines()

            # Line is a string of digits separated by a space, with a newline appended to the last character
            for line in lines:
                curr_list = []
                numbers = line.replace('\n', '').split(' ')
                numbers = list(map(int, numbers)) # Convert numbers from string to int

                for number in numbers:
                    curr_list.append(number)
                self.map_tile_numbers.append(curr_list)

    def create_tile_image(self, directory, filename, is_solid):
        tile = Tile(directory, filename, is_solid)
        tile.image = pygame.transform.scale(tile.image, (constants.TILE_SIZE, constants.TILE_SIZE))
        self.map_tiles.append(tile)

    def load_images(self):
        self.create_tile_image('assets/tiles', 'Grass.png', False)
        self.create_tile_image('assets/tiles', 'Tree1.png', True)
        self.create_tile_image('assets/tiles', 'Tree2.png', True)
        self.create_tile_image('assets/tiles', 'Tree3.png', True)
        self.create_tile_image('assets/tiles', 'Shrub.png', True)
        self.create_tile_image('assets/tiles', 'Underbrush.png', False)
        self.create_tile_image('assets/tiles', 'Shrub_Underbrush.png', True)
        self.create_tile_image('assets/tiles', 'OrangeFlower.png', False)
        self.create_tile_image('assets/tiles', 'Tree1_Flies1.png', True)
        self.create_tile_image('assets/tiles', 'Tree1_Beehive1.png', True)
        self.create_tile_image('assets/tiles', 'Tree1_Woodpecker1.png', True)

    def draw_all(self):
        for i, world_col in enumerate(self.map_tile_numbers):
            for j, world_row in enumerate(world_col):
                curr_number = self.map_tile_numbers[i][j]
                tile = self.map_tiles[curr_number]

                world_x = world_col * constants.TILE_SIZE
                world_y = world_row * constants.TILE_SIZE

                camera_x = world_x - self.game_window.beetle.world_x + self.game_window.beetle.world_x
                camera_y = world_y - self.game_window.beetle.world_y + self.game_window.beetle.world_y


                if world_x + constants.TILE_SIZE > self.game_window.beetle.world_x - self.game_window.beetle.camera_x and \
                    world_x - constants.TILE_SIZE < self.game_window.beetle.world_x + self.game_window.beetle.camera_x and \
                    world_y + constants.TILE_SIZE > self.game_window.beetle.world_y - self.game_window.beetle.camera_y and \
                    world_y - constants.TILE_SIZE < self.game_window.beetle.world_y + self.game_window.beetle.camera_y:

                        self.game_window.window.blit(tile.image, (camera_x, camera_y))


