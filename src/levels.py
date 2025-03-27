import os
import pygame
from enemy import Enemigo  # Importar la clase de los enemigos si los hay


class Level:
    def __init__(self, name, background, enemies=[]):
        self.name = name  # Nombre del nivel
        ruta_base = os.path.dirname(__file__)  # Ruta de este archivo
        self.background = pygame.image.load(os.path.join(ruta_base, f"../assets/{background}"))
        self.background = pygame.transform.scale(self.background, (800, 600))
        self.enemies = enemies  # Lista de enemigos en el nivel

    def draw(self, screen):
        screen.blit(self.background, (0, 0))  # Dibujar el fondo
        for enemy in self.enemies:
            enemy.dibujar(screen)  # Dibujar los enemigos


    def update(self):
        for enemy in self.enemies:
            enemy.move()  # Mover enemigos si hay
