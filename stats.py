import pygame

class Stats():
    def __init__(self):
        self.reset_stats()
        self.run_game = True

    def reset_stats(self):
        self.lifes = 1
        self.score = 0