import numpy as np
import matplotlib.pyplot as plt
import random as rnd
def plot_walk(x_list, y_list):
    '''Generating plot for random walk.'''
    plt.figure()
    plt.title("Random Walk")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(x_list, y_list)
    plt.show()

def rand_int(r, a, c, m, N):
    '''Generating random number, given certain parameters.'''
    list = []
    for i in range(0, N):
        r = (a*r +c) % m
        list.append(r)
            
    return list


def random_walk(r0, a, c, m, N):
    '''Generating random walk.'''
    x = 0
    y = 0
    x_list = []
    y_list = []
    list = rand_int(r0, a, c, m, N)
    for r in list:
        step = r// (m//4)
        #print(step)
        if step == 0:
            x -=1
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

random_walk(1, 3, 4, 128, 1000)
