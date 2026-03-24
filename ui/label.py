import loggerric as lr
import pygame as pg

from utils.settings import Settings

class Label:
    """
    **Create a label widget using pygame.**
    
    Supports multiline functionality.
    
    *Methods*:
    - `set_text(text:str) -> None`: Set the text of the label.
    """

    def __init__(
        self, text:str, center_pos:tuple, font:pg.font.Font,
        padding:int=12, size:tuple=None, bg_color:tuple=None,
        text_color:tuple=None, outline:int=3, outline_color:tuple=None
    ):
        """
        **Initialization.**
        
        *Parameters*:
        - `text` (str): The text that should be displayed.
        - `center_pos` (tuple): Center position of the widget.
        - `font` (pg.font.Font): Font that should be used.
        - `padding` (int=12): Padding the button should use.
        - `size` (tuple=None): Size of the label.
        - `bg_color` (tuple=None): Background color of the label.
        - `text_color` (tuple=None): Color of the text.
        - `outline` (int=3): Outline thickness.
        - `outline_color` (tuple=None): Color of the outline.
        """

        # Increase scope
        self.text    = text
        self.font    = font
        self.size    = size or (padding * 2, padding * 2)
        self.padding = padding
        self.outline = outline

        # Set colors
        self.colors      = Settings.get('color_palette')
        self.bg_color    = bg_color or self.colors['primary_accent']
        self.text_color  = text_color or self.colors['dark_text']
        self.outline_color = outline_color or self.colors['secondary_accent']

        # Graphics
        self.text_surface = self.font.render(text, True, self.text_color)
        self.rect         = pg.Rect(0, 0, *self.size)
        self.rect.center  = center_pos
        self.text_rect    = self.text_surface.get_rect(center=self.rect.center)

        lr.Log.debug(
            'Initialized label:', f'{text[0:7]}...' if len(text) > 10 else text
        )

    def set_text(self, text:str):
        """
        **Set the text of the widget.**
        
        *Parameters*:
        - `text` (str): The text that should be displayed.
        """

        self.text_surface = self.font.render(text, True, self.text_color)

    # <-----> State Methods <-----> #
    def update(self, mouse_pos:tuple[int, int]):
        pass

    def draw(self, screen:pg.Surface):
        pg.draw.rect(screen, self.bg_color, self.rect, border_radius=10)

        pg.draw.rect(
            screen, (0, 0, 0), self.rect, width=self.outline, border_radius=10
        )

        screen.blit(self.text_surface, self.text_rect)