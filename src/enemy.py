import pygame
import os

class Enemigo:
    def __init__(self, x, y):
        ruta_base = os.path.dirname(__file__)  
        ruta_imagen = os.path.join(ruta_base, "../assets/sombra.png")  # Imagen del enemigo
        
        if os.path.exists(ruta_imagen):
            self.image = pygame.image.load(ruta_imagen)
            self.image = pygame.transform.scale(self.image, (50, 50))  
        else:
            print(f"Error: No se encontró la imagen {ruta_imagen}")
            self.image = pygame.Surface((50, 50))  # Rectángulo en caso de error
            self.image.fill((255, 0, 0))  # Rojo para indicar error

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def dibujar(self, screen):
        """Dibuja al enemigo en pantalla."""
        screen.blit(self.image, self.rect)

class Enemigo:
    def __init__(self, x, y):
        ruta_base = os.path.dirname(__file__)
        ruta_imagen = os.path.join(ruta_base, "../assets/sombra.png")  # Imagen de la sombra

        # Cargar la imagen del enemigo
        self.image = pygame.image.load(ruta_imagen)
        self.image = pygame.transform.scale(self.image, (150, 150))  # Ajustar tamaño
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        # Variables de movimiento
        self.velocidad = 2  # Velocidad de la sombra
        self.direccion = 1  # 1 para derecha, -1 para izquierda
        self.limite_izq = x - 100  # Límite de movimiento izquierda
        self.limite_der = x + 100  # Límite de movimiento derecha

    def mover(self):
        """La sombra se mueve de un lado a otro entre sus límites."""
        self.rect.x += self.velocidad * self.direccion

        # Cambiar dirección cuando llega a un límite
        if self.rect.x <= self.limite_izq or self.rect.x >= self.limite_der:
            self.direccion *= -1  # Invertir dirección

        # Voltear la imagen cuando cambia de dirección
        if self.direccion == -1:
            self.image = pygame.transform.flip(self.image, True, False)

    def dibujar(self, pantalla):
        """Dibuja la sombra en la pantalla."""
        pantalla.blit(self.image, self.rect)
