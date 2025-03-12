from circleshape import *
from constants import ASTEROID_MIN_RADIUS
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        print("position: " +  str(self.position))

    def draw(self, screen):
        pygame.draw.circle(screen, (255,0,0), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self, ):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        baby_radius = self.radius - ASTEROID_MIN_RADIUS
        angle = random.uniform(20, 50)
        baby1_velocity = self.velocity.rotate(angle)
        baby2_velocity = self.velocity.rotate(angle * -1)

        baby1 = Asteroid(self.position[0], self.position[1], baby_radius)
        baby2 = Asteroid(self.position[0], self.position[1], baby_radius)
        baby1.velocity = baby1_velocity * 1.2
        baby2.velocity = baby2_velocity * 1.2




        
        

