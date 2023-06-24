import pygame.font

class Scores():
    def __init__(self, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (255, 255, 255)
        self.background_color = (0, 0, 0)
        self.font = pygame.font.SysFont('couriernew', 32)
        self.draw_score()

    def draw_score(self):
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, self.background_color)
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 50
        self.score_rect.top = self.screen_rect.top + 10

    def show_score(self):
        self.screen.blit(self.score_img, self.score_rect)
