import loggerric as lr
import pygame as pg

from ui.background import ResponsiveParallexGrid
from states.base_state import BaseState
from utils.settings import Settings
from ui.slider import Slider
from ui.button import Button
from game import Game
from utils.sound import AudioManager

class SettingsMenu(BaseState):
    """
    **Settings menu state.**
    
    Handles the settings menu screen.
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
        self.button_font = pg.font.SysFont('Verdana', 24)

        # Grab settings values
        self.colors = Settings.get('color_palette')
        self.screen_width, self.screen_height = Settings.get('window_size').values()

        # Init responsive background class
        self.background = ResponsiveParallexGrid(cell_size=40, max_speed=50)

        self.widgets = {
            "back": Button(
                text='Back', center_pos=(20 + (self.screen_width / 10), self.screen_height - 55),
                callback=self.back, font=self.button_font,
                size=(self.screen_width / 5, 50), bg_color=self.colors['blue'],
                hover_color=self.colors['blue_light']
            ),
            "general_volume": Slider(
                text='General', center_pos=((self.screen_width / 2), 50), font=self.button_font,
                size=(self.screen_width / 2, 50), init_value=Settings.get('sound', 'general')
            ),
            "music_volume": Slider(
                text='Music', center_pos=((self.screen_width / 2), 150), font=self.button_font,
                size=(self.screen_width / 2, 50), init_value=Settings.get('sound', 'music')
            ),
            "sfx_volume": Slider(
                text='Sfx', center_pos=((self.screen_width / 2), 250), font=self.button_font,
                size=(self.screen_width / 2, 50), init_value=Settings.get('sound', 'sfx')
            ),
            "ui_sounds": Slider(
                text='UI Sounds', center_pos=((self.screen_width / 2), 350), font=self.button_font,
                size=(self.screen_width / 2, 50), init_value=Settings.get('sound', 'ui')
            )
        }

        lr.Log.debug('Settings menu initialized!')

    # <-----> Button Callbacks <-----> #
    def back(self):
        Settings.set(AudioManager.volumes['general'], "sound", "general")
        Settings.set(AudioManager.volumes['music'], "sound", "music")
        Settings.set(AudioManager.volumes['sfx'], "sound", "sfx")
        Settings.set(AudioManager.volumes['ui'], "sound", "ui")
        
        from states.main_menu import MainMenu
        self.game.change_state(MainMenu(self.game))

    # <-----> State Methods <-----> #
    def handle_events(self, events:list[pg.event.Event]):
        for button in self.widgets.values():
            button.handle_events(events)

    def update(self, delta_time:float):
        mouse_pos = pg.mouse.get_pos()

        for button in self.widgets.values():
            button.update(mouse_pos)
        
        volume = self.widgets['general_volume'].get_value()
        AudioManager.set_general_volume(volume)

        volume = self.widgets['music_volume'].get_value()
        AudioManager.set_volume('music', volume)

        volume = self.widgets['sfx_volume'].get_value()
        AudioManager.set_volume('sfx', volume)

        volume = self.widgets['ui_sounds'].get_value()
        AudioManager.set_volume('ui', volume)

        self.background.update(delta_time, mouse_pos)
    
    def draw(self, screen:pg.Surface):
        # Reset background
        screen.fill(self.colors['background'])
        self.background.draw(screen)

        # Draw buttons
        for button in self.widgets.values():
            button.draw(screen)