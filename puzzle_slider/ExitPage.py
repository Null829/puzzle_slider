import pygame.surface
import GameConfig as Gc

ws = Gc.shared['window_size']


class ExitPage(pygame.Surface):
    def __init__(self):
        pygame.Surface.__init__(self, ws)
        self.set_alpha(Gc.page['exit_alpha'])
        self.content = 'Process finished with exit code 0'
        self.fill(Gc.page['background_color'])
        font = pygame.font.SysFont(Gc.page['font_type'], Gc.page['font_size_e'], True)
        text = font.render(str(self.content), True, Gc.page['font_color_e'])
        self.blit(text, text.get_rect(center=(ws[0] / 2, ws[1] / 4)))

