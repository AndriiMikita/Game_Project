import pygame as pyg


class Bullet(pyg.sprite.Sprite):

    def __init__(self, screen, gun):
        super(Bullet, self).__init__()
        self.screen = screen
        self.image = pyg.image.load("Sprites/bullet.png")
        self.rect = self.image.get_rect()
        #self.color = (196, 5, 36)
        #self.rect = pyg.Rect(0, 0, 4 , 12)
        self.screen_rect = screen.get_rect()
        self.speed = 2
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def draw(self):
        #pyg.draw.rect(self.screen, self.color, self.rect)
        self.screen.blit(self.image, self.rect)