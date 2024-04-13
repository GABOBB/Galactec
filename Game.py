import pygame
import sys

# Colores
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))  # Tamaño del jugador
        self.image.fill(ROJO)  # Color del jugador
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)  # Posición inicial del jugador

    def update(self, keys):
        if keys[pygame.K_w]:
            self.rect.y -= 40
        if keys[pygame.K_s]:
            self.rect.y += 40
        if keys[pygame.K_a]:
            self.rect.x -= 40
        if keys[pygame.K_d]:
            self.rect.x += 40

def Game():
    pygame.init()
    ventana = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Galatec")
    reloj = pygame.time.Clock()

    jugador = Jugador()
    jugadores = pygame.sprite.Group()
    jugadores.add(jugador)

    jugando = True
    while jugando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jugando = False

        keys = pygame.key.get_pressed()
        jugador.update(keys)

        ventana.fill(BLANCO)
        jugadores.draw(ventana)
        pygame.display.flip()

        reloj.tick(5)

    pygame.quit()
    sys.exit()


Game()


