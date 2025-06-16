import pygame
from abc import ABC, abstractmethod


from direction import Direction
from window import GameWindow

class GameObject(ABC):
    def __init__(self, x, y, speed, window):
        self.x = x
        self.y = y
        self.speed = speed
        self.window = window
        self.direction = Direction.DOWN

    @abstractmethod
    def draw(self):
        pass
        
    def update(self):

        window_width, window_height = pygame.display.get_surface().get_size()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.direction = Direction.UP
            self.y -= self.speed
            if self.y < 0:
                self.y = 0
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.direction = Direction.DOWN
            self.y += self.speed
            if self.y + GameWindow.TILE_SIZE > GameWindow.GAME_HEIGHT:
                self.y = GameWindow.GAME_HEIGHT - GameWindow.TILE_SIZE
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.x - self.speed >= 0:
            self.direction = Direction.LEFT
            self.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d] and self.x + self.speed <= window_width:
            self.direction = Direction.RIGHT
            self.x += self.speed
