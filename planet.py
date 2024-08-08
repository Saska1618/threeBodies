G = 10

class Planet:
    def __init__(self, x = 50, y = 50, velocity_x = 0, velocity_y = 0, mass = 100, color = (0, 0, 255), max_width = 800, max_height = 600):
        self.x = x
        self.y = y
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.mass = mass
        self.color = color

        self.max_width = max_width
        self.max_height = max_height

    def update_position(self, force_x, force_y, dt = 1):

        acceleration_x = force_x / self.mass
        acceleration_y = force_y / self.mass
        

        self.velocity_x += acceleration_x * dt
        self.velocity_y += acceleration_y * dt

        self.x += self.velocity_x
        self.y += self.velocity_y 

        # if self.x < self.mass:
        #     self.x = self.mass
        # if self.y < self.mass:
        #     self.y = self.mass

        # if self.x > self.max_width - self.mass:
        #     self.x = self.max_width - self.mass
        # if self.y > self.max_height - self.mass:
        #     self.y = self.max_height - self.mass

    def get_gravitational_force(self, other_planet):
        distance_x = self.x - other_planet.x
        distance_y = self.y - other_planet.y
        distance = (distance_x**2 + distance_y**2) ** 0.5

        if distance == 0:
            return 0, 0
        
        force = (G * self.mass * other_planet.mass) / (distance ** 2)

        force_x = force * distance_x / distance
        force_y = force * distance_y / distance

        return -force_x, -force_y
        