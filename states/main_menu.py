import loggerric as lr
import pygame as pg

from states.base_state import BaseState
from ui.button import Button
from states.name_input import NameInput
from ui.background import ResponsiveParallexGrid
from utils.settings import Settings
from game import Game

class MainMenu(BaseState):
    def __init__(self, game:Game):
        super().__init__(game)

        self.game = game

        # Define fonts
        self.title_font  = pg.font.SysFont('Verdana', 72, bold=True)
        self.button_font = pg.font.SysFont('Verdana', 24)

        # Grab settings values
        self.colors = Settings.get('color_palette')
        self.screen_width, self.screen_height = Settings.get('window_size').values()

        # Init responsive background class
        self.background = ResponsiveParallexGrid(cell_size=40, max_speed=50)

        # Define buttons
        self.buttons:list[Button] = [
            Button(
                text='Start', center_pos=(self.screen_width / 2, 250),
                callback=self.start_game, font=self.button_font,
                size=(self.screen_width / 3, 50)
            ),
            Button(
                text='Leaderboard', center_pos=(self.screen_width / 2, 310),
                callback=self.open_leaderboard, font=self.button_font,
                size=(self.screen_width / 3, 50), bg_color=self.colors['blue'],
                hover_color=self.colors['blue_light']
            ),
            Button(
                text='Settings', center_pos=(self.screen_width / 2, 370),
                callback=self.open_settings, font=self.button_font,
                size=(self.screen_width / 3, 50), bg_color=self.colors['blue'],
                hover_color=self.colors['blue_light']
            ),
            Button(
                text='Quit', center_pos=(self.screen_width / 2, 430),
                callback=self.quit_game, font=self.button_font,
                size=(self.screen_width / 3, 50), bg_color=self.colors['red'],
                hover_color=self.colors['red_light']
            )
        ]

        lr.Log.debug('Main menu initialized!')

    # <-----> Button Callbacks <-----> #
    def start_game(self):
        self.game.change_state(NameInput(self.game))

    def open_settings(self):
        from states.settings_menu import SettingsMenu
        self.game.change_state(SettingsMenu(self.game))

    def open_leaderboard(self):
        from states.leaderboard_menu import LeaderboardMenu
        self.game.change_state(LeaderboardMenu(self.game))

    def quit_game(self):
        pg.quit()

    # <-----> State Methods <-----> #
    def handle_events(self, events:list[pg.event.Event]):
        for button in self.buttons:
            button.handle_event(events)

    def update(self, delta_time:float):
        mouse_pos = pg.mouse.get_pos()

        for button in self.buttons:
            button.update(mouse_pos)

        self.background.update(delta_time, mouse_pos)

    def draw(self, screen:pg.Surface):
        # Reset background
        screen.fill(self.colors['background'])
        self.background.draw(screen)

        # Draw title shadow
        shadow_surface = self.title_font.render('Snake', True, self.colors['primary_accent'])
        shadow_rect = shadow_surface.get_rect(center=(self.screen_width / 2 + 4, 120 + 4))
        screen.blit(shadow_surface, shadow_rect)

        # Draw title text
        title_surface = self.title_font.render('Snake', True, self.colors['light_accent'])
        title_rect = title_surface.get_rect(center=(self.screen_width / 2, 120))
        screen.blit(title_surface, title_rect)

        # Draw buttons
        for button in self.buttons:
            button.draw(screen)