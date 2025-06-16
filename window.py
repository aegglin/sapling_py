import pygame 
from sys import exit
from beetle import Beetle

class GameWindow:
    
    RAW_PIXEL_TILE_SIZE = 16
    SCALE = 3
    TILE_SIZE = RAW_PIXEL_TILE_SIZE * SCALE
    MAX_SCREEN_COL = 16
    MAX_SCREEN_ROW = 12
    GAME_WIDTH = TILE_SIZE * MAX_SCREEN_COL # 768 pixels
    GAME_HEIGHT = TILE_SIZE * MAX_SCREEN_ROW # 576 pixels
    FPS = 60
    STARTING_X = GAME_WIDTH / 2
    STARTING_Y = GAME_HEIGHT / 2

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((self.GAME_WIDTH, self.GAME_HEIGHT))
        pygame.display.set_caption('Sapling by Aiden Egglin')
        self.clock = pygame.time.Clock()

        self.beetle = Beetle(self.STARTING_X, self.STARTING_Y, 15, self.window)
        pygame.display.set_icon(self.beetle.down1)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                self.beetle.update()
                self.beetle.draw()

                self.window.fill((20, 18, 167, 167))
                
                self.window.blit(self.beetle.curr_sprite, (self.beetle.x, self.beetle.y))
                pygame.display.update()
                self.clock.tick(self.FPS) # 60 fps

if __name__ == '__main__':
    window = GameWindow()
    window.run()
