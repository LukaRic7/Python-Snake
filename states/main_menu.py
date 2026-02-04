import pygame as pg
from states.base_state import BaseState
from ui.button import Button

from states.name_input import NameInput
from states.settings_menu import SettingsMenu
from states.leaderboard_menu import LeaderboardMenu
from ui.background import ParallaxGrid, MouseResponsiveParallexGrid

class MainMenu(BaseState):
    def __init__(self, game):
        super().__init__(game)

        self.font = pg.font.SysFont("arial", 72, bold=True)

        self.bg = MouseResponsiveParallexGrid(640, 640, 40, color=(0, 200, 0), max_speed=50)

        # Settings
        start_y = 250
        spacing = 70

        self.buttons = [Button("Start", (400, 250), self.start_game, self.font)]

    # Button callbacks

    def start_game(self):
        pass

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
        screen.fill((20, 20, 20))

        self.bg.draw(screen)

        title_surface = self.font.render("total god titel", True, (255, 255, 255))
        title_rect = title_surface.get_rect(center=(400, 120))
        screen.blit(title_surface, title_rect)

        for button in self.buttons:
            button.draw(screen)