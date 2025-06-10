import pygame
import utils

from gameobject import GameObject

class Beetle(GameObject):

    def __init__(self, x, y, speed):
        GameObject.__init__(self, x, y, speed)
        # images
        self.down1 = utils.load_image("assets", "BeetleDown1.png")
        self.down1 = pygame.transform.scale(self.down1, (40, 40))

        self.down2 = utils.load_image("assets", "BeetleDown2.png")

        self.up1 = utils.load_image("assets", "BeetleUp1.png")
        self.up2 = utils.load_image("assets", "BeetleUp2.png")

        self.left1 = utils.load_image("assets", "BeetleLeft1.png")
        self.left2 = utils.load_image("assets", "BeetleLeft2.png")

        self.right1 = utils.load_image("assets", "BeetleRight1.png")
        self.right2 = utils.load_image("assets", "BeetleRight2.png")

        self.curr_sprite = self.down1
    

    