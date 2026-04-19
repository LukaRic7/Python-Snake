import loggerric as lr
import pygame as pg

from utils.settings import Settings

class Label:
    """
    **Create a label widget using pygame.**
    
    Supports multiline functionality via '\n'.
    
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
        - `size` (tuple=None): Minimum size of the label.
        - `bg_color` (tuple=None): Background color of the label.
        - `text_color` (tuple=None): Color of the text.
        - `outline` (int=3): Outline thickness.
        - `outline_color` (tuple=None): Color of the outline.
        """

        # Increase scope
        self.text       = text
        self.center_pos = center_pos
        self.font       = font
        self.base_size  = size
        self.padding    = padding
        self.outline    = outline

        # Set colors
        self.colors        = Settings.get('color_palette')
        self.bg_color      = bg_color or self.colors['primary_accent']
        self.text_color    = text_color or self.colors['dark_text']
        self.outline_color = outline_color or self.colors['secondary_accent']

        # Setup graphics & sizes
        self._render_text()

        lr.Log.debug(
            'Initialized label:', f'{text[0:7]}...' if len(text) > 10 else text
        )

    def _render_text(self):
        """
        Internal method to handle multiline splitting, rendering, and rect sizing.
        """
        lines = self.text.split('\n')
        self.text_elements = []  # Will hold tuples of (Surface, Rect)
        
        temp_surfs = []
        max_width = 0
        total_height = 0
        line_height = self.font.get_linesize()
        
        # Render each line and find the maximum width and total height
        for line in lines:
            surf = self.font.render(line, True, self.text_color)
            temp_surfs.append(surf)
            
            if surf.get_width() > max_width:
                max_width = surf.get_width()
            total_height += line_height

        # Calculate the final expanding background rect size
        min_w = self.base_size[0] if self.base_size else 0
        min_h = self.base_size[1] if self.base_size else 0
        
        final_width = max(min_w, max_width + (self.padding * 2))
        final_height = max(min_h, total_height + (self.padding * 2))

        self.rect = pg.Rect(0, 0, final_width, final_height)
        self.rect.center = self.center_pos

        # Position each text line so the whole block is centered
        start_y = self.rect.centery - (total_height / 2)
        
        for i, surf in enumerate(temp_surfs):
            line_rect = surf.get_rect()
            line_rect.centerx = self.rect.centerx
            line_rect.top = start_y + (i * line_height)
            self.text_elements.append((surf, line_rect))

    def set_text(self, text:str):
        """
        **Set the text of the widget.**
        
        *Parameters*:
        - `text` (str): The text that should be displayed.
        """
        self.text = text
        self._render_text()

    # <-----> State Methods <-----> #
    def update(self, mouse_pos:tuple[int, int]):
        pass

    def draw(self, screen:pg.Surface):
        # Draw background
        pg.draw.rect(screen, self.bg_color, self.rect, border_radius=10)

        # Draw outline 
        pg.draw.rect(
            screen, self.outline_color, self.rect, width=self.outline, border_radius=10
        )

        # Draw each line of text
        for surf, text_rect in self.text_elements:
            screen.blit(surf, text_rect)