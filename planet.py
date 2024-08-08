G = 6.6743e-11

class Planet:
    def __init__(self, x = 50, y = 50, velocity = 1, mass = 100, color = (0, 0, 255), max_width = 800, max_height = 600):
        self.x = x
        self.y = y
        self.velocity = velocity
        self.mass = mass
        self.color = color

        self.max_width = max_width
        self.max_height = max_height

    def move(self, x, y):
        self.x += (x * self.velocity * 1000000000000)
        self.y += (y * self.velocity * 1000000000000)

        if self.x < self.mass:
            self.x = self.mass
        if self.y < self.mass:
            self.y = self.mass

        if self.x > self.max_width - self.mass:
            self.x = self.max_width - self.mass
        if self.y > self.max_height - self.mass:
            self.y = self.max_height - self.mass

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
        