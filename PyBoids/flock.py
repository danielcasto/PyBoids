from vector import TwoVector
import random
import copy

class Flock:
    def __init__(self, window_size, size=0):
        self.boids = []
        self.flocking_area_size = window_size
        for i in range(size):
            self.boids.append(self.Boid(random.randint(1, window_size[0]-1), random.randint(1, window_size[1]-1)))
        
    def _boid_pos_correction(self, boid):
        THRESHOLD = 0
        # corrects the position of the boid if out of bounds

        if boid.pos.x >= self.flocking_area_size[0] - THRESHOLD:
            boid.pos.x -= self.flocking_area_size[0] - THRESHOLD
        elif boid.pos.x <= THRESHOLD:
            boid.pos.x += self.flocking_area_size[0] + THRESHOLD 
        
        if boid.pos.y >= self.flocking_area_size[0] - THRESHOLD:
            boid.pos.y -= self.flocking_area_size[0] - THRESHOLD
        elif boid.pos.y <= THRESHOLD:
            boid.pos.y += self.flocking_area_size[0] + THRESHOLD
        
    
    def update(self):
        for primary_boid in self.boids:
            net_force = TwoVector()
            vel_sum_vec = TwoVector()
            pos_sum_vec = TwoVector()
            opposing_vec_sum = TwoVector()
            total_boids = 0 # In radius

            for secondary_boid in self.boids:
                secondary_vel = secondary_boid.velocity           
                primary_pos = primary_boid.pos
                secondary_pos = secondary_boid.pos
                from_sec_to_prim_pos = TwoVector(primary_pos.x-secondary_pos.x, primary_pos.y-secondary_pos.y)

                if from_sec_to_prim_pos.norm() < self.Boid.VISION_RADIUS:
                    total_boids += 1
                    temp_vec = TwoVector()
                    # Alignment
                    vel_sum_vec.add(secondary_vel)
                    # Cohesion
                    pos_sum_vec.add(secondary_pos)
                    # Separation
                    if from_sec_to_prim_pos.norm() != 0:
                        temp_vec = copy.deepcopy(from_sec_to_prim_pos)
                        temp_vec.mult(1/temp_vec.norm())
                        opposing_vec_sum.add(temp_vec)

            
            avg_vel = copy.deepcopy(vel_sum_vec) 
            avg_vel.mult(1/total_boids)
            avg_pos = copy.deepcopy(pos_sum_vec) 
            avg_pos.mult(1/total_boids)
            avg_opposing = copy.deepcopy(opposing_vec_sum)
            avg_opposing.mult(1/total_boids)
     
            net_force.add(avg_vel)
            net_force.sub(primary_boid.velocity)
            net_force.add(avg_pos)
            net_force.sub(primary_boid.pos)     
            net_force.add(avg_opposing)

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
        MAX_ACCEL_NORM = 5

        def __init__(self, pos_x=0, pos_y=0):
            self.pos = TwoVector(pos_x, pos_y)
            self.velocity = TwoVector(random.randint(-self.MAX_SPEED, self.MAX_SPEED), random.randint(-self.MAX_SPEED,self.MAX_SPEED))
            self.accel = TwoVector() # warning: acceleration is VERY sensitive

        def update(self):
            self.pos.add(self.velocity)
            self.velocity.add(self.accel) # TODO update pos, velocity, and acceleration in flock's update function

            if self.velocity.norm() > self.MAX_SPEED:
                self.velocity.mult((1/self.velocity.norm())*self.MAX_SPEED)

            if self.accel.norm() > self.MAX_ACCEL_NORM:
                self.accel.mult((1/self.accel.norm())*self.MAX_ACCEL_NORM)

        def draw(self, pygame, surface):
            pygame.draw.circle(surface, self.FILL_COLOR, self.pos.to_tuple(), self.BOID_RADIUS)
