import os
import sys
import pymorphy2
import pygame_gui
from pygame_gui.elements.ui_text_entry_line import UITextEntryLine
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


def start():
    pygame.display.set_caption('words')
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
    letters = [chr(i) for i in range(ord('а'), ord('а') + 32)]
    letters.append('ё')
    random.shuffle(letters)
    selectedletters = []
    a = random.randint(7, 15)
    for i in range(a):
        selectedletters.append(letters[random.randrange(0, 33)])
    text = pygame.font.Font(None, 90)
    text2 = pygame.font.Font(None, 80)
    textrestart = pygame.font.Font(None, 70)
    textrend = text.render('Вам даны буквы:', True, 'white')
    textrestart1 = textrestart.render('Сменить', True, 'black')
    textrestart2 = textrestart.render('буквы', True, 'black')
    textplay = textrestart.render('Играть', True, 'black')
    textrendletters = text.render(', '.join(selectedletters), True, 'green')
    textstring1 = text.render('Необходимо составить из них', True, 'white')
    textstring2 = text.render('наибольшее количество слов.', True, 'white')
    textstring3 = text2.render('Регистр букв и буквы е-ё имеют значение.', True, 'red')
    buttonscolors = ['grey', 'grey']
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if 330 < event.pos[0] < 530 and 580 < event.pos[1] < 680:
                    playing(selectedletters)
                    running = False
                if 730 < event.pos[0] < 930 and 580 < event.pos[1] < 680:
                    a = random.randint(7, 15)
                    selectedletters = []
                    for i in range(a):
                        letter = letters[random.randrange(0, 33)]
                        while letter in selectedletters:
                            letter = letters[random.randrange(0, 33)]
                        selectedletters.append(letter)
                    textrendletters = text.render(', '.join(selectedletters), True, 'green')
            if event.type == pygame.MOUSEMOTION:
                sprite.rect.x, sprite.rect.y = event.pos
                if 330 < event.pos[0] < 530 and 580 < event.pos[1] < 680:
                    buttonscolors[0] = 'green'
                else:
                    buttonscolors[0] = 'grey'
                if 730 < event.pos[0] < 930 and 580 < event.pos[1] < 680:
                    buttonscolors[1] = 'green'
                else:
                    buttonscolors[1] = 'grey'
            if pygame.mouse.get_focused():
                pygame.mouse.set_visible(False)
            else:
                pygame.mouse.set_visible(True)
        screen.fill('black')
        screen.blit(background, backgroundrect)
        screen.blit(textrend, (400, 50))
        x = 400 - 20 * len(selectedletters)
        screen.blit(textrendletters, (x, 120))
        screen.blit(textstring1, (20, 220))
        screen.blit(textstring2, (20, 320))
        screen.blit(textstring3, (20, 420))
        pygame.draw.rect(screen, buttonscolors[0], (330, 580, 200, 100))
        pygame.draw.rect(screen, buttonscolors[1], (730, 580, 200, 100))
        screen.blit(textrestart1, (730, 580))
        screen.blit(textrestart2, (730, 630))
        screen.blit(textplay, (340, 600))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(fps)


def playing(letters):
    pygame.display.set_caption('words')
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
    text = pygame.font.Font(None, 80)
    textfortest = pygame.font.Font(None, 50)
    textrend = text.render('Буквы: ' + ', '.join(letters), True, 'white')
    exitcolor = 'grey'
    textexit = text.render('Закончить', True, 'black')
    manager = pygame_gui.UIManager((1280, 720))
    text_input = UITextEntryLine(relative_rect=pygame.Rect(500, 500, 300, 50), manager=manager)
    morph = pymorphy2.MorphAnalyzer()
    register = ''
    usedwords = []
    bigscore = 0
    with open('data/Saves/wordsrecord.txt', 'r', encoding='utf8') as a:
        line = a.readline()
        bigscore = int(line)
    score = 0
    running = True
    while running:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                    if event.ui_element == text_input:
                        entered_text = event.text
                        bad = []
                        flag = True
                        for i in entered_text:
                            if i not in letters and i not in bad:
                                bad.append(i)
                                flag = False
                        if len(bad) > 0:
                            register = 'Ой! Вы использовали недопустимый символ: ' + ', '.join(bad)
                            flag = False
                        else:
                            try:
                                test_word = morph.word_is_known(entered_text)
                                if not test_word:
                                    register = 'Кажется, это не слово, или его нет в словаре'
                                    flag = False
                                else:
                                    if entered_text not in usedwords:
                                        score += 1
                                        if score > bigscore:
                                            bigscore = score
                                        usedwords.append(entered_text)
                                    else:
                                        register = 'Вы уже вводили это слово'
                                        flag = False
                            except:
                                register = 'Ой, кажется это не слово.'
                                flag = False
                        if flag:
                            register = ''
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if 900 < event.pos[0] < 1200 and 600 < event.pos[1] < 700:
                    with open('data/Saves/wordsrecord.txt', 'w', encoding='utf8') as a:
                        a.write(str(bigscore))
                    running = False
            if event.type == pygame.MOUSEMOTION:
                sprite.rect.x, sprite.rect.y = event.pos
                if 900 < event.pos[0] < 1200 and 600 < event.pos[1] < 700:
                    exitcolor = 'green'
                else:
                    exitcolor = 'grey'
            if pygame.mouse.get_focused():
                pygame.mouse.set_visible(False)
            else:
                pygame.mouse.set_visible(True)
            manager.process_events(event)
        manager.update(time_delta)
        screen.fill('black')
        screen.blit(background, backgroundrect)
        screen.blit(textrend, (20, 50))
        pygame.draw.rect(screen, exitcolor, (900, 600, 300, 100))
        screen.blit(textexit, (900, 615))
        infotext = textfortest.render(register, True, 'red')
        screen.blit(infotext, (20, 300))
        scoretext = text.render('Рекорд: ' + str(score) + '/' + str(bigscore), True, 'white')
        screen.blit(scoretext, (20, 120))
        manager.draw_ui(screen)
        all_sprites.draw(screen)
        pygame.display.flip()
