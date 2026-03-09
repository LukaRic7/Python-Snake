import loggerric as lr
import pygame as pg

from ui.background import ResponsiveParallexGrid
from utils.leaderboard import Leaderboard
from states.base_state import BaseState
from utils.settings import Settings
from ui.button import Button
from ui.label import Label
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

        self.game = game

        # Define fonts
        self.font = pg.font.SysFont('Verdana', 24)

        # Grab settings values
        self.colors = Settings.get('color_palette')
        self.screen_width, self.screen_height = Settings.get('window_size').values()

        # Init responsive background class
        self.background = ResponsiveParallexGrid(cell_size=40, max_speed=50)

        # Populate labels
        self.labels:list[Label] = []
        for index, (name, score) in enumerate(Leaderboard.get().items()):
            if index == 10: break # Only show top 10
            
            self.labels.append(Label(
                f'#{index + 1}', ((self.screen_width / 2) - 230, 50 + (index * 50)),
                font=self.font, size=(80, 45)
            ))
            self.labels.append(Label(
                name, ((self.screen_width / 2) - 30, 50 + (index * 50)),
                font=self.font, size=(300, 45)
            ))
            self.labels.append(Label(
                f'{score} P', ((self.screen_width / 2) + 200, 50 + (index * 50)),
                font=self.font, size=(150, 45)
            ))

        self.buttons = [
            Button(
                text='Back', center_pos=(20 + (self.screen_width / 10), self.screen_height - 55),
                callback=self.back, font=self.font,
                size=(self.screen_width / 5, 50), bg_color=self.colors['blue'],
                hover_color=self.colors['blue_light']
            )
        ]

        lr.Log.debug('Leaderboard menu initialized!')

    # <-----> Button Callbacks <-----> #
    def back(self):
        from states.main_menu import MainMenu
        self.game.change_state(MainMenu(self.game))

    # <-----> State Methods <-----> #
    def handle_events(self, events:list[pg.event.Event]):
        for button in self.buttons:
            button.handle_events(events)

    def update(self, delta_time:float):
        mouse_pos = pg.mouse.get_pos()

        for button in self.buttons:
            button.update(mouse_pos)

        self.background.update(delta_time, mouse_pos)
    
    def draw(self, screen:pg.Surface):
        # Reset background
        screen.fill(self.colors['background'])
        self.background.draw(screen)

        # Draw buttons
        for button in self.buttons:
            button.draw(screen)

        # Draw labels
        for label in self.labels:
            label.draw(screen)