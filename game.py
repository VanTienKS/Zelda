import pygame
import sys

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
        
        # sound
        main_sound = pygame.mixer.Sound('audio/main.ogg')
        main_sound.set_volume(0.4)
        main_sound.play(loops=1)

    def run(self):
        while self.playing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level.toggle_menu()

            # render
            self.screen.fill(WATER_COLOR)
            self.level.render()

            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
