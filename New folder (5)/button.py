import pygame as pg


class Button:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pg.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        pos = pg.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pg.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
                action = True
            if not pg.mouse.get_pressed()[0]:
                self.clicked = False
                action = False

        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action
