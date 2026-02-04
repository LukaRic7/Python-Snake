import pygame as pg
from states.base_state import BaseState
from ui.button import Button

class LeaderboardMenu(BaseState):
    def __init__(self, game):
        super().__init__(game)

        # Settings
        start_y = 250
        spacing = 70

        self.buttons = []

    # Button callbacks

    def back(self):
        pass

    # State methods

    def handle_events(self, events):
        pass

    def update(self):
        pass

    def draw(self, screen):
        pass