import pygame as pg

class Button:
    def __init__(
        self, text, center_pos, callback, font, padding=12,
        size=None,
        bg_color=(60, 60, 60), hover_color=(100, 100, 100),
        text_color=(255, 255, 255),
    ):
        self.text = text
        self.callback = callback
        self.font = font

        self.bg_color = bg_color
        self.hover_color = hover_color
        self.text_color = text_color

        self.padding = padding
        self.hovered = False

        # Render text
        self.text_surf = self.font.render(text, True, text_color)
        self.text_surf = self.font.render(text, True, text_color)

        if size:
            self.rect = pg.Rect(0, 0, *size)
            self.rect.center = center_pos
            self.text_rect = self.text_surf.get_rect(center=self.rect.center)
        else:
            self.text_rect = self.text_surf.get_rect(center=center_pos)
            self.rect = self.text_rect.inflate(padding * 2, padding * 2)

    # Events
    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            if self.hovered:
                self.callback()

    def update(self, mouse_pos):
        self.hovered = self.rect.collidepoint(mouse_pos)

    # Draw
    def draw(self, screen):
        color = self.hover_color if self.hovered else self.bg_color
        pg.draw.rect(screen, color, self.rect, border_radius=100)
        screen.blit(self.text_surf, self.text_rect)