from vector import TwoVector

class Flock:
    def __init__(self, size=0):
        self.boids = []
        
        for i in range(size):
            self.boids.append(self.Boid())
    
    def update(self):
        for boid in self.boids:
            boid.update()

    def draw(self, pygame, surface):
        for boid in self.boids:
            boid.draw(pygame, surface)

    class Boid:
        def __init__(self):
            self.fill_color = (255, 255, 255) # white
            self.boid_radius = 5
            self.vision_radius = 30 # TODO subject to change

            self.pos = TwoVector(0, 0)
            self.velocity = TwoVector(1, 1)
            self.accel = TwoVector() # warning: acceleration is VERY sensitive

        def update(self):
            self.pos.vec_add(self.velocity)
            self.velocity.vec_add(self.accel)
        
        def draw(self, pygame, surface):
            pygame.draw.circle(surface, self.fill_color, self.pos.to_tuple(), self.boid_radius)
