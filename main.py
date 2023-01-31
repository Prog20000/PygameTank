import pygame
import sys
import os

pygame.font.init()
FPS = 60
W = 570
H = 570
BLUE = (0, 70, 225)

sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
rim = False

USERNAME = None
glav = True
x = 266
y = 532
mi = 225
li = 225
r = 10
y1 = y
all_sprites = pygame.sprite.Group()
prep_coordinates = [[76, 76, 'n'], [76, 152, 'n'], [76, 266, 'r']]
mine = [[228, 190], [304, 228], [190, 380]]
kopy = mine
mine1 = [[304, 190], [76, 380], [190, 266]]
death = False


def load_image(name, colorkey=None):
    fullname = os.path.join(name)
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


bg = pygame.image.load("3333.jpg")
image = load_image("tank.jpg")
imagek1 = load_image("tank2.jpg")
imagek2 = load_image("tank3.jpg")
imagek3 = load_image("tank4.jpg")
image1 = load_image("bul.jpg")
prep = load_image("prep.jpg")
prep2 = load_image("prep2.jpg")
prep1 = load_image("prep1.jpg")
vz = load_image("vz.jpg")
zv = load_image("zve.jpg")
vrag = load_image("vrag.jpg")
vrag2 = load_image("vrag2.jpg")
vrag3 = load_image("vrag3.jpg")
vrag4 = load_image("vrag4.jpg")
mina = load_image("mina.jpg")
mata = False
kount = 0
lu = True
mark1 = True
pol = 0
pira = True
vy = 0
running = True
while running:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                for kila in range(len(prep_coordinates)):
                    if x - 38 == prep_coordinates[kila][0] and y == prep_coordinates[kila][1]:
                        pira = False
                if pira:
                    x -= 38
                    if x == 76 and y == 266:
                        mata = True
                    for ku in range(len(mine)):
                        if x == mine[ku][0] and y == mine[ku][1]:
                            death = True
                    pol = 3
                pira = True
            elif i.key == pygame.K_RIGHT:
                for kila in range(len(prep_coordinates)):
                    if x + 38 == prep_coordinates[kila][0] and y == prep_coordinates[kila][1]:
                        pira = False
                if pira:
                    x += 38
                    if x == 76 and y == 266:
                        mata = True
                    for ku in range(len(mine)):
                        if x == mine[ku][0] and y == mine[ku][1]:
                            death = True
                    pol = 1
                pira = True
            if i.key == pygame.K_UP:
                for kila in range(len(prep_coordinates)):
                    if x == prep_coordinates[kila][0] and y - 38 == prep_coordinates[kila][1]:
                        pira = False
                if pira:
                    y -= 38
                    if x == 76 and y == 266:
                        mata = True
                    for ku in range(len(mine)):
                        if x == mine[ku][0] and y == mine[ku][1]:
                            death = True
                    if y < 0:
                        y = 532
                        mine = mine1
                        bg = load_image("4444.jpg")
                    pol = 0
                pira = True
            elif i.key == pygame.K_DOWN:
                for kila in range(len(prep_coordinates)):
                    if x == prep_coordinates[kila][0] and y + 38 == prep_coordinates[kila][1]:
                        pira = False
                if pira:
                    y += 38
                    if x == 76 and y == 266:
                        mata = True
                    for ku in range(len(mine)):
                        if x == mine[ku][0] and y == mine[ku][1]:
                            death = True
                    if y > 532:
                        y = 0
                        bg = load_image("3333.jpg")
                        mine = kopy
                    pol = 2
                pira = True
            elif i.key == pygame.K_SPACE:
                rim = True
    if pol == 0:
        sc.blit(bg, (0, 0))
        all_sprites.draw(sc)
        for i in range(len(mine)):
            sc.blit(mina, (mine[i][0], mine[i][1]))
        sc.blit(prep, (76, 76))
        sc.blit(prep2, (76, 152))
        if mark1:
            sc.blit(prep1, (76, 266))
        elif not mark1 and not mata:
            sc.blit(zv, (76, 266))
        sc.blit(image, (x, y))
        if death:
            os.system('python finish.py')
            break
        if rim:
            x1 = x
            y1 = y
            ki = y1
            ki1 = x1
            while rim:
                sc.blit(bg, (0, 0))
                sc.blit(prep, (76, 76))
                sc.blit(prep2, (76, 152))
                sc.blit(image, (x, y))
                sc.blit(image1, (x + 18, y1))
                for i in range(len(mine)):
                    sc.blit(mina, (mine[i][0], mine[i][1]))
                if mark1:
                    sc.blit(prep1, (76, 266))
                elif not mark1 and not mata:
                    sc.blit(zv, (76, 266))
                pygame.display.update()
                if (y1 == 266 + 38 or y1 == 266 or y1 == 266 + 38 + 38) and x == 76:
                    mark1 = False
                elif not mark1 and lu:
                    sc.blit(vz, (76, 266))
                    lu = False
                    prep_coordinates.remove(prep_coordinates[2])
                    break
                y1 -= 3
                clock.tick(FPS)
                pygame.display.update()
                if y1 <= ki - 38:
                    rim = False
                    y1 = y
                    break
    elif pol == 1:
        sc.blit(bg, (0, 0))
        sc.blit(prep, (76, 76))
        sc.blit(prep2, (76, 152))
        for i in range(len(mine)):
            sc.blit(mina, (mine[i][0], mine[i][1]))
        if mark1:
            sc.blit(prep1, (76, 266))
        elif not mark1 and not mata:
            sc.blit(zv, (76, 266))
        sc.blit(imagek1, (x, y))
        if death:
            os.system('python finish.py')
            break
        if rim:
            x1 = x
            y1 = y
            ki = y1
            ki1 = x1
            while rim:
                sc.blit(bg, (0, 0))
                sc.blit(prep, (76, 76))
                sc.blit(prep2, (76, 152))
                if mark1:
                    sc.blit(prep1, (76, 266))
                elif not mark1 and not mata:
                    sc.blit(zv, (76, 266))
                sc.blit(imagek1, (x, y))
                sc.blit(image1, (x1 + 38, y1 + 16))
                for i in range(len(mine)):
                    sc.blit(mina, (mine[i][0], mine[i][1]))
                pygame.display.update()
                if (x1 == 76 - 38 or x1 == 76 or x1 == 76 - 38 - 38) and y == 266:
                    mark1 = False
                elif not mark1 and lu:
                    sc.blit(vz, (76, 266))
                    lu = False
                    prep_coordinates.remove(prep_coordinates[2])
                    break
                x1 += 3
                clock.tick(FPS)
                pygame.display.update()
                if x1 >= ki1 + 38:
                    rim = False
                    x1 = x
                    break
    elif pol == 2:
        sc.blit(bg, (0, 0))
        sc.blit(prep, (76, 76))
        sc.blit(prep2, (76, 152))
        for i in range(len(mine)):
            sc.blit(mina, (mine[i][0], mine[i][1]))
        if mark1:
            sc.blit(prep1, (76, 266))
        elif not mark1 and not mata:
            sc.blit(zv, (76, 266))
        sc.blit(imagek2, (x, y))
        if death:
            os.system('python finish.py')
            break
        if rim:
            x1 = x
            y1 = y
            ki = y1
            ki1 = x1
            while rim:
                sc.blit(bg, (0, 0))
                sc.blit(prep, (76, 76))
                sc.blit(prep2, (76, 152))
                for i in range(len(mine)):
                    sc.blit(mina, (mine[i][0], mine[i][1]))
                if mark1:
                    sc.blit(prep1, (76, 266))
                elif not mark1 and not mata:
                    sc.blit(zv, (76, 266))
                sc.blit(imagek2, (x, y))
                sc.blit(image1, (x + 16, y1 + 38))
                pygame.display.update()
                if (y1 == 266 - 38 or y1 == 266 or y1 == 266 - 38 - 38) and x == 76:
                    mark1 = False
                elif not mark1 and lu:
                    sc.blit(vz, (76, 266))
                    lu = False
                    prep_coordinates.remove(prep_coordinates[2])
                    break
                y1 += 3
                clock.tick(FPS)
                pygame.display.update()
                if y1 >= ki + 38:
                    rim = False
                    y1 = y
                    break
    elif pol == 3:
        sc.blit(bg, (0, 0))
        sc.blit(prep, (76, 76))
        sc.blit(prep2, (76, 152))
        for i in range(len(mine)):
            sc.blit(mina, (mine[i][0], mine[i][1]))
        if mark1:
            sc.blit(prep1, (76, 266))
        elif not mark1 and not mata:
            sc.blit(zv, (76, 266))
        sc.blit(imagek3, (x, y))
        if death:
            os.system('python finish.py')
            break
        if rim:
            x1 = x
            y1 = y
            ki = y1
            ki1 = x1
            while rim:
                sc.blit(bg, (0, 0))
                sc.blit(prep, (76, 76))
                sc.blit(prep2, (76, 152))
                for i in range(len(mine)):
                    sc.blit(mina, (mine[i][0], mine[i][1]))
                if mark1:
                    sc.blit(prep1, (76, 266))
                elif not mark1 and not mata:
                    sc.blit(zv, (76, 266))
                sc.blit(imagek3, (x, y))
                sc.blit(image1, (x1 - 3, y1 + 17))
                pygame.display.update()
                if (x1 == 76 + 38 or x1 == 76 or x1 == 76 + 38 + 38) and y == 266:
                    mark1 = False
                elif not mark1 and lu:
                    sc.blit(vz, (76, 266))
                    lu = False
                    prep_coordinates.remove(prep_coordinates[2])
                    break
                x1 -= 3
                clock.tick(FPS)
                pygame.display.update()
                if x1 <= ki1 - 38:
                    rim = False
                    y1 = y
                    break
    if mata:
        kount = 100
        os.system('python finish.py')
        running = False
    pygame.display.update()
    clock.tick(FPS)
