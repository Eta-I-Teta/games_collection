import pygame
import sys

from engine.global_variables import *

# Инициализация Pygame
pygame.init()

# Настройки окна
screen = pygame.display.set_mode((CONFIG_SCREEN["main"]["width"], CONFIG_SCREEN["main"]["height"]))
pygame.display.set_caption("Коллекция игр")

# Частота кадров
clock = pygame.time.Clock()

# Основной игровой цикл
def main():
    running = True
    
    while running:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        # Обновление игровой логики
        
        # Отрисовка
        screen.fill(COLOR["black"])
        
        # Здесь будет код отрисовки
        
        pygame.display.flip()
        clock.tick(CONFIG_SCREEN["FPS"])
    
    # Завершение работы
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()