from typing import Callable
import loggerric as lr
import pygame as pg

from utils.sound import AudioManager
from utils.settings import Settings

class Button:
    """
    **Creates a simple button for pygame.**
    
    Widens and changes color on hover, changes color on press, has a black
    outline, and calls the callback function when clicked.
    """

    def __init__(
        self, text:str, center_pos:tuple, callback:Callable, font:pg.font.Font,
        padding:int=12, size:tuple=None, bg_color:tuple=None,
        hover_color:tuple=None, text_color:tuple=None, outline:int=3
    ):
        """
        **Initialization.**
        
        *Parameters*:
        - `text` (str): The text label of the button.
        - `center_pos` (tuple): The position of the buttons center.
        - `callback` (Callable): The callback function.
        - `font` (pg.font.Font): Font used for the button label.
        - `padding` (int=12): padding inside the button.
        - `size` (tuple=None): Size of the button (defaults to padding*2).
        - `bg_color` (tuple=None): Color of the button background (defaults to primary accent).
        - `hover_color` (tuple=None): Color of the hovered button (defaults to light accent).
        - `text_color` (tuple=None): Color of the label text (defaults to dark text).
        - `outline` (int=3): Outline thickness of the button.
        """

        # Increase scope
        self.text     = text
        self.callback = callback
        self.font     = font
        self.size     = size or (padding * 2, padding * 2)
        self.padding  = padding
        self.outline  = outline

        # Set colors
        self.colors      = Settings.get('color_palette')
        self.bg_color    = bg_color or self.colors['primary_accent']
        self.hover_color = hover_color or self.colors['light_accent']
        self.text_color  = text_color or self.colors['dark_text']

        # States
        self.hovered          = False
        self.played_hover_sfx = False

        # Graphics
        self.text_surface = self.font.render(text, True, self.text_color)
        self.rect         = pg.Rect(0, 0, *self.size)
        self.rect.center  = center_pos
        self.text_rect    = self.text_surface.get_rect(center=self.rect.center)

        lr.Log.debug('Initializing button:', text)

    # <-----> State Methods <-----> #
    def handle_events(self, events:list[pg.event.Event]):
        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                if self.hovered:
                    self.callback()
                    AudioManager.play('button_click.mp3', 'ui')

    def update(self, mouse_pos:tuple[int, int]):
        self.hovered = self.rect.collidepoint(mouse_pos)

        if not self.hovered and self.played_hover_sfx:
            self.played_hover_sfx = False
        elif self.hovered and not self.played_hover_sfx:
            AudioManager.play('button_hover.mp3', 'ui')
            self.played_hover_sfx = True

        # Figure out the hover scale
        scale = 1.1 if self.hovered else 1
        new_size = (int(self.size[0] * scale), self.size[1])

        # Update button size
        center           = self.rect.center
        self.rect.size   = new_size
        self.rect.center = center
        self.text_rect   = self.text_surface.get_rect(center=self.rect.center)

    def draw(self, screen:pg.Surface):
        color = self.hover_color if self.hovered else self.bg_color

        # Button
        pg.draw.rect(screen, color, self.rect, border_radius=100)
        
        # Outline
        pg.draw.rect(screen, (0, 0, 0), self.rect, width=self.outline, border_radius=100)

        screen.blit(self.text_surface, self.text_rect)