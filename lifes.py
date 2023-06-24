import pygame

class Lifes():
    def __init__(self, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (255, 255, 255)
        self.background_color = (0, 0, 0)
        self.font = pygame.font.SysFont('couriernew', 32)
        self.draw_lifes()

    def draw_lifes(self):
        self.lifes_image = self.font.render("Guns left: " + str(self.stats.lifes), True, self.text_color, self.background_color)
        self.lifes_rect = self.lifes_image.get_rect()
        self.lifes_rect.left = self.screen_rect.left + 10
        self.lifes_rect.top = self.screen_rect.top + 10

    def show_lifes(self):
        self.screen.blit(self.lifes_image, self.lifes_rect)