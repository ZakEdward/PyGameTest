# obstacle.py

import pygame
import random
from obstacles import obstacle_models

class Obstacle:
    def __init__(self, size, window_size):
        self.size = size
        self.window_size = window_size
        self.reset_position()

    def reset_position(self):
        self.model = random.choice(obstacle_models)
        self.position = [random.randint(0, self.window_size[0] - self.size * len(self.model[0])),
                         random.randint(0, self.window_size[1] - self.size * len(self.model))]

    def draw(self, screen):
        for y, row in enumerate(self.model):
            for x, cell in enumerate(row):
                if cell == 1:
                    pygame.draw.rect(screen, (0, 0, 0), (self.position[0] + x * self.size, self.position[1] + y * self.size, self.size, self.size))

    def get_bounding_rect(self):
        return pygame.Rect(self.position[0], self.position[1], self.size * len(self.model[0]), self.size * len(self.model))

    def check_collision(self, other_obstacle):
        return self.get_bounding_rect().colliderect(other_obstacle.get_bounding_rect())
