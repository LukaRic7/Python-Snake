import pygame as pg
import random

class Food:
    """
    **Food instance.**
    
    Creates a food instance the snake can collect.
    
    *Methods*:
    - `respawn(snake_body=None) -> None`: Respawns the food
    """

    def __init__(self, screen_width, screen_height, cell_size):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.cell_size = cell_size
        self.position = pg.Vector2(0, 0)
        self.respawn()

    def respawn(self, snake_body:list[pg.Vector2]=None):
        """
        **Respawn the food on the grid.**
        
        *Parameters*:
        - `snake_body` (list[pg.Vector2]): The snakes body, to avoid spawning
        inside of the snake.
        """

        # Random position on the grid
        cols = self.screen_width // self.cell_size
        rows = self.screen_height // self.cell_size
        
        valid_position = False
        while not valid_position:
            x = random.randint(0, cols - 1) * self.cell_size
            y = random.randint(0, rows - 1) * self.cell_size
            pos = pg.Vector2(x, y)
            
            # Check if position collides with snake
            if snake_body and pos in snake_body:
                continue
            
            self.position = pos
            valid_position = True

    # <-----> State Methods <-----> #
    def draw(self, screen:pg.Surface, color:tuple[int]):
        pg.draw.rect(
            screen, color,
            (self.position.x, self.position.y, self.cell_size, self.cell_size)
        )