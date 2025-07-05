import pygame
import os

# Инициализация Pygame
pygame.init()

from engine.global_variables import *
from engine.classes.GUI import *
from engine.classes.path_finder import *

# Настройки окна
screen = pygame.display.set_mode((CONFIG_SCREEN["path_finder"]["width"], CONFIG_SCREEN["path_finder"]["height"]))
pygame.display.set_caption(CONFIG_SCREEN["path_finder"]["window_name"])
pygame.display.set_icon(pygame.image.load(CONFIG_SCREEN["main"]["icon"]))

# Частота кадров
clock = pygame.time.Clock()

# Основной игровой цикл
from data.levels.path_finder.level_1 import *
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if (event.key == pygame.K_w) and (LEVEL.get_player().moving == False) and ([0, -1] in LEVEL.get_directions()):
                LEVEL.move([0, -1])
            if (event.key == pygame.K_a) and (LEVEL.get_player().moving == False) and ([-1, 0] in LEVEL.get_directions()):
                LEVEL.move([-1, 0])
            if (event.key == pygame.K_s) and (LEVEL.get_player().moving == False) and ([0, 1] in LEVEL.get_directions()):
                LEVEL.move([0, 1])
            if (event.key == pygame.K_d) and (LEVEL.get_player().moving == False) and ([1, 0] in LEVEL.get_directions()):
                LEVEL.move([1, 0])
    
    # Обновление игровых объектов
    LEVEL.move()

    # Отрисовка
    screen.fill(COLOR["black"])
    LEVEL.draw(screen)
    
    # Код отрисовки
    
    pygame.display.flip()
    clock.tick(CONFIG_SCREEN["FPS"])

# Завершение работы
pygame.quit()