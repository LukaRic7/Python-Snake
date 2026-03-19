import pygame as pg

from utils.settings import Settings

scr_width, scr_height = Settings.get('window_size').values()

def check_wall_collision(head:pg.Vector2) -> bool:
    """
    **Checks if the snakes head collides with a wall.**
    
    *Parameters*:
    - `head` (pg.Vector2): The snake head cell position.
    
    *Returns*:
    - (bool): Does the snake collide.
    """

    x, y = head.x, head.y
    return x < 0 or x >= scr_width or y < 0 or y >= scr_height

def check_self_collision(body:list[pg.Vector2]) -> bool:
    """
    **Checks if the snake collides with itself.**
    
    *Parameters*:
    - `body` (list[pg.Vector2]): All snake segments.
    
    *Returns*:
    - (bool): Does the snake self-collide.
    """

    head = body[0]
    return head in body[1:]