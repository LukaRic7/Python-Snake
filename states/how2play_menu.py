import loggerric as lr
import pygame as pg

from ui.background import ResponsiveParallexGrid
from states.base_state import BaseState
from utils.settings import Settings
from ui.button import Button
from game import Game
from ui.label import Label

class How2Play(BaseState):
    """
    **How to play menu state.**
    
    Handles the instructions menu screen.
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
        self.scr_width, self.scr_height = Settings.get('window_size').values()

        # Init responsive background class
        self.background = ResponsiveParallexGrid(cell_size=40, max_speed=50)

        self.widgets = {
            "back": Button(
                text='Back',
                center_pos=(20 + (self.scr_width / 10), self.scr_height - 55),
                callback=self.back, font=self.button_font,
                size=(self.scr_width / 5, 50), bg_color=self.colors['blue'],
                hover_color=self.colors['blue_light']
            ),
            "instructions": Label(
                text=("""Use wasd or the arrow keys to move
                      \nthe snake around and eat the apples!
                      \nAvoid running into yourself or the walls!
                      \nThe snakes size grows with each apple consumed,
                      \neat apples to increase your score! 
                      \nClimb the leaderboard and edge your place
                      \nas the best snaker in the world!"""),
                center_pos=(self.scr_width / 2, self.scr_height / 2),
                font=self.button_font, size=(self.scr_width / 1.5, self.scr_height / 2)
            
             )
        }
        lr.Log.debug('Instructions menu initialized!')

    # <-----> Button Callbacks <-----> #
    def back(self):
        """
        **Return back to the main menu.**
        """

        from states.main_menu import MainMenu
        self.game.change_state(MainMenu(self.game))

    # <-----> State Methods <-----> #
    def handle_events(self, events:list[pg.event.Event]):
        for widget in self.widgets.values():
            try:
                widget.handle_events(events)
            except Exception: pass

    def update(self, delta_time:float):
        mouse_pos = pg.mouse.get_pos()
        
        for widget in self.widgets.values():
            widget.update(mouse_pos)

        self.background.update(delta_time, mouse_pos)
    
    def draw(self, screen:pg.Surface):
        # Reset background
        screen.fill(self.colors['background'])
        self.background.draw(screen)

        for widget in self.widgets.values():
            widget.draw(screen)

