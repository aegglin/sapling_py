import pygame

import constants
import utils
from direction import Direction
from game_object import GameObject


class Beetle(GameObject):

    def __init__(self, world_x, world_y, speed, game_window):
        GameObject.__init__(self, world_x, world_y, speed)
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

        self.game_window = game_window

        self.direction = Direction.DOWN
        self.curr_sprite = self.down1
        self.curr_sprite_number = 1
        self.curr_sprite_frame_count = 0

        offset = constants.TILE_SIZE / 2

        self.camera_x = constants.SCREEN_WIDTH / 2 - offset
        self.camera_y = constants.SCREEN_HEIGHT / 2 - offset
    
    def draw(self):
        if self.direction == Direction.UP:
            if self.curr_sprite_number == 1:
                self.curr_sprite = self.up1
            elif self.curr_sprite_number == 2:
                self.curr_sprite = self.up2
        elif self.direction == Direction.DOWN:
            if self.curr_sprite_number == 1:
                self.curr_sprite = self.down1
            elif self.curr_sprite_number == 2:
                self.curr_sprite = self.down2
        elif self.direction == Direction.RIGHT:
            if self.curr_sprite_number == 1:
                self.curr_sprite = self.right1
            elif self.curr_sprite_number == 2:
                self.curr_sprite = self.right2
        elif self.direction == Direction.LEFT:
            if self.curr_sprite_number == 1:
                self.curr_sprite = self.left1
            elif self.curr_sprite_number == 2:
                self.curr_sprite = self.left2

        self.game_window.window.blit(self.curr_sprite, (self.camera_x, self.camera_y))

    
    def update(self):
        window_width, window_height = pygame.display.get_surface().get_size()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w] \
            or keys[pygame.K_DOWN] or keys[pygame.K_s] \
            or keys[pygame.K_LEFT] or keys[pygame.K_a] \
            or keys[pygame.K_RIGHT] or keys[pygame.K_d]:

            if keys[pygame.K_UP] or keys[pygame.K_w]:
                self.direction = Direction.UP
                self.world_y -= self.speed
                if self.world_y < 0:
                    self.world_y = 0
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                self.direction = Direction.DOWN
                self.world_y += self.speed
                if self.world_y + 48 > window_height:
                    self.world_y = window_height - 48
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.direction = Direction.LEFT
                self.world_x -= self.speed
                if self.world_x < 0:
                    self.world_x = 0
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.direction = Direction.RIGHT
                self.world_x += self.speed
                if self.world_x + 48 > window_width:
                    self.world_x = window_width - 48

            self.curr_sprite_frame_count += 1
            if self.curr_sprite_frame_count > constants.SPRITE_FRAME_SWITCH_THRESHOLD:
                self.curr_sprite_number = 1 if self.curr_sprite_number == 2  else 2
                self.curr_sprite_frame_count = 0