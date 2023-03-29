import numpy as np
import matplotlib.pyplot as plt
import random as rnd
def plot_R2(steps_list, distance_list):
    '''Plot the relation between root-mean-squared end-to-end distance and number of steps.'''
    plt.figure()
    plt.title("$\sqrt{<R^2>}$-vs-N-plot")
    plt.xlabel('N (number of steps)')
    plt.ylabel('$\sqrt{<R^2>}$')
    plt.plot(steps_list, distance_list)
    plt.show()

def plot_fluct(steps_list, fluct_list):
    '''Plot the relation between root-mean-squared end-to-end distance and number of steps.'''
    plt.figure()
    plt.title("Fluctuation-vs-N-plot")
    plt.xlabel('N (number of steps)')
    plt.ylabel('Fluctuation')
    plt.plot(steps_list, fluct_list)
    plt.show()

def plotter(steps_list, sample_list, x_label, y_label, title):
    '''plotting the things necessary to display '''
    plt.figure()
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.plot(steps_list, sample_list)
    plt.show()


def random_walk(n):
    '''Makes a random walk, given n number of steps.'''
    x = 0
    y = 0
    #x_list = []
    #y_list = []
    for i in range(n): 
        rand_float = rnd.random()
        step = int(4*rand_float)
        if step == 0:
            x -= 1
        elif step == 1:
            x += 1
        elif step == 2:
            y -= 1
        elif step == 3: 
            y += 1

    return (x,y)

def e_to_e_dist(walks, steps):
    '''Calculates the rot-mean-sqaured end-to-end distance over a *walks* number of 
    random walks for each number of steps between 1 and *steps*.'''
    distance_list = []
    steps_list = []
    for step in range(1, steps):
        steps_list.append(step)
        R2_values = []
        for i in range(walks):
            (x,y) = random_walk(step)
            R2 = x**2 + y**2    
            R2_values.append(R2)
        R2_mean = np.sum(R2_values) / len(R2_values)
        distance = np.sqrt(R2_mean)
        distance_list.append(distance)
    plotter = plot_R2(steps_list, distance_list)
    #print(distance_list)
    return plotter 

def fluctuation(walks, steps):
    '''Calculates the rot-mean-sqaured end-to-end distance over a *walks* number of 
    random walks for each number of steps between 1 and *steps*.'''
    fluct_list = []
    steps_list = []
    std_err_list = []
    for step in range(1, steps):
        steps_list.append(step)
        R2_values = []
        R_values = []
        for i in range(walks):
            (x,y) = random_walk(step)
            R2 = x**2 + y**2
            R = np.sqrt(R2)
            R2_values.append(R2)
            R_values.append(R)
        assert len(R_values) == len(R2_values)

        R2_mean = np.sum(R2_values) / len(R2_values)
        R_mean = np.sum(R_values) / len(R_values)
        fluct = np.divide(np.sqrt(R2_mean - R_mean ** 2) * walks, walks - 1)

        #i included the standard error here as well.
        std_err = np.divide(np.sqrt(R2_mean - R_mean **2), walks-1)
        
        std_err_list.append(std_err)
        fluct_list.append(fluct)

    plotter_fluct = plot_fluct(steps_list, fluct_list)
    plot_std_err = plotter(steps_list, std_err_list, 'N (number of steps)', 'standard error', 'Standard error for N steps')
    return plotter_fluct, plot_std_err

fluctuation(1000, 400)
#e_to_e_dist(1000, 400)