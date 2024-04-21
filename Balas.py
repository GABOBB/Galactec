import pygame

# Clase de la bala normal
class Laser:
    def __init__(self, x, y):
        super().__init__()
        self.laser = pygame.image.load("Imagenes/Auxiliares/bala_normal.png").convert()
        self.rect = self.laser.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def update(self):
        self.rect.y -= 5
        
    def dibujar(self, ventana):
        ventana.blit(self.laser, self.rect)
