import os
import pygame

class Player:
    def __init__(self, x, y):
        ruta_base = os.path.dirname(__file__)

        # Cargar imágenes
        self.imagen_idle = pygame.image.load(os.path.join(ruta_base, "../assets/cristian.png"))
        self.imagen_walk1 = pygame.image.load(os.path.join(ruta_base, "../assets/cristian1.png"))
        self.imagen_walk2 = pygame.image.load(os.path.join(ruta_base, "../assets/cristian2.png"))

        # Ajustar tamaño de las imágenes
        self.imagen_idle = pygame.transform.scale(self.imagen_idle, (150, 150))
        self.imagen_walk1 = pygame.transform.scale(self.imagen_walk1, (150, 150))
        self.imagen_walk2 = pygame.transform.scale(self.imagen_walk2, (150, 150))

        # Lista de animación para caminar
        self.animacion_caminando = [self.imagen_walk1, self.imagen_walk2]
        self.image = self.imagen_idle  # Imagen inicial

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        # Variables de movimiento
        self.velocidad = 4  
        self.contador_pasos = 0  # Para alternar la animación
        self.direccion = "derecha"  # Para saber hacia dónde está mirando

        # Variables para el salto
        self.velocidad_y = 0
        self.gravedad = 1  # Hace que caiga después de saltar
        self.saltando = False  # Saber si está en el aire
        self.salto_potencia = -15  # Fuerza del salto
        self.suelo = y  # Nivel del suelo

    def mover(self, teclas):
        moviendose = False  

        # Movimiento lateral
        if teclas[pygame.K_LEFT]:  
            self.rect.x -= self.velocidad
            self.direccion = "izquierda"
            moviendose = True

        if teclas[pygame.K_RIGHT]:  
            self.rect.x += self.velocidad
            self.direccion = "derecha"
            moviendose = True

        # Salto
        if teclas[pygame.K_SPACE] and not self.saltando:  # Solo puede saltar si no está en el aire
            self.saltando = True
            self.velocidad_y = self.salto_potencia  # Aplica la fuerza del salto

        # Aplicar gravedad
        self.velocidad_y += self.gravedad  # Aumenta la velocidad hacia abajo
        self.rect.y += self.velocidad_y  # Modifica la posición en Y

        # Evitar que caiga más del suelo
        if self.rect.y >= self.suelo:
            self.rect.y = self.suelo
            self.saltando = False  # Puede volver a saltar

        # Animación de caminar
        if moviendose:
            self.contador_pasos += 1
            if self.contador_pasos >= 10:
                self.contador_pasos = 0
            self.image = self.animacion_caminando[self.contador_pasos // 5]
        else:
            self.image = self.imagen_idle  # Si no se mueve, usa la imagen normal

        # Si está mirando a la izquierda, voltea la imagen
        if self.direccion == "izquierda":
            self.image = pygame.transform.flip(self.image, True, False)

    def dibujar(self, pantalla):
        pantalla.blit(self.image, self.rect)
