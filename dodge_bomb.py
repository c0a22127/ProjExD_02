import sys
import pygame as pg
from random import randint
import time

WIDTH, HEIGHT = 1600, 900

# 爆弾の初期位置設定
bomb_position = (randint(0, WIDTH), randint(0, HEIGHT))


# 移動量のリスト
move_lst = {
    pg.K_LEFT: (-5, 0),
    pg.K_RIGHT: (5, 0),
    pg.K_UP: (0, -5),
    pg.K_DOWN: (0, 5),
}

rotozoom_lst = {
    "(-5, 0)": pg.transform.rotozoom(pg.image.load("fig/3.png"), 0, 2.0),
    "(5, 0)": pg.transform.rotozoom(pg.transform.flip(pg.image.load("fig/3.png"), True, False), 0, 2.0),
    "(0, -5)": pg.transform.rotozoom(pg.transform.flip(pg.image.load("fig/3.png"), False, True), -90, 2.0),
    "(0, 5)": pg.transform.rotozoom(pg.image.load("fig/3.png"), 90, 2.0),
    "(5, -5)": pg.transform.rotozoom(pg.transform.flip(pg.image.load("fig/3.png"), True, False), -45, 2.0),
    "(-5, -5)": pg.transform.rotozoom(pg.image.load("fig/3.png"), -45, 2.0),
    "(5, 5)": pg.transform.rotozoom(pg.transform.flip(pg.image.load("fig/3.png"), True, False), 45, 2.0),
}

def render_game_over(screen: pg.Surface, kk_rct: tuple) -> None:
    """
    ゲームオーバーを表示する関数\n
    引数: screen: Surface, kk_rct: こうかとんRect\n
    戻り値: なし
    """
    kk_pien = pg.image.load("fig/8.png")
    kk_pien = pg.transform.rotozoom(kk_pien, 0, 2.0)
    pien_rct = kk_pien.get_rect()
    pien_rct = kk_rct
    screen.blit(kk_pien, pien_rct)
    pg.display.update()
    time.sleep(3)
    return

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("fig/pg_bg.jpg")

    # ===========================
    # こうかとん作成
    # ===========================
    kk_img = pg.image.load("fig/3.png")

    kk_rct = kk_img.get_rect()
    kk_rct.center = (900, 400)  # 画像の中心座標を設定

    # ===========================
    # 爆弾作成
    # ===========================
    circle = pg.Surface((20, 20))
    circle.set_colorkey((0, 0, 0))
    pg.draw.circle(circle, (255, 0, 0), (10, 10), 10)
    bomb_rct = circle.get_rect()
    bomb_rct.center = bomb_position
    # ===========================

    clock = pg.time.Clock()
    tmr = 0

    # 爆弾の移動量
    vx, vy = 5, 5

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
            
        if kk_rct.colliderect(bomb_rct):
            print("GAME OVER")
            # こうかとんが泣く
            render_game_over(screen, kk_rct)
            return
        
        key_lst = pg.key.get_pressed()
        total_movement = [0, 0]
        key_movement = (0, 0)

        for key, mv in move_lst.items():
            if key_lst[key]:
                total_movement[0] += mv[0]
                total_movement[1] += mv[1]
                key_movement = mv

        kk_rct.move_ip(total_movement) # こうかとんの移動

        if is_obj_outside(kk_rct) != (True, True):
            kk_rct.move_ip(-total_movement[0], -total_movement[1])

        bomb_rct.move_ip(vx, vy) # 爆弾の移動
        bomb_tate, bomb_yoko = is_obj_outside(bomb_rct)
        if not bomb_yoko:
            vy *= -1
        if not bomb_tate:
            vx *= -1

        screen.blit(bg_img, [0, 0])
        if key_movement != (0, 0):
            screen.blit(rotozoom_lst[str(key_movement)], kk_rct)
        else:
            screen.blit(pg.transform.rotozoom(kk_img, 0, 2.0), kk_rct)
        screen.blit(circle, bomb_rct)
        pg.display.flip()
        tmr += 1
        clock.tick(50)

def is_obj_outside(obj: tuple) -> tuple:
    """
    オブジェクトの画面外判定 (obj: tuple) -> tuple(bool, bool))\n
    引数: obj: こうかとんRect, 爆弾Rect\n
    戻り値: (幅判定, 高さ判定)
    """
    width, height = True, True
    if obj.left < 0 or  WIDTH < obj.right:
        width = False
    elif obj.top < 0 or HEIGHT < obj.bottom:
        height = False

    return width, height

    

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
