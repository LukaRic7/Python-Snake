import loggerric as lr
import pygame as pg

from states.base_state import BaseState
from utils.settings import Settings
from ui.background import Grid
from game import Game

class PlayState(BaseState):
    """
    **Play state menu state.**
    
    Handles the play state menu screen.
    """

    def __init__(self, game:Game):
        """
        **Initialization.**
        
        *Parameters*:
        - `game` (Game): The game to tie the class too.
        """

        super().__init__(game)

        # Grab settings values
        self.colors = Settings.get('color_palette')

        # Init plain background class
        self.background = Grid(cell_size=40)

        lr.Log.debug('Play menu initialized!')

    # <-----> State Methods <-----> #
    def handle_events(self, events:list[pg.event.Event]):
        pass

    def update(self, delta_time:float):
        pass
    
    def draw(self, screen:pg.Surface):
        # Reset background
        screen.fill(self.colors['background'])
        self.background.draw(screen)