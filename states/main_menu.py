import pygame as pg
from states.base_state import BaseState
from ui.button import Button
 
from states.name_input import NameInput
from states.settings_menu import SettingsMenu
from states.leaderboard_menu import LeaderboardMenu
from ui.background import MouseResponsiveParallexGrid
from utils.settings import Settings

class MainMenu(BaseState):
    def __init__(self, game):
        super().__init__(game)

        self.font = pg.font.SysFont('Verdana', 72, bold=True)
        self.btn_font = pg.font.SysFont('Verdana', 32)

        self.title_color = Settings.get('color_palette', 'primary_accent')
        self.background_color = Settings.get('color_palette', 'background')

        self.screen_width, self.screen_height = Settings.get('window').values()

        self.bg = MouseResponsiveParallexGrid(self.screen_width, self.screen_height, 40, color=Settings.get('color_palette', 'secondary_accent'), max_speed=50)

        self.buttons = [
            Button('Start', (self.screen_width / 2, 250), self.start_game, self.btn_font, size=(self.screen_width / 2.5, 75), bg_color=self.title_color)
        ]

    # Button callbacks

    def start_game(self):
        print('pressed start game')

    def open_settings(self):
        pass

    def open_leaderboard(self):
        pass

    def quit_game(self):
        pg.quit()

    # State methods

    def handle_events(self, events):
        pass

    def update(self, dt):
        mouse_pos = pg.mouse.get_pos()

        self.bg.update(dt, mouse_pos)

    def draw(self, screen):
        screen.fill(self.background_color)

        self.bg.draw(screen)

        title_surface = self.font.render('Snake', True, self.title_color)
        title_rect = title_surface.get_rect(center=(self.screen_width / 2, 120))
        screen.blit(title_surface, title_rect)

        for button in self.buttons:
            button.draw(screen)