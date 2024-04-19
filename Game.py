import pygame
import sys

# Colores
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)

# Pantalla
largo = 800
alto = 600

class Jugador:
    def __init__(self, imagen_ruta, posicion_x, posicion_y):
        self.imagen = pygame.image.load(imagen_ruta)
        self.rect = self.imagen.get_rect()
        self.rect.x = posicion_x
        self.rect.y = posicion_y

    def dibujar(self, ventana):
        ventana.blit(self.imagen, self.rect)

    def update(self, keys):
        if keys[pygame.K_w]:
            self.rect.y -= 50
        if keys[pygame.K_s]:
            self.rect.y += 50
        if keys[pygame.K_a]:
            self.rect.x -= 50
        if keys[pygame.K_d]:
            self.rect.x += 50

def Game():
    # Inicializa Pygame
    pygame.init()
    
    # Crea la ventana
    ventana = pygame.display.set_mode((largo, alto))
    pygame.display.set_caption("Galatec")

    # Crea al jugador
    jugador = Jugador("Imagenes/Jugador/Nave.png", 300, 400)

    # Crea un timer
    reloj = pygame.time.Clock()
    
    # Ciclo principal del juego
    jugando = True
    while jugando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jugando = False

        # Actualizar el jugador
        keys = pygame.key.get_pressed()
        jugador.update(keys)

        # Limpia la ventana
        ventana.fill(BLANCO)
        
        # Dibuja al jugador
        jugador.dibujar(ventana)
        
        # Actualiza la pantalla
        pygame.display.flip()

        # Velocidad de los fps
        reloj.tick(20)

    # Finaliza pygame y sys
    pygame.quit()
    sys.exit()

#Game()