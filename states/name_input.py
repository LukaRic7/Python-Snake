import loggerric as lr
import pygame as pg

from states.base_state import BaseState
from utils.settings import Settings
from ui.background import ResponsiveParallexGrid
from ui.input_box import InputBox

class NameInput(BaseState):
    def __init__(self, game):
        super().__init__(game)

        # Grab settings values
        self.colors = Settings.get('color_palette')

        # Init plain background class
        self.background = ResponsiveParallexGrid(cell_size=40, max_speed=50)

        # Font
        self.font = pg.font.SysFont('Verdana', 24)

        # Controls
        self.input_box = InputBox(
            (100, 100), self.input_callback, self.font, size=(400, 50),
            can_submit=False
        )

        lr.Log.debug('Name input menu initialized!')

    # <-----> Input Callback <-----> #
    def input_callback(self, text:str):
        print(text)

    # <-----> State Methods <-----> #
    def handle_events(self, events:list[pg.event.Event]):
        self.input_box.handle_events(events)

    def update(self, delta_time:float):
        mouse_pos = pg.mouse.get_pos()

        self.input_box.update(mouse_pos)

        self.background.update(delta_time, mouse_pos)
    
    def draw(self, screen:pg.Surface):
        # Reset background
        screen.fill(self.colors['background'])
        self.background.draw(screen)

        # Inputbox
        self.input_box.draw(screen)