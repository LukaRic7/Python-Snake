import pygame as pg

from utils.settings import Settings

class ResponsiveParallexGrid:
    def __init__(
            self, cell_size:int, width:int=None, height:int=None,
            color:tuple=None, max_speed:float=100
        ):

        self.width     = width or Settings.get('window_size', 'width')
        self.height    = height or Settings.get('window_size', 'height')
        self.color     = color or Settings.get('color_palette', 'secondary_accent')
        self.cell_size = cell_size
        self.max_speed = max_speed

        self.offset_x = 0
        self.offset_y = 0

    def update(self, delta_time:float, mouse_pos:tuple[int, int]):
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
        self.offset_x += speed_x * delta_time
        self.offset_y += speed_y * delta_time

        # Loop offsets
        self.offset_x %= self.cell_size
        self.offset_y %= self.cell_size

    def draw(self, screen:pg.Surface):
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

class Grid:
    def __init__(
            self, cell_size:int, width:int=None, height:int=None,
            color:tuple=None
        ):

        self.width     = width or Settings.get('window_size', 'width')
        self.height    = height or Settings.get('window_size', 'height')
        self.color     = color or Settings.get('color_palette', 'secondary_accent')
        self.cell_size = cell_size

    def draw(self, screen:pg.Surface):
        # Draw vertical lines
        while x < self.width:
            pg.draw.line(screen, self.color, (x, 0), (x, self.height))
            x += self.cell_size

        # Draw horizontal lines
        while y < self.height:
            pg.draw.line(screen, self.color, (0, y), (self.width, y))
            y += self.cell_size
