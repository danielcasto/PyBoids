from vector import TwoVector
import random

class Flock:
    def __init__(self, window_size, size=0):
        self.boids = []
        
        for i in range(size):
            self.boids.append(self.Boid(random.randint(1, window_size[0]-1), random.randint(1, window_size[1]-1)))
    
    def update(self):
        for boid in self.boids:
            boid.update()

    def draw(self, pygame, surface):
        for boid in self.boids:
            boid.draw(pygame, surface)

    class Boid:
        def __init__(self, pos_x=0, pos_y=0):
            self.fill_color = (255, 255, 255) # white
            self.boid_radius = 5
            self.vision_radius = 30 # TODO subject to change

            self.pos = TwoVector(pos_x, pos_y)
            self.velocity = TwoVector(1, 1)
            self.accel = TwoVector() # warning: acceleration is VERY sensitive

        def update(self):
            self.pos.vec_add(self.velocity)
            self.velocity.vec_add(self.accel) # TODO update pos, velocity, and acceleration in flock's update function
        
        def draw(self, pygame, surface):
            pygame.draw.circle(surface, self.fill_color, self.pos.to_tuple(), self.boid_radius)
