import numpy as np
import time
from matplotlib import pyplot as plt
import pygame as pg

BG_COLOR = (10, 10, 10)
COLOR_GRID = (40,40,40)
COLOR_DIE_NEXT = (250, 25 ,25)
PREDATOR_COLOR = (200, 10, 10) #PREDATOR COLOR (red)
OMNIVORE_COLOR = (200, 10, 200) #OMNIVORE COLOR (purple)
HERBAVORE_COLOR = (25, 255, 25) #HERBAVORE COLOR (green)


def  update(screen, cells, size, with_progress = False):
    '''RULES:
    LIVE CELL: 
    If the live cell is a predator:
    1) If the surrounding cells sum up to 1 or 2 omnivores, the cell lives on.
    2) If the surrounding cells sum up to 2 or 3 herbavores, the cell lives on.
    4) If the surrounding cells sum up to 2 predators or more, the cell dies. 
    5) If the surrounding cells sum up to at least 3 omnivores, the cell dies.
    6) If the surrounding cells sum up to at least 4 herbavores, the cell dies.
    
    If the live cell is an omnivore:
    1) If the surrounding cells sum up to 1 or 2 herbavores, the cell lives on
    2) If the surrounding cells sum up to 3 herbavores or more, the cell dies.
    3) If the surrounding cells sum up to at least 1 predator, the cell dies.
    
    If the live cell is a herbavore:
    1) If the surrounding cells sum up to to at least 1 predator, the cell dies.
    2) If the surrounding cells sum up to at least 2 omnivores, the cell dies.
    3) If the surrounding cells sum up to at most 1 omnivore, the cell lives on.'''

    '''Conditions for dead middle ells:
    1) If it has'''

    '''The step of each frame'''
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))

    for row, col in np.ndindex(cells.shape):
        '''alive = []
        for i in range(row-1, row+2):
            for j in range(col-1, col+2):
                alive.append'''
        print(row, col)
        alive = np.sum(cells[row-1 : row+2, col-1 : col +2] ) - cells[row, col]
        #if cells[row, col] == 0:
        #color = BG_COLOR if cells[row, col] == 0 else COLOR_ALIVE_NEXT
        if cells[row, col] == 0:
            color = BG_COLOR

        elif cells[row, col] == 1:
            '''PREDATOR'''
            color = PREDATOR_COLOR
        elif cells[row, col] == 2:
            '''OMNIVORE''' 
            color = OMNIVORE_COLOR
        else: 
            '''HERBAVORE'''
            color = HERBAVORE_COLOR

        if cells[row, col] == 1:
            #We don't have to assign updated_cells[row, col] any new value then, 
            #because it already has the value 0, which is dead
            if alive < 2 or alive > 3:
                #Same as the above mentioned goes here
                if with_progress: 
                    color = COLOR_DIE_NEXT
            elif 2 <= alive <= 3:
                #But now, the updated cell must be assigned 1 instead of 0, so that it lives in the next timestep.'''
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
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                '''Left mouse-click, PREDATOR'''
                pos = pg.mouse.get_pos()
                cells[pos[1] // 10, pos[0] // 10 ] = 1
                update(screen, cells, 10)
                print(pg.mouse.get_pressed())
                pg.display.update()

            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 2:
                '''Middle mouse-click, OMNIVORE'''
                pos = pg.mouse.get_pos()
                cells[pos[1] // 10 , pos[0] // 10] = 2
                update(screen, cells, 10)
                print(pg.mouse.get_pressed())
                pg.display.update()

            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 3:
                '''Right mouse-click, HERBAVORE'''
                pos = pg.mouse.get_pos()
                cells[pos[1] // 10, pos[0] // 10] = 3
                update(screen, cells, 10)
                print(pg.mouse.get_pressed())
                pg.display.update()

        screen.fill(COLOR_GRID)
        if running:
            cells = update(screen, cells, 10 , with_progress=True)
            pg.display.update()
        time.sleep(0.001)


if __name__ == '__main__':
    main()   