import pygame as pg
import button
import random as r
import menu
pg.init()



def chests():
    global money, file, screen, chest_win, chest_lose, start, pos1, pos2, a, timer
    for event in pg.event.get():
        if event.type == pg.QUIT:
            # saving money
            menu.data[0] = str(money)
            with open('money.txt', 'w') as file:
                file.writelines(menu.data)
            pg.quit()

    screen.fill((255, 0, 230))

    def chest_work():
        global pos1, pos2, chest_win, chest_lose
        pos_chests = r.randint(1, 2)

        if pos_chests == 1:
            pos1 = 50, 150
            pos2 = 400, 150
            chest_win = button.Button(pos1[0], pos1[1], menu.chest_default, 15)
            chest_win.draw(screen)
            chest_lose = button.Button(pos2[0], pos2[1], menu.chest_default, 15)
            chest_lose.draw(screen)
        elif pos_chests == 2:
            pos1 = 400, 150
            pos2 = 50, 150
            chest_win = button.Button(pos1[0], pos1[1], menu.chest_default, 15)
            chest_win.draw(screen)
            chest_lose = button.Button(pos2[0], pos2[1], menu.chest_default, 15)
            chest_lose.draw(screen)

    if timer:
        a += 1
        if a >= 120:
            chest_work()
            a = 0
            timer = False

    if start:
        chest_work()
        start = False

    if menu.back_button.draw(screen):
        menu.GameState.state = "menu"
        start = True

    if chest_win.draw(screen) and not timer:
        chest_win = button.Button(pos1[0], pos1[1], menu.chest_win_img, 15)
        chest_win.draw(screen)
        money += menu.bet * 2
        timer = True

    if chest_lose.draw(screen) and not timer:
        chest_lose = button.Button(pos2[0], pos2[1], menu.chest_lose_img, 15)
        chest_lose.draw(screen)
        money -= menu.bet
        timer = True

    menu.clock.tick(60)

    img = menu.font.render(str(money), True, (255, 255, 255))
    screen.blit(img, (10, 10))

    pg.display.flip()

