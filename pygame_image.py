import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    #ゲーム初期化
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    koukaton = pg.image.load("fig/3.png")
    koukaton = pg.transform.flip(koukaton,True,False)
    kouka_rct = koukaton.get_rect()
    kouka_rct.center = 300,200
    tmr = 0
    #動作部分
    while True:
        #ゲームの終了条件とスコアの表示
        x = (-tmr * 10) % -3200
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        screen.blit(bg_img,[x,0])
        screen.blit(pg.transform.flip(bg_img,True,False),[x+1600,0])
        screen.blit(bg_img,[x+3200,0])
        what = pg.key.get_pressed()
        if(what[pg.K_d]):
            kouka_rct.move_ip((1,0))
        if(what[pg.K_a]):
            kouka_rct.move_ip((-1,0))
        if(what[pg.K_w]):
            kouka_rct.move_ip((0,-1))
        if(what[pg.K_s]):
            kouka_rct.move_ip((0,1))
        screen.blit(koukaton,kouka_rct)
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()