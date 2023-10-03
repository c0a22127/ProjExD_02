import sys
import pygame as pg
from random import randint

WIDTH, HEIGHT = 1600, 900


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("fig/pg_bg.jpg")
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)

    # 爆弾の初期位置設定
    bomb_position = (randint(0, WIDTH), randint(0, HEIGHT))

    circle = pg.Surface((20, 20))
    circle.set_colorkey((0, 0, 0))
    pg.draw.circle(circle, (255, 0, 0), (10, 10), 10)
    bomb_rct = circle.get_rect()
    bomb_rct.center = (bomb_position[0], bomb_position[1])

    clock = pg.time.Clock()
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, [900, 400])
        screen.blit(circle, bomb_rct)
        pg.display.update()
        tmr += 1
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
