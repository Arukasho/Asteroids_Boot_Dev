import pygame
import random
from logger import log_event
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position , self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return ;

        else:
            log = log_event("asteroid_split")
            rand_angle = random.uniform(20, 50)
            rotate_asteroid_1 = self.velocity.rotate(rand_angle)
            rotate_asteroid_2 = self.velocity.rotate(-rand_angle)
            self.radius -= ASTEROID_MIN_RADIUS
            smaller_asteroid_1 = Asteroid(self.position.x, self.position.y, self.radius)
            smaller_asteroid_2 = Asteroid(self.position.x, self.position.y, self.radius)
            smaller_asteroid_1.velocity = rotate_asteroid_1 * 1.2
            smaller_asteroid_2.velocity = rotate_asteroid_2 * 1.2

            

