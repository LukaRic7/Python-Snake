import loggerric as lr
import pygame as pg

from entities.snake import Snake
from entities.food import Food
from systems.input_handler import InputHandler
from systems.collision import check_wall_collision, check_self_collision
from states.base_state import BaseState

class Game:
    """
    **Game instance, owns screen and state.**
    
    *Methods*:
    - `change_state(new_state) -> None`: Change the game state.
    """

    def __init__(self, screen:pg.Surface):
        self.screen          = screen
        self.state:BaseState = None
        self.name:str        = None # Gets set before entering play state

        lr.Log.debug('Game state handler initialized!')

    def change_state(self, new_state:BaseState):
        """
        **Changes the game state.**
        
        *Parameters*:
        - `new_state` (BaseState): New state to change to.
        """
        
        self.state = new_state

        lr.Log.debug('Switched state:', new_state)

    def set_fullscreen(self, fullscreen:bool):
        """**Toggle fullscreen mode.**"""
        if fullscreen:
            info = pg.display.Info()
            self.screen = pg.display.set_mode((info.current_w, info.current_h), pg.FULLSCREEN)
        else:
            w, h = Settings.get('window_size').values()
            self.screen = pg.display.set_mode((w, h))

    # <-----> State Methods <-----> #
    def handle_events(self, events:list[pg.event.Event]):
        pass

    def update(self, delta_time:float):
        pass
    
    def draw(self, screen:pg.Surface):
        pass