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
    pygame.display.set_caption('snake')
    size = width, height = 1280, 720
    screen = pygame.display.set_mode(size)
    background = load_image("background.png")
    background = pygame.transform.scale(background, (1280, 720))
    backgroundrect = background.get_rect()
    clock = pygame.time.Clock()
    fps = 60
    text = pygame.font.Font(None, 80)
    running = True
    speedx = 0
    speedy = 0
    x = random.randrange(300, 600)
    y = random.randrange(100, 300)
    snakebody = [pygame.Rect(x, y, 50, 50)]
    snake = 1
    pygame.mouse.set_visible(False)
    xf = random.randrange(200, 600, 50)
    yf = random.randrange(200, 600, 50)
    food = pygame.Rect(xf, yf, 50, 50)
    textrend = text.render('Длина:' + str(snake), True, 'white')
    speedm = 5
    speed = speedm // 1
    moved = None
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        if pygame.key.get_pressed()[pygame.K_LEFT] and moved != 'right':
            moved = 'left'
            speedx = -1
            speedy = 0
        elif pygame.key.get_pressed()[pygame.K_RIGHT] and moved != 'left':
            moved = 'right'
            speedx = 1
            speedy = 0
        elif pygame.key.get_pressed()[pygame.K_UP] and moved != 'down':
            moved = 'up'
            speedx = 0
            speedy = -1
        elif pygame.key.get_pressed()[pygame.K_DOWN] and moved != 'up':
            moved = 'down'
            speedx = 0
            speedy = 1
        x += speedx * speed
        y += speedy * speed
        snakebody.append(pygame.Rect(x, y, 50, 50))
        snakebody = snakebody[-snake:]
        for i in snakebody:
            if food.colliderect(i[0], i[1], 50, 50):
                snake += 1
                speedm += 0.2
                speed = speedm // 1
                xf = random.randrange(50, 1200, 50)
                yf = random.randrange(50, 700, 50)
                food = pygame.Rect(xf, yf, 50, 50)
                textrend = text.render('Длина:' + str(snake), True, 'white')
        screen.fill('black')
        screen.blit(background, backgroundrect)
        for i in snakebody:
            if i.x < 0 or i.x > 1230:
                running = False
            if i.y < 0 or i.y > 670:
                running = False
        for i in snakebody:
            pygame.draw.rect(screen, 'blue', i)
        pygame.draw.rect(screen, 'green', food)
        screen.blit(textrend, (30, 20))
        pygame.display.flip()
        clock.tick(fps)
