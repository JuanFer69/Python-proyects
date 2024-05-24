import pygame
import random

# Inicializar pygame
pygame.init()

# Dimensiones de la pantalla
ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600

# Crear pantalla
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))

# Establecer título e icono
pygame.display.set_caption('Invasion espacial')
icono = pygame.image.load('ovni.png')
pygame.display.set_icon(icono)

# Cargar imagen de fondo
imagen_fondo = pygame.image.load('cielo-estrellado.jpg')

# Definir la variable misiles
misiles = []

# Lista de imágenes de corazones
corazones = ['corazon.gif', 'corazon.gif', 'corazon.gif']

# Función para eliminar el último corazón de la lista
def eliminar_corazon():
    if corazones:
        corazones.pop()

# Variable para almacenar el número de vidas restantes
vidas_restantes = len(corazones)

# Función para reiniciar el estado del juego
def reiniciar_juego():
    global jugador, enemigo

    # Crear instancia de jugador
    jugador = Jugador(368, 500, 'cohete.png')

    # Crear instancia de enemigo dentro de la pantalla
    enemigo = Enemigo('enemigo.png')

class Jugador:
    def __init__(self, x, y, img_path):
        self.img_jugador = pygame.image.load(img_path)
        self.ancho, self.alto = self.img_jugador.get_size()
        self.x = x
        self.y = y
        self.velocidad = 2.5
        self.velocidad_x = 0
        self.velocidad_y = 0

    def actualizar_velocidad(self, teclas_presionadas):
        self.velocidad_x = 0
        self.velocidad_y = 0
        if pygame.K_LEFT in teclas_presionadas:
            self.velocidad_x -= self.velocidad
        if pygame.K_RIGHT in teclas_presionadas:
            self.velocidad_x += self.velocidad
        if pygame.K_UP in teclas_presionadas:
            self.velocidad_y -= self.velocidad
        if pygame.K_DOWN in teclas_presionadas:
            self.velocidad_y += self.velocidad

    def mover(self):
        self.x += self.velocidad_x
        self.y += self.velocidad_y

    def obtener_centro(self):
        centro_x = self.x + self.ancho // 2
        centro_y = self.y + self.alto // 2
        return (centro_x, centro_y)

    def dibujar(self):
        pantalla.blit(self.img_jugador, (self.x, self.y))

class Misil:
    def __init__(self, x, y, img_path):
        self.img_misil = pygame.image.load(img_path)
        self.ancho, self.alto = self.img_misil.get_size()
        self.x = x - self.ancho // 2  # Ajustar posición para que el misil se centre en el jugador
        self.y = y - self.alto // 2
        self.velocidad = 2

    def mover(self):
        self.y -= self.velocidad

    def dibujar(self):
        pantalla.blit(self.img_misil, (self.x, self.y))

class Enemigo:
    def __init__(self, img_path):
        self.img_enemigo = pygame.image.load(img_path)
        self.ancho, self.alto = self.img_enemigo.get_size()
        self.resetear_posicion()

    def resetear_posicion(self):
        self.x = random.randint(0, ANCHO_PANTALLA - self.ancho)
        self.y = random.randint(0, ALTO_PANTALLA // 2)  # Aparece en la parte superior de la pantalla
        self.velocidad = 2
        self.direccion = 1

    def mover(self):
        self.x += self.velocidad * self.direccion
        if self.x <= 0 or self.x >= ANCHO_PANTALLA - self.ancho:
            self.direccion *= -1
            self.y += 10

    def dibujar(self):
        pantalla.blit(self.img_enemigo, (self.x, self.y))

# Crear instancia de jugador
reiniciar_juego()

# Loop del juego
se_ejecuta = True
teclas_presionadas = set()  # Mantener un registro de las teclas presionadas
while se_ejecuta:
    pantalla.fill((0, 0, 0))  # Limpiar la pantalla en cada iteración
    pantalla.blit(imagen_fondo, (0, 0))  # Dibujar el fondo de pantalla

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # Eventos de teclado para movimiento horizontal
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                teclas_presionadas.add(pygame.K_LEFT)
            elif evento.key == pygame.K_RIGHT:
                teclas_presionadas.add(pygame.K_RIGHT)
            if evento.key == pygame.K_UP:
                teclas_presionadas.add(pygame.K_UP)
            elif evento.key == pygame.K_DOWN:
                teclas_presionadas.add(pygame.K_DOWN)
            elif evento.key == pygame.K_SPACE:  # Disparar misil cuando se presiona la tecla de espacio
                centro_jugador = jugador.obtener_centro()  # Obtener el centro del jugador
                misiles.append(Misil(centro_jugador[0], centro_jugador[1], 'misil.png'))

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT:
                teclas_presionadas.discard(pygame.K_LEFT)
            elif evento.key == pygame.K_RIGHT:
                teclas_presionadas.discard(pygame.K_RIGHT)
            if evento.key == pygame.K_UP:
                teclas_presionadas.discard(pygame.K_UP)
            elif evento.key == pygame.K_DOWN:
                teclas_presionadas.discard(pygame.K_DOWN)

    # Actualizar velocidad del jugador
    jugador.actualizar_velocidad(teclas_presionadas)

    # Actualizar posición del jugador
    jugador.mover()
    # Dibujar jugador
    jugador.dibujar()

    # Limitar jugador dentro de los límites de la pantalla
    if jugador.x <= 0:
        jugador.x = 0
    elif jugador.x >= pantalla.get_width() - jugador.ancho:
        jugador.x = pantalla.get_width() - jugador.ancho
    if jugador.y <= 0:
        jugador.y = 0
    elif jugador.y >= pantalla.get_height() - jugador.alto:
        jugador.y = pantalla.get_height() - jugador.alto

    # Mover y dibujar al enemigo
    enemigo.mover()
    enemigo.dibujar()

    # Verificar colisión entre misiles y enemigos
    for misil in misiles:
        if misil.y <= enemigo.y + enemigo.alto and misil.x >= enemigo.x and misil.x <= enemigo.x + enemigo.ancho:
            enemigo.resetear_posicion()
            misiles.remove(misil)

    # Verificar colisión entre enemigo y jugador
    rect_jugador = pygame.Rect(jugador.x, jugador.y, jugador.ancho, jugador.alto)
    rect_enemigo = pygame.Rect(enemigo.x, enemigo.y, enemigo.ancho, enemigo.alto)

    if rect_jugador.colliderect(rect_enemigo):
        eliminar_corazon()
        vidas_restantes = len(corazones)
        if vidas_restantes == 0:
            game_over_img = pygame.image.load('game_over.jpg')
            pantalla.blit(game_over_img, ((ANCHO_PANTALLA - game_over_img.get_width()) / 2, (ALTO_PANTALLA - game_over_img.get_height()) / 2))
            pygame.display.update()
            pygame.time.delay(2000)
            se_ejecuta = False
        else:
            reiniciar_juego()

    # Dibujar corazones
    x_corazon = 10
    y_corazon = 10
    for corazon in corazones:
        corazon_img = pygame.image.load(corazon)
        corazon_img = pygame.transform.scale(corazon_img, (60, 60))  # Redimensionar corazón
        pantalla.blit(corazon_img, (x_corazon, y_corazon))
        x_corazon += corazon_img.get_width() + 5

    # Actualizar posición de los misiles y dibujarlos
    for misil in misiles:
        misil.mover()
        misil.dibujar()

    # Limpiar la lista de misiles cuando salen de la pantalla
    misiles = [misil for misil in misiles if misil.y > 0]

    # Actualizar pantalla
    pygame.display.update()

# Salir de pygame
pygame.quit()
