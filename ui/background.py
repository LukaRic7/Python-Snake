import pygame as pg

class ParallaxGrid:
    def __init__(self, width, height, cell_size, speed=(0.5, 0.5), color=(50,50,50)):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.color = color
        self.speed_x, self.speed_y = speed

        self.offset_x = 0
        self.offset_y = 0

    def update(self, dt):
        # Move offsets
        self.offset_x += self.speed_x * dt
        self.offset_y += self.speed_y * dt

        # Loop offsets
        self.offset_x %= self.cell_size
        self.offset_y %= self.cell_size

    def draw(self, screen):
        # Draw vertical lines
        x = -self.offset_x
        while x < self.width:
            pg.draw.line(screen, self.color, (x, 0), (x, self.height))
            x += self.cell_size

        # Draw horizontal lines
        y = -self.offset_y
        while y < self.height:
            pg.draw.line(screen, self.color, (0, y), (self.width, y))
            y += self.cell_size

class MouseResponsiveParallexGrid:
    def __init__(self, width, height, cell_size, color=(50,50,50), max_speed=100):
        """
        max_speed: maximum pixels per second when mouse at farthest corner
        """
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.color = color
        self.max_speed = max_speed

        self.offset_x = 0
        self.offset_y = 0

    def update(self, dt, mouse_pos):
        """
        dt: seconds since last frame
        mouse_pos: (x, y) of mouse
        """

        # Compute vector from center
        center_x = self.width / 2
        center_y = self.height / 2

        mx, my = mouse_pos
        dx = (mx - center_x) / center_x  # -1 to 1
        dy = (my - center_y) / center_y  # -1 to 1

        # Compute speed
        speed_x = dx * self.max_speed
        speed_y = dy * self.max_speed

        # Update offsets
        self.offset_x += speed_x * dt
        self.offset_y += speed_y * dt

        # Loop offsets
        self.offset_x %= self.cell_size
        self.offset_y %= self.cell_size

    def draw(self, screen):
        # Draw vertical lines
        x = -self.offset_x
        while x < self.width:
            pg.draw.line(screen, self.color, (x, 0), (x, self.height))
            x += self.cell_size

        # Draw horizontal lines
        y = -self.offset_y
        while y < self.height:
            pg.draw.line(screen, self.color, (0, y), (self.width, y))
            y += self.cell_size
