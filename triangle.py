import pygame

class Triangle:
    def __init__(self, vertices, position, speed, window_size):
        self.vertices = vertices
        self.position = position
        self.speed = speed
        self.window_size = window_size

    def reset_position(self):
        self.position = pygame.math.Vector2(self.window_size[0] - 25, self.window_size[1] - 25)

    def move(self, keys):
        if keys[pygame.K_w]:
            self.position.y -= self.speed
        if keys[pygame.K_s]:
            self.position.y += self.speed
        if keys[pygame.K_a]:
            self.position.x -= self.speed
        if keys[pygame.K_d]:
            self.position.x += self.speed

    def draw(self, screen):
        triangle_points = [(int(v.x + self.position.x), int(v.y + self.position.y)) for v in self.vertices]
        pygame.draw.polygon(screen, (0, 0, 255), triangle_points)

    def check_collision(self, obstacles):
        for obstacle in obstacles:
            for y, row in enumerate(obstacle.model):
                for x, cell in enumerate(row):
                    if cell == 1:
                        square_rect = pygame.Rect(obstacle.position[0] + x * obstacle.size,
                                                 obstacle.position[1] + y * obstacle.size,
                                                 obstacle.size, obstacle.size)
                        for i in range(3):
                            p1 = self.vertices[i] + self.position
                            p2 = self.vertices[(i + 1) % 3] + self.position
                            if square_rect.clipline(p1, p2):
                                return True
        return False
