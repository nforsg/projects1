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

def density(area, predator_number, omnivore_number, herbavore_number):

    '''predator_number = 0
    omnivore_number = 0
    herbavore_number = 0
    for row, col in np.ndindex(array.shape):
        if array[row, col] == 1:
            predator_number += 1
        elif array[row, col] == 2:
            omnivore_number += 1
        elif array[row, col] == 3:
            herbavore_number += 1'''
    predator_density = predator_number / area
    omnivore_density = omnivore_number / area
    herbavore_density = herbavore_number / area

    return predator_density, omnivore_density, herbavore_density
    


def plotter(time_array, array1, array2, array3, x_label, y_label, label1, label2, label3, title):
    '''Plotting the standard error for different values of delta'''
    plt.figure()
    plt.title('Number of species vs time')
    plt.plot(time_array, array1, label = label1)
    plt.plot(time_array, array2, label = label2)
    plt.plot(time_array, array3, label = label3)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()
    plt.show()


def initialize(screen, cells, size):
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
        elif cells[row, col] == 3: 
            '''HERBAVORE'''
            color = HERBAVORE_COLOR
        pg.draw.rect(screen, color, (col * size, row * size, size - 1, size - 1))
        

def timestep(screen, size1, size2, cells, size, p_energy, pred_p, omni_p, herba_p, energy_magnitude, n_p = 3, n_o = 2, n_h = 3, energy_decrease_m = 1, energy_decrease_n = 3, 
energy_increase_s = 1, m_o_omnivores = 2, m_p_o_predators = 1, m_p_h_predators = 1, m_o_h_omnivores = 2,with_progress = False):

    '''The step of each frame'''
    
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))

    for row, col in np.ndindex(cells.shape):

        live_predators = [] #Array of neighbor predators
        live_omnivores = [] #Array of nighbor omnivores
        live_herbavores = [] #Array of neighbor herbavores

        pred_pos = [] #The position of each neighbor predator

        for i in range(row-1, row+2):
            for j in range(col-1, col+2):
                '''Periodic boundary conditions'''
                if j == size1:
                    j = 0
                if i == size2:
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
        
        if cells[row, col] == 0:
                '''Empty/dead cell'''
                color = BG_COLOR

        if cells[row, col] == 1:
            '''Survival-/energy conditions for a cell containing a live predator'''
            if np.sum(live_omnivores) >= 2 * m_o_omnivores:
                p_energy[row, col] -= energy_decrease_n
            if p_energy[row, col] <= 0:
                if with_progress: 
                    color = COLOR_DIE_NEXT
                    p_energy[row, col] = 0
                    #print('dead at row ', row, 'and column', col)#, 'at time ', time.time())
            else: 
                updated_cells[row, col] = 1 
                if with_progress:
                    color = PREDATOR_COLOR
                p_energy[row, col] -= energy_decrease_m

        elif cells[row, col] == 2:
            '''Survival conditions for a cell containing a live omnivore'''
            if np.sum(live_predators) >= 1 * m_p_o_predators: #At least one neighbor predator
                if with_progress:
                    color = COLOR_DIE_NEXT
                    for (y, x) in pred_pos:
                        p_energy[y, x] += energy_increase_s

            else:
                updated_cells[row, col] = 2
                if with_progress:
                    color = OMNIVORE_COLOR

        elif cells[row, col] == 3:
            '''Survival conditions for a cell containing a live herbavore'''
            if np.sum(live_predators) >= 1 * m_p_h_predators: #at least one neighbor predator
                if with_progress:
                    color = COLOR_DIE_NEXT
                    for (y,x) in pred_pos:
                        p_energy[y,x] += 1

            elif np.sum(live_omnivores) >= 2 * m_o_h_omnivores: #at least two neighbor omnivores
                    if with_progress:
                        color = COLOR_DIE_NEXT

            else:
                updated_cells[row, col] = 3
                color = HERBAVORE_COLOR
        
        else: 
            '''Reproduction conditions for a non-living cell'''

            if np.sum(live_predators) == 1 * n_p:
                '''Reproduction conditions for predator. Predators required to reproduct: 3'''
                randfloat_pred = rnd()
                if randfloat_pred < pred_p:
                    updated_cells[row, col] = 1
                    if with_progress:
                        color = PREDATOR_COLOR
                        p_energy[row, col] += energy_magnitude           
                else:
                    continue
            
            elif np.sum(live_omnivores) == 2 * n_o:
                '''Reproduction conditions for omnivore. Omnivores required to reproduct: 3'''
                randfloat_omni = rnd()
                if randfloat_omni < omni_p:
                    updated_cells[row, col] = 2
                    if with_progress:
                        color = OMNIVORE_COLOR

            elif np.sum(live_herbavores) == 3 * n_h:
                '''Reproduction conditions for herbavore. Herbavores required to reproduct: 3'''
                randfloat_herba = rnd()
                if randfloat_herba < herba_p:
                    updated_cells[row, col] = 3
                    if with_progress:
                        color = HERBAVORE_COLOR
                else:
                    continue

        pg.draw.rect(screen, color, (col * size, row * size, size - 1, size - 1))
        
    return updated_cells

def pygame_iterator(time_array, predators, omnivores, herbavores, pred_vs_omni, pred_vs_herba, omni_vs_herba, pixels1, pixels2):
    '''Executes the pygame initiation and iteration.'''
    pg.init()
    screen = pg.display.set_mode((pixels1, pixels2))
    size1 = pixels1 // 10
    size2 = pixels2 // 10

    #cells = np.zeros((pixels2 // 10, pixels1 // 10))
    cells = np.zeros((size2, size1))
    predator_energy = np.zeros((size2, size1))
    energy_magnitude = 25
    omnivore_energy = np.zeros((size2, size1))

    pred_p = 0.4
    omni_p = 0.4
    herba_p = 0.6

    screen.fill(COLOR_GRID)
    initialize(screen, cells, 10)
    #timestep(screen, size1, size2, cells, 10, predator_energy, pred_p, omni_p, herba_p, energy_magnitude)

    pg.display.flip()
    pg.display.update()

    running = False

    while True:

        #updated_cells = np.zeros((cells.shape[0], cells.shape[1]))

        for event in pg.event.get():
            '''Initiating the state of the grid'''
            if event.type == pg.QUIT:
                pg.quit()
                return
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    running = not running
                    initialize(screen, cells, 10)
                    #timestep(screen, size1, size2, cells, 10, predator_energy, pred_p, omni_p, herba_p, energy_magnitude)
                    pg.display.update()
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                '''Left mouse-click, PREDATOR'''
                pos = pg.mouse.get_pos()
                cells[pos[1] // 10, pos[0] // 10 ] = 1
                predator_energy[pos[1] // 10, pos[0] // 10] = energy_magnitude
                #print('predator energy bar at row ', pos[1] // 10, 'and column ', pos[0] // 10, 'is ', predator_energy[pos[1] // 10, pos[0] // 10])
                #timestep(screen, size1, size2, cells, 10, predator_energy, pred_p, omni_p, herba_p, energy_magnitude)
                initialize(screen, cells, 10)
                pg.display.update()

            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 2:
                '''Middle mouse-click, OMNIVORE'''
                pos = pg.mouse.get_pos()
                cells[pos[1] // 10 , pos[0] // 10] = 2
                #omnivore_energy[pos[1] // 10, pos[0] // 2] = 20
                #timestep(screen, size1, size2, cells, 10, predator_energy, pred_p, omni_p, herba_p, energy_magnitude)
                initialize(screen, cells, 10)
                #print(pg.mouse.get_pressed())
                pg.display.update()

            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 3:
                '''Right mouse-click, HERBAVORE'''
                pos = pg.mouse.get_pos()
                cells[pos[1] // 10, pos[0] // 10] = 3
                #herbavore_energy
                #timestep(screen, size1, size2, cells, 10, predator_energy, pred_p, omni_p, herba_p, energy_magnitude)
                initialize(screen, cells, 10)
                pg.display.update()
            

        screen.fill(COLOR_GRID)
        if running:
            cells = timestep(screen, size1, size2, cells, 10 ,predator_energy, pred_p, omni_p, herba_p, energy_magnitude, with_progress=True)
            predator_number, omnivore_number, herbavore_number = counter(cells) # count the number of species in each step.
            #predator_density, omnivore_density, herbavore_density = density(size1 * size2, predator_number, omnivore_number, herbavore_number)
            predators.append(predator_number)
            omnivores.append(omnivore_number)
            herbavores.append(herbavore_number)
            #pred_vs_omni.append(predator_number / omnivore_number)
            #pred_vs_herba.append(predator_number / herbavore_number)
            #omni_vs_herba.append(omnivore_number / herbavore_number)
            time_array.append(time.time())
            pg.display.update()
        #
        time.sleep(0.0001)
        #print(time.time())
    #return time_array, predators, omnivores, herbavores)

def main():
    time_array = []
    predators = []
    omnivores = []
    herbavores = []

    pred_vs_omni = []
    pred_vs_herba = []
    omni_vs_herba = []
    
    pygame_iterator(time_array, predators, omnivores, herbavores, pred_vs_omni, pred_vs_herba, omni_vs_herba, 800, 600)
    #plotter(time_array, predators, omnivores, herbavores)
    plotter(time_array, predators, omnivores, herbavores, 'time', 'Number of Species', 'Predators', 'Omnivores', 'Herbivores', 'Numer of species vs Time')
   #plotter(time_array, pred_vs_omni, pred_vs_herba, omni_vs_herba, 'time', 'Relative Population Ratio', '$\frac{#Predators}{#Omnivores}$', '$\frac{#Predators}{#Herbavores}$', '$\frac{#Omnivores}{#Herbavores}$', 'Relative Population Ratio of Each Species vs Time')

if __name__ == '__main__':
    main()   

