import loggerric as lr
import pygame as pg

from utils.settings import Settings

class Label:
    def __init__(
        self, text:str, center_pos:tuple, font:pg.font.Font,
        padding:int=12, size:tuple=None, bg_color:tuple=None,
        text_color:tuple=None, outline:int=3, outline_color:tuple=None
    ):
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

        lr.Log.debug('Initialized label:', f'{text[0:7]}...' if len(text) > 10 else text)

    def set_text(self, text:str):
        self.text_surface = self.font.render(text, True, self.text_color)

    # <-----> State Methods <-----> #
    def update(self, mouse_pos:tuple[int, int]):
        pass

    def draw(self, screen:pg.Surface):
        pg.draw.rect(screen, self.bg_color, self.rect, border_radius=10)

        pg.draw.rect(screen, (0, 0, 0), self.rect, width=self.outline, border_radius=10)

        screen.blit(self.text_surface, self.text_rect)