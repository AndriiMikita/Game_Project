import pygame

class Wave():
    def __init__(self, screen):
        self.wave_number = 0
        self.bonus_speed = 0
        self.points = 0
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.text_color = (255, 255, 255)
        self.background_color = (0, 0, 0)
        self.font = pygame.font.SysFont('couriernew', 32)
        self.draw_wave()

    def draw_wave(self):
        self.wave_image = self.font.render("Wave: " + str(self.wave_number), True, self.text_color, self.background_color)
        self.wave_rect = self.wave_image.get_rect()
        self.wave_rect.left = self.screen_rect.left + 10
        self.wave_rect.top = self.screen_rect.top + 10 + 42

    def show_wave(self):
        self.screen.blit(self.wave_image, self.wave_rect)

    def boost(self):
        self.bonus_speed += 0.02
        self.points += 5