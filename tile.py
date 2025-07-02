import utils

class Tile:
    def __init__(self, directory, filename, is_solid):
        self.image = utils.load_image(directory, filename)
        self.is_solid = is_solid