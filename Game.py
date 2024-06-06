import math
import pygame
import random
import time
import User_Profile

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

pygame.init()
pygame.mixer.init()

# Conectar controll
pygame.joystick.init()
control_conectado = False
controller = None
controller_path = "/dev/input/event0"
if pygame.joystick.get_count() > 0:
    controller = pygame.joystick.Joystick(0)
    controller.init()
    control_conectado = True

# Obtén el tamaño de la pantalla del sistema
screen_info = pygame.display.Info()

# Configuración de la pantalla
largo = screen_info.current_w
alto = screen_info.current_h - 30


# Cargar música de fondo
pygame.mixer.music.load("musica.mp3")
pygame.mixer.music.set_volume(0.7)  # Ajusta el volumen de la música
pygame.mixer.music.play(-1)  # Reproduce la música en bucle


corazon_img = pygame.image.load('Imagenes/Jugador/corazon.png')
fondo = pygame.image.load("Imagenes/Auxiliares/setting_image.png")
laser_sonido = pygame.mixer.Sound("Sonidos/Efectos de sonido/laser.mp3")
laser_sonido_2 = pygame.mixer.Sound("Sonidos/Efectos de sonido/Laser_2.wav")
laser_sonido_3 = pygame.mixer.Sound("Sonidos/Efectos de sonido/Laser_3.mp3")
explosion_sonido = pygame.mixer.Sound("Sonidos/Efectos de sonido/Explosion.wav")
golpe_sonido = pygame.mixer.Sound("Sonidos/Efectos de sonido/Golpe.wav")
propulsores_sonido = pygame.mixer.Sound("Sonidos/Efectos de sonido/Propulsores de nave.mp3")
propulsores_sonido.set_volume(0.25)
vida_extra_activa = pygame.image.load('Imagenes/Auxiliares/vida extra activa.png')
vida_extra_desactiva = pygame.image.load('Imagenes/Auxiliares/vida extra desactivada.png')
puntos_extra_activo = pygame.image.load('Imagenes/Auxiliares/puntos extra activa.png')
puntos_extra_desactivo = pygame.image.load('Imagenes/Auxiliares/puntos extra desactiva.png')
escudo_activo = pygame.image.load('Imagenes/Auxiliares/escudo activo.png')
escudo_desactivo = pygame.image.load('Imagenes/Auxiliares/escudo desactivo.png')
marco_poderes = pygame.image.load('Imagenes/Auxiliares/Marco de poderes.png')
bonus_vida_image = pygame.image.load('Imagenes/Auxiliares/bonus vida.png')
bonus_escudo_image = pygame.image.load('Imagenes/Auxiliares/bonus escudo.png')
bonus_puntos_image = pygame.image.load('Imagenes/Auxiliares/bonus puntos.png')
escudo1_image = pygame.image.load('Imagenes/Auxiliares/escudo1capas.png')
escudo2_image = pygame.image.load('Imagenes/Auxiliares/escudo2capas.png')
escudo3_image = pygame.image.load('Imagenes/Auxiliares/escudo3capas.png')
nave_image = pygame.image.load("Imagenes/Jugador/Nave.png")
aura_image = pygame.image.load("Imagenes/Auxiliares/aura puntos dobles.png")
default_profile_image = "Imagenes/Jugador/PlayerDefault.png"

# Power-up images
power_up_images = [
    bonus_vida_image,
    bonus_puntos_image,
    bonus_escudo_image
]

# Lista de índices para seleccionar imágenes sin repetición
image_indices = list(range(len(power_up_images)))

# Variables globales para los bonus
bonus_escudo = False
bonus_vidas = False
bonus_puntos = False
power_up_puntos_activo = False

# Jugador actual
current_player = None

# Nivel actual
nivel = 1
patron_actual = None
posiciones_enemigos = None

# Pausar juego
pausado = False

def texto_puntuacion(frame, text, size, x, y):
    font = pygame.font.SysFont("Small Fonts", size, bold=True)
    text_frame = font.render(text, True, BLANCO, NEGRO)
    text_rect = text_frame.get_rect()
    text_rect.midtop = (x, y)
    frame.blit(text_frame, text_rect)

def barra_vida(frame, x, y, nivel):
    num_corazones = nivel // 10

    for i in range(num_corazones):
        frame.blit(corazon_img, (i * corazon_img.get_width(), y))

def perfiles_jugadores(win, name1, img1, name2, img2):
    font = pygame.font.Font(None, 36)
    text_frame1 = font.render(name1, True, BLANCO, NEGRO)
    text_rect1 = text_frame1.get_rect()
    text_rect1.midtop = (100, 65)
    image1 = pygame.transform.scale(pygame.image.load(img1), (50, 50))
    win.blit(text_frame1, text_rect1)
    win.blit(image1, (0, 50))

    if name2 != "":
        text_frame2 = font.render(name2, True, BLANCO, NEGRO)
        text_rect2 = text_frame2.get_rect()
        text_rect2.midtop = (screen_info.current_w - 100, 65)
        image2 = pygame.transform.scale(pygame.image.load(img2), (50, 50))

        win.blit(text_frame1, text_rect1)
        win.blit(text_frame2, text_rect2)
        win.blit(image1, (0, 50))
        win.blit(image2, (screen_info.current_w - 200, 50))

    else:
        print("Problema al leer el nombre del segundo jugador...")

def patron_triangular(filas, ancho_fila, max_enemigos=20):
    posiciones = []
    enemigos_generados = 0
    for fila in range(filas):
        for i in range(fila + 1):
            if enemigos_generados < 15:
                x = (screen_info.current_w // 2) - (ancho_fila // 2) * fila + ancho_fila * i
                y = -(fila * 100)
                posiciones.append((x, y))
                enemigos_generados += 1
            else:
                x = (screen_info.current_w // 2) - (ancho_fila // 2) * fila + ancho_fila * (i + 0.5)
                y = -(fila * 100)
                posiciones.append((x, y))
                enemigos_generados += 1

                if enemigos_generados >= max_enemigos:
                    break
        if enemigos_generados >= max_enemigos:
            break
    return posiciones

def patron_onda(max_enemigos):
    posiciones = []
    for i in range(max_enemigos):
        x = i * (screen_info.current_w // max_enemigos)
        y = 200 * math.sin(2 * math.pi * i / max_enemigos)
        posiciones.append((x, y))
    return posiciones

def patron_lluvia(max_enemigos):
    posiciones = []
    for i in range(max_enemigos):
        x = random.randint(50, screen_info.current_w - 100)
        y = random.randint(i * -150, 0)  # Ajusta el rango vertical
        posiciones.append((x, y))
    return posiciones

def patron_espiral(max_enemigos):
    posiciones = []
    for i in range(max_enemigos):
        angle = 2 * math.pi * i / max_enemigos
        radius = 400  # Ajusta el radio de la espiral
        x = (screen_info.current_w - 1000) + radius * math.cos(angle)
        y = -radius * math.sin(angle)
        posiciones.append((x, y))
    return posiciones

def patron_linea_recta(max_enemigos):
    enemigos_generados = 0
    posiciones = []
    for i in range(max_enemigos):
        if enemigos_generados >= 10:
            x = i * (screen_info.current_w // max_enemigos)
            y = -100
            enemigos_generados += 1
            posiciones.append((x, y))
        else:
            x = i * (screen_info.current_w // max_enemigos)
            y = 0
            enemigos_generados += 1
            posiciones.append((x, y))
    return posiciones

class Jugador(pygame.sprite.Sprite):
    global pausado, control_conectado, controller
    def __init__(self, name, ship_img, profile_img):
        super().__init__()
        self.name = name
        self.profile_image = profile_img
        if ship_img == "" or ship_img == None or ship_img == '':
            ship_img = "Imagenes/Jugador/Nave.png"
            self.image = pygame.image.load(ship_img).convert_alpha()
        else:
            self.image = nave_image
        self.color_fondo = self.image.get_at((0, 0))
        self.image.set_colorkey(self.color_fondo)
        pygame.display.set_icon(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = largo // 2
        self.rect.centery = alto - 50
        self.vida = 50
        self.escudo = 0

    def update(self):
        if not pausado:
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
            
            if control_conectado:
                if controller.get_axis(0) < -0.5:
                    self.rect.x -= 50
                    propulsores_sonido.play()
                elif controller.get_axis(0) > 0.5:
                    self.rect.x += 50
                    propulsores_sonido.play()
                elif controller.get_axis(1) < -0.5:
                    self.rect.y -= 50
                    propulsores_sonido.play()
                elif controller.get_axis(1) > 0.5:
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
        laser_sonido.set_volume(0.25)
        laser_sonido.play()

    def activar_escudo(self):
        self.escudo = 3

    def dibujar_escudo(self, frame):
        if self.escudo == 3:
            escudo_image = escudo3_image
        elif self.escudo == 2:
            escudo_image = escudo2_image
        elif self.escudo == 1:
            escudo_image = escudo1_image
        else:
            return  # No dibujar escudo si no hay capas

        escudo_rect = escudo_image.get_rect(center=(self.rect.centerx, self.rect.centery - 30))
        frame.blit(escudo_image, escudo_rect.topleft)

    def dibujar_aura(self, frame, estado):
        if estado:
            aura = aura_image
        else:
            return
        aura_rect = aura.get_rect(center=(self.rect.centerx, self.rect.centery))
        frame.blit(aura, aura_rect.topleft)

    def reiniciar(self):
        self.rect.centerx = largo // 2
        self.rect.centery = alto - 50

class Enemigos(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("Imagenes/Enemigos/enemigo.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.shoot = False
        self.power_shot = False
        self.last_powered_shot_time = 0  # Temporizador para el disparo potenciado

    def mover(self):
        self.rect.y += 5
        if self.rect.top > alto:
            self.rect.y = 0

    def mover_horizontal(self):
        self.rect.x += 10
        if self.rect.left > largo:
            self.rect.x = 0

    def disparo_enemigo(self):
        bala = Balas_enemigos(self.rect.centerx, self.rect.bottom)
        grupo_jugador.add(bala)
        grupo_balas_enemigos.add(bala)
        laser_sonido_2.play()

    def disparo_potenciado(self):
        bala_potenciada = DisparoPotenciado(self.rect.centerx, self.rect.bottom)
        grupo_jugador.add(bala_potenciada)
        grupo_balas_cargadas_enemigos.add(bala_potenciada)
        laser_sonido_3.play()

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
        if self.rect.y > alto:
            self.kill()

class DisparoPotenciado(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("Imagenes/Auxiliares/bala_enemigo_cargada.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.y = y

    def update(self):
        self.rect.y += 25
        if self.rect.y > alto:
            self.kill()

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.y += 10
        if self.rect.top > alto:
            self.kill()

grupo_jugador = pygame.sprite.Group()
grupo_enemigos = pygame.sprite.Group()
grupo_balas_jugador = pygame.sprite.Group()
grupo_balas_enemigos = pygame.sprite.Group()
grupo_balas_cargadas_enemigos = pygame.sprite.Group()
grupo_powerups = pygame.sprite.Group()

def reiniciar_enemigos():
    grupo_enemigos.empty()

def cambiar_nivel():
    global nivel, patron_actual, posiciones_enemigos, image_indices, power_up_images, window, grupo_enemigos, grupo_jugador

    image_indices = list(range(len(power_up_images)))
    grupo_enemigos.empty()
    grupo_jugador.empty()

    if nivel == 1:
        posiciones_enemigos = patron_triangular(6, 200)
    elif nivel == 2:
        posiciones_enemigos = patron_onda(20)
    elif nivel == 3:
        posiciones_enemigos = patron_lluvia(20)
    elif nivel == 4:
        posiciones_enemigos = patron_espiral(20)
    elif nivel == 5:
        posiciones_enemigos = patron_linea_recta(20)

    for pos in posiciones_enemigos:
        enemigo = Enemigos(pos[0], pos[1])
        grupo_enemigos.add(enemigo)
        grupo_jugador.add(enemigo)

# Ciclo del juego
def Game(Player1, Player2):
    global bonus_vidas, bonus_puntos, bonus_escudo, current_player, nivel, patron_actual, posiciones_enemigos, power_up_puntos_activo, window, pausado
    pygame.init()
    window = pygame.display.set_mode((largo, alto), pygame.RESIZABLE)

    play = True
    fps = 10
    clock = pygame.time.Clock()
    score = 0

    pygame.display.set_caption("Galatec")
    pygame.display.set_icon(nave_image)

    players = (Jugador(Player1[0], Player1[1], Player1[2]), Jugador(Player2[0], Player2[1], Player2[2]))
    current_player = players[0]

    cambiar_nivel()

    grupo_jugador.add(current_player)

    coord_list = []
    for i in range(60):
        x = random.randint(0, largo)
        y = random.randint(0, alto)
        coord_list.append([x, y])

    last_power_up_time = time.time()
    power_up_interval = 5
    power_up_start_time = None

    enemigos_que_han_disparado = []
    last_shot_time = 0  # Añadido para rastrear el tiempo del último disparo

    # Lista de enemigos que han disparado el disparo potenciado
    enemigos_que_han_disparado_potenciado = []
    last_power_shot_time = 0

    while play:
        clock.tick(fps)
        current_time = time.time()

        if not pausado:
            if power_up_puntos_activo and (current_time - power_up_start_time >= 15):
                power_up_puntos_activo = False

            if power_up_puntos_activo:
                score_multiplier = 2
            else:
                score_multiplier = 1

            if len(enemigos_que_han_disparado) == len(grupo_enemigos):
                enemigos_que_han_disparado = []

            for enemigo in grupo_enemigos:
                enemigo.mover()
                if patron_actual == "onda" or patron_actual == "recta":
                    enemigo.mover_horizontal()

            if grupo_enemigos and (current_time - last_shot_time >= 2):  # Solo permitir disparar si han pasado 2 segundos
                enemigo_disparo = random.choice([e for e in grupo_enemigos if e not in enemigos_que_han_disparado])
                if not enemigo_disparo.shoot:
                    enemigo_disparo.disparo_enemigo()
                    enemigo_disparo.shoot = True
                    enemigos_que_han_disparado.append(enemigo_disparo)
                    last_shot_time = current_time  # Actualizar el tiempo del último disparo

            # Disparo potenciado cada 5 segundos, asegurando que una sola nave lo haga a la vez
            if grupo_enemigos and (current_time - last_power_shot_time >= 5):  # Solo permitir disparar si han pasado 5 segundos
                enemigo_disparo = random.choice([e for e in grupo_enemigos if e not in enemigos_que_han_disparado_potenciado])
                if not enemigo_disparo.shoot:
                    enemigo_disparo.disparo_potenciado()
                    enemigo_disparo.power_shot = True
                    enemigos_que_han_disparado_potenciado.append(enemigo_disparo)
                    last_power_shot_time = current_time  # Actualizar el tiempo del último disparo

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
            if control_conectado:
                if controller.get_button(4):
                    play = False
                if controller.get_button(6):
                    pausado = not pausado
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pausado = not pausado
            
            if not pausado:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        current_player.disparo_normal()
                    elif event.key == pygame.K_a and bonus_vidas:
                        current_player.vida += 10
                        bonus_vidas = False
                    elif event.key == pygame.K_d and bonus_puntos:
                        power_up_puntos_activo = True
                        power_up_start_time = current_time
                        bonus_puntos = False
                    elif event.key == pygame.K_s and bonus_escudo:
                        current_player.activar_escudo()
                        bonus_escudo = False
                
                # Bonus activados con el control
                if control_conectado:
                    if controller.get_button(0):
                        current_player.disparo_normal()
                    elif controller.get_button(1) and bonus_vidas:
                        current_player.vida += 10
                        bonus_vidas = False
                    elif controller.get_button(2) and bonus_puntos:
                        power_up_puntos_activo = True
                        power_up_start_time = current_time
                        bonus_puntos = False
                    elif controller.get_button(3) and bonus_escudo:
                        current_player.activar_escudo()
                        bonus_escudo = False

        if not pausado:
            grupo_jugador.update()
            grupo_enemigos.update()
            grupo_balas_jugador.update()
            grupo_balas_enemigos.update()
            grupo_balas_cargadas_enemigos.update()
            grupo_powerups.update()

            if current_time - last_power_up_time >= power_up_interval and image_indices:
                index = random.choice(image_indices)
                power_up_image = power_up_images[index]
                power_up = PowerUp(power_up_image, random.randint(0, largo - power_up_image.get_width()), 0)
                grupo_powerups.add(power_up)
                image_indices.remove(index)
                last_power_up_time = current_time

        grupo_jugador.draw(window)
        grupo_enemigos.draw(window)
        grupo_balas_jugador.draw(window)
        grupo_balas_enemigos.draw(window)
        grupo_balas_cargadas_enemigos.draw(window)
        grupo_powerups.draw(window)

        window.blit(marco_poderes, [largo - 207, alto - 60])
        current_player.dibujar_escudo(window)

        current_player.dibujar_aura(window, power_up_puntos_activo)

        if bonus_vidas:
            bonus_vidas_frame = vida_extra_activa
        else:
            bonus_vidas_frame = vida_extra_desactiva

        window.blit(bonus_vidas_frame, [largo - 202, alto - 55])

        if bonus_escudo:
            bonus_escudo_frame = escudo_activo
        else:
            bonus_escudo_frame = escudo_desactivo

        window.blit(bonus_escudo_frame, [largo - 138, alto - 55])

        if bonus_puntos:
            bonus_puntos_frame = puntos_extra_activo
        else:
            bonus_puntos_frame = puntos_extra_desactivo

        window.blit(bonus_puntos_frame, [largo - 74, alto - 55])

        if current_player.vida <= 0:
            if current_player == players[0]:
                current_player = players[1]
            else:
                current_player = players[0]
            current_player.vida = 50
            current_player.rect.centerx = largo // 2
            current_player.rect.centery = alto - 50

            reiniciar_enemigos()

        if len(grupo_enemigos) == 0:
            nivel += 1
            cambiar_nivel()
            current_player.reiniciar()
            current_player = players[1]
            grupo_jugador.add(current_player)

        # Colicion entre balas y enemigos
        colicion1 = pygame.sprite.groupcollide(grupo_enemigos, grupo_balas_jugador, True, True)
        for i in colicion1:
            score += 200 * score_multiplier
            explosion_sonido.play()

        # Colicion entre jugador y balas enemigos
        colicion2 = pygame.sprite.spritecollide(current_player, grupo_balas_enemigos, True)
        for j in colicion2:
            if control_conectado:
                controller.rumble(1, 1, 300)
            if current_player.escudo > 0:
                current_player.escudo -= 1
            else:
                current_player.vida -= 10
            golpe_sonido.play()
            
        # Colicion entre jugador y balas cargadas enemigos
        colicion3 = pygame.sprite.spritecollide(current_player, grupo_balas_cargadas_enemigos, True)
        for j in colicion3:
            if control_conectado:
                controller.rumble(1, 1, 300)
            if current_player.escudo > 1:
                current_player.escudo -= 2
            elif current_player.escudo == 1:
                current_player.escudo == 0
                current_player.vida -= 50
            else:
                current_player.vida -= 50
            golpe_sonido.play()

        # Colicion entre jugador y nave enemiga
        hits = pygame.sprite.spritecollide(current_player, grupo_enemigos, False)
        for hit in hits:
            if control_conectado:
                controller.rumble(1, 1, 300)
            if current_player.escudo > 0:
                current_player.escudo -= 1
                score += 200 * score_multiplier
            else:
                current_player.vida -= 50
                score += 200 * score_multiplier

        # Colicion entre jugador y power ups
        power_up_hits = pygame.sprite.spritecollide(current_player, grupo_powerups, True)
        for power_up_hit in power_up_hits:
            if power_up_hit.image == bonus_vida_image:
                bonus_vidas = True
            elif power_up_hit.image == bonus_puntos_image:
                bonus_puntos = True
            elif power_up_hit.image == bonus_escudo_image:
                bonus_escudo = True

        texto_puntuacion(window, ("SCORE: " + str(score) + " "), 30, largo - 85, 2)
        barra_vida(window, largo - 285, 0, current_player.vida)

        if players[1] != None:
            perfiles_jugadores(window, players[0].name, players[0].profile_image, players[1].name,
                               players[1].profile_image)
        else:
            perfiles_jugadores(window, players[0].name, players[0].profile_image, "", "")

        pygame.display.flip()

    pygame.quit()

Game(("Jugador1", "", default_profile_image), ("Jugador2", "", default_profile_image))
