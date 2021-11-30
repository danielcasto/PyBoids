import pygame as pg, sys
from flock import Flock

def main():
    flock = Flock()
    pg.init()
    # TODO see if there is a way to set screen size relative to display size
    window_size = 400, 500 # width, height 
    screen = pg.display.set_mode(window_size, pg.RESIZABLE)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                sys.exit()
        
        screen.fill((0, 0, 0))
        pg.display.flip()


if __name__ == '__main__':
    main()