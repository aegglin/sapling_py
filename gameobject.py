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
        
    @abstractmethod
    def update(self):
        pass
        