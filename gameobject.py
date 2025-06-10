import pygame

from direction import Direction

class GameObject:
    def __init__(self, x, y, speed, curr_sprite, direction):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = direction
        self.curr_sprite = curr_sprite

    def draw(self, surface):
        
        if self.direction == Direction.UP:
            pass
        elif self.direction == Direction.DOWN:
            pass
        elif self.direction == Direction.RIGHT:
            pass
        elif self.direction == Direction.LEFT:
            pass

    def update(self, surface):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y += self.speed
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += self.speed