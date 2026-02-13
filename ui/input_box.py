from typing import Callable
import loggerric as lr
import pygame as pg

from utils.sound import AudioManager
from utils.settings import Settings

class InputBox:
    """
    **Creates a simple inputbox for pygame.**
    
    Changes outline color on focus, waits for enter key press before passing
    text content to the callback function.
    """

    def __init__(
        self, center_pos:tuple, callback:Callable, font:pg.font.Font,
        padding:int=3, size:tuple=None, bg_color:tuple=None,
        hover_color:tuple=None, text_color:tuple=None, outline:int=3,
        outline_selected_color:tuple=None, can_submit:bool=True,
        valid_symbols:str=None
    ):
        """
        **Initialization.**
        
        *Parameters*:
        - `center_pos` (tuple): The position of the buttons center.
        - `callback` (Callable): The callback function.
        - `font` (pg.font.Font): Font used for the button label.
        - `padding` (int=12): padding inside the button.
        - `size` (tuple=None): Size of the button (defaults to padding*2).
        - `bg_color` (tuple=None): Color of the button background (defaults to primary accent).
        - `hover_color` (tuple=None): Color of the hovered button (defaults to light accent).
        - `text_color` (tuple=None): Color of the label text (defaults to dark text).
        - `outline` (int=3): Outline thickness of the button.
        - `outline_selected_color` (tuple=None): Color of the outline when selected (defaults to blue).
        - `can_submit` (bool=True): Weather the user can press enter to submit
        the text content, if this is false, callback won't be called.
        - `valid_symbols` (str=None): Whitelist of symbols that can be entered
        (default is english alphabet, including all capitalized letters)
        """

        # Increase scope
        self.callback      = callback
        self.font          = font
        self.size          = size or (padding * 2, padding * 2)
        self.padding       = padding
        self.outline       = outline
        self.can_submit    = can_submit
        self.valid_symbols = list(valid_symbols or 'abcdefghijklmnopqrstuvwxyz'
                                  + 'abcdefghijklmnopqrstuvwxyz'.upper())

        # Set colors
        self.colors                 = Settings.get('color_palette')
        self.bg_color               = bg_color or self.colors['primary_accent']
        self.hover_color            = hover_color or self.colors['light_accent']
        self.text_color             = text_color or self.colors['dark_text']
        self.selected_outline       = outline_selected_color or self.colors['blue']
        self.outline_color_inactive = '#000000' # Hardcoded cus fuck you

        # States / Values
        self.text             = ''
        self.active           = False
        self.hovered          = False
        self.played_click_sfx = False

        # Graphics
        self.input_box = pg.Rect(*center_pos, *self.size)

        lr.Log.debug('Initialized input box!')

    # <-----> State Methods <-----> #
    def handle_events(self, events:list[pg.event.Event]):
        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN:
                self.active = self.input_box.collidepoint(event.pos)
            if event.type == pg.KEYDOWN and self.active:
                if event.key == pg.K_RETURN and self.can_submit:
                    lr.Log.debug(f'InputBox entered: {self.text}')
                    self.callback(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                    AudioManager.play('key_press.mp3', 'ui')
                elif event.unicode in self.valid_symbols:
                    self.text += event.unicode
                    AudioManager.play('key_press.mp3', 'ui')

    def update(self, mouse_pos:tuple[int, int]):
        self.hovered = self.input_box.collidepoint(mouse_pos)

        if not self.active and self.played_click_sfx:
            self.played_click_sfx = False
        elif self.active and not self.played_click_sfx:
            AudioManager.play('button_hover.mp3', 'ui')
            self.played_click_sfx = True

    def draw(self, screen:pg.Surface):
        outline_color = self.selected_outline if self.active else self.outline_color_inactive
        box_color = self.hover_color if self.hovered or self.active else self.bg_color

        # Box
        pg.draw.rect(screen, box_color, self.input_box, border_radius=100)
        
        # Outline
        pg.draw.rect(screen, outline_color, self.input_box, width=self.outline, border_radius=100)

        # Text
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.input_box.center)
        screen.blit(text_surface, text_rect)