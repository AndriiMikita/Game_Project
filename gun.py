import pygame as pyg

class Gun():
    def __init__(self, screen):

        self.screen = screen
        self.image = pyg.image.load("Sprites/gun.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.move_right = False
        self.move_left = False

    def draw(self):

        self.screen.blit(self.image, self.rect)

    def update_pos(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.center += 1.5
        elif self.move_left and self.rect.left > self.screen_rect.left:
            self.center -= 1.5

        self.rect.centerx = self.center

    def create_gun(self):
        self.center = self.screen_rect.centerx