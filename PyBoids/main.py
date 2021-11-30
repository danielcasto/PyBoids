import pygame as pg
import sys
import time
from flock import Flock

def main():
    background_color = (63, 63, 63) # rgb
    flock = Flock(1)
    pg.init()
    # TODO see if there is a way to set screen size relative to display size
    window_size = 1000, 600 # width, height 
    screen = pg.display.set_mode(window_size, pg.RESIZABLE)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                sys.exit()
        
        screen.fill(background_color)
        flock.update()
        flock.draw(pg, screen)

        pg.display.flip()
        time.sleep(0.01) # 0.005 seems optimal


if __name__ == '__main__':
    main()