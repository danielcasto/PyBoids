from vector import TwoVector
import random

class Flock:
    def __init__(self, window_size, size=0):
        self.boids = []
        self.flocking_area_size = window_size
        for i in range(size):
            self.boids.append(self.Boid(random.randint(1, window_size[0]-1), random.randint(1, window_size[1]-1)))

    def _boid_pos_correction(self, boid):
        # corrects the position of the boid if out of bounds

        if boid.pos.x >= self.flocking_area_size[0]:
            boid.pos.x -= self.flocking_area_size[0]
        elif boid.pos.x <= 0:
            boid.pos.x += self.flocking_area_size[0]
        
        if boid.pos.y >= self.flocking_area_size[0]:
            boid.pos.y -= self.flocking_area_size[0]
        elif boid.pos.y <= 0:
            boid.pos.y += self.flocking_area_size[0]
        
    
    def update(self):
        for primary_boid in self.boids:
            vel_sum_vec = TwoVector()
            pos_sum_vec = TwoVector()
            total_boids = 0 # In radius

            for secondary_boid in self.boids:
                # Separation
                # Alignment
                secondary_vel = secondary_boid.velocity
                # Cohesion
                primary_pos = primary_boid.pos
                secondary_pos = secondary_boid.pos
                from_prim_to_sec_pos = TwoVector(secondary_pos.x-primary_pos.x, secondary_pos.y-primary_pos.y)

                if from_prim_to_sec_pos.norm() < self.Boid.BOID_RADIUS:
                    vel_sum_vec.add(secondary_vel)
                    pos_sum_vec.add(secondary_pos)
                    total_boids += 1
            
            avg_vel = vel_sum_vec
            avg_vel.mult(1/total_boids)
            avg_pos = pos_sum_vec
            avg_pos.mult(1/total_boids)

            # TODO factor in some influence on acceleration
            net_force = TwoVector()
            net_force.add(TwoVector(1 if avg_vel.x >= 0 else -1, 1 if avg_vel.x >= 0 else -1))
            net_force.add(TwoVector(1 if avg_pos.x >= 0 else -1, 1 if avg_pos.x >= 0 else -1))            
            self._boid_pos_correction(primary_boid)
            primary_boid.accel.add(net_force)
            primary_boid.update()

    def draw(self, pygame, surface):
        for boid in self.boids:
            boid.draw(pygame, surface)

    class Boid:
        FILL_COLOR = (255, 255, 255) # white
        BOID_RADIUS = 5
        VISION_RADIUS = 50 # TODO subject to change
        MAX_SPEED = 10

        def __init__(self, pos_x=0, pos_y=0):
            self.pos = TwoVector(pos_x, pos_y)
            self.velocity = TwoVector(random.randint(-1, 1), random.randint(-1,1))
            self.accel = TwoVector() # warning: acceleration is VERY sensitive

        def update(self):
            self.pos.add(self.velocity)
            self.velocity.add(self.accel) # TODO update pos, velocity, and acceleration in flock's update function

            if self.velocity.norm() > self.MAX_SPEED:
                self.velocity.mult(1/self.velocity.norm())

        def draw(self, pygame, surface):
            pygame.draw.circle(surface, self.FILL_COLOR, self.pos.to_tuple(), self.BOID_RADIUS)
