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
    kk_rct = kk_img.get_rect()

    kk_rct.center = (900, 400)

    # 爆弾の初期位置設定
    bomb_position = (randint(0, WIDTH), randint(0, HEIGHT))

    circle = pg.Surface((20, 20))
    circle.set_colorkey((0, 0, 0))
    pg.draw.circle(circle, (255, 0, 0), (10, 10), 10)
    bomb_rct = circle.get_rect()
    bomb_rct.center = (bomb_position[0], bomb_position[1])

    clock = pg.time.Clock()
    tmr = 0

    # 移動量
    vx, vy = 5, 5

    move_lst = {
        pg.K_LEFT: (-5, 0),
        pg.K_RIGHT: (5, 0),
        pg.K_UP: (0, -5),
        pg.K_DOWN: (0, 5),
    }

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        
        key_lst = pg.key.get_pressed()
        total_movement = [0, 0]

        for key, mv in move_lst.items():
            if key_lst[key]:
                total_movement[0] += mv[0]
                total_movement[1] += mv[1]

        kk_rct.move_ip(total_movement)

        bomb_rct.move_ip(vx, vy)
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rct )
        screen.blit(circle, bomb_rct)
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
