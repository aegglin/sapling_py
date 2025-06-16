import pygame

from direction import Direction

class GameObject:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = Direction.DOWN

    def draw(self):
        pass
        

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.direction = Direction.UP
            self.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.direction = Direction.DOWN
            self.y += self.speed
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction = Direction.LEFT
            self.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction = Direction.RIGHT
            self.x += self.speed
