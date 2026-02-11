import loggerric as lr
import pygame as pg

from states.base_state import BaseState
from utils.settings import Settings
from ui.background import ResponsiveParallexGrid

class NameInput(BaseState):
    def __init__(self, game):
        super().__init__(game)

        # Grab settings values
        self.colors = Settings.get('color_palette')

        # Init plain background class
        self.background = ResponsiveParallexGrid(cell_size=40, max_speed=50)

        self.text = ''

        # testing
        self.font = pg.font.Font(None, 36)
        self.input_box = pg.Rect(100, 100, 400, 40)
        self.color_inactive = pg.Color('gray')
        self.color_active = pg.Color('dodgerblue')
        self.color = self.color_inactive

        lr.Log.debug('Name input menu initialized!')

    # <-----> State Methods <-----> #
    def handle_events(self, events:list[pg.event.Event]):
        # testing
        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN:
                self.active = self.input_box.collidepoint(event.pos)
                self.color = self.color_active if self.active else self.color_inactive
            if event.type == pg.KEYDOWN and self.active:
                if event.key == pg.K_RETURN:
                    print("Entered:", self.text)
                    self.text = ""
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

    def update(self, delta_time:float):
        mouse_pos = pg.mouse.get_pos()

        self.background.update(delta_time, mouse_pos)
    
    def draw(self, screen:pg.Surface):
        # Reset background
        screen.fill(self.colors['background'])
        self.background.draw(screen)

        # testing
        pg.draw.rect(screen, (40, 40, 40), self.input_box)
        pg.draw.rect(screen, self.color, self.input_box, 3)

        txt_surface = self.font.render(self.text, True, (255, 255, 255))
        screen.blit(txt_surface, (self.input_box.x + 5, self.input_box.y + 5))