# game.py

import pygame
import sys
import random
from obstacle import Obstacle
from triangle import Triangle
from circle import Circle

class Game:
    def __init__(self, window_size):
        self.window_size = window_size
        self.screen = pygame.display.set_mode(window_size)
        pygame.display.set_caption("Окно с треугольником и препятствиями")
        self.obstacles = self.create_obstacles()
        self.triangle = Triangle(
            [pygame.math.Vector2(0, 0), pygame.math.Vector2(25, 0), pygame.math.Vector2(12.5, 25)],
            pygame.math.Vector2(200, 200),
            5,
            window_size
        )
        self.circle = Circle(25, window_size)
        self.running = True

    def create_obstacles(self):
        num_obstacles = random.randint(1, 5)
        obstacles = []
        for _ in range(num_obstacles):
            while True:
                new_obstacle = Obstacle(20, self.window_size)
                if not any(new_obstacle.check_collision(obstacle) for obstacle in obstacles):
                    obstacles.append(new_obstacle)
                    break
        return obstacles

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def update(self):
        keys = pygame.key.get_pressed()
        self.triangle.move(keys)

        if (self.triangle.position.x < 0 or self.triangle.position.x > self.window_size[0] or
            self.triangle.position.y < 0 or self.triangle.position.y > self.window_size[1]):
            self.triangle.reset_position()
            self.obstacles = self.create_obstacles()

        if self.triangle.check_collision(self.obstacles):
            self.triangle.reset_position()
            self.obstacles = self.create_obstacles()

        if self.circle.check_collision(self.triangle):
            direction = (self.circle.position - self.triangle.position).normalize()
            self.circle.move(-direction)

    def draw(self):
        self.screen.fill((255, 255, 255))
        pygame.draw.rect(self.screen, (255, 0, 0), (0, 0, self.window_size[0], self.window_size[1]), 5)
        for obstacle in self.obstacles:
            obstacle.draw(self.screen)
        self.triangle.draw(self.screen)
        self.circle.draw(self.screen)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            pygame.time.Clock().tick(60)
