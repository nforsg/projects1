import numpy as np
import time
from matplotlib import pyplot as plt
import pygame as pg

BG_COLOR = (10, 10, 10) #Background color
COLOR_GRID = (40,40,40) #Grid color
COLOR_DIE_NEXT = (250, 25 ,25)
PREDATOR_COLOR = (200, 10, 10) #PREDATOR COLOR (red)
OMNIVORE_COLOR = (200, 10, 200) #OMNIVORE COLOR (purple)
HERBAVORE_COLOR = (25, 255, 25) #HERBAVORE COLOR (green)


def update(screen, cells, size, with_progress = False):

    '''The step of each frame'''
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))
    print(cells.shape[0])
    for row, col in np.ndindex(cells.shape):
        #alive = np.sum(cells[row-1 : row+2, col-1 : col +2] ) - cells[row, col]
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
        live_predators = []
        live_omnivores = []
        live_herbavores = []
        if 1<= row < 59   and 1<= col < 79:
            for i in range(row-1, row+2):
                for j in range(col-1, col+2):
                    #print((i,j))
                    if (i, j) == (row, col):
                        continue
                    else:
                        if cells[i,j] == 1:
                            live_predators.append(cells[i,j])
                        elif cells[i,j] == 2:
                            live_omnivores.append(cells[i,j])
                        elif cells[i,j] == 3: 
                            live_herbavores.append(cells[i,j])
                        else:
                            continue
        elif row == 0 and col == 79:
            for i in range(row, row+2):
                for j in range(col-1, col+1):
                    if (i, j) == (row, col):
                        continue
                    else:
                        if cells[i,j] == 1:
                            live_predators.append(cells[i,j])
                        elif cells[i,j] == 2:
                            live_omnivores.append(cells[i,j])
                        elif cells[i,j] == 3: 
                            live_herbavores.append(cells[i,j])
                        else:
                            continue
        elif row == 0 and col == 0:
            for i in range(row, row+2):
                for j in range(col, col+2):
                    if (i, j) == (row, col):
                        continue
                    else:
                        if cells[i,j] == 1:
                            live_predators.append(cells[i,j])
                        elif cells[i,j] == 2:
                            live_omnivores.append(cells[i,j])
                        elif cells[i,j] == 3: 
                            live_herbavores.append(cells[i,j])
                        else:
                            continue
        elif row == 59 and col == 0:
            for i in range(row-1, row+1):
                for j in range(col, col+2):
                    if (i, j) == (row, col):
                        continue
                    else:
                        if cells[i,j] == 1:
                            live_predators.append(cells[i,j])
                        elif cells[i,j] == 2:
                            live_omnivores.append(cells[i,j])
                        elif cells[i,j] == 3: 
                            live_herbavores.append(cells[i,j])
                        else:
                            continue
        elif row == 59 and col == 79:
            for i in range(row-1, row+1):
                for j in range(col-1, col+1):
                    if (i, j) == (row, col):
                        continue
                    else:
                        if cells[i,j] == 1:
                            live_predators.append(cells[i,j])
                        elif cells[i,j] == 2:
                            live_omnivores.append(cells[i,j])
                        elif cells[i,j] == 3: 
                            live_herbavores.append(cells[i,j])
                        else:
                            continue

        if cells[row, col] == 1:
            '''Survival conditions for a cell containing a live predator'''
            #if np.sum(live_predators) >= 2 or np.sum(live_omnivores) >= 6 or np.sum(live_herbavores) >= 12:
            if np.sum(live_omnivores) >= 6 or np.sum(live_herbavores) >= 12:
                if with_progress: 
                    color = COLOR_DIE_NEXT
            else: 
                updated_cells[row, col] = 1 
                if with_progress:
                    color = PREDATOR_COLOR
        elif cells[row, col] == 2:
            if np.sum(live_predators) >= 1 or np.sum(live_herbavores) >= 6: 
                if with_progress:
                    color = COLOR_DIE_NEXT
            else:
                updated_cells[row, col] = 2
                if with_progress:
                    color = OMNIVORE_COLOR
        elif cells[row, col] == 3:
            if np.sum(live_predators) >= 1 or np.sum(live_omnivores) >= 4: 
                if with_progress:
                    color = COLOR_DIE_NEXT
            else:
                updated_cells[row, col] = 3
                color = HERBAVORE_COLOR
        
        else: 
            #this is where the conditions for a non-living cell occurs.
            if np.sum(live_predators) == 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = PREDATOR_COLOR
        
            elif np.sum(live_omnivores) == 6:
                updated_cells[row, col] = 2
                if with_progress:
                    color = OMNIVORE_COLOR

            elif np.sum(live_herbavores) == 9:
                updated_cells[row, col] = 3
                if with_progress:
                    color = HERBAVORE_COLOR

        pg.draw.rect(screen, color, (col * size, row * size, size - 1, size - 1))
    return updated_cells

def main():
    pg.init()
    screen = pg.display.set_mode((800, 600))
    #predator_energy = 10
    #omnivore_energy = 20
    #herbavore_energy = 25
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
                #print(pg.mouse.get_pressed())
                pg.display.update()

            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 2:
                '''Middle mouse-click, OMNIVORE'''
                pos = pg.mouse.get_pos()
                cells[pos[1] // 10 , pos[0] // 10] = 2
                update(screen, cells, 10)
                #print(pg.mouse.get_pressed())
                pg.display.update()

            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 3:
                '''Right mouse-click, HERBAVORE'''
                pos = pg.mouse.get_pos()
                cells[pos[1] // 10, pos[0] // 10] = 3
                update(screen, cells, 10)
                #print(pg.mouse.get_pressed())
                pg.display.update()

        screen.fill(COLOR_GRID)
        if running:
            cells = update(screen, cells, 10 , with_progress=True)
            pg.display.update()
        
        time.sleep(0.001)


if __name__ == '__main__':
    main()   