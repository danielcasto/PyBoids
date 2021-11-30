import pygame as pg, sys

def main():
    pg.init()
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