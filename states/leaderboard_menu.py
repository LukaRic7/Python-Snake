import loggerric as lr
import pygame as pg

from ui.background import ResponsiveParallexGrid
from states.base_state import BaseState
from utils.settings import Settings
from ui.button import Button
from game import Game

class LeaderboardMenu(BaseState):
    """
    **Leaderboard menu state.**
    
    Handles the leaderboard menu screen.
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

        # Init responsive background class
        self.background = ResponsiveParallexGrid(cell_size=40, max_speed=50)

        self.buttons = []

        lr.Log.debug('Leaderboard menu initialized!')

    # <-----> Button Callbacks <-----> #
    def back(self):
        pass

    # <-----> State Methods <-----> #
    def handle_events(self, events:list[pg.event.Event]):
        pass

    def update(self, delta_time:float):
        mouse_pos = pg.mouse.get_pos()

        self.background.update(delta_time, mouse_pos)
    
    def draw(self, screen:pg.Surface):
        # Reset background
        screen.fill(self.colors['background'])
        self.background.draw(screen)