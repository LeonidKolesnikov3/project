import os
import sys
import pygame
import random

fps = 60


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


def checker(board):
    pole = board
    win = '-'
    for i in pole:
        if i[0] == i[1] == i[2] and i[0] != '':
            win = i[0]
            break
    if win == '-':
        for i in range(3):
            if pole[0][i] == pole[1][i] == pole[2][i] and pole[0][i] != '':
                win = pole[0][i]
                break
    if win == '-':
        if pole[0][0] == pole[1][1] == pole[2][2] and pole[0][0] != '':
            win = pole[0][0]
        elif pole[0][2] == pole[1][1] == pole[2][0] and pole[0][2] != '':
            win = pole[0][2]
    return win


def start():
    buttonscolors = ['grey', 'grey', 'grey']
    pygame.display.set_caption('Tic-tac-toe')
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
    text = pygame.font.Font(None, 90)
    textsm = pygame.font.Font(None, 60)
    texttitle = pygame.font.Font(None, 100)
    texttitlerend = texttitle.render('Выберете режим игры', True, 'white')
    textrend = textsm.render('На двоих', True, 'black')
    textrend2 = textsm.render('С ботом', True, 'black')
    textrend3 = text.render('Назад', True, 'black')
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if 530 < event.pos[0] < 730 and 580 < event.pos[1] < 680:
                    running = False
                if 330 < event.pos[0] < 530 and 280 < event.pos[1] < 380:
                    gamefortwo()
                if 730 < event.pos[0] < 930 and 280 < event.pos[1] < 380:
                    gameforone()
            if event.type == pygame.MOUSEMOTION:
                sprite.rect.x, sprite.rect.y = event.pos
                if 530 < event.pos[0] < 730 and 580 < event.pos[1] < 680:
                    buttonscolors[0] = 'green'
                else:
                    buttonscolors[0] = 'grey'
                if 330 < event.pos[0] < 530 and 280 < event.pos[1] < 380:
                    buttonscolors[1] = 'green'
                else:
                    buttonscolors[1] = 'grey'
                if 730 < event.pos[0] < 930 and 280 < event.pos[1] < 380:
                    buttonscolors[2] = 'green'
                else:
                    buttonscolors[2] = 'grey'
            if pygame.mouse.get_focused():
                pygame.mouse.set_visible(False)
            else:
                pygame.mouse.set_visible(True)
        screen.fill('black')
        screen.blit(background, backgroundrect)
        pygame.draw.rect(screen, buttonscolors[0], (530, 580, 200, 100))
        pygame.draw.rect(screen, buttonscolors[1], (330, 280, 200, 100))
        pygame.draw.rect(screen, buttonscolors[2], (730, 280, 200, 100))
        screen.blit(textrend, (330, 300))
        screen.blit(textrend2, (740, 300))
        screen.blit(textrend3, (530, 600))
        screen.blit(texttitlerend, (250, 20))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(fps)


def gamefortwo():
    exitcolor = 'grey'
    bcolor = 'grey'
    turn = 'x'
    turncount = 0
    gamemap = [['', '', ''],
               ['', '', ''],
               ['', '', '']]
    coord = []
    blocker = True
    y = 150
    for i in range(len(gamemap)):
        string = gamemap[i]
        x = 100
        for j in range(len(string)):
            x += 200
            coord.append((x - 95, y - 95, 190, 190, j, i))
        y += 200
    pygame.display.set_caption('Tic-tac-toe for two')
    size = width, height = 1280, 720
    screen = pygame.display.set_mode(size)
    all_sprites = pygame.sprite.Group()
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("Blue_Arrow.png")
    sprite.rect = sprite.image.get_rect()
    all_sprites.add(sprite)
    background = load_image("background.png")
    ximage = load_image("x.png")
    ximage = pygame.transform.scale(ximage, (170, 170))
    background = pygame.transform.scale(background, (1280, 720))
    backgroundrect = background.get_rect()
    clock = pygame.time.Clock()
    text = pygame.font.Font(None, 90)
    textrend = text.render('Ходит - ' + turn, True, 'white')
    textexit = text.render('Рестарт', True, 'black')
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if 0 < event.pos[0] < 50 and 0 < event.pos[1] < 50:
                    running = False
                if 900 < event.pos[0] < 1200 and 600 < event.pos[1] < 700 and not blocker:
                    blocker = True
                    turn = 'x'
                    turncount = 0
                    gamemap = [['', '', ''],
                               ['', '', ''],
                               ['', '', '']]
                for i in range(len(coord)):
                    ycords = coord[i][-1]
                    xcords = coord[i][-2]
                    if coord[i][0] <= event.pos[0] <= coord[i][0] + coord[i][2] and coord[i][1] <= event.pos[1] <= \
                            coord[i][3] + coord[i][1]:
                        if turn == 'x' and gamemap[ycords][xcords] == '' and blocker:
                            turn = 'o'
                            gamemap[ycords][xcords] = 'x'
                            turncount += 1
                            if checker(gamemap) != '-':
                                blocker = False
                        elif turn == 'o' and gamemap[ycords][xcords] == '' and blocker:
                            turn = 'x'
                            gamemap[ycords][xcords] = 'o'
                            turncount += 1
                            if checker(gamemap) != '-':
                                blocker = False
            if event.type == pygame.MOUSEMOTION:
                sprite.rect.x, sprite.rect.y = event.pos
                if 0 < event.pos[0] < 50 and 0 < event.pos[1] < 50:
                    bcolor = 'green'
                else:
                    bcolor = 'grey'
                if 900 < event.pos[0] < 1200 and 600 < event.pos[1] < 700:
                    exitcolor = 'green'
                else:
                    exitcolor = 'grey'
            if pygame.mouse.get_focused():
                pygame.mouse.set_visible(False)
            else:
                pygame.mouse.set_visible(True)
        if blocker:
            textrend = text.render('Ходит - ' + turn.upper(), True, 'white')
        if not blocker and checker(gamemap) == '-':
            textrend = text.render('Ничья!', True, 'white')
        if checker(gamemap) == 'x':
            textrend = text.render('Х победил!', True, 'white')
        if checker(gamemap) == 'o':
            textrend = text.render('О победил!', True, 'white')
        screen.fill('black')
        screen.blit(background, backgroundrect)
        pygame.draw.line(screen, 'black', (400, 20), (400, 700), width=5)
        pygame.draw.line(screen, 'black', (600, 20), (600, 700), width=5)
        pygame.draw.line(screen, 'black', (200, 250), (800, 250), width=5)
        pygame.draw.line(screen, 'black', (200, 450), (800, 450), width=5)
        screen.blit(textrend, (800, 100))
        y = 150
        for i in gamemap:
            x = 100
            for j in i:
                x += 200
                if j == 'x':
                    screen.blit(ximage, (x - 85, y - 85, 100, 100))
                if j == 'o':
                    pygame.draw.circle(screen, 'yellow', (x, y), 80, 5)
            y += 200
        if turncount >= 9:
            blocker = False
        pygame.draw.rect(screen, bcolor, (0, 0, 50, 50))
        pygame.draw.line(screen, 'red', (0, 0), (50, 50), 5)
        pygame.draw.line(screen, 'red', (50, 0), (0, 50), 5)
        if not blocker:
            pygame.draw.rect(screen, exitcolor, (900, 600, 300, 100))
            screen.blit(textexit, (910, 610))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(fps)


def gameforone():
    exitcolor = 'grey'
    bcolor = 'grey'
    turn = 'x'
    turncount = 0
    gamemap = [['', '', ''],
               ['', '', ''],
               ['', '', '']]
    coord = []
    blocker = True
    y = 150
    for i in range(len(gamemap)):
        string = gamemap[i]
        x = 100
        for j in range(len(string)):
            x += 200
            coord.append((x - 95, y - 95, 190, 190, j, i))
        y += 200
    pygame.display.set_caption('Tic-tac-toe for one')
    size = width, height = 1280, 720
    screen = pygame.display.set_mode(size)
    all_sprites = pygame.sprite.Group()
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("Blue_Arrow.png")
    sprite.rect = sprite.image.get_rect()
    all_sprites.add(sprite)
    background = load_image("background.png")
    ximage = load_image("x.png")
    ximage = pygame.transform.scale(ximage, (170, 170))
    background = pygame.transform.scale(background, (1280, 720))
    backgroundrect = background.get_rect()
    clock = pygame.time.Clock()
    text = pygame.font.Font(None, 90)
    textrend = text.render('Ходит - ' + turn, True, 'white')
    textexit = text.render('Рестарт', True, 'black')
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if 0 < event.pos[0] < 50 and 0 < event.pos[1] < 50:
                    running = False
                if 900 < event.pos[0] < 1200 and 600 < event.pos[1] < 700 and not blocker:
                    blocker = True
                    turn = 'x'
                    turncount = 0
                    gamemap = [['', '', ''],
                               ['', '', ''],
                               ['', '', '']]
                for i in range(len(coord)):
                    ycords = coord[i][-1]
                    xcords = coord[i][-2]
                    if coord[i][0] <= event.pos[0] <= coord[i][0] + coord[i][2] and coord[i][1] <= event.pos[1] <= \
                            coord[i][3] + coord[i][1]:
                        if turn == 'x' and gamemap[ycords][xcords] == '' and blocker:
                            player = True
                            turn = 'o'
                            gamemap[ycords][xcords] = 'x'
                            turncount += 1
                            if checker(gamemap) != '-':
                                blocker = False
                        else:
                            player = False
                        turn = 'x'
                        if turncount < 9 and blocker and player:
                            gamex = random.randrange(0, 3)
                            gamey = random.randrange(0, 3)
                            while gamemap[gamey][gamex] != '':
                                gamex = random.randrange(0, 3)
                                gamey = random.randrange(0, 3)
                            gamemap[gamey][gamex] = 'o'
                            turncount += 1
                        if checker(gamemap) != '-':
                            blocker = False
            if event.type == pygame.MOUSEMOTION:
                sprite.rect.x, sprite.rect.y = event.pos
                if 0 < event.pos[0] < 50 and 0 < event.pos[1] < 50:
                    bcolor = 'green'
                else:
                    bcolor = 'grey'
                if 900 < event.pos[0] < 1200 and 600 < event.pos[1] < 700:
                    exitcolor = 'green'
                else:
                    exitcolor = 'grey'
            if pygame.mouse.get_focused():
                pygame.mouse.set_visible(False)
            else:
                pygame.mouse.set_visible(True)
        if blocker:
            textrend = text.render('Ходит - ' + turn.upper(), True, 'white')
        if not blocker and checker(gamemap) == '-':
            textrend = text.render('Ничья!', True, 'white')
        if checker(gamemap) == 'x':
            textrend = text.render('Х победил!', True, 'white')
        if checker(gamemap) == 'o':
            textrend = text.render('О победил!', True, 'white')
        screen.fill('black')
        screen.blit(background, backgroundrect)
        pygame.draw.line(screen, 'black', (400, 20), (400, 700), width=5)
        pygame.draw.line(screen, 'black', (600, 20), (600, 700), width=5)
        pygame.draw.line(screen, 'black', (200, 250), (800, 250), width=5)
        pygame.draw.line(screen, 'black', (200, 450), (800, 450), width=5)
        screen.blit(textrend, (800, 100))
        y = 150
        for i in gamemap:
            x = 100
            for j in i:
                x += 200
                if j == 'x':
                    screen.blit(ximage, (x - 85, y - 85, 100, 100))
                if j == 'o':
                    pygame.draw.circle(screen, 'yellow', (x, y), 80, 5)
            y += 200
        if turncount >= 9:
            blocker = False
        pygame.draw.rect(screen, bcolor, (0, 0, 50, 50))
        pygame.draw.line(screen, 'red', (0, 0), (50, 50), 5)
        pygame.draw.line(screen, 'red', (50, 0), (0, 50), 5)
        if not blocker:
            pygame.draw.rect(screen, exitcolor, (900, 600, 300, 100))
            screen.blit(textexit, (910, 610))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(fps)
