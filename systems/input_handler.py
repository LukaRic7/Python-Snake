from collections import deque
import pygame as pg

# Queue snake movements så det ikke føles choppy og shitty
class InputHandler:
    def __init__(self):
        self.queue = deque()

        self.key_map = {
            pg.K_UP: (0, -1),
            pg.K_DOWN: (0, 1),
            pg.K_LEFT: (-1, 0),
            pg.K_RIGHT: (1, 0),
        }

    # Called every frame
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

    # Called at snake move (10fps ish)
    def get_next_direction(self, current_dir):
        if not self.queue:
            return current_dir

        next_dir = self.queue.popleft()

        # extra safety (no reverse)
        if next_dir == (-current_dir[0], -current_dir[1]):
            return current_dir

        return next_dir

    def clear(self):
        self.queue.clear()
