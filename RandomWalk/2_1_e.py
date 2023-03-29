import numpy as np
import matplotlib.pyplot as plt
import random as rnd

def plot_R2(steps_list1, distance_list1, steps_list2, distance_list2, x_label, y_label, plot_title):
    '''Plot the relation between root-mean-squared end-to-end distance and number of steps.'''
    plt.figure()
    plt.title(plot_title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.loglog(steps_list1, distance_list1, label = 'Ordinary Random Walk')
    plt.loglog(steps_list2, distance_list2, label = 'Self Avoiding Random Walk - Method 2')
    #plt.plot(steps_list1, distance_list1, label = 'Ordinary Random Walk')
    #plt.plot(steps_list2, distance_list2, label = 'Self Avoiding Random Walk - Method 2')
    plt.legend()
    plt.show()

def e_to_e_dist(walks, steps, random_walk_function):
    '''Calculates the rot-mean-sqaured end-to-end distance over a *walks* number of 
    random walks for each number of steps between 1 and *steps*.'''
    distance_list = []
    steps_list = []
    for step in range(1, steps):
        steps_list.append(step)
        R2_values = []
        for i in range(walks):
            (x,y) = random_walk_function(step)
            R2 = x**2 + y**2
            R2_values.append(R2)
        print(R2_values)
        R2_mean = np.mean(R2_values)
        distance = np.sqrt(R2_mean)
        distance_list.append(distance)
    #plotter = plot_R2(steps_list, distance_list)
    #print(distance_list)
    return steps_list, distance_list#plotter 

def Method_1(n):
    x = 0
    y = 0
    visited = [(x,y)]
    
    #x_list = [x]
    #y_list = [y]
    for i in range(0,n+1): 
        rand_float = rnd.random()
        step = int(4*rand_float)

        if step == 0:
            if (x-1, y) in visited:
                #print('Walk terminated because of ', (x-1, y))
                break
            else:
                x -= 1

        elif step == 1:
            if (x+1, y) in visited:
                #print('Walk terminated because of ', (x+1, y))
                break
            else:
                x += 1

        elif step == 2:
            if (x, y-1) in visited:
                #print('Walk terminated because of ', (x, y-1))
                break
            else:
                y -= 1

        elif step == 3:
            if (x, y+1) in visited:
                #print('Walk terminated because of ', (x, y+1))
                break 
            else:
                y += 1
    print((x,y))
    return (x,y)
    
def Method_2(n):
    x = 0
    y = 0
    visited = [(x,y)]
    for i in range(0, n+1): 
        rand_float = rnd.random()
        step = int(3*rand_float)
        #print(step)
        if visited == [(0,0)]:
                init_step = int(4*rand_float)
                if init_step == 0:
                    x -= 1
                elif init_step == 1:
                    x += 1
                elif init_step == 2:
                    y -= 1
                elif init_step == 3:
                    y += 1

        elif (x-1, y) in visited: 
            if (x+1, y) and (x, y-1) and (x, y+1) not in visited:
                if step == 0:
                    x += 1
                elif step ==1:
                    y -= 1
                elif step == 2:
                    y += 1
            else:
                #print('Walk terminated')
                break
        elif (x+1, y) in visited:
            if (x-1, y) and (x, y-1) and (x, y+1) not in visited:
                if step == 0:
                    x -= 1
                elif step == 1:
                    y -=1
                elif step == 2:
                    y += 1
            else:
                #print('Walk terminated')
                break
        elif (x, y-1) in visited:
            if (x-1, y) and (x+1, y) and (x, y+1) not in visited:
                if step == 0:
                    x -= 1
                elif step == 1: 
                    x += 1
                elif step == 2:
                    y += 1
            else: 
                #print('Walk terminated')
                break
        elif (x, y+1) in visited:
            if (x-1, y) and (x+1, y) and (x, y-1) not in visited:
                if step == 0:
                    x -= 1
                elif step == 1: 
                    x += 1
                elif step == 2:
                    y -= 1
            else: 
                #print('Walk terminated')
                break   
    return (x, y)
def random_walk_a(n):
    '''Generates a random walk of n blocks'''
    x = 0
    y = 0
    x_list = []
    y_list = []
    for i in range(0, n+1): 
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
        #x_list.append(x)
        #y_list.append(y)
    #walk = plot_walk(x_list, y_list)
    return (x,y)

a_stepslist, a_distlist = e_to_e_dist(1000, 400, random_walk_a)
meth1_stepslist, meth1_distlist = e_to_e_dist(1000, 400, Method_1)
meth2_stepslist, meth2_distlist = e_to_e_dist(1000, 400, Method_2)
plot_R2(a_stepslist, a_distlist, meth1_stepslist, meth1_distlist, 'log(N)', 'log($\sqrt{<R^2>}$)', 'log-log scale of $\sqrt{<R^2>}$ for N steps')