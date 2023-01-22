import os
import sys
import pygame
import tictactoe
import words
import arca
import balls


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


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Launcher')
    size = width, height = 1280, 720
    screen = pygame.display.set_mode(size)
    all_sprites = pygame.sprite.Group()
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("Blue_Arrow.png")
    sprite.rect = sprite.image.get_rect()
    all_sprites.add(sprite)
    sprite.rect.x = 5
    sprite.rect.y = 20
    background = load_image("background.png")
    background = pygame.transform.scale(background, (1280, 720))
    backgroundrect = background.get_rect()
    text = pygame.font.Font(None, 34)
    text2 = pygame.font.Font(None, 40)
    texttitle = pygame.font.Font(None, 100)
    textrend = text.render('Крестики-Нолики', True, 'white')
    textrend2 = text2.render('Слова из букв', True, 'white')
    textrend3 = text2.render('Шашки', True, 'white')
    textrend4 = text2.render('Арканоид', True, 'white')
    texttitlerend = texttitle.render('Выберете игру из списка', True, 'white')
    clock = pygame.time.Clock()
    gameicons = []
    for i in range(1, 5):
        gameicon = load_image(str(i) + '.png')
        gameicon = pygame.transform.scale(gameicon, (200, 200))
        gameicons.append(gameicon)
    fps = 60
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if 100 < event.pos[0] < 300 and 100 < event.pos[1] < 300:
                    tictactoe.start()
                if 500 < event.pos[0] < 700 and 100 < event.pos[1] < 300:
                    words.start()
                if 900 < event.pos[0] < 1100 and 100 < event.pos[1] < 300:
                    arca.start()
                if 100 < event.pos[0] < 300 and 400 < event.pos[1] < 600:
                    balls.start()
            if event.type == pygame.MOUSEMOTION:
                sprite.rect.x, sprite.rect.y = event.pos
            if pygame.mouse.get_focused():
                pygame.mouse.set_visible(False)
            else:
                pygame.mouse.set_visible(True)
        screen.fill('black')
        screen.blit(background, backgroundrect)
        x = 100
        y = 100
        c = 0
        for i in gameicons:
            c += 1
            if c != 4:
                screen.blit(i, (x, y))
            if c == 1:
                screen.blit(textrend, (x, y + 200 + 20))
            elif c == 2:
                screen.blit(textrend2, (x, y + 200 + 20))
            elif c == 3:
                screen.blit(textrend3, (x, y + 200 + 20))
            elif c == 4:
                y += 300
                x = 100
                screen.blit(i, (x, y))
                screen.blit(textrend4, (x, y + 200 + 20))
            x += 400
        screen.blit(texttitlerend, (200, 20))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
