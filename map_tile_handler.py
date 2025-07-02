from tile import Tile
from utils import load_image

class MapTileHandler:

    def __init__(self, map_file):
        self.map_file = map_file
        self.map_tile_numbers = []
        self.map_tiles = []
        self.load_images()
        self.load_map(map_file)

    def load_map(self, map_file):
        with open(map_file, 'r') as f:
            lines = f.readlines()

            # Line is a string of digits separated by a space, with a newline appended to the last character
            for line in lines:
                curr_list = []
                line = line.replace('\n', '')
                numbers = line.split(' ')
                numbers = list(map(int, numbers)) # Convert numbers from string to int
                for number in numbers:
                    curr_list.append(number)
                self.map_tile_numbers.append(curr_list)

    def create_tile_image(self, directory, filename, is_solid):
        tile = Tile(directory, filename, is_solid)
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