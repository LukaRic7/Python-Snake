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