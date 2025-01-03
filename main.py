import pygame
import sys

# Инициализация Pygame
pygame.init()

# Определение размеров окна
window_size = (800, 600)

# Создание окна
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Окно с квадратом")

# Определение цветов
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Определение размеров и начальной позиции квадрата
square_size = 30
square_position = [window_size[0] // 2 - square_size // 2, window_size[1] // 2 - square_size // 2]

# Скорость движения квадрата
speed = 5

# Функция для перемещения квадрата в центр
def reset_square_position():
    square_position[0] = window_size[0] // 2 - square_size // 2
    square_position[1] = window_size[1] // 2 - square_size // 2

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Получение состояния клавиш
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        square_position[1] -= speed
    if keys[pygame.K_s]:
        square_position[1] += speed
    if keys[pygame.K_a]:
        square_position[0] -= speed
    if keys[pygame.K_d]:
        square_position[0] += speed

    # Проверка столкновений с границами окна
    if (square_position[0] < 0 or square_position[0] + square_size > window_size[0] or
        square_position[1] < 0 or square_position[1] + square_size > window_size[1]):
        reset_square_position()

    # Заполнение окна белым цветом
    screen.fill(white)

    # Рисование границ окна
    pygame.draw.rect(screen, red, (0, 0, window_size[0], window_size[1]), 5)

    # Рисование квадрата
    pygame.draw.rect(screen, black, (*square_position, square_size, square_size))

    # Обновление экрана
    pygame.display.flip()

    # Ограничение частоты кадров
    pygame.time.Clock().tick(60)

# Завершение работы Pygame
pygame.quit()
sys.exit()
