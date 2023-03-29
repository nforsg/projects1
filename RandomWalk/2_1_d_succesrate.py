
import numpy as np
import matplotlib.pyplot as plt
import random as rnd
def plot(x_list1, y_list1, x_list2, y_list2, x_label, y_label, plot_title):
    plt.figure()
    plt.title(plot_title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.plot(x_list1, y_list1, label = 'Method 1')
    plt.plot(x_list2, y_list2, label = 'Method 2')
    plt.legend()
    plt.show()

def succes_rate(walks, steps, random_walk_function):
    success_list = []
    steps_list = []
    for step in range(1, steps):
        success_counter = 0
        for walk in range(walks):
            observer = random_walk_function(step)
            if observer == True:
                success_counter += 1
        success_list.append(success_counter)
        steps_list.append(step)
    #succes_plot = plot(steps_list, success_list, 'N', 'Y', "Succelsful walks Y for N steps - " + random_walk_function.__name__)

    return steps_list, success_list#succes_plot

#random_walk_primitive = Method 1

def Method_1(n):
    x = 0
    y = 0
    visited = [(x,y)]
    
    x_list = [x]
    y_list = [y]
    for i in range(n): 
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
        #print((x,y))

        visited.append((x,y))
        x_list.append(x)
        y_list.append(y)

    if i + 1 == n:
        #print('method1', )
        return True

    else: 
        #print('failed', i)
        return False
    #return walk

#random_walk_improved = Method_2

def Method_2(n):
    x = 0
    y = 0
    visited = [(x,y)]
    x_list = [x]
    y_list = [y]
    for i in range(n): 
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
        
        visited.append((x,y))
        x_list.append(x)
        y_list.append(y)
    if i+1 == n:
        #print('method2', i)
        return True
    else: 
        #print('failed', i)
        return False

meth1_xlist, meth1_ylist = succes_rate(1000, 40, Method_1)
meth2_xlist, meth2_ylist = succes_rate(1000, 40, Method_2)
plot(meth1_xlist, meth1_ylist, meth2_xlist, meth2_ylist, 'N', 'Successes', 'Method 1 vs Method 2 successes')
#plt.show()
