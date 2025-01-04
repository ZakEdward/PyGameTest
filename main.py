import pygame
from game import Game

# Инициализация Pygame
pygame.init()

# Определение размеров окна
window_size = (800, 600)

# Запуск игры
if __name__ == "__main__":
    game = Game(window_size)
    game.run()
    pygame.quit()
