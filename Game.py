import pygame, random

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Pantalla
largo = 800
alto = 600

pygame.init()
pygame.mixer.init()

fondo = pygame.image.load("Imagenes/Auxiliares/setting_image.png")
laser_sonido = pygame.mixer.Sound("Sonidos/Efectos de sonido/laser.mp3")
laser_sonido_2 = pygame.mixer.Sound("Sonidos/Efectos de sonido/Laser_2.wav")
explosion_sonido = pygame.mixer.Sound("Sonidos/Efectos de sonido/Explosion.wav")
golpe_sonido = pygame.mixer.Sound("Sonidos/Efectos de sonido/Golpe.wav")
propulsores_sonido = pygame.mixer.SoundType("Sonidos/Efectos de sonido/Propulsores de nave.mp3")
propulsores_sonido.set_volume(0.25)
           
def texto_puntuacion(frame, text, size, x, y):
    font = pygame.font.SysFont("Small Fonts", size, bold=True)
    text_frame = font.render(text, True, BLANCO, NEGRO)
    text_rect = text_frame.get_rect()
    text_rect.midtop = (x, y)
    frame.blit(text_frame, text_rect)
    
def barra_vida(frame, x, y, nivel):
    longitud = 100
    alto = 20
    fill = int((nivel/100)*longitud)
    border = pygame.Rect(x, y, longitud, alto)
    fill = pygame.Rect(x, y, fill, alto)
    pygame.draw.rect(frame, (255, 0, 55), fill)
    pygame.draw.rect(frame, NEGRO, border, 4)

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Imagenes/Jugador/Nave.png").convert_alpha()
        # Obtiene el color de fondo de la imagen
        self.color_fondo = self.image.get_at((0, 0))
        # Elimina el color de fondo de la imagen
        self.image.set_colorkey(self.color_fondo)
        # Icono de la app
        pygame.display.set_icon(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = largo//2
        self.rect.centery = alto-50
        self.vida = 100
    
    def update(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.rect.x -= 50
            propulsores_sonido.play()
        elif keystate[pygame.K_RIGHT]:
            self.rect.x += 50
            propulsores_sonido.play()
        elif keystate[pygame.K_UP]:
            self.rect.y -= 50
            propulsores_sonido.play()
        elif keystate[pygame.K_DOWN]:
            self.rect.y += 50
            propulsores_sonido.play()
            
        if self.rect.right > largo:
            self.rect.right = largo
        elif self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > alto:
            self.rect.bottom = alto
    
    def disparo_normal(self):
        bala_normal = Balas(self.rect.centerx, self.rect.top)
        grupo_jugador.add(bala_normal)
        grupo_balas_jugador.add(bala_normal)
        laser_sonido.play()
        
class Enemigos(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("Imagenes/Enemigos/enemigo.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(1, largo-50)
        self.rect.y = 10
        
    def update(self):
        self.rect.x += 5
        if self.rect.x >= largo:
            self.rect.x = 0
            self.rect.y += 50
            
    def disparo_enemigo(self):
        bala = Balas_enemigos(self.rect.centerx, self.rect.bottom)
        grupo_jugador.add(bala)
        grupo_balas_enemigos.add(bala)
        laser_sonido_2.play()
        
class Balas(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("Imagenes/Auxiliares/bala_normal.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.y = y
    
    def update(self):
        self.rect.y += -25
        if self.rect.bottom < 0:
            self.kill()
            
class Balas_enemigos(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("Imagenes/Auxiliares/bala_enemigo.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.y = y
    
    def update(self):
        self.rect.y += 25
        if self.rect.bottom > alto:
            self.kill()

grupo_jugador = pygame.sprite.Group()
grupo_enemigos = pygame.sprite.Group()
grupo_balas_jugador = pygame.sprite.Group()
grupo_balas_enemigos = pygame.sprite.Group()

# Ciclo del juego
def Game():  
    play = True
    fps = 10
    clock = pygame.time.Clock()
    score = 0
    vida = 100

    window = pygame.display.set_mode((largo, alto))
    pygame.display.set_caption("Galatec")
        
    player = Jugador()
    grupo_jugador.add(player)
    grupo_balas_jugador.add(player)

    for x in range(10):
        enemigo = Enemigos(10, 10)
        grupo_enemigos.add(enemigo)
        grupo_jugador.add(enemigo)
    
    # Carga fondo del nivel
    coord_list = []
    for i in range(60):
        x = random.randint(0, largo)
        y = random.randint(0, alto)
        coord_list.append([x, y])
    
    while play:
        clock.tick(fps)

        # Dibuja el fondo
        window.fill(NEGRO)
        for coord in coord_list:
            x = coord[0]
            y = coord[1]
            pygame.draw.circle(window, BLANCO, (x, y), 2)
            coord[1] += 2
            if coord[1] > alto:
                coord[1] = 0
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.disparo_normal()
        
        grupo_jugador.update()
        grupo_enemigos.update()
        grupo_balas_jugador.update()
        grupo_balas_enemigos.update()
        
        grupo_jugador.draw(window)
        
        # Coliciones balas_jugador - enemigo
        colicion1 = pygame.sprite.groupcollide(grupo_enemigos, grupo_balas_jugador, True, True)
        for i in colicion1:
            score += 10
            enemigo.disparo_enemigo()
            explosion_sonido.play()
            enemigo = Enemigos(300, 10)
            grupo_enemigos.add(enemigo)
            grupo_jugador.add(enemigo)
            
        # Coliciones jugador - balas_enemigo
        colicion2 = pygame.sprite.spritecollide(player, grupo_balas_enemigos, True)
        for j in colicion2:
            player.vida -= 20
            golpe_sonido.play()
            if player.vida <= 0:
                play = False
        
        # Coliciones jugador - enemigo
        hits = pygame.sprite.spritecollide(player, grupo_enemigos, False)
        for hit in hits:
            player.vida -= 100
            enemigos = Enemigos(10, 10)
            grupo_jugador.ad(enemigos)
            grupo_enemigos.add(enemigos)
            if player.vida <= 0:
                play = False
                
        texto_puntuacion(window, ("SCORE: " + str(score) + " "), 30, largo - 85, 2)
        barra_vida(window, largo-285, 0, player.vida)
        
        pygame.display.flip()
        
    pygame.quit()

Game()
