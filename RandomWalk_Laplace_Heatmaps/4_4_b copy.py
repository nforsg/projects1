import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import random as rnd

def randomwalk(coord1, coord2, n, count_array):
    
    x = coord1
    y =  coord2 

    while x > 0 and x < n and y > 0 and y < n:
        rand_float = rnd.random()
        step = int(4 * rand_float)
        if step == 0:
            x -= 1
        elif step == 1:
            x += 1
        elif step == 2:
            y -= 1
        elif step == 3:
            y += 1

    count_array[x,y] += 1
    return count_array

def get_count_array(n, walks, coord1, coord2):

    count_array = np.zeros((n+1, n+1))
    count_array[coord1, coord2] = 6
    for i in range(walks):

        count_array = randomwalk(coord1, coord2, n, count_array)
    return count_array

def get_potential(count_array, v,n):
    pot_list = []
    for i in range(1,n):
            pot_list.append(count_array[0,i] * v[0,i])
            pot_list.append(count_array[n,i] * v[n,i])
            pot_list.append(count_array[i,0] * v[i,0])
            pot_list.append(count_array[i, n] * v[i,n])
    v_final = np.mean(pot_list)
    return v_final

def heatmap(n, walks):

    '''10-boundaries are being weighted in order to just look around for the best placements of V = 20''' 

    v = np.zeros((n+1, n+1))
    for i in range(1,n):
        v[0,i] = 10
        v[n,i] = 10 
        v[i,0] = 5
        v[i,n] = 5 
    #v[7,0] = 20
    #v[0,2] = 20
    v[2,0] = 20
    v[3,0] = 20
    v[2,n] = 20
    v[3,n] = 20
    v[0,5] = 20
   
    for x in range(1,n):
        
        for y in range(1,n):
            count_array = get_count_array(n, walks, x, y)
            for i in range(1,n):
                v[x,y] += count_array[0, i] * (2/3) * v[0,i]
                v[x,y] += count_array[n,i] *(2/3)* v[n,i]
                v[x,y] += count_array[i,0] * v[i,0]
                v[x,y] += count_array[i,n] * v[i,n]
            v[x,y] = v[x,y] / walks
    #print(v[5,3])
    plt.imshow(v)
    plt.title('Potential in square surface, V(x = 5, y = 3) = ' + str(v[3,5]))
    plt.colorbar()
    plt.show()

def main():

    heatmap(10, 500)

#if __name__ == '_main_':
main()