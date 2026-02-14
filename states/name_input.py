import loggerric as lr
import pygame as pg

from states.base_state import BaseState
from utils.settings import Settings
from states.play_state import PlayState
from ui.background import ResponsiveParallexGrid
from ui.input_box import InputBox
from ui.button import Button
from game import Game

class NameInput(BaseState):
    def __init__(self, game:Game):
        super().__init__(game)

        self.game = game

        # Grab settings values
        self.colors = Settings.get('color_palette')
        self.scr_width, self.scr_height = Settings.get('window_size').values()

        # Init plain background class
        self.background = ResponsiveParallexGrid(cell_size=40, max_speed=50)

        # Font
        self.font = pg.font.SysFont('Verdana', 24)

        # Controls
        self.input_box = InputBox(
            (100, 100), self.input_callback, self.font, size=(400, 50),
            can_submit=False
        )
        self.confirm_button = Button(
            text='Confirm', center_pos=(self.scr_width / 2, 250),
            callback=self.confirm_callback, font=self.font,
            size=(self.scr_width / 3, 50)
        )

        self.text:str = '' # Sat by the input callback

        lr.Log.debug('Name input menu initialized!')

    # <-----> Control Callbacks <-----> #
    def input_callback(self, text:str):
        self.text = text

    def confirm_callback(self):
        if not self.text.replace(' ', ''):
            self.text = 'Unknown Player'

        self.game.name = self.text
        self.game.change_state(PlayState(self.game))

    # <-----> State Methods <-----> #
    def handle_events(self, events:list[pg.event.Event]):
        self.input_box.handle_events(events)
        self.confirm_button.handle_events(events)

    def update(self, delta_time:float):
        mouse_pos = pg.mouse.get_pos()

        self.input_box.update(mouse_pos)
        self.confirm_button.update(mouse_pos)

        self.background.update(delta_time, mouse_pos)
    
    def draw(self, screen:pg.Surface):
        # Reset background
        screen.fill(self.colors['background'])
        self.background.draw(screen)

        # Inputbox
        self.input_box.draw(screen)

        # Button
        self.confirm_button.draw(screen)