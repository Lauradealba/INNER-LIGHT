import os
import pygame
from player import Player  
from enemy import Enemigo
from levels import Level 

pygame.init()

# Configuración de la ventana
ANCHO = 800
ALTO = 600
screen = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("INNER LIGHT")

# Cargar imagen de fondo
ruta_base = os.path.dirname(__file__)
ruta_fondo = os.path.abspath(os.path.join(ruta_base, "../assets/bosque1.jpg"))

if os.path.exists(ruta_fondo):
    fondo = pygame.image.load(ruta_fondo)
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))
else:
    print(f"Error: No se encontró {ruta_fondo}")
    pygame.quit()
    exit()

#Niveles 
initial_void = Level("El Vacío Inicial", "vacio.jpg")
forgotten_city = Level("La Ciudad Olvidada", "ciudad.jpg", [Enemigo(300, 500)])
shadow_forest = Level("El Bosque de Sombras", "bosque1.jpg", [Enemigo(200, 500), Enemigo(500, 500)])
final_abyss = Level("El Abismo Final", "abismo.jpg", [Enemigo(400, 500)])

# Lista de niveles en orden
levels = [initial_void, forgotten_city, shadow_forest, final_abyss]

# Iniciar en el primer nivel
current_level_index = 0
current_level = levels[current_level_index]

# Crear al personaje Cristian
cristian = Player(0, ALTO - 150)
sombra = Enemigo(ANCHO // 2 + 200, ALTO - 150)  # Posición inicial del enemigo

# Bucle principal del juego
clock = pygame.time.Clock()
running = True
while running:
    current_level = levels[current_level_index]
    current_level.draw(screen)  # Dibujar el nivel actual


    teclas = pygame.key.get_pressed()  # Detectar teclas presionadas
    cristian.mover(teclas)  # Mover el personaje
    cristian.dibujar(screen)  # Dibujar al personaje

    # 🔹 MOVER DENTRO DEL BUCLE: Verificar si pasa al siguiente nivel
    if cristian.rect.x > 750:  # Si llega al borde derecho de la pantalla
        if current_level_index < len(levels) - 1:  # Si hay un siguiente nivel
            current_level_index += 1  # Cambiar de nivel
            current_level = levels[current_level_index]  # Actualizar nivel actual
            cristian.rect.x = 50  # Cristian reaparece al inicio del nuevo nivel

    sombra.mover()
    sombra.dibujar(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()  # Actualizar la pantalla
    clock.tick(60)  # Limitar a 60 FPS

pygame.quit()
