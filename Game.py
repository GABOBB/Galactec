import pygame, random
import Player, Balas

# Colores
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
NEGRO = (0, 0, 0)

# Pantalla
largo = 800
alto = 600

# Ciclo del juego
def Game():
    # Inicializa Pygame
    pygame.init()
    
    # Crea la ventana
    ventana = pygame.display.set_mode((largo, alto))
    pygame.display.set_caption("Galatec")

    # Crea al jugador
    jugador = Player.Jugador("Imagenes/Jugador/Nave.png", 300, 400)

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

#Game()
