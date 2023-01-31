import pygame
import sys

pygame.font.init()

size = width, height = 500, 500
screen = pygame.display.set_mode(size)

USERNAME = None


def draw_intro():
    imgtank = pygame.image.load('tanki.jpg')
    words = pygame.font.SysFont('calibri', 45)
    text_welcome = words.render('Игра "Танки"', True, 'white')
    name = 'Введите имя:'
    is_find_name = False
    while not is_find_name:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    if name == 'Введите имя:':
                        name = event.unicode
                    else:
                        name += event.unicode
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif event.key == pygame.K_RETURN:
                    if len(name) > 2:
                        global USERNAME
                        USERNAME = name
                        is_find_name = True
                        break

        screen.fill('black')
        text_name = words.render(name, True, 'white')
        rect_name = text_name.get_rect()
        rect_name.center = screen.get_rect().center
        screen.blit(pygame.transform.scale(imgtank, [200, 200]), [10, 10])
        screen.blit(text_welcome, (250, 60))
        screen.blit(text_name, rect_name)
        pygame.display.update()
    screen.fill('black')


draw_intro()


def draw_game_over():
    words = pygame.font.SysFont('calibri', 35)
    word = pygame.font.SysFont('calibri', 25)
    text_gameover = words.render('Игра завершена!', True, 'white')
    text_score = words.render('Ваш счет: {# ПЕРЕМЕННАЯ ОТВЕЧАЮЩАЯ ЗА СЧЕТ}', True, 'white')
    text_i = word.render('Для рестарта игры нажмите клавишу пробел', True, 'white')
    imgtank = pygame.image.load('tanki.jpg')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    draw_intro()

        screen.fill('black')
        screen.blit(text_gameover, (230, 60))
        screen.blit(pygame.transform.scale(imgtank, [200, 200]), [10, 10])
        screen.blit(text_score, (30, 250))
        screen.blit(text_i, (15, 400))
        pygame.display.update()

        screen.fill('black')


draw_game_over()

pygame.quit()
