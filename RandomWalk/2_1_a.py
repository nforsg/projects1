import numpy as np
import matplotlib.pyplot as plt
import random as rnd
def plot_walk(x_list, y_list):
    '''Diaplays the random walk in a graph'''
    plt.figure()
    plt.title("Random Walk")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(x_list, y_list)
    plt.show()

def random_walk(n):
    '''Generates a random walk of n blocks'''
    x = 0
    y = 0
    x_list = []
    y_list = []
    for i in range(n): 
        rand_float = rnd.random()
        step = int(4*rand_float)
        #print(step)
        if step == 0:
            x -= 1
        elif step == 1:
            x += 1
        elif step == 2:
            y -= 1
        elif step == 3: 
            y += 1
        x_list.append(x)
        y_list.append(y)
    walk = plot_walk(x_list, y_list)
    
    return walk

random_walk(1000)

