import os
import sys
import pygame
import random


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


def start():
    pygame.display.set_caption('balls')
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
    fps = 60
    text = pygame.font.Font(None, 80)
    levels = []
    for i in range(1, 13):
        with open(f'data/levelsinfo/{str(i)}.txt', 'r', encoding='utf8') as data:
            info = data.readline()
            levels.append(info)
    running = True
    coords = []
    while running:
        textrend = text.render('Выбор уровня', True, 'white')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if 0 < event.pos[0] < 50 and 0 < event.pos[1] < 50:
                    running = False
                for i in coords:
                    if i[0][0] < event.pos[0] < i[0][2] and i[0][1] < event.pos[1] < i[0][3] and i[1] == 0:
                        level1info()
                        level1()
                        levels = []
                        for j in range(1, 13):
                            with open(f'data/levelsinfo/{str(j)}.txt', 'r', encoding='utf8') as data:
                                info = data.readline()
                                levels.append(info)
                    if i[0][0] < event.pos[0] < i[0][2] and i[0][1] < event.pos[1] < i[0][3] and i[1] == 1:
                        level2info()
                        level2()
                        levels = []
                        for j in range(1, 13):
                            with open(f'data/levelsinfo/{str(j)}.txt', 'r', encoding='utf8') as data:
                                info = data.readline()
                                levels.append(info)
                    if i[0][0] < event.pos[0] < i[0][2] and i[0][1] < event.pos[1] < i[0][3] and i[1] == 2:
                        level3info()
                        level3()
                        levels = []
                        for j in range(1, 13):
                            with open(f'data/levelsinfo/{str(j)}.txt', 'r', encoding='utf8') as data:
                                info = data.readline()
                                levels.append(info)
                    if i[0][0] < event.pos[0] < i[0][2] and i[0][1] < event.pos[1] < i[0][3] and i[1] == 3:
                        level4info()
                        level4()
                        levels = []
                        for j in range(1, 13):
                            with open(f'data/levelsinfo/{str(j)}.txt', 'r', encoding='utf8') as data:
                                info = data.readline()
                                levels.append(info)
                    if i[0][0] < event.pos[0] < i[0][2] and i[0][1] < event.pos[1] < i[0][3] and i[1] == 4:
                        level5info()
                        level5()
                        levels = []
                        for j in range(1, 13):
                            with open(f'data/levelsinfo/{str(j)}.txt', 'r', encoding='utf8') as data:
                                info = data.readline()
                                levels.append(info)
                    if i[0][0] < event.pos[0] < i[0][2] and i[0][1] < event.pos[1] < i[0][3] and i[1] == 5:
                        level6info()
                        level6()
                        levels = []
                        for j in range(1, 13):
                            with open(f'data/levelsinfo/{str(j)}.txt', 'r', encoding='utf8') as data:
                                info = data.readline()
                                levels.append(info)
                    if i[0][0] < event.pos[0] < i[0][2] and i[0][1] < event.pos[1] < i[0][3] and i[1] == 6:
                        level7info()
                        level7()
                        levels = []
                        for j in range(1, 13):
                            with open(f'data/levelsinfo/{str(j)}.txt', 'r', encoding='utf8') as data:
                                info = data.readline()
                                levels.append(info)
                    if i[0][0] < event.pos[0] < i[0][2] and i[0][1] < event.pos[1] < i[0][3] and i[1] == 7:
                        level8info()
                        level8()
                        levels = []
                        for j in range(1, 13):
                            with open(f'data/levelsinfo/{str(j)}.txt', 'r', encoding='utf8') as data:
                                info = data.readline()
                                levels.append(info)
                    if i[0][0] < event.pos[0] < i[0][2] and i[0][1] < event.pos[1] < i[0][3] and i[1] == 8:
                        level9info()
                        level9()
                        levels = []
                        for j in range(1, 13):
                            with open(f'data/levelsinfo/{str(j)}.txt', 'r', encoding='utf8') as data:
                                info = data.readline()
                                levels.append(info)
                    if i[0][0] < event.pos[0] < i[0][2] and i[0][1] < event.pos[1] < i[0][3] and i[1] == 9:
                        level10info()
                        level10()
                        levels = []
                        for j in range(1, 13):
                            with open(f'data/levelsinfo/{str(j)}.txt', 'r', encoding='utf8') as data:
                                info = data.readline()
                                levels.append(info)
                    if i[0][0] < event.pos[0] < i[0][2] and i[0][1] < event.pos[1] < i[0][3] and i[1] == 10:
                        level11info()
                        level11()
                        levels = []
                        for j in range(1, 13):
                            with open(f'data/levelsinfo/{str(j)}.txt', 'r', encoding='utf8') as data:
                                info = data.readline()
                                levels.append(info)
                    if i[0][0] < event.pos[0] < i[0][2] and i[0][1] < event.pos[1] < i[0][3] and i[1] == 11:
                        level12info()
                        level12()
                        levels = []
                        for j in range(1, 13):
                            with open(f'data/levelsinfo/{str(j)}.txt', 'r', encoding='utf8') as data:
                                info = data.readline()
                                levels.append(info)
            if event.type == pygame.MOUSEMOTION:
                sprite.rect.x, sprite.rect.y = event.pos
            if pygame.mouse.get_focused():
                pygame.mouse.set_visible(False)
            else:
                pygame.mouse.set_visible(True)
        screen.fill('black')
        screen.blit(background, backgroundrect)
        screen.blit(textrend, (410, 30))
        x = 100
        y = 100
        level = 0
        for j in range(4):
            for i in range(3):
                if levels[level] == 'open':
                    textrend = text.render(str(level + 1), True, 'black')
                    pygame.draw.rect(screen, 'grey', (x, y, 80, 80))
                    if ((x, y, x + 80, y + 80), level) not in coords:
                        coords.append(((x, y, x + 80, y + 80), level))
                    screen.blit(textrend, (x + 26, y + 13))
                x += 90
                level += 1
            y += 100
        pygame.draw.rect(screen, 'grey', (0, 0, 50, 50))
        pygame.draw.line(screen, 'red', (0, 0), (50, 50), 5)
        pygame.draw.line(screen, 'red', (50, 0), (0, 50), 5)
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(fps)


def level1():
    pygame.display.set_caption('balls')
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
    fps = 60
    playerw = 300
    playerh = 40
    playerspd = 10
    bulletr = int(30 * 2 ** 0.5)
    bullet = pygame.Rect(bulletr, 360, bulletr, bulletr)
    bullets = 5
    player = pygame.Rect(640 - playerw // 2, 720 - playerh - 50, playerw, playerh)
    speedx = 1
    speedy = -1
    walls = []
    x = 20
    y = 50
    for i in range(3):
        for j in range(6):
            color = (random.randrange(1, 255), random.randrange(1, 255), random.randrange(1, 255))
            walls.append((pygame.Rect(x, y, 190, 30), color))
            x += 210
        x = 20
        y += 50
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEMOTION:
                sprite.rect.x, sprite.rect.y = event.pos
            if pygame.mouse.get_focused():
                pygame.mouse.set_visible(False)
            else:
                pygame.mouse.set_visible(True)
        if pygame.key.get_pressed()[pygame.K_LEFT] and player.left > 0:
            player.left -= playerspd
        elif pygame.key.get_pressed()[pygame.K_RIGHT] and player.right < 1280:
            player.right += playerspd
        screen.fill('black')
        screen.blit(background, backgroundrect)
        pygame.draw.circle(screen, 'red', bullet.center, 30)
        pygame.draw.rect(screen, 'green', player)
        bullet.x += bullets * speedx
        bullet.y += bullets * speedy
        if bullet.colliderect(player) and speedy > 0:
            speedy = -speedy
        if bullet.centery < 30:
            speedy = -speedy
        if bullet.centerx < 30 or bullet.centerx > 1250:
            speedx = -speedx
        if bullet.centery > 690:
            speedy = -speedy
        for i in range(len(walls)):
            j = walls[i][0]
            if j.colliderect(bullet):
                walls.pop(i)
                break
        for i in walls:
            pygame.draw.rect(screen, i[1], i[0])
        if len(walls) == 0:
            with open('data/levelsinfo/2.txt', 'w', encoding='utf8') as data:
                data.write('open')
            running = False
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(fps)


def level1info():
    pygame.display.set_caption('balls')
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
    text = pygame.font.Font(None, 70)
    text2 = pygame.font.Font(None, 70)
    textrestart = pygame.font.Font(None, 70)
    textrend = text.render('Уровень 1', True, 'white')
    textplay = textrestart.render('Чтобы начать игру, нажмите любую клавишу', True, 'black')
    textstring1 = text.render('Уничтожьте все плитки. Они разрушаются при', True, 'white')
    textstring2 = text.render('столкновении с мячом', True, 'white')
    textstring3 = text2.render('используйте <- и -> для перемещения своей плитки', True, 'red')
    fps = 60
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEMOTION:
                sprite.rect.x, sprite.rect.y = event.pos
            if pygame.mouse.get_focused():
                pygame.mouse.set_visible(False)
            else:
                pygame.mouse.set_visible(True)
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                running = False
        screen.fill('black')
        screen.blit(background, backgroundrect)
        screen.blit(textrend, (400, 50))
        screen.blit(textstring1, (20, 220))
        screen.blit(textstring2, (20, 320))
        screen.blit(textstring3, (20, 420))
        screen.blit(textplay, (120, 600))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(fps)


def level2():
    pygame.display.set_caption('balls')
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
    fps = 60
    playerw = 300
    playerh = 40
    playerspd = 10
    bulletr = int(30 * 2 ** 0.5)
    bullet = pygame.Rect(bulletr, 360, bulletr, bulletr)
    bullets = 5
    player = pygame.Rect(640 - playerw // 2, 720 - playerh - 50, playerw, playerh)
    speedx = 1
    speedy = -1
    walls = []
    x = 20
    y = 50
    for i in range(3):
        for j in range(6):
            color = (random.randrange(1, 255), random.randrange(1, 255), random.randrange(1, 255))
            walls.append((pygame.Rect(x, y, 190, 30), color))
            x += 210
        x = 20
        y += 50
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEMOTION:
                sprite.rect.x, sprite.rect.y = event.pos
            if pygame.mouse.get_focused():
                pygame.mouse.set_visible(False)
            else:
                pygame.mouse.set_visible(True)
        if pygame.key.get_pressed()[pygame.K_LEFT] and player.left > 0:
            player.left -= playerspd
        elif pygame.key.get_pressed()[pygame.K_RIGHT] and player.right < 1280:
            player.right += playerspd
        screen.fill('black')
        screen.blit(background, backgroundrect)
        pygame.draw.circle(screen, 'red', bullet.center, 30)
        pygame.draw.rect(screen, 'green', player)
        bullet.x += bullets * speedx
        bullet.y += bullets * speedy
        if bullet.colliderect(player) and speedy > 0:
            speedy = -speedy
        if bullet.centery < 30:
            speedy = -speedy
        if bullet.centerx < 30 or bullet.centerx > 1250:
            speedx = -speedx
        if bullet.centery > 720:
            running = False
        for i in range(len(walls)):
            j = walls[i][0]
            if j.colliderect(bullet):
                walls.pop(i)
                break
        for i in walls:
            pygame.draw.rect(screen, i[1], i[0])
        if len(walls) == 0:
            with open('data/levelsinfo/3.txt', 'w', encoding='utf8') as data:
                data.write('open')
            running = False
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(fps)


def level2info():
    pygame.display.set_caption('balls')
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
    text = pygame.font.Font(None, 70)
    text2 = pygame.font.Font(None, 70)
    textrestart = pygame.font.Font(None, 70)
    textrend = text.render('Уровень 2', True, 'white')
    textplay = textrestart.render('Чтобы начать игру, нажмите любую клавишу', True, 'black')
    textstring1 = text.render('Правила прежние, но теперь при', True, 'white')
    textstring2 = text.render('столкновении мяча с нижним краем вы проиграете', True, 'white')
    textstring3 = text2.render('используйте <- и -> для перемещения своей плитки', True, 'red')
    fps = 60
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEMOTION:
                sprite.rect.x, sprite.rect.y = event.pos
            if pygame.mouse.get_focused():
                pygame.mouse.set_visible(False)
            else:
                pygame.mouse.set_visible(True)
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                running = False
        screen.fill('black')
        screen.blit(background, backgroundrect)
        screen.blit(textrend, (400, 50))
        screen.blit(textstring1, (20, 220))
        screen.blit(textstring2, (20, 320))
        screen.blit(textstring3, (20, 420))
        screen.blit(textplay, (120, 600))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(fps)


def level3():
    pygame.display.set_caption('balls')
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
    fps = 60
    playerw = 300
    playerh = 40
    playerspd = 10
    bulletr = int(30 * 2 ** 0.5)
    bullet = pygame.Rect(bulletr, 360, bulletr, bulletr)
    bullets = 5
    player = pygame.Rect(640 - playerw // 2, 720 - playerh - 50, playerw, playerh)
    speedx = 1
    speedy = -1
    walls = []
    x = 20
    y = 50
    for i in range(3):
        for j in range(6):
            color = (random.randrange(1, 255), random.randrange(1, 255), random.randrange(1, 255))
            walls.append((pygame.Rect(x, y, 190, 30), color))
            x += 210
        x = 20
        y += 50
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEMOTION:
                sprite.rect.x, sprite.rect.y = event.pos
            if pygame.mouse.get_focused():
                pygame.mouse.set_visible(False)
            else:
                pygame.mouse.set_visible(True)
        if pygame.key.get_pressed()[pygame.K_LEFT] and player.left > 0:
            player.left -= playerspd
        elif pygame.key.get_pressed()[pygame.K_RIGHT] and player.right < 1280:
            player.right += playerspd
        screen.fill('black')
        screen.blit(background, backgroundrect)
        pygame.draw.circle(screen, 'red', bullet.center, 30)
        pygame.draw.rect(screen, 'green', player)
        bullet.x += bullets * speedx
        bullet.y += bullets * speedy
        if bullet.colliderect(player) and speedy > 0:
            speedy = -speedy
        if bullet.centery < 30:
            speedy = -speedy
        if bullet.centerx < 30 or bullet.centerx > 1250:
            speedx = -speedx
        if bullet.centery > 720:
            running = False
        for i in range(len(walls)):
            j = walls[i][0]
            if j.colliderect(bullet):
                walls.pop(i)
                speedy = -speedy
                break
        for i in walls:
            pygame.draw.rect(screen, i[1], i[0])
        if len(walls) == 0:
            with open('data/levelsinfo/4.txt', 'w', encoding='utf8') as data:
                data.write('open')
            running = False
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(fps)


def level3info():
    pygame.display.set_caption('balls')
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
    text = pygame.font.Font(None, 70)
    text2 = pygame.font.Font(None, 70)
    textrestart = pygame.font.Font(None, 70)
    textrend = text.render('Уровень 3', True, 'white')
    textplay = textrestart.render('Чтобы начать игру, нажмите любую клавишу', True, 'black')
    textstring1 = text.render('Правила прежние, но теперь блоки', True, 'white')
    textstring2 = text.render('отбивают мяч', True, 'white')
    textstring3 = text2.render('используйте <- и -> для перемещения своей плитки', True, 'red')
    fps = 60
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEMOTION:
                sprite.rect.x, sprite.rect.y = event.pos
            if pygame.mouse.get_focused():
                pygame.mouse.set_visible(False)
            else:
                pygame.mouse.set_visible(True)
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                running = False
        screen.fill('black')
        screen.blit(background, backgroundrect)
        screen.blit(textrend, (400, 50))
        screen.blit(textstring1, (20, 220))
        screen.blit(textstring2, (20, 320))
        screen.blit(textstring3, (20, 420))
        screen.blit(textplay, (120, 600))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(fps)


def level4():
    pygame.display.set_caption('balls')
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
    fps = 60
    playerw = 300
    playerh = 40
    playerspd = 10
    bulletr = int(30 * 2 ** 0.5)
    bullet = pygame.Rect(bulletr, 360, bulletr, bulletr)
    bullets = 10
    player = pygame.Rect(640 - playerw // 2, 720 - playerh - 50, playerw, playerh)
    speedx = 1
    speedy = -1
    walls = []
    x = 20
    y = 50
    for i in range(3):
        for j in range(10):
            color = (random.randrange(1, 255), random.randrange(1, 255), random.randrange(1, 255))
            walls.append((pygame.Rect(x, y, 100, 30), color))
            x += 110
        x = 20
        y += 50
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEMOTION:
                sprite.rect.x, sprite.rect.y = event.pos
            if pygame.mouse.get_focused():
                pygame.mouse.set_visible(False)
            else:
                pygame.mouse.set_visible(True)
        if pygame.key.get_pressed()[pygame.K_LEFT] and player.left > 0:
            player.left -= playerspd
        elif pygame.key.get_pressed()[pygame.K_RIGHT] and player.right < 1280:
            player.right += playerspd
        screen.fill('black')
        screen.blit(background, backgroundrect)
        pygame.draw.circle(screen, 'red', bullet.center, 30)
        pygame.draw.rect(screen, 'green', player)
        bullet.x += bullets * speedx
        bullet.y += bullets * speedy
        if bullet.colliderect(player) and speedy > 0:
            speedy = -speedy
        if bullet.centery < 30:
            speedy = -speedy
        if bullet.centerx < 30 or bullet.centerx > 1250:
            speedx = -speedx
        if bullet.centery > 720:
            running = False
        for i in range(len(walls)):
            j = walls[i][0]
            if j.colliderect(bullet):
                walls.pop(i)
                speedy = -speedy
                break
        for i in walls:
            pygame.draw.rect(screen, i[1], i[0])
        if len(walls) == 0:
            with open('data/levelsinfo/5.txt', 'w', encoding='utf8') as data:
                data.write('open')
            running = False
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(fps)


def level4info():
    pygame.display.set_caption('balls')
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
    text = pygame.font.Font(None, 70)
    text2 = pygame.font.Font(None, 70)
    textrestart = pygame.font.Font(None, 70)
    textrend = text.render('Уровень 4', True, 'white')
    textplay = textrestart.render('Чтобы начать игру, нажмите любую клавишу', True, 'black')
    textstring1 = text.render('Наш мяч теперь намного быстрее', True, 'white')
    textstring2 = text.render('а блоков - больше', True, 'white')
    textstring3 = text2.render('используйте <- и -> для перемещения своей плитки', True, 'red')
    fps = 60
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEMOTION:
                sprite.rect.x, sprite.rect.y = event.pos
            if pygame.mouse.get_focused():
                pygame.mouse.set_visible(False)
            else:
                pygame.mouse.set_visible(True)
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                running = False
        screen.fill('black')
        screen.blit(background, backgroundrect)
        screen.blit(textrend, (400, 50))
        screen.blit(textstring1, (20, 220))
        screen.blit(textstring2, (20, 320))
        screen.blit(textstring3, (20, 420))
        screen.blit(textplay, (120, 600))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(fps)


def level5():
    pygame.display.set_caption('balls')
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
    fps = 60
    playerw = 300
    playerh = 40
    playerspd = 10
    bulletr = int(30 * 2 ** 0.5)
    bullet = pygame.Rect(bulletr, 360, bulletr, bulletr)
    bullets = 10
    player = pygame.Rect(640 - playerw // 2, 720 - playerh - 50, playerw, playerh)
    speedx = 1
    speedy = -1
    walls = []
    x = 20
    y = 50
    for i in range(3):
        for j in range(10):
            color = (random.randrange(1, 255), random.randrange(1, 255), random.randrange(1, 255))
            walls.append((pygame.Rect(x, y, 100, 30), color))
            x += 110
        x = 20
        y += 50
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEMOTION:
                sprite.rect.x, sprite.rect.y = event.pos
            if pygame.mouse.get_focused():
                pygame.mouse.set_visible(False)
            else:
                pygame.mouse.set_visible(True)
        if pygame.key.get_pressed()[pygame.K_LEFT] and player.left > 0:
            player.left -= playerspd
        elif pygame.key.get_pressed()[pygame.K_RIGHT] and player.right < 1280:
            player.right += playerspd
        screen.fill('black')
        screen.blit(background, backgroundrect)
        pygame.draw.circle(screen, 'red', bullet.center, 30)
        pygame.draw.rect(screen, 'green', player)
        bullet.x += bullets * speedx
        bullet.y += bullets * speedy
        if bullet.colliderect(player) and speedy > 0:
            speedy = -speedy
        if bullet.centery < 30:
            speedy = -speedy
        if bullet.centerx < 30 or bullet.centerx > 1250:
            speedx = -speedx
        if bullet.centery > 720:
            running = False
        for i in range(len(walls)):
            j = walls[i][0]
            if j.bottom == player.top:
                running = False
            if j.colliderect(bullet):
                walls.pop(i)
                speedy = -speedy
                break
        for i in range(len(walls)):
            j = walls[random.randrange(0, len(walls))][0]
            j.top += 1
            break
        for i in walls:
            pygame.draw.rect(screen, i[1], i[0])
        if len(walls) == 0:
            with open('data/levelsinfo/6.txt', 'w', encoding='utf8') as data:
                data.write('open')
            running = False
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(fps)


def level5info():
    pygame.display.set_caption('balls')
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
    text = pygame.font.Font(None, 70)
    text2 = pygame.font.Font(None, 70)
    textrestart = pygame.font.Font(None, 70)
    textrend = text.render('Уровень 5', True, 'white')
    textplay = textrestart.render('Чтобы начать игру, нажмите любую клавишу', True, 'black')
    textstring1 = text.render('Теперь блоки медленно падают вниз, если', True, 'white')
    textstring2 = text.render('они дойдут до вашей плитки - вы проиграете', True, 'white')
    textstring3 = text2.render('используйте <- и -> для перемещения своей плитки', True, 'red')
    fps = 60
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEMOTION:
                sprite.rect.x, sprite.rect.y = event.pos
            if pygame.mouse.get_focused():
                pygame.mouse.set_visible(False)
            else:
                pygame.mouse.set_visible(True)
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                running = False
        screen.fill('black')
        screen.blit(background, backgroundrect)
        screen.blit(textrend, (400, 50))
        screen.blit(textstring1, (20, 220))
        screen.blit(textstring2, (20, 320))
        screen.blit(textstring3, (20, 420))
        screen.blit(textplay, (120, 600))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(fps)


def level6():
    pygame.display.set_caption('balls')
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
    fps = 60
    playerw = 800
    playerh = 40
    playerspd = 10
    bulletr = int(30 * 2 ** 0.5)
    bullet = pygame.Rect(bulletr, 360, bulletr, bulletr)
    bullets = 20
    player = pygame.Rect(640 - playerw // 2, 720 - playerh - 50, playerw, playerh)
    speedx = 1
    speedy = -1
    walls = []
    x = 20
    y = 50
    for i in range(3):
        for j in range(10):
            color = (random.randrange(1, 255), random.randrange(1, 255), random.randrange(1, 255))
            walls.append((pygame.Rect(x, y, 100, 30), color))
            x += 110
        x = 20
        y += 50
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEMOTION:
                sprite.rect.x, sprite.rect.y = event.pos
            if pygame.mouse.get_focused():
                pygame.mouse.set_visible(False)
            else:
                pygame.mouse.set_visible(True)
        if pygame.key.get_pressed()[pygame.K_LEFT] and player.left > 0:
            player.left -= playerspd
        elif pygame.key.get_pressed()[pygame.K_RIGHT] and player.right < 1280:
            player.right += playerspd
        screen.fill('black')
        screen.blit(background, backgroundrect)
        pygame.draw.circle(screen, 'red', bullet.center, 30)
        pygame.draw.rect(screen, 'green', player)
        bullet.x += bullets * speedx
        bullet.y += bullets * speedy
        if bullet.colliderect(player) and speedy > 0:
            speedy = -speedy
        if bullet.centery < 30:
            speedy = -speedy
        if bullet.centerx < 30 or bullet.centerx > 1250:
            speedx = -speedx
        if bullet.centery > 720:
            running = False
        for i in range(len(walls)):
            j = walls[i][0]
            if j.bottom == player.top:
                running = False
            if j.colliderect(bullet):
                walls.pop(i)
                speedy = -speedy
                break
        for i in range(len(walls)):
            j = walls[random.randrange(0, len(walls))][0]
            j.top += 1
            break
        for i in walls:
            pygame.draw.rect(screen, i[1], i[0])
        if len(walls) == 0:
            with open('data/levelsinfo/7.txt', 'w', encoding='utf8') as data:
                data.write('open')
            running = False
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(fps)


def level6info():
    pygame.display.set_caption('balls')
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
    text = pygame.font.Font(None, 70)
    text2 = pygame.font.Font(None, 70)
    textrestart = pygame.font.Font(None, 70)
    textrend = text.render('Уровень 6', True, 'white')
    textplay = textrestart.render('Чтобы начать игру, нажмите любую клавишу', True, 'black')
    textstring1 = text.render('Теперь ваша плитка - гигантская, а', True, 'white')
    textstring2 = text.render('мяч - очень быстрый', True, 'white')
    textstring3 = text2.render('используйте <- и -> для перемещения своей плитки', True, 'red')
    fps = 60
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEMOTION:
                sprite.rect.x, sprite.rect.y = event.pos
            if pygame.mouse.get_focused():
                pygame.mouse.set_visible(False)
            else:
                pygame.mouse.set_visible(True)
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                running = False
        screen.fill('black')
        screen.blit(background, backgroundrect)
        screen.blit(textrend, (400, 50))
        screen.blit(textstring1, (20, 220))
        screen.blit(textstring2, (20, 320))
        screen.blit(textstring3, (20, 420))
        screen.blit(textplay, (120, 600))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(fps)


def level7info():
    pygame.display.set_caption('balls')
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
    text = pygame.font.Font(None, 70)
    text2 = pygame.font.Font(None, 70)
    textrestart = pygame.font.Font(None, 70)
    textrend = text.render('Уровень 7', True, 'white')
    textplay = textrestart.render('Чтобы начать игру, нажмите любую клавишу', True, 'black')
    textstring1 = text.render('Правила из первых уровней,', True, 'white')
    textstring2 = text.render('но блоков еще больше', True, 'white')
    textstring3 = text2.render('используйте <- и -> для перемещения своей плитки', True, 'red')
    fps = 60
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEMOTION:
                sprite.rect.x, sprite.rect.y = event.pos
            if pygame.mouse.get_focused():
                pygame.mouse.set_visible(False)
            else:
                pygame.mouse.set_visible(True)
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                running = False
        screen.fill('black')
        screen.blit(background, backgroundrect)
        screen.blit(textrend, (400, 50))
        screen.blit(textstring1, (20, 220))
        screen.blit(textstring2, (20, 320))
        screen.blit(textstring3, (20, 420))
        screen.blit(textplay, (120, 600))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(fps)


def level7():
    pygame.display.set_caption('balls')
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
    fps = 60
    playerw = 300
    playerh = 40
    playerspd = 10
    bulletr = int(30 * 2 ** 0.5)
    bullet = pygame.Rect(bulletr, 360, bulletr, bulletr)
    bullets = 10
    player = pygame.Rect(640 - playerw // 2, 720 - playerh - 50, playerw, playerh)
    speedx = 1
    speedy = -1
    walls = []
    x = 20
    y = 50
    for i in range(3):
        for j in range(15):
            color = (random.randrange(1, 255), random.randrange(1, 255), random.randrange(1, 255))
            walls.append((pygame.Rect(x, y, 70, 30), color))
            x += 80
        x = 20
        y += 50
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEMOTION:
                sprite.rect.x, sprite.rect.y = event.pos
            if pygame.mouse.get_focused():
                pygame.mouse.set_visible(False)
            else:
                pygame.mouse.set_visible(True)
        if pygame.key.get_pressed()[pygame.K_LEFT] and player.left > 0:
            player.left -= playerspd
        elif pygame.key.get_pressed()[pygame.K_RIGHT] and player.right < 1280:
            player.right += playerspd
        screen.fill('black')
        screen.blit(background, backgroundrect)
        pygame.draw.circle(screen, 'red', bullet.center, 30)
        pygame.draw.rect(screen, 'green', player)
        bullet.x += bullets * speedx
        bullet.y += bullets * speedy
        if bullet.colliderect(player) and speedy > 0:
            speedy = -speedy
        if bullet.centery < 30:
            speedy = -speedy
        if bullet.centerx < 30 or bullet.centerx > 1250:
            speedx = -speedx
        if bullet.centery > 720:
            running = False
        for i in range(len(walls)):
            j = walls[i][0]
            if j.colliderect(bullet):
                walls.pop(i)
                speedy = -speedy
                break
        for i in walls:
            pygame.draw.rect(screen, i[1], i[0])
        if len(walls) == 0:
            with open('data/levelsinfo/8.txt', 'w', encoding='utf8') as data:
                data.write('open')
            running = False
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(fps)


def level8info():
    pygame.display.set_caption('balls')
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
    text = pygame.font.Font(None, 70)
    text2 = pygame.font.Font(None, 70)
    textrestart = pygame.font.Font(None, 70)
    textrend = text.render('Уровень 8', True, 'white')
    textplay = textrestart.render('Чтобы начать игру, нажмите любую клавишу', True, 'black')
    textstring1 = text.render('Правила из первых уровней,', True, 'white')
    textstring2 = text.render('но плитка движется в другую сторону', True, 'white')
    textstring3 = text2.render('используйте <- и -> для перемещения своей плитки', True, 'red')
    fps = 60
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEMOTION:
                sprite.rect.x, sprite.rect.y = event.pos
            if pygame.mouse.get_focused():
                pygame.mouse.set_visible(False)
            else:
                pygame.mouse.set_visible(True)
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                running = False
        screen.fill('black')
        screen.blit(background, backgroundrect)
        screen.blit(textrend, (400, 50))
        screen.blit(textstring1, (20, 220))
        screen.blit(textstring2, (20, 320))
        screen.blit(textstring3, (20, 420))
        screen.blit(textplay, (120, 600))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(fps)


def level8():
    pygame.display.set_caption('balls')
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
    fps = 60
    playerw = 300
    playerh = 40
    playerspd = 10
    bulletr = int(30 * 2 ** 0.5)
    bullet = pygame.Rect(bulletr, 360, bulletr, bulletr)
    bullets = 10
    player = pygame.Rect(640 - playerw // 2, 720 - playerh - 50, playerw, playerh)
    speedx = 1
    speedy = -1
    walls = []
    x = 20
    y = 50
    for i in range(3):
        for j in range(15):
            color = (random.randrange(1, 255), random.randrange(1, 255), random.randrange(1, 255))
            walls.append((pygame.Rect(x, y, 70, 30), color))
            x += 80
        x = 20
        y += 50
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEMOTION:
                sprite.rect.x, sprite.rect.y = event.pos
            if pygame.mouse.get_focused():
                pygame.mouse.set_visible(False)
            else:
                pygame.mouse.set_visible(True)
        if pygame.key.get_pressed()[pygame.K_LEFT] and player.right < 1280:
            player.left += playerspd
        elif pygame.key.get_pressed()[pygame.K_RIGHT] and player.left > 0:
            player.right -= playerspd
        screen.fill('black')
        screen.blit(background, backgroundrect)
        pygame.draw.circle(screen, 'red', bullet.center, 30)
        pygame.draw.rect(screen, 'green', player)
        bullet.x += bullets * speedx
        bullet.y += bullets * speedy
        if bullet.colliderect(player) and speedy > 0:
            speedy = -speedy
        if bullet.centery < 30:
            speedy = -speedy
        if bullet.centerx < 30 or bullet.centerx > 1250:
            speedx = -speedx
        if bullet.centery > 720:
            running = False
        for i in range(len(walls)):
            j = walls[i][0]
            if j.colliderect(bullet):
                walls.pop(i)
                speedy = -speedy
                break
        for i in walls:
            pygame.draw.rect(screen, i[1], i[0])
        if len(walls) == 0:
            with open('data/levelsinfo/9.txt', 'w', encoding='utf8') as data:
                data.write('open')
            running = False
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(fps)


def level9info():
    pygame.display.set_caption('balls')
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
    text = pygame.font.Font(None, 70)
    text2 = pygame.font.Font(None, 70)
    textrestart = pygame.font.Font(None, 70)
    textrend = text.render('Уровень 9', True, 'white')
    textplay = textrestart.render('Чтобы начать игру, нажмите любую клавишу', True, 'black')
    textstring1 = text.render('Правила из первых уровней,', True, 'white')
    textstring2 = text.render('но плитка немного меньше', True, 'white')
    textstring3 = text2.render('используйте <- и -> для перемещения своей плитки', True, 'red')
    fps = 60
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEMOTION:
                sprite.rect.x, sprite.rect.y = event.pos
            if pygame.mouse.get_focused():
                pygame.mouse.set_visible(False)
            else:
                pygame.mouse.set_visible(True)
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                running = False
        screen.fill('black')
        screen.blit(background, backgroundrect)
        screen.blit(textrend, (400, 50))
        screen.blit(textstring1, (20, 220))
        screen.blit(textstring2, (20, 320))
        screen.blit(textstring3, (20, 420))
        screen.blit(textplay, (120, 600))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(fps)


def level9():
    pygame.display.set_caption('balls')
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
    fps = 60
    playerw = 200
    playerh = 30
    playerspd = 10
    bulletr = int(30 * 2 ** 0.5)
    bullet = pygame.Rect(bulletr, 360, bulletr, bulletr)
    bullets = 10
    player = pygame.Rect(640 - playerw // 2, 720 - playerh - 50, playerw, playerh)
    speedx = 1
    speedy = -1
    walls = []
    x = 20
    y = 50
    for i in range(3):
        for j in range(15):
            color = (random.randrange(1, 255), random.randrange(1, 255), random.randrange(1, 255))
            walls.append((pygame.Rect(x, y, 70, 30), color))
            x += 80
        x = 20
        y += 50
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEMOTION:
                sprite.rect.x, sprite.rect.y = event.pos
            if pygame.mouse.get_focused():
                pygame.mouse.set_visible(False)
            else:
                pygame.mouse.set_visible(True)
        if pygame.key.get_pressed()[pygame.K_LEFT] and player.left > 0:
            player.left -= playerspd
        elif pygame.key.get_pressed()[pygame.K_RIGHT] and player.right < 1280:
            player.right += playerspd
        screen.fill('black')
        screen.blit(background, backgroundrect)
        pygame.draw.circle(screen, 'red', bullet.center, 30)
        pygame.draw.rect(screen, 'green', player)
        bullet.x += bullets * speedx
        bullet.y += bullets * speedy
        if bullet.colliderect(player) and speedy > 0:
            speedy = -speedy
        if bullet.centery < 30:
            speedy = -speedy
        if bullet.centerx < 30 or bullet.centerx > 1250:
            speedx = -speedx
        if bullet.centery > 720:
            running = False
        for i in range(len(walls)):
            j = walls[i][0]
            if j.colliderect(bullet):
                walls.pop(i)
                speedy = -speedy
                break
        for i in walls:
            pygame.draw.rect(screen, i[1], i[0])
        if len(walls) == 0:
            with open('data/levelsinfo/10.txt', 'w', encoding='utf8') as data:
                data.write('open')
            running = False
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(fps)


def level10info():
    pygame.display.set_caption('balls')
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
    text = pygame.font.Font(None, 70)
    text2 = pygame.font.Font(None, 70)
    textrestart = pygame.font.Font(None, 70)
    textrend = text.render('Уровень 9', True, 'white')
    textplay = textrestart.render('Чтобы начать игру, нажмите любую клавишу', True, 'black')
    textstring1 = text.render('Смешенные правила с первых', True, 'white')
    textstring2 = text.render('уровней', True, 'white')
    textstring3 = text2.render('используйте <- и -> для перемещения своей плитки', True, 'red')
    fps = 60
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEMOTION:
                sprite.rect.x, sprite.rect.y = event.pos
            if pygame.mouse.get_focused():
                pygame.mouse.set_visible(False)
            else:
                pygame.mouse.set_visible(True)
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                running = False
        screen.fill('black')
        screen.blit(background, backgroundrect)
        screen.blit(textrend, (400, 50))
        screen.blit(textstring1, (20, 220))
        screen.blit(textstring2, (20, 320))
        screen.blit(textstring3, (20, 420))
        screen.blit(textplay, (120, 600))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(fps)


def level10():
    pygame.display.set_caption('balls')
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
    fps = 60
    playerw = 700
    playerh = 50
    playerspd = 20
    bulletr = int(30 * 2 ** 0.5)
    bullet = pygame.Rect(bulletr, 360, bulletr, bulletr)
    bullets = 15
    player = pygame.Rect(640 - playerw // 2, 720 - playerh - 50, playerw, playerh)
    speedx = 1
    speedy = -1
    walls = []
    x = 20
    y = 50
    for i in range(3):
        for j in range(15):
            color = (random.randrange(1, 255), random.randrange(1, 255), random.randrange(1, 255))
            walls.append((pygame.Rect(x, y, 70, 30), color))
            x += 80
        x = 20
        y += 50
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEMOTION:
                sprite.rect.x, sprite.rect.y = event.pos
            if pygame.mouse.get_focused():
                pygame.mouse.set_visible(False)
            else:
                pygame.mouse.set_visible(True)
        if pygame.key.get_pressed()[pygame.K_LEFT] and player.left > 0:
            player.left -= playerspd
        elif pygame.key.get_pressed()[pygame.K_RIGHT] and player.right < 1280:
            player.right += playerspd
        screen.fill('black')
        screen.blit(background, backgroundrect)
        pygame.draw.circle(screen, 'red', bullet.center, 30)
        pygame.draw.rect(screen, 'green', player)
        bullet.x += bullets * speedx
        bullet.y += bullets * speedy
        if bullet.colliderect(player) and speedy > 0:
            speedy = -speedy
        if bullet.centery < 30:
            speedy = -speedy
        if bullet.centerx < 30 or bullet.centerx > 1250:
            speedx = -speedx
        if bullet.centery > 720:
            running = False
        for i in range(len(walls)):
            j = walls[i][0]
            if j.colliderect(bullet):
                walls.pop(i)
                speedy = -speedy
                break
        for i in walls:
            pygame.draw.rect(screen, i[1], i[0])
        if len(walls) == 0:
            with open('data/levelsinfo/11.txt', 'w', encoding='utf8') as data:
                data.write('open')
            running = False
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(fps)


def level11info():
    pygame.display.set_caption('balls')
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
    text = pygame.font.Font(None, 70)
    text2 = pygame.font.Font(None, 70)
    textrestart = pygame.font.Font(None, 70)
    textrend = text.render('Уровень 11', True, 'white')
    textplay = textrestart.render('Чтобы начать игру, нажмите любую клавишу', True, 'black')
    textstring1 = text.render('Смешенные правила с первых', True, 'white')
    textstring2 = text.render('уровней', True, 'white')
    textstring3 = text2.render('используйте <- и -> для перемещения своей плитки', True, 'red')
    fps = 60
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEMOTION:
                sprite.rect.x, sprite.rect.y = event.pos
            if pygame.mouse.get_focused():
                pygame.mouse.set_visible(False)
            else:
                pygame.mouse.set_visible(True)
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                running = False
        screen.fill('black')
        screen.blit(background, backgroundrect)
        screen.blit(textrend, (400, 50))
        screen.blit(textstring1, (20, 220))
        screen.blit(textstring2, (20, 320))
        screen.blit(textstring3, (20, 420))
        screen.blit(textplay, (120, 600))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(fps)


def level11():
    pygame.display.set_caption('balls')
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
    fps = 60
    playerw = 700
    playerh = 50
    playerspd = 20
    bulletr = int(30 * 2 ** 0.5)
    bullet = pygame.Rect(bulletr, 360, bulletr, bulletr)
    bullets = 15
    player = pygame.Rect(640 - playerw // 2, 720 - playerh - 50, playerw, playerh)
    speedx = 1
    speedy = -1
    walls = []
    x = 20
    y = 50
    for i in range(3):
        for j in range(15):
            color = (random.randrange(1, 255), random.randrange(1, 255), random.randrange(1, 255))
            walls.append((pygame.Rect(x, y, 70, 30), color))
            x += 80
        x = 20
        y += 50
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEMOTION:
                sprite.rect.x, sprite.rect.y = event.pos
            if pygame.mouse.get_focused():
                pygame.mouse.set_visible(False)
            else:
                pygame.mouse.set_visible(True)
        if pygame.key.get_pressed()[pygame.K_LEFT] and player.left > 0:
            player.left -= playerspd
        elif pygame.key.get_pressed()[pygame.K_RIGHT] and player.right < 1280:
            player.right += playerspd
        screen.fill('black')
        screen.blit(background, backgroundrect)
        pygame.draw.circle(screen, 'red', bullet.center, 30)
        pygame.draw.rect(screen, 'green', player)
        bullet.x += bullets * speedx
        bullet.y += bullets * speedy
        if bullet.colliderect(player) and speedy > 0:
            speedy = -speedy
        if bullet.centery < 30:
            speedy = -speedy
        if bullet.centerx < 30 or bullet.centerx > 1250:
            speedx = -speedx
        if bullet.centery > 720:
            running = False
        for i in range(len(walls)):
            j = walls[i][0]
            if j.bottom == player.top:
                running = False
            if j.colliderect(bullet):
                walls.pop(i)
                speedy = -speedy
                break
        for i in range(len(walls)):
            j = walls[random.randrange(len(walls))][0]
            j.top += 1
            break
        for i in walls:
            pygame.draw.rect(screen, i[1], i[0])
        if len(walls) == 0:
            with open('data/levelsinfo/12.txt', 'w', encoding='utf8') as data:
                data.write('open')
            running = False
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(fps)


def level12info():
    pygame.display.set_caption('balls')
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
    text = pygame.font.Font(None, 70)
    text2 = pygame.font.Font(None, 70)
    textrestart = pygame.font.Font(None, 70)
    textrend = text.render('Уровень 12', True, 'white')
    textplay = textrestart.render('Чтобы начать игру, нажмите любую клавишу', True, 'black')
    textstring1 = text.render('Смешенные правила всех', True, 'white')
    textstring2 = text.render('уровней', True, 'white')
    textstring3 = text2.render('используйте <- и -> для перемещения своей плитки', True, 'red')
    fps = 60
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEMOTION:
                sprite.rect.x, sprite.rect.y = event.pos
            if pygame.mouse.get_focused():
                pygame.mouse.set_visible(False)
            else:
                pygame.mouse.set_visible(True)
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                running = False
        screen.fill('black')
        screen.blit(background, backgroundrect)
        screen.blit(textrend, (400, 50))
        screen.blit(textstring1, (20, 220))
        screen.blit(textstring2, (20, 320))
        screen.blit(textstring3, (20, 420))
        screen.blit(textplay, (120, 600))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(fps)


def level12():
    pygame.display.set_caption('balls')
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
    fps = 60
    playerw = 700
    playerh = 50
    playerspd = 20
    bulletr = int(30 * 2 ** 0.5)
    bullet = pygame.Rect(bulletr, 360, bulletr, bulletr)
    bullets = 15
    player = pygame.Rect(640 - playerw // 2, 720 - playerh - 50, playerw, playerh)
    speedx = 1
    speedy = -1
    walls = []
    x = 20
    y = 50
    for i in range(3):
        for j in range(15):
            color = (random.randrange(1, 255), random.randrange(1, 255), random.randrange(1, 255))
            walls.append((pygame.Rect(x, y, 70, 30), color))
            x += 80
        x = 20
        y += 50
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEMOTION:
                sprite.rect.x, sprite.rect.y = event.pos
            if pygame.mouse.get_focused():
                pygame.mouse.set_visible(False)
            else:
                pygame.mouse.set_visible(True)
        if pygame.key.get_pressed()[pygame.K_LEFT] and player.right < 1280:
            player.left += playerspd
        elif pygame.key.get_pressed()[pygame.K_RIGHT] and player.left > 0:
            player.right -= playerspd
        screen.fill('black')
        screen.blit(background, backgroundrect)
        pygame.draw.circle(screen, 'red', bullet.center, 30)
        pygame.draw.rect(screen, 'green', player)
        bullet.x += bullets * speedx
        bullet.y += bullets * speedy
        if bullet.colliderect(player) and speedy > 0:
            speedy = -speedy
        if bullet.centery < 30:
            speedy = -speedy
        if bullet.centerx < 30 or bullet.centerx > 1250:
            speedx = -speedx
        if bullet.centery > 720:
            running = False
        for i in range(len(walls)):
            j = walls[i][0]
            if j.bottom == player.top:
                running = False
            if j.colliderect(bullet):
                walls.pop(i)
                speedy = -speedy
                break
        for i in range(len(walls)):
            j = walls[random.randrange(len(walls))][0]
            j.top += 1
            break
        for i in walls:
            pygame.draw.rect(screen, i[1], i[0])
        if len(walls) == 0:
            running = False
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(fps)
