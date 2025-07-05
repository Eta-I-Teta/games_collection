import pygame
import os

# Инициализация Pygame
pygame.init()

from engine.global_variables import *
from engine.utilities import *
from engine.classes.GUI import *
from engine.classes.mini_game import *

# Настройки окна
screen = pygame.display.set_mode((CONFIG_SCREEN["main"]["width"], CONFIG_SCREEN["main"]["height"]))
pygame.display.set_caption(CONFIG_SCREEN["main"]["window_name"])
pygame.display.set_icon(pygame.image.load(CONFIG_SCREEN["main"]["icon"]))

# Частота кадров
clock = pygame.time.Clock()

# Игровые переменные
mini_games = [
    MiniGame(
        "Path finder", "path_finder.py",
        "Вам придётся построить путь от начальной клетки, до конечной\n" \
        "Постарайтесь не натыкаться на шипи и правильно используйте телепорты"
    )
]
choosed_game_id = 0

# Основной игровой цикл
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_d:
                if choosed_game_id != len(mini_games) - 1:
                    choosed_game_id += 1
            if event.key == pygame.K_a:
                if choosed_game_id != 0:
                    choosed_game_id -= 1
            if event.key == pygame.K_RETURN:
                run_python_file(mini_games[choosed_game_id].way)
    
    # Обновление игровых объектов
    
    # Отрисовка
    screen.fill(COLOR["black"])

    MultilineText(
        mini_games[choosed_game_id].name
    ).draw(
        screen,
        [CONFIG_SCREEN["font"]["line_spacing"]] * 2
    )
    MultilineText(
        mini_games[choosed_game_id].info
    ).draw(
        screen,
        [
            CONFIG_SCREEN["font"]["line_spacing"],
            CONFIG_SCREEN["font"]["line_spacing"] * 4 + CONFIG_SCREEN["font"]["size"]
        ]
    )

    MultilineText(
        "Enter - запустить игру"
    ).draw(
        screen,
        [
            CONFIG_SCREEN["font"]["line_spacing"],
            CONFIG_SCREEN["main"]["height"] - CONFIG_SCREEN["font"]["size"] - CONFIG_SCREEN["font"]["line_spacing"]
        ]
    )
    
    # Код отрисовки
    
    pygame.display.flip()
    clock.tick(CONFIG_SCREEN["FPS"])

# Завершение работы
pygame.quit()