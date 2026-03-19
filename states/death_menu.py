import loggerric as lr
import pygame as pg


from ui.background import ResponsiveParallexGrid
from states.base_state import BaseState
from utils.settings import Settings
from ui.button import Button
from ui.label import Label
from game import Game
from utils.leaderboard import Leaderboard

class DeathMenu(BaseState):
    """
    **Death menu state.**
    
    Handles the death menu screen after game over.
    """

    def __init__(self, game:Game, username:str, score:int):
        """
        **Initialization.**
        
        *Parameters*:
        - `game` (Game): The game to tie the class too.
        - `score` (int): The final score.
        """

        super().__init__(game)

        # Grab settings values
        self.colors = Settings.get('color_palette')
        self.window_size = Settings.get('window_size')

        self.score = score

        # Define fonts
        self.font = pg.font.SysFont('Verdana', 24)

        # Check if new high score
        self.is_high_score = Leaderboard.is_high_score(self.score)
        if self.is_high_score:
            Leaderboard.upsert(username, score)

        # Init responsive background class
        self.background = ResponsiveParallexGrid(cell_size=40, max_speed=50)

        # UI Elements
        center_x = self.window_size['width'] // 2
        center_y = self.window_size['height'] // 2

        self.game_over_label = Label("Game Over", (center_x, center_y - 100), self.font, size=(self.window_size['width'] / 2, 45))
        self.score_label = Label(f"Score: {self.score}", (center_x, center_y - 50), self.font, size=(self.window_size['width'] / 2, 45))
        
        if self.is_high_score:
            self.high_score_label = Label("New High Score!", (center_x, center_y), self.font, size=(self.window_size['width'] / 2, 45))
        else:
            self.high_score_label = None

        self.main_menu_button = Button("Main Menu", (center_x, center_y + 50), self.go_to_main_menu, self.font, size=(self.window_size['width'] / 2, 45))

        lr.Log.debug('Death menu initialized!')

    # <-----> Button Callbacks <-----> #
    def go_to_main_menu(self):
        from states.main_menu import MainMenu
        self.game.change_state(MainMenu(self.game))

    # <-----> State Methods <-----> #
    def handle_events(self, events:list[pg.event.Event]):
        self.main_menu_button.handle_events(events)

    def update(self, delta_time:float):
        mouse_pos = pg.mouse.get_pos()

        self.main_menu_button.update(mouse_pos)

        self.background.update(delta_time, mouse_pos)
    
    def draw(self, screen:pg.Surface):
        screen.fill(self.colors['background'])
        self.background.draw(screen)

        self.game_over_label.draw(screen)
        self.score_label.draw(screen)

        if self.high_score_label:
            self.high_score_label.draw(screen)

        self.main_menu_button.draw(screen)
