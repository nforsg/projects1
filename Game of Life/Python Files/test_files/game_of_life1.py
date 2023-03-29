import numpy as np
import time
from matplotlib import pyplot as plt
import pygame as pg

BG_COLOR = (10, 10, 10)
COLOR_GRID = (40,40,40)
COLOR_DIE_NEXT = (250, 25 ,25)
COLOR_ALIVE_NEXT = (25, 255, 25)


def  update(screen, cells, size, with_progress = False):
    '''The step of each frame'''
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))

    for row, col in np.ndindex(cells.shape):
        alive = np.sum(cells[row-1 : row+2, col-1 : col +2] ) - cells[row, col]
        #if cells[row, col] == 0:
        #color = BG_COLOR if cells[row, col] == 0 else COLOR_ALIVE_NEXT
        if cells[row, col] == 0:
            color = BG_COLOR

        else:
            color = COLOR_ALIVE_NEXT

        if cells[row, col] == 1:
            '''We don't have to assign updated_cells[row, col] any new value then, 
            because it already has the value 0, which is dead'''
            if alive < 2 or alive > 3:
                '''Same as the above mentioned goes here'''
                if with_progress: 
                    color = COLOR_DIE_NEXT
            elif 2 <= alive <= 3:
                '''But now, the curent cell is '''
                updated_cells[row, col] = 1

                if with_progress:
                    color = COLOR_ALIVE_NEXT
            
        else:
            if alive == 3: 
                updated_cells[row, col] = 1 
                if with_progress:
                    color = COLOR_ALIVE_NEXT
        pg.draw.rect(screen, color, (col * size, row * size, size - 1, size - 1))
    return updated_cells

def main():
    pg.init()
    screen = pg.display.set_mode((800, 600))
    
    cells = np.zeros((60, 80))
    screen.fill(COLOR_GRID)
    update(screen, cells, 10)

    pg.display.flip()
    pg.display.update()

    running = False

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    running = not running
                    update(screen, cells, 10)
                    pg.display.update()
            if pg.mouse.get_pressed()[0]:
                pos = pg.mouse.get_pos()
                cells[pos[1] // 10, pos[0] // 10 ] = 1
                update(screen, cells, 10)
                pg.display.update()
        screen.fill(COLOR_GRID)
        if running:
            cells = update(screen, cells, 10 , with_progress=True)
            pg.display.update()
        time.sleep(0.001)


if __name__ == '__main__':
    main()   