from circleshape import *
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (125,0,125), self.position, self.radius, SHOT_RADIUS)

    def update(self, dt):
        self.position += self.velocity * dt
        
