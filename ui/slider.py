import loggerric as lr
import pygame as pg

from utils.sound import AudioManager
from utils.settings import Settings
from ui.label import Label

class Slider:
    def __init__(
        self, text:str, center_pos:tuple, font:pg.font.Font, size:tuple,
        thumb_color:tuple=None, slide_color:tuple=None, outline:int=3,
        outline_color:tuple=None, text_color:tuple=None,
        thumb_hover_color:tuple=None, init_value:float=0.5
    ):
        # Increase scope
        self.text = text
        self.font = font
        self.size = size
        self.outline = outline
        self.init_value = init_value

        # Set colors
        self.colors = Settings.get('color_palette')
        self.thumb_color = thumb_color or self.colors['primary_accent']
        self.thumb_hover_color = thumb_hover_color or self.colors['light_accent']
        self.text_color = text_color or self.colors['primary_text']
        self.outline_color = outline_color or self.colors['secondary_accent']
        self.slide_color = slide_color or self.colors['dark_text']

        # States
        self.hovered = False
        self.played_hover_sfx = False
        self.is_dragging = False

        self.title_label = Label(text, (center_pos[0] - size[0] / 2 - 100, center_pos[1]), font=font, size=(150, size[1]))
        self.value_label = Label(f'{self.init_value * 100:.0f}%', (center_pos[0] + size[0] / 2 + 100, center_pos[1]), font=font, size=(150, size[1]))

        # Graphics
        self.text_surface = self.font.render(text, True, self.text_color)
        self.rect = pg.Rect(0, 0, *self.size)
        self.slide_rect = pg.Rect(0, 0, self.size[0], self.size[1] / 4)
        self.thumb_rect = pg.Rect(0, 0, 20, self.size[1])
        self.rect.center = center_pos
        self.slide_rect.center = center_pos
        self.thumb_rect.center = center_pos
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)

        lr.Log.debug('Initialized slider:', text)
    
    def get_value(self) -> float:
        return self.init_value
    
    # <-----> State Methods <-----> #
    def handle_events(self, events:list[pg.event.Event]):
        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                if self.hovered:
                    AudioManager.play('button_click.mp3', 'ui')
                self.is_dragging = True
            elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
                self.is_dragging = False
    
    def update(self, mouse_pos:tuple[int, int]):
        self.hovered = self.thumb_rect.collidepoint(mouse_pos)

        if not self.hovered and self.played_hover_sfx:
            self.played_hover_sfx = False
        elif self.hovered and not self.played_hover_sfx:
            AudioManager.play('button_hover.mp3', 'ui')
            self.played_hover_sfx = True

        if self.is_dragging:
            clamped = min(self.rect.center[0] + self.size[0] / 2, max(self.rect.center[0] - self.size[0] / 2, mouse_pos[0]))
            self.thumb_rect.center = (clamped, self.thumb_rect.center[1])
            self.init_value = (clamped - self.size[0] / 2) / self.size[0]
            self.value_label.set_text(f'{self.init_value * 100:.0f}%')

    def draw(self, screen:pg.Surface):
        thumb_color = self.thumb_hover_color if self.hovered else self.thumb_color

        self.title_label.draw(screen)
        self.value_label.draw(screen)

        pg.draw.rect(screen, self.slide_color, self.slide_rect, border_radius=100)

        pg.draw.rect(screen, thumb_color, self.thumb_rect, border_radius=50)
        pg.draw.rect(screen, self.outline_color, self.thumb_rect, width=self.outline, border_radius=50)