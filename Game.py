import pygame

# Colores
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)

# Pantalla
largo = 800
alto = 600

class Jugador:
    def __init__(self, imagen_ruta, posicion_x, posicion_y):
        # Carga la skin del jugador
        self.nave = pygame.image.load(imagen_ruta)
        # Verifica el tamaño de la imagen cargada
        if self.nave.get_size() != [100, 100]: # Si es diferente a (100, 100), transforma la escala a (100, 100)
            self.nave = pygame.transform.scale(self.nave, (100, 100))
        # Obtiene el color de fondo de la imagen
        self.color_fondo = self.nave.get_at((0, 0))
        # Elimina el color de fondo de la imagen
        self.nave.set_colorkey(self.color_fondo)
        # Crea la hitbox de la imagen
        self.rect = self.nave.get_rect()
        self.rect.x = posicion_x
        self.rect.y = posicion_y

    def dibujar(self, ventana):
        ventana.blit(self.nave, self.rect)

    def update(self, keys):
        if self.rect.y >= 50:
            if keys[pygame.K_UP]:
                self.rect.y -= 50
        if self.rect.y <= alto - 150:
            if keys[pygame.K_DOWN]:
                self.rect.y += 50
        if self.rect.x >= 50:
            if keys[pygame.K_LEFT]:
                self.rect.x -= 50
        if self.rect.x <= largo - 150:
            if keys[pygame.K_RIGHT]:
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
        reloj.tick(30)

    # Finaliza pygame y sys
    pygame.quit()

Game()