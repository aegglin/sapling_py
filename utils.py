import os
import pygame

def load_image(directory, filename):
    image = pygame.image.load(os.path.join(directory, filename))
    return image