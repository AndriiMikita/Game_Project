import pygame as pyg

class Allien(pyg.sprite.Sprite):
    def __init__(self, screen):
        super(Allien, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pyg.image.load("Sprites/allien.png")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.speed = 0
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self):
        self.y += self.speed
        self.rect.y = self.y

    def draw(self):
        self.screen.blit(self.image, self.rect)