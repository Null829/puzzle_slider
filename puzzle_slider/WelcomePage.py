import pygame
import GameConfig as Gc


ws = Gc.shared['window_size']


class WelcomePage(pygame.Surface):
    def __init__(self):
        super().__init__(ws)
        self.content = 'Choose:'
        self.fill(Gc.page['background_color'])
        font = pygame.font.SysFont(Gc.page['font_type'], Gc.page['font_size'], True)
        text = font.render(str(self.content), True, Gc.page['font_color_w'])
        self.blit(text,
                  text.get_rect(center=(ws[0] / 2, ws[1] / 4)))

    def show(self, background: pygame.Surface):
        background.blit(self, (0, 0))


class Button(pygame.Rect):
    def __init__(self, position: tuple, number: int, page: pygame.Surface):
        super().__init__(position, Gc.page['button_size'])
        self.center = position
        self.number = number
        self.page = page

    def appear(self):
        pygame.draw.rect(self.page, Gc.page['button_color'], self)
        t = pygame.font.SysFont(Gc.page['font_type'], Gc.page['font_size'], True).render(
            str(self.number), True, Gc.page['font_color_w'])
        self.page.blit(t, t.get_rect(center=self.center))
