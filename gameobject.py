import pygame
from abc import ABC, abstractmethod

from direction import Direction

class GameObject(ABC):
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
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
            if self.y + 48 > window_height:
                self.y = window_height - 48
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]):
            self.direction = Direction.LEFT
            self.x -= self.speed
            if self.x < 0:
                self.x = 0
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction = Direction.RIGHT
            self.x += self.speed
            if self.x + 48 > window_width:
                self.x = window_width - 48