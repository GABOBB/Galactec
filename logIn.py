import pygame
import sys

class Juego:
    def __init__(self):
        pygame.init()
        screen = pygame.display.set_mode((300,500))
        self.begin()

               
    def begin(self):
        while True:
            for event in pygame.event.get():
                print(event)
                if(event.type)==pygame.QUIT:
                    sys.exit()

Juego()