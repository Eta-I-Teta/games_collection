import pygame
import sys
import time

# Инициализация Pygame
pygame.init()

from engine.global_variables import *
from engine.classes.GUI import *

# Настройки окна
screen = pygame.display.set_mode((CONFIG_SCREEN["path_finder"]["width"], CONFIG_SCREEN["end_game"]["height"]))
pygame.display.set_caption(CONFIG_SCREEN["end_game"]["window_name"])
pygame.display.set_icon(pygame.image.load(CONFIG_SCREEN["end_game"]["icon"]))

# Частота кадров
clock = pygame.time.Clock()

# Основной игровой цикл
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Отрисовка
    screen.fill(COLOR["black"])
    MultilineText(sys.argv[1])
    time.sleep(5)
    running = False
    
    # Код отрисовки
    
    pygame.display.flip()
    clock.tick(CONFIG_SCREEN["FPS"])

# Завершение работы
pygame.quit()