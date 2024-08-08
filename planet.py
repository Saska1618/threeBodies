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
        self.x += (x * self.velocity)
        self.y += (y * self.velocity)

        if self.x < self.mass:
            self.x = self.mass
        if self.y < self.mass:
            self.y = self.mass

        if self.x > self.max_width - self.mass:
            self.x = self.max_width - self.mass
        if self.y > self.max_height - self.mass:
            self.y = self.max_height - self.mass
        