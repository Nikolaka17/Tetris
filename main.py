import pygame
from sys import exit

class Window:
    def __init__(self):
        self.width = 800
        self.height = 630

        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.fill((0, 0, 0))
        self.clock = pygame.time.Clock()
        self.fps = 60
    
    def draw_grid(self):
        for x in range(250, self.width - 250, 30):
            for y in range(15, self.height - 15, 30):
                pygame.draw.rect(self.screen, (255, 255, 255), (x, y, 30, 30), 1)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            
            self.draw_grid()
            pygame.display.update()
            self.clock.tick(self.fps)


if __name__ == "__main__":
    game = Window()
    game.run()