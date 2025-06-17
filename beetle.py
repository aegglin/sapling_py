import pygame

import constants
import utils
from direction import Direction
from gameobject import GameObject


class Beetle(GameObject):

    def __init__(self, x, y, speed):
        GameObject.__init__(self, x, y, speed)
        # images
        self.down1 = utils.load_image("assets/beetle", "BeetleDown1.png")
        self.down1 = pygame.transform.scale(self.down1, (constants.TILE_SIZE, constants.TILE_SIZE))
        self.down2 = utils.load_image("assets/beetle", "BeetleDown2.png")
        self.down2 = pygame.transform.scale(self.down2, (constants.TILE_SIZE, constants.TILE_SIZE))

        self.up1 = utils.load_image("assets/beetle", "BeetleUp1.png")
        self.up1 = pygame.transform.scale(self.up1, (constants.TILE_SIZE, constants.TILE_SIZE))
        self.up2 = utils.load_image("assets/beetle", "BeetleUp2.png")
        self.up2 = pygame.transform.scale(self.up2, (constants.TILE_SIZE, constants.TILE_SIZE))

        self.left1 = utils.load_image("assets/beetle", "BeetleLeft1.png")
        self.left1 = pygame.transform.scale(self.left1, (constants.TILE_SIZE, constants.TILE_SIZE))
        self.left2 = utils.load_image("assets/beetle", "BeetleLeft2.png")
        self.left2 = pygame.transform.scale(self.left2, (constants.TILE_SIZE, constants.TILE_SIZE))

        self.right1 = utils.load_image("assets/beetle", "BeetleRight1.png")
        self.right1 = pygame.transform.scale(self.right1, (constants.TILE_SIZE, constants.TILE_SIZE))
        self.right2 = utils.load_image("assets/beetle", "BeetleRight2.png")
        self.right2 = pygame.transform.scale(self.right2, (constants.TILE_SIZE, constants.TILE_SIZE))

        self.direction = Direction.DOWN
        self.curr_sprite = self.down1
    
    def draw(self):
        if self.direction == Direction.UP:
            self.curr_sprite = self.up1
        elif self.direction == Direction.DOWN:
            self.curr_sprite = self.down1
        elif self.direction == Direction.RIGHT:
            self.curr_sprite = self.right1
        elif self.direction == Direction.LEFT:
            self.curr_sprite = self.left1
    
    def update(self):
        GameObject.update(self)