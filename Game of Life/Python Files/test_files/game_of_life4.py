import numpy as np
import time
from matplotlib import pyplot as plt
import pygame as pg
from random import random as rnd

BG_COLOR = (10, 10, 10) #Background color
COLOR_GRID = (40,40,40) #Grid color
COLOR_DIE_NEXT = (250, 25 ,25)
PREDATOR_COLOR = (10, 10, 200) #PREDATOR COLOR (red)
OMNIVORE_COLOR = (200, 10, 200) #OMNIVORE COLOR (purple)
HERBAVORE_COLOR = (25, 255, 25) #HERBAVORE COLOR (green)


def counter(array):
    predator_number = 0
    omnivore_number = 0
    herbavore_number = 0

    for row, col in np.ndindex(array.shape):
        if array[row, col] == 1:
            predator_number += 1
        elif array[row, col] == 2:
            omnivore_number += 1
        elif array[row, col] == 3:
            herbavore_number += 1
        else:
            continue
    return predator_number, omnivore_number, herbavore_number
    


def plotter(time_array, pred_array, omni_array, herba_array):#, y_label):
    '''Plotting the standard error for different values of delta'''
    plt.figure()
    plt.title('Number of species vs time')
    plt.plot(time_array, pred_array, label = 'predators')
    plt.plot(time_array, omni_array, label = 'omnivores')
    plt.plot(time_array, herba_array, label = 'herbavores')
    plt.xlabel('time')
    plt.ylabel('number of species')
    plt.legend()
    plt.show()


def timestep(screen, cells, size, p_energy, pred_p, omni_p, herba_p, with_progress = False):

    '''The step of each frame'''
    
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))

    for row, col in np.ndindex(cells.shape):

        if cells[row, col] == 0:
            '''Empty/dead cell'''
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
        live_predators = [] #Array of neighbor predators
        live_omnivores = [] #Array of nighbor omnivores
        live_herbavores = [] #Array of neighbor herbavores

        pred_pos = [] #The position of each neighbor predator

        for i in range(row-1, row+2):
            for j in range(col-1, col+2):
                '''Periodic boundary conditions'''
                if j == 80:
                    j = 0
                if i == 60:
                    i = 0

                if (i, j) == (row, col):
                    continue
                else:
                    if cells[i,j] == 1:
                        live_predators.append(cells[i,j])
                        pred_pos.append((i,j))
                     
                    elif cells[i,j] == 2:
                        live_omnivores.append(cells[i,j])
                    elif cells[i,j] == 3: 
                        live_herbavores.append(cells[i,j])
                    else:
                        continue

        if cells[row, col] == 1:
            '''Survival-/energy conditions for a cell containing a live predator'''
            if np.sum(live_omnivores) >= 4:
                p_energy[row, col] -=2
            if p_energy[row, col] == 0:
                if with_progress: 
                    color = COLOR_DIE_NEXT
                    p_energy[row, col] == 0
            else: 
                updated_cells[row, col] = 1 
                if with_progress:
                    color = PREDATOR_COLOR
                p_energy[row, col] -= 1

        elif cells[row, col] == 2:
            '''Survival conditions for a cell containing a live omnivore'''
            if np.sum(live_predators) >= 1: 
                if with_progress:
                    color = COLOR_DIE_NEXT
                    for (y, x) in pred_pos:
                        p_energy[y, x] += 1
                    #p_energy[row, col] += 1
            else:
                updated_cells[row, col] = 2
                if with_progress:
                    color = OMNIVORE_COLOR

        elif cells[row, col] == 3:
            '''Survival conditions for a cell containing a live herbavore'''
            if np.sum(live_predators) >= 1:# or np.sum(live_omnivores) >= 4: 
                if with_progress:
                    color = COLOR_DIE_NEXT
                    for (y,x) in pred_pos:
                        p_energy[y,x] += 1

            elif np.sum(live_omnivores) >= 4:
                    if with_progress:
                        color = COLOR_DIE_NEXT

            else:
                updated_cells[row, col] = 3
                color = HERBAVORE_COLOR
        
        else: 
            '''Reproduction conditions for a non-living cell'''

            if np.sum(live_predators) == 3:
                '''Reproduction conditions for predator. Predators required to reproduct: 3'''
                #randfloat_pred = rnd()
                #if randfloat_pred < pred_p:
                updated_cells[row, col] = 1
                if with_progress:
                    color = PREDATOR_COLOR
                    p_energy[row, col] += 7
                                        
                else:
                    continue

                
        
            elif np.sum(live_omnivores) == 4:
                '''Reproduction conditions for omnivore. Omnivores required to reproduct: 3'''
                #randfloat_omni = rnd()
                #if randfloat_omni < omni_p:
                updated_cells[row, col] = 2
                if with_progress:
                    color = OMNIVORE_COLOR

            elif np.sum(live_herbavores) == 9:
                '''Reproduction conditions for herbavore. Herbavores required to reproduct: 3'''
                updated_cells[row, col] = 3
                if with_progress:
                    color = HERBAVORE_COLOR

        pg.draw.rect(screen, color, (col * size, row * size, size - 1, size - 1))
        
    return updated_cells

def pygame_iterator(time_array, predators, omnivores, herbavores):
    '''Executes the pygame initiation and iteration.'''
    pg.init()
    screen = pg.display.set_mode((800, 600))

    cells = np.zeros((60, 80))
    predator_energy = np.zeros((60, 80))
    omnivore_energy = np.zeros((60, 80))

    pred_p = 0.2
    omni_p = 0.3
    herba_p = 0.5

    screen.fill(COLOR_GRID)
    timestep(screen, cells, 10, predator_energy, pred_p, omni_p, herba_p)

    pg.display.flip()
    pg.display.update()

    running = False

    while True:
        for event in pg.event.get():
            '''Initiating the state of the grid'''
            if event.type == pg.QUIT:
                pg.quit()
                return
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    running = not running
                    timestep(screen, cells, 10, predator_energy, pred_p, omni_p, herba_p)
                    pg.display.update()
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                '''Left mouse-click, PREDATOR'''
                pos = pg.mouse.get_pos()
                cells[pos[1] // 10, pos[0] // 10 ] = 1
                predator_energy[pos[1] // 10, pos[0] // 10] = 7 #giving the predator an energy of 10 units
                timestep(screen, cells, 10, predator_energy, pred_p, omni_p, herba_p)
                #print(pg.mouse.get_pressed())
                pg.display.update()

            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 2:
                '''Middle mouse-click, OMNIVORE'''
                pos = pg.mouse.get_pos()
                cells[pos[1] // 10 , pos[0] // 10] = 2
                #omnivore_energy[pos[1] // 10, pos[0] // 2] = 20
                timestep(screen, cells, 10, predator_energy, pred_p, omni_p, herba_p)
                #print(pg.mouse.get_pressed())
                pg.display.update()

            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 3:
                '''Right mouse-click, HERBAVORE'''
                pos = pg.mouse.get_pos()
                cells[pos[1] // 10, pos[0] // 10] = 3
                #herbavore_energy
                timestep(screen, cells, 10, predator_energy, pred_p, omni_p, herba_p)
                pg.display.update()

        screen.fill(COLOR_GRID)
        if running:
            cells = timestep(screen, cells, 10 ,predator_energy,  pred_p, omni_p, herba_p, with_progress=True)
            predator_number, omnivore_number, herbavore_number = counter(cells) # count the number of species in each step.
            predators.append(predator_number)
            omnivores.append(omnivore_number)
            herbavores.append(herbavore_number)
            time_array.append(time.time())
            pg.display.update()
        #print(time.time())
        time.sleep(0.001)
    #return time_array, predators, omnivores, herbavores)

def main():
    time_array = []
    predators = []
    omnivores = []
    herbavores = []
    
    pygame_iterator(time_array, predators, omnivores, herbavores)
    plotter(time_array, predators, omnivores, herbavores)
if __name__ == '__main__':
    main()   

