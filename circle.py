import pygame
import random

class Circle:
    def __init__(self, radius, window_size):
        self.radius = radius
        self.window_size = window_size
        self.reset_position()
        self.speed = 5

    def reset_position(self):
        self.position = pygame.math.Vector2(random.randint(self.radius, self.window_size[0] - self.radius),
                                           random.randint(self.radius, self.window_size[1] - self.radius))

    def move(self, direction):
        self.position += direction * self.speed

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 0), (int(self.position.x), int(self.position.y)), self.radius)

    def check_collision(self, triangle):
        for i in range(3):
            p1 = triangle.vertices[i] + triangle.position
            p2 = triangle.vertices[(i + 1) % 3] + triangle.position
            if self.position.distance_to(p1) <= self.radius or self.position.distance_to(p2) <= self.radius:
                return True
        return False
