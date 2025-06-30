import utils

class Tile:
    def __init__(self, image, is_solid):
        self.image = utils.load_image(image)
        self.is_solid = is_solid