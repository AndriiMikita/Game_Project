import pygame as pyg
import  sys as sys
from  gun import Gun
import controls
from pygame.sprite import Group
from stats import Stats
from scores import Scores
from lifes import Lifes
from wave import Wave
from srart_menu import Start_menu
from end_menu import End_menu

pyg.init()
screen = pyg.display.set_mode((700, 800))
pyg.display.set_caption("Own game")
background_color = (0, 0, 0)
start_menu = Start_menu(screen)


def run():
    gun = Gun(screen)
    bullets = Group()
    alliens = Group()
    stats = Stats()
    lifes = Lifes(screen, stats)
    score = Scores(screen, stats)
    wave = Wave(screen)
    end_menu = End_menu(screen, stats)
    controls.create_army(screen, alliens, wave)

    while True:
        controls.events(screen, gun, bullets)
        if stats.run_game:
            gun.update_pos()
            bullets.update()
            controls.update(background_color, screen, gun, bullets, alliens, stats, score, lifes, wave)
            score.draw_score()
        else:
            end_menu.draw_menu()
            end_menu.show_menu()
            pyg.display.flip()
        if controls.events(screen, gun, bullets):
            start()

def start():
    while True:
        screen.fill(background_color)
        start_menu.show_menu()
        start_menu.draw_menu()
        pyg.display.flip()
        if controls.start():
            run()

start()
