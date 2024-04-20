import pygame, random

# Colores
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
NEGRO = (0, 0, 0)

# Pantalla
largo = 800
alto = 600

# Clase jugador
class Jugador:
    def __init__(self, imagen_ruta, posicion_x, posicion_y):
        # Carga la skin del jugador
        self.nave = pygame.image.load(imagen_ruta).convert()
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
        
        # Carga sonidos de la nave
        self.propulsores = pygame.mixer.Sound("Sonidos/Efectos de sonido/Propulsores de nave.mp3")
        self.propulsores.set_volume(0.25)

    def dibujar(self, ventana):
        ventana.blit(self.nave, self.rect)

    def update(self, keys, ventana):
        if self.rect.y >= 50:
            if keys[pygame.K_UP]:
                self.propulsores.play()
                self.rect.y -= 50
        if self.rect.y <= 450:
            if keys[pygame.K_DOWN]:
                self.propulsores.play()
                self.rect.y += 50
        if self.rect.x >= 50:
            if keys[pygame.K_LEFT]:
                self.propulsores.play()
                self.rect.x -= 50
        if self.rect.x <= 650:
            if keys[pygame.K_RIGHT]:
                self.propulsores.play()
                self.rect.x += 50
        if keys[pygame.K_a]:
            x = self.rect.x + 47
            y = self.rect.y - 30
            laser = Laser(x, y)
            laser.dibujar(ventana)

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

# Ciclo del juego
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
    
    # Carga fondo del nivel
    coord_list = []
    for i in range(60):
        x = random.randint(0, largo)
        y = random.randint(0, alto)
        coord_list.append([x, y])
    
    # Ciclo principal del juego
    jugando = True
    while jugando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jugando = False

        # Dibuja el fondo
        ventana.fill(NEGRO)
        for coord in coord_list:
            x = coord[0]
            y = coord[1]
            pygame.draw.circle(ventana, BLANCO, (x, y), 2)
            coord[1] += 2
            if coord[1] > alto:
                coord[1] = 0
        
        # Dibuja al jugador
        jugador.dibujar(ventana)
        
        # Actualizar el jugador
        keys = pygame.key.get_pressed()
        jugador.update(keys, ventana)
        
        # Actualiza la pantalla
        pygame.display.flip()

        # Velocidad de los fps
        reloj.tick(10)

    # Finaliza pygame
    pygame.quit()

Game()