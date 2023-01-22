import os
import sys
import pygame


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen, gamemap):
        color = 'black'
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, color, (
                x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size, self.cell_size))
                if color == 'black':
                    color = 'white'
                else:
                    color = 'black'
        for y in range(len(gamemap)):
            for x in range(len(gamemap)):
                if gamemap[y][x] == 'bU':
                    pygame.draw.ellipse(screen, 'red', (300 + x * 50, 100 + y * 50, 50, 50))
                if gamemap[y][x] == 'wU':
                    pygame.draw.ellipse(screen, 'blue', (300 + x * 50, 100 + y * 50, 50, 50))
                if gamemap[y][x] == 'sU':
                    pygame.draw.ellipse(screen, 'yellow', (300 + x * 50, 100 + y * 50, 50, 50))
                if gamemap[y][x] == 1:
                    pygame.draw.ellipse(screen, 'green', (300 + x * 50, 100 + y * 50, 50, 50))

    def get_click(self, a):
        b = self.get_cell(a)
        if b is None:
            return
        self.on_click(b)

    def get_cell(self, a):
        x = self.width * self.cell_size
        y = self.height * self.cell_size
        if self.left < a[0] < self.left + x:
            if self.top < a[1] < self.top + y:
                return (a[1] - self.left) // self.cell_size, (a[0] - self.top) // self.cell_size
        return None

    def on_click(self, a):
        x = (a[0] // 50) - (self.left // 50)
        y = (a[1] // 50) - (self.top // 50)
        if (x > -1 and y > -1) and (x < self.width and y < self.height):
            print((x, y))
            return (x, y)
        else:
            print('None')


def start():
    pygame.display.set_caption('шашки')
    size = width, height = 1280, 720
    screen = pygame.display.set_mode(size)
    all_sprites = pygame.sprite.Group()
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("Blue_Arrow.png")
    sprite.rect = sprite.image.get_rect()
    all_sprites.add(sprite)
    background = load_image("background.png")
    background = pygame.transform.scale(background, (1280, 720))
    backgroundrect = background.get_rect()
    clock = pygame.time.Clock()
    board = Board(9, 9)
    board.set_view(300, 100, 50)
    gamemap = [
        ['bU', 2, 'bU', 2, 'bU', 2, 'bU', 2, 'bU'],
        [2, 'bU', 2, 'bU', 2, 'bU', 2, 'bU', 2],
        ['bU', 2, 'bU', 2, 'bU', 2, 'bU', 2, 'bU'],
        [2, 0, 2, 0, 2, 0, 2, 0, 2],
        [0, 2, 0, 2, 0, 2, 0, 2, 0],
        [2, 0, 2, 0, 2, 0, 2, 0, 2],
        ['wU', 2, 'wU', 2, 'wU', 2, 'wU', 2, 'wU'],
        [2, 'wU', 2, 'wU', 2, 'wU', 2, 'wU', 2],
        ['wU', 2, 'wU', 2, 'wU', 2, 'wU', 2, 'wU']
    ]
    turn = 'wU'
    running = True
    eatinginfo = []
    location = ''
    fps = 60
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if 0 < event.pos[0] < 50 and 0 < event.pos[1] < 50:
                    running = False
                coords = board.on_click(event.pos)
                if coords is not None:
                    if turn == 'wU':
                        if gamemap[coords[1]][coords[0]] == turn:
                            for y in range(len(gamemap)):
                                for x in range(len(gamemap)):
                                    if gamemap[y][x] == 'sU':
                                        gamemap[y][x] = 'wU'
                                    if gamemap[y][x] == 1:
                                        gamemap[y][x] = 0
                            gamemap[coords[1]][coords[0]] = 'sU'
                            try:
                                if gamemap[coords[1] - 1][coords[0] - 1] == 0:
                                    gamemap[coords[1] - 1][coords[0] - 1] = 1
                            except:
                                pass
                            try:
                                if gamemap[coords[1] - 1][coords[0] + 1] == 0:
                                    gamemap[coords[1] - 1][coords[0] + 1] = 1
                            except:
                                pass
                            try:
                                if gamemap[coords[1] - 1][coords[0] + 1] == 'bU' and gamemap[coords[1] - 2][coords[0] + 2] == 0:
                                    if gamemap[coords[1] - 1][coords[0] + 1] not in eatinginfo:
                                        eatinginfo.append(gamemap[coords[1] - 1][coords[0] + 1])
                                    gamemap[coords[1] - 2][coords[0] + 2] = 1
                                    location = '1'
                            except:
                                pass
                            try:
                                if gamemap[coords[1] - 1][coords[0] - 1] == 'bU' and gamemap[coords[1] - 2][coords[0] - 2] == 0:
                                    if gamemap[coords[1] - 1][coords[0] - 1] not in eatinginfo:
                                        eatinginfo.append(gamemap[coords[1] - 1][coords[0] - 1])
                                    gamemap[coords[1] - 2][coords[0] - 2] = 1
                                    location = '2'
                            except:
                                pass
                        if gamemap[coords[1]][coords[0]] == 1:
                            gamemap[coords[1]][coords[0]] = 'wU'
                            for i in range(len(eatinginfo)):
                                try:
                                    if eatinginfo[i] == gamemap[coords[1] + 1][coords[0] - 1] and location == '1':
                                        gamemap[coords[1] + 1][coords[0] - 1] = 1
                                        break
                                except:
                                    pass
                                try:
                                    if eatinginfo[i] == gamemap[coords[1] + 1][coords[0] + 1] and location == '2':
                                        gamemap[coords[1] + 1][coords[0] + 1] = 1
                                        break
                                except:
                                    pass
                            for y in range(len(gamemap)):
                                for x in range(len(gamemap)):
                                    if gamemap[y][x] == 'sU':
                                        gamemap[y][x] = 0
                                    if gamemap[y][x] == 1:
                                        gamemap[y][x] = 0
                            turn = 'bU'
                            eatinginfo = []
                    else:
                        if gamemap[coords[1]][coords[0]] == turn:
                            for y in range(len(gamemap)):
                                for x in range(len(gamemap)):
                                    if gamemap[y][x] == 'sU':
                                        gamemap[y][x] = 'bU'
                                    if gamemap[y][x] == 1:
                                        gamemap[y][x] = 0
                            gamemap[coords[1]][coords[0]] = 'sU'
                            try:
                                if gamemap[coords[1] + 1][coords[0] - 1] == 0:
                                    gamemap[coords[1] + 1][coords[0] - 1] = 1
                            except:
                                pass
                            try:
                                if gamemap[coords[1] + 1][coords[0] + 1] == 0:
                                    gamemap[coords[1] + 1][coords[0] + 1] = 1
                            except:
                                pass
                            try:
                                if gamemap[coords[1] + 1][coords[0] - 1] == 'wU' and gamemap[coords[1] + 2][coords[0] - 2] == 0:
                                    if gamemap[coords[1] + 1][coords[0] - 1] not in eatinginfo:
                                        eatinginfo.append(gamemap[coords[1] + 1][coords[0] - 1])
                                    gamemap[coords[1] + 2][coords[0] - 2] = 1
                                    location = '2'
                            except:
                                pass
                            try:
                                if gamemap[coords[1] + 1][coords[0] + 1] == 'wU' and gamemap[coords[1] + 2][coords[0] + 2] == 0:
                                    if gamemap[coords[1] + 1][coords[0] + 1] not in eatinginfo:
                                        eatinginfo.append(gamemap[coords[1] + 1][coords[0] + 1])
                                    gamemap[coords[1] + 2][coords[0] + 2] = 1
                                    location = '1'
                            except:
                                pass
                        if gamemap[coords[1]][coords[0]] == 1:
                            gamemap[coords[1]][coords[0]] = 'bU'
                            for i in range(len(eatinginfo)):
                                try:
                                    if eatinginfo[i] == gamemap[coords[1] - 1][coords[0] - 1] and location == '1':
                                        gamemap[coords[1] - 1][coords[0] - 1] = 1
                                        break
                                except:
                                    pass
                                try:
                                    if eatinginfo[i] == gamemap[coords[1] - 1][coords[0] + 1] and location == '2':
                                        gamemap[coords[1] - 1][coords[0] + 1] = 1
                                        break
                                except:
                                    pass
                            for y in range(len(gamemap)):
                                for x in range(len(gamemap)):
                                    if gamemap[y][x] == 'sU':
                                        gamemap[y][x] = 0
                                    if gamemap[y][x] == 1:
                                        gamemap[y][x] = 0
                            turn = 'wU'
                            eatinginfo = []
            if event.type == pygame.MOUSEMOTION:
                sprite.rect.x, sprite.rect.y = event.pos
            if pygame.mouse.get_focused():
                pygame.mouse.set_visible(False)
            else:
                pygame.mouse.set_visible(True)
        screen.fill('black')
        screen.blit(background, backgroundrect)
        pygame.draw.rect(screen, 'grey', (0, 0, 50, 50))
        pygame.draw.line(screen, 'red', (0, 0), (50, 50), 5)
        pygame.draw.line(screen, 'red', (50, 0), (0, 50), 5)
        board.render(screen, gamemap)
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(fps)
