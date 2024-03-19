import pygame, sys

from scripts.settings import *
from scripts.level import Level

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Zelda")
        
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        
        
        self.level = Level()
        
        self.playing = True
        
    def run(self):
        while self.playing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            # update
            
            # render   
            self.level.render(self.screen)
            
                    
            pygame.display.update()
            self.clock.tick(FPS)
            
if __name__ == '__main__':
    game = Game()
    game.run()