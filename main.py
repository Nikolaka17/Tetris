import pygame
from sys import exit

class Window:
    def __init__(self):
        self.width = 800
        self.height = 600

        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.fill((0, 0, 0))
        self.clock = pygame.time.Clock()
        self.fps = 60

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            
            pygame.display.update()
            self.clock.tick(self.fps)


if __name__ == "__main__":
    game = Window()
    game.run()