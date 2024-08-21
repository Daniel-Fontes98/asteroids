import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random

class Asteriod(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.radius = radius
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)
        v1 = self.velocity.rotate(random_angle) * 1.2
        v2 = self.velocity.rotate(-1 * random_angle) * 1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        a1 = Asteriod(self.position.x, self.position.y, new_radius)
        a2 = Asteriod(self.position.x, self.position.y, new_radius)
        a1.velocity = v1
        a2.velocity = v2
