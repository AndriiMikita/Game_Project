import pygame

class End_menu():
    def __init__(self, screen, stats):
        self.screen = screen
        self.stats = stats
        self.screen_rect = self.screen.get_rect()
        self.text_color = (255, 255, 255)
        self.background_color = (0, 0, 0)
        self.font = pygame.font.SysFont('couriernew', 32)
        self.draw_menu()

    def draw_menu(self):
        self.menu_image = self.font.render("Your score: " + str(self.stats.score) + ",\n r to restart", True, self.text_color, self.background_color)
        self.menu_rect = self.menu_image.get_rect()
        self.menu_rect.centery = self.screen_rect.centery - 32
        self.menu_rect.centerx = self.screen_rect.centerx

    def show_menu(self):
        self.screen.blit(self.menu_image, self.menu_rect)