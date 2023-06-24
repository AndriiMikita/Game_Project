import  pygame as pyg
import sys
from bullet import Bullet
from allien import Allien
import time

def start():
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            sys.exit()
        if event.type == pyg.KEYDOWN:
            if event.key == pyg.K_SPACE:
                return True

def events(screen, gun, bullets):
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            sys.exit()
        elif event.type == pyg.KEYDOWN:
            #right
            if event.key == pyg.K_RIGHT:
                gun.move_right = True
            #right
            #left
            elif event.key == pyg.K_LEFT:
                gun.move_left = True
            #left
            #space
            elif event.key == pyg.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
            #space
            #r
            elif event.key == pyg.K_r:
                return True
            #r

        elif event.type == pyg.KEYUP:
            #right
            if event.key == pyg.K_RIGHT:
                gun.move_right = False
            #right
            #left
            elif event.key == pyg.K_LEFT:
                gun.move_left = False
            #left

def update(background_color, screen, gun, bullets, alliens, stats, score, lifes, wave):
    screen.fill(background_color)
    score.show_score()
    lifes.show_lifes()
    wave.show_wave()
    update_bullets(bullets, alliens, screen, stats, score, wave)
    alliens.draw(screen)
    update_alliens(alliens, gun, screen, stats, bullets, lifes, wave)
    gun.draw()
    pyg.display.flip()

def update_bullets(bullets, alliens, screen, stats, score, wave):
    bullets.update()
    for bullet in bullets.sprites():
        if bullet.rect.bottom <= bullet.screen_rect.top:
            bullets.remove(bullet)
        bullet.draw()
    colisions = pyg.sprite.groupcollide(bullets, alliens, True , True)
    if colisions:
        for allien in colisions.values():
            stats.score += wave.points * len(allien)
        score.draw_score()
    if len(alliens) == 0:
        bullets.empty()
        create_army(screen, alliens, wave)


def update_alliens(alliens, gun, screen, stats, bullets, lifes, wave):
    alliens.update()
    allien = Allien(screen)
    if pyg.sprite.spritecollideany(gun, alliens):
        guns_death(stats, screen, gun, alliens, bullets, lifes, wave)
    alliens_surv(screen, alliens, stats, gun, bullets, lifes, wave)

def create_army(screen, alliens, wave):
    all = Allien(screen)
    wave.wave_number += 1
    wave.boost()
    wave.draw_wave()
    col_alliens = (700 - 2 * all.rect.width) // all.rect.width
    row_alliens = (800 - 200 - 2 * all.rect.height) // all.rect.height

    for row in range(3):
        for count in range(col_alliens):
            allien = Allien(screen)
            allien.speed = wave.bonus_speed
            allien.x = all.rect.width * (count + 1)
            allien.y = 2 * all.rect.height * (row + 1)
            allien.rect.x = allien.x
            allien.rect.y = allien.y
            alliens.add(allien)
            print(allien.speed)


def guns_death(stats, screeen, gun, alliens, bullets, lifes, wave):
    if stats.lifes > 1:
        stats.lifes -= 1
        lifes.draw_lifes()
        alliens.empty()
        bullets.empty()
        wave.wave_number -= 1
        stats.score = max(0, stats.score - 300)
        wave.bonus_speed -= 0.02
        wave.points -= 5
        create_army(screeen, alliens, wave)
        gun.create_gun()
        time.sleep(0.5)
    else:
        stats.run_game = False

def alliens_surv(screen, alliens, stats, gun, bullets, lifes, wave):
    screen_rect = screen.get_rect()
    for alli in alliens.sprites():
        if alli.rect.bottom >= screen_rect.bottom:
            guns_death(stats, screen, gun, alliens, bullets, lifes, wave)
            break

