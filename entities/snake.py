import pygame as pg

from utils.color import darken_rgb

# TODO: Make start_len work

class Snake:
    """
    **Snake instance.**
    
    *Methods*:
    - `head() -> pg.Vector2`: Returns the head position.
    - `move() -> None`: Move the snake one step.
    - `grow() -> None`: Grow the snake one time.
    - `set_direction(new_dir) -> None`: Set a new heading direction for the
    snake.
    """

    def __init__(self, start_pos:tuple[int]=(400, 400), start_len:int=3):
        """
        **Initialization.**
        
        *Parameters*:
        - `start_pos` (tuple[int]): Starting position.
        - `start_len` (int): Starting length.
        """

        self.body = [pg.Vector2(start_pos)]
        self.direction = pg.Vector2(0, -1)  # Up
        self.grow_pending = False

    def head(self) -> pg.Vector2:
        """
        **Return the snake head position**

        *Returns*:
        - (pg.Vector2): Head position of the snake.
        """

        return self.body[0]

    def move(self):
        """
        **Move the snake one step**
        """

        head = self.head()
        new_head = head + self.direction * 40  # Assuming cell size 40
        self.body.insert(0, new_head)
        if not self.grow_pending:
            self.body.pop()
        else:
            self.grow_pending = False

    def grow(self):
        """
        **Grow the snake one time.**
        """

        self.grow_pending = True

    def set_direction(self, new_dir:tuple[int]):
        """
        **Set the new heading direction for the snake.**
        
        *Parameters*:
        - `new_dir` (tuple[int]): The new heading.
        """

        self.direction = pg.Vector2(new_dir)

    # <-----> State Methods <-----> #
    def draw(self, screen:pg.Surface, color:tuple[int]):
        for index, segment in enumerate(self.body):
            pg.draw.rect(screen, darken_rgb(color, min(50, 1 * index)), (segment.x, segment.y, 40, 40))