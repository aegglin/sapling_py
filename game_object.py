import pygame
from abc import ABC, abstractmethod

from direction import Direction

class GameObject(ABC):
    def __init__(self, world_x, world_y, speed):
        self.world_x = world_x
        self.world_y = world_y
        self.speed = speed
        self.direction = Direction.DOWN

    @abstractmethod
    def draw(self):
        pass
        
    @abstractmethod
    def update(self):
        pass
        