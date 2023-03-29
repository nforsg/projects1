import numpy as np
import matplotlib.pyplot as plt
import random as rnd
def plot(x_list, y_list, x_label, y_label, title):
    plt.figure()
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.plot(x_list, y_list)
    plt.show()

def random_walk(n):
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
                print('Walk terminated')
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
                print('Walk terminated')
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
                print('Walk terminated')
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
                print('Walk terminated')
                break   
        
        visited.append((x,y))
        print(i)
        #print(visited)
        x_list.append(x)
        y_list.append(y)
    #if i+1 == n:
    #    return True
    #else:
    #    return False
            #print('Walk survived through all steps.')
    #return visited
    walk = plot(x_list, y_list, 'x', 'y', 'Random Walk')
    #return walk

print(random_walk(10))
