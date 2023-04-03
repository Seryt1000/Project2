import pygame as pg
import random as r
import button
import chests_p
# file read
with open('money.txt', 'r') as file:
    data = file.readlines()
money = int(data[0])
# inits

pg.init()

screen = pg.display.set_mode([700, 500])

font = pg.font.SysFont("arial", 24)

clock = pg.time.Clock()
pos1 = []
pos2 = []
# buttons images
button_ladder_img = pg.image.load("ladder_img.png").convert_alpha()
button_crash_img = pg.image.load("button_crash.png").convert_alpha()
button_deposit_img = pg.image.load("deposit_img.png").convert_alpha()
button_chests_img = pg.image.load("chests_img.png").convert_alpha()
button_slots_img = pg.image.load("button_slots.png").convert_alpha()

# buttons setup
button_ladder = button.Button(50, 200, button_ladder_img, 7)
button_crash = button.Button(400, 200, button_crash_img, 1)
button_chests = button.Button(50, 350, button_chests_img,7)
button_slots = button.Button(400, 350, button_slots_img, 1)
button_deposit = button.Button(50, 50, button_deposit_img, 7)

# advertisements setup
advertisement1_img = pg.image.load("advertisement1.png").convert_alpha()
advertisement2_img = pg.image.load("advertisement2.png").convert_alpha()
advertisement3_img = pg.image.load("advertisement3.png").convert_alpha()

advertisement1 = button.Button(0, 0, advertisement1_img, 1)
advertisement2 = button.Button(0, 0, advertisement2_img, 1)
advertisement3 = button.Button(0, 0, advertisement3_img, 1)

ads = [advertisement1, advertisement2, advertisement3]

a = 0

timer = False

start = True

bet = 100

# chests setup
chest_default = pg.image.load("chest_default.png").convert_alpha()
chest_win_img = pg.image.load("chest_win_img.png").convert_alpha()
chest_lose_img = pg.image.load("chest_lose_img.png").convert_alpha()

chest_win = button.Button(0, 0, chest_default, 25)
chest_lose = button.Button(0, 0, chest_default, 25)

back_img = pg.image.load("back.png").convert_alpha()
take_img = pg.image.load("take.png").convert_alpha()

back_button = button.Button(600, 0, back_img, 5)
take_button = button.Button(0, 500, take_img, 1)

class GameState:

    def __init__(self):
        self.state = "menu"

    def menu(self):
        global money, file, screen
        for event in pg.event.get():
            if event.type == pg.QUIT:
                # saving money
                data[0] = str(money)
                with open('money.txt', 'w') as file:
                    file.writelines(data)
                pg.quit()

        screen.fill((255, 0, 230))

        # ladder button
        if button_ladder.draw(screen):
            money -= 1
        # crash button
        if button_crash.draw(screen):
            print("Start")
        # chests button
        if button_chests.draw(screen):
            self.state = "chests"
        # slots button
        if button_slots.draw(screen):
            self.state = "menu"
        # deposit money button
        if button_deposit.draw(screen):
            self.state = "advertisements"

        img = font.render(str(money), True, (255, 255, 255))
        screen.blit(img, (10, 10))

        pg.display.flip()

    def advertisements(self):

        global money, file, screen, a
        for event in pg.event.get():
            if event.type == pg.QUIT:
                # saving money
                data[0] = str(money)
                with open('money.txt', 'w') as file:
                    file.writelines(data)
                pg.quit()

        if a == 0:
            screen.fill((255, 0, 230))
            r.choice(ads).draw(screen)

        a += 1
        if a >= 1800:
            screen.fill((255, 0, 230))
            money += 50
            self.state = "menu"
            a = 0
        clock.tick(60)

        pg.display.flip()

    def state_manager(self):
        if self.state == "menu":
            self.menu()
        if self.state == "chests":
            chests_p.chests()
        if self.state == "advertisements":
            self.advertisements()


game_state = GameState()

run = True
# loop
while run:
    game_state.state_manager()

