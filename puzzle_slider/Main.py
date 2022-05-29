import pygame
import PuzzlePage as Pp
import GameConfig as Gc
import WelcomePage as Wp
import ExitPage as Ep
import sys
import os.path


directory_img = os.path.join(os.path.split(os.path.abspath(__file__))[0], 'Images')
num_img = len(os.listdir(directory_img)) - 1
if '.DSstore' in os.listdir(directory_img):
    num_img -= 1

    
# noinspection PyGlobalUndefined
def main():
    running = True
    welcome = True
    puzzle = False
    complete = False
    level = False
    pygame.font.init()
    screen = pygame.display.set_mode(Gc.shared['window_size'])
    color = Gc.page['background_color']
    ws = Gc.shared['window_size']
    bs = Gc.page['button_size']
    while running:
        global bu
        global di
        global board_
        global completed

        if welcome is True:
            current_page = Wp.WelcomePage()
            buttons = [Wp.Button((ws[0] / 12 * (2 * (i % 6) + 1), ws[1] / 2 + bs[1] * (i // 6) + 30 * (i // 6)), i + 1,
                       current_page) for i in range(num_img)]
            for button in buttons:
                button.appear()
            current_page.show(screen)
            pygame.display.set_caption('Welcome')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for button in buttons:
                        if button.collidepoint(pygame.mouse.get_pos()) is True:
                            current_page.fill(color)
                            current_page.show(screen)
                            bu = Pp.load_picture(button.number)
                            welcome = False
                            level = True
        elif level is True:
            current_page = Wp.WelcomePage()
            current_page.content = 'Choose(2-7):'
            buttons = [Wp.Button((ws[0] / 12 * (2*i-3), ws[1] / 2), i, current_page) for i in range(2, 8)]
            for button in buttons:
                button.appear()
            current_page.show(screen)
            pygame.display.set_caption('Choose Difficulty')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for button in buttons:
                        if button.collidepoint(pygame.mouse.get_pos()) is True:
                            current_page.fill(color)
                            current_page.show(screen)
                            di = button.number
                            board_ = Pp.produce(di)
                            i = 0
                            completed = {}
                            for row in range(di):
                                for column in range(di):
                                    if i == (di * di - 1):
                                        i = 0
                                    else:
                                        i = i + 1
                                    completed[i] = (column, row)
                            level = False
                            puzzle = True
        elif puzzle is True:
            pygame.display.set_caption('Play')
            blocks = [Pp.Block(i, board_, bu, di) for i in board_.keys() if i != 0]
            screen.fill(color)
            for block in blocks:
                block.draw(screen)
            for event_ in pygame.event.get():
                if event_.type == pygame.QUIT:
                    running = False
                    sys.exit()
                if event_.type == pygame.MOUSEBUTTONDOWN:
                    for block in blocks:
                        if block.collidepoint(pygame.mouse.get_pos()) is True:
                            block.alter()
            if blocks[1].board == completed: 
                blocks[1].board = {}
                complete = True
                puzzle = False
        elif complete is True:
            pygame.display.set_caption('Congratulations')
            screen.blit(bu, bu.get_rect())
            current_page = Ep.ExitPage()
            screen.blit(current_page, (0, 0))
            for _event in pygame.event.get():
                if _event.type == pygame.QUIT:
                    running = False
                    sys.exit()
                if _event.type == pygame.MOUSEBUTTONDOWN:
                    complete = False
                    welcome = True
        pygame.display.update()


if __name__ == '__main__':
    main()
    