from collections import deque
import pygame as pg

class InputHandler:
    """
    **Handles input from the player.**
    
    *Methods*:
    - `get_next_direction(current_dir) -> tuple[int]`: Direction to move.
    - `clear() -> None`: Clear the queue.
    """

    def __init__(self):
        self.queue = deque(maxlen=3)

        self.key_map = {
            pg.K_UP: (0, -1),
            pg.K_DOWN: (0, 1),
            pg.K_LEFT: (-1, 0),
            pg.K_RIGHT: (1, 0),
        }

    # Called at snake move (10fps ish)
    def get_next_direction(self, current_dir:tuple[int]) -> tuple[int]:
        """
        **Get the next direction in the queue.**

        Makes sure the snake can't reverse.
        
        *Parameters*:
        - `current_dir` (tuple[int]): Current heading direction.
        
        *Returns*:
        - (tuple[int]): The next direction heading.
        """

        if not self.queue:
            return current_dir

        next_dir = self.queue.popleft()

        # Make sure the snake cant reverse
        if next_dir == (-current_dir[0], -current_dir[1]):
            return current_dir

        return next_dir

    def clear(self):
        """
        **Clear the queue.**
        """

        self.queue.clear()

    # <-----> State Methods <-----> #
    def handle_event(self, event, snake):
        if event.type != pg.KEYDOWN:
            return

        if event.key not in self.key_map:
            return

        new_dir = self.key_map[event.key]

        # Prevent reverse direction
        current = snake.direction
        opposite = (-current[0], -current[1])

        if new_dir == opposite:
            return

        # Prevent duplicates (spam)
        if len(self.queue) == 0 or self.queue[-1] != new_dir:
            self.queue.append(new_dir)