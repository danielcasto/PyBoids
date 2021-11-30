class Flock:
    def __init__(self, size=0):
        self.boids = []
    
    def draw(self, surface):
        for boid in self.boids:
            boid.draw(surface)

    class Boid:
        def __init__():
            pass
