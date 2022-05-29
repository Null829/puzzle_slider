import pygame
import GameConfig as Gc
import os
import random


def load_picture(name):
    directory_img = os.path.join(os.path.split(os.path.abspath(__file__))[0], 'Images')
    path = os.path.join(directory_img, str(name) + '.png')
    try:
        img = pygame.image.load(path).convert()
        img_sec = pygame.transform.scale(img, Gc.shared['puzzle_size'])
        return img_sec
    except pygame.error or FileNotFoundError:
        print('Image Not Found:' + path)


def produce(side):
    i = 0
    boards = {}
    for row in range(side):
        for column in range(side):
            if i == (side * side - 1):  # 最后一个坐标对应的数字应该是空的，用'0'表示
                i = 0
            else:
                i = i + 1
            boards[i] = (column, row)  # 列，行，数字
    vectors = [[1, 0], [-1, 0], [0, 1], [0, -1]]  # 右，左，上，下
    i = 20 * side ** 2  # 移动的步数范围
    a = 0
    while a < i:
        b = random.randint(0, 3)  # 移动任意方向
        vector = vectors[b]
        for num in boards.keys():
            if num == 0:  # 改变'0'的位置
                n = boards[num][0] + vector[0]
                m = boards[num][1] + vector[1]
                if n != side and m != side and n != -1 and m != -1:
                    for nu in boards.keys():
                        if boards[nu] == (n, m):
                            boards[nu] = (boards[num][0], boards[num][1])
                    boards[num] = (n, m)
                    a += 1
    return boards


class Block(pygame.Rect):
    def __init__(self, number, board: dict, p, d):
        self.w = int(Gc.shared['puzzle_size'][0] / d)
        self.number = number
        self.board = board
        self.position = self.board[self.number]
        pygame.Rect.__init__(self, self)
        self.left = self.position[0] * self.w
        self.top = self.position[1] * self.w
        self.height = self.w
        self.width = self.w
        self.neighbors = [(self.position[0] + 1, self.position[1]), (self.position[0] - 1, self.position[1]),
                          (self.position[0], self.position[1] + 1),
                          (self.position[0], self.position[1] - 1)]
        self.image = p.subsurface((((self.number - 1) % d * self.w, ((self.number-1) // d) * self.w), (self.w, self.w)))

    def draw(self, screen_: pygame.Surface):
        self.position = self.board[self.number]
        self.top = self.position[1] * self.w
        self.left = self.position[0] * self.w
        screen_.blit(self.image, (self.position[0] * self.w, self.position[1] * self.w, self.w, self.w))

    def alter(self):
        for neighbor in self.neighbors:
            if neighbor == self.board[0]:
                self.board[0] = self.position
                self.board[self.number] = neighbor
                self.position = self.board[self.number]
                break
