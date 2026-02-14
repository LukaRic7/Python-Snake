import pygame as pg

from utils.settings import Settings

class ResponsiveParallexGrid:
    """
    **creates a responsive parallex grid for pygame.**
    
    A mouse responsive paralelex grid that moves away from the mouse.
    """

    def __init__(
            self, cell_size:int, width:int=None, height:int=None,
            color:tuple=None, max_speed:float=100
        ):
        """
        **Initialization.**
        
        *Parameters*:
        - `cell_size` (int): Pixel size of the grid.
        - `width` (int=None): Width of the entire grid (defaults to window width).
        - `height` (int=None): Height of the entire grid (defaults to window height).
        - `color` (tuple=None): Color of the grid lines (defaults to secondary accent).
        - `max_speed` (float=100): Max moving speed for the grid.
        """

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
    """
    **Creates a grid for pygame.**
    """

    def __init__(
            self, cell_size:int, width:int=None, height:int=None,
            color:tuple=None
        ):
        """
        **Initialization.**
        
        *Parameters*:
        - `cell_size` (int): Size of each cell in pixels.
        - `width` (int=None): Width of the entire grid (defaults to window width).
        - `height` (int=None): Height of the entire grid (defaults to window height).
        - `color` (tuple=None): Color of the grid (defaults to secondary accent).
        """

        self.width     = width or Settings.get('window_size', 'width')
        self.height    = height or Settings.get('window_size', 'height')
        self.color     = color or Settings.get('color_palette', 'secondary_accent')
        self.cell_size = cell_size

    def draw(self, screen:pg.Surface):
        x = 0
        y = 0

        # Draw vertical lines
        while x < self.width:
            pg.draw.line(screen, self.color, (x, 0), (x, self.height))
            x += self.cell_size

        # Draw horizontal lines
        while y < self.height:
            pg.draw.line(screen, self.color, (0, y), (self.width, y))
            y += self.cell_size
