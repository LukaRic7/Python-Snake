import pygame
from states.base_state import BaseState
from ui.button import Button

from states.name_input import NameInput
from states.settings_menu import SettingsMenu
from states.leaderboard_menu import LeaderboardMenu

class MainMenu(BaseState):
    def __init__(self, game):
        super().__init__(game)

        # Settings
        start_y = 250
        spacing = 70

        self.buttons = []

    # Button callbacks

    def start_game(self):
        pass

    def open_settings(self):
        pass

    def open_leaderboard(self):
        pass

    def quit_game(self):
        pygame.quit()

    # State methods

    def handle_events(self, events):
        pass

    def update(self):
        pass

    def draw(self, screen):
        pass