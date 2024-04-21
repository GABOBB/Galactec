import pygame
import Balas

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
            laser = Balas.Laser(self.rect.x + 47, self.rect.y - 30)
            laser.dibujar(ventana)
