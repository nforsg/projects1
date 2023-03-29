import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import random

L = 10

# The grid is n+1 points along x and y, including boundary points 0 and n. Är randen en del av griden?
n = 10

# The grid spacing is L/n

# The number of iterations
nsteps = 1000

# Initialize the grid to 0
v = np.zeros((n + 1, n + 1))
vnew = np.zeros((n + 1, n + 1))

for i in range(1, n):
    for j in range(1, n):
        v[i, j] = 0

# Set the boundary conditions
for i in range(1, n):
    v[0, i] = 10
    v[n, i] = 10
    v[i, 0] = 5
    v[i, n] = 5


# random walk method.

def create_walker(x, y):
    walker = [x, y]  # Starting positions
    return walker


def take_step(walker):  # 0 = x + 1, 1 = x -1, 2 = y + 1, 3 = y - 1
    direction = random.randint(0, 3)
    if direction == 0:
        walker[0] += 1
    elif direction == 1:
        walker[0] -= 1
    elif direction == 2:
        walker[1] += 1
    elif direction == 3:
        walker[1] -= 1
    return walker


def boundary_check(walker):
    if walker[0] % n == 0:
        return (walker[0], walker[1])
    elif walker[1] % n == 0:
        return (walker[0], walker[1])
    else:
        return False


def a_walk(x, y, v):
    walker = create_walker(x, y)
    for j in range(100000):  # essentially while True
        walker = take_step(walker)
        if boundary_check(walker) != False:
            wall_potential = v[walker[0], walker[1]]
            #print([walker[0], walker[1]])
            return walker[0], walker[1]


def walk_solution(x, y, v, m, predicted):  # Starting coordinates, grid, number of steps
    sum = 0;
    stored_wall_potentials = [];
    for i in range(m):
        wall_potential = a_walk(x, y, v)
        stored_wall_potentials.append(wall_potential)
        sum = sum + wall_potential
    RMSE_val = np.std(stored_wall_potentials) / np.sqrt(m)
    print(RMSE_val)
    v_estimate = sum / m
    return v_estimate, RMSE_val


def end_condition(perc_err, condition):
    if float(perc_err) < float(condition):
        return True


def max_error(v):
    answer = 10
    differences = np.zeros((n + 1, n + 1))
    for i in range(1, n):
        for j in range(1, n):
            difference = answer - v[i, j]
            differences[i, j] = difference
    max_err = np.max(differences)
    return max_err


def error_percentage(max_wrong):
    answer = 10
    perc = ((answer - max_wrong) * 100 / answer)
    perc = 100 - perc
    return (perc)

def residual(answer, input_list):
    res = []
    for i in range(len(input_list)):
        res.append(abs(answer - input_list[i]))
    return res


    """
    [[ 0.         10.         10.         10.         10.         10.
  10.         10.         10.         10.          0.        ]
 [ 5.          7.5         8.47891937  8.91567748  9.11328702  9.17113396
   9.11328702  8.91567748  8.47891937  7.5         5.        ]
 [ 5.          6.52108063  7.5         8.07050353  8.36633663  8.45796182
   8.36633663  8.07050353  7.5         6.52108063  5.        ]
 [ 5.          6.08432252  6.92949647  7.5         7.82359417  7.92804004
   7.82359417  7.5         6.92949647  6.08432252  5.        ]
 [ 5.          5.88671298  6.63366337  7.17640583  7.5         7.60701001
   7.5         7.17640583  6.63366337  5.88671298  5.        ]
 [ 5.          5.82886604  6.54203818  7.07195996  7.39298999  7.5
   7.39298999  7.07195996  6.54203818  5.82886604  5.        ]
 [ 5.          5.88671298  6.63366337  7.17640583  7.5         7.60701001
   7.5         7.17640583  6.63366337  5.88671298  5.        ]
 [ 5.          6.08432252  6.92949647  7.5         7.82359417  7.92804004
   7.82359417  7.5         6.92949647  6.08432252  5.        ]
 [ 5.          6.52108063  7.5         8.07050353  8.36633663  8.45796182
   8.36633663  8.07050353  7.5         6.52108063  5.        ]
 [ 5.          7.5         8.47891937  8.91567748  9.11328702  9.17113396
   9.11328702  8.91567748  8.47891937  7.5         5.        ]
 [ 0.         10.         10.         10.         10.         10.
  10.         10.         10.         10.          0.        ]]"""


def RMSE_graph(x_axis, list1, list2, list3):
    plt.plot(x_axis, list1, label="RMSE for (2, 2)")
    plt.plot(x_axis, list2, label="RMSE for (4, 4)")
    # plt.plot(x_axis, list3, label = "RMSE for (2, 4)")
    plt.legend()
    plt.ylabel("RMSE")
    plt.xlabel("Number of walkers")
    plt.show()
    plt.clf()
    plt.ylabel("log of RMSE")
    plt.xlabel("log of number of walkers")
    plt.loglog(x_axis, list1, label="For (2, 2) ")
    plt.loglog(x_axis, list2, label="For (4, 4) ")
    plt.legend()
    plt.show()

def create_touch_array(n):
    touches = np.zeros((n+1, n+1, n+1, n+1))
    return touches

def graph_touches(touches, x, y):
    touches[x,y,x,y] = 20
    im = plt.imshow(touches[x,y], cmap ='hot', interpolation = 'nearest')
    plt.colorbar()
    plt.show()

def graph_v_map(v_map):
    im = plt.imshow(v_map, interpolation='nearest')
    plt.colorbar()
    plt.show()

def green(n):
    touches = create_touch_array(n)
    for x in range(1, 10):
        for y in range(1, 10):
            for k in range(1000):
                x_touch, y_touch = a_walk(x, y, v)
                touches[x][y][x_touch][y_touch] += 1
    return touches

def pot_find(touches):
    v = np.zeros((n + 1, n + 1))
    for x in range(1, 10):
        for y in range(1, 10):
            for i in range(1, 10):
                v[x][y] += touches[x][y][0][i] * 10
                v[x][y] += touches[x][y][10][i] * 10
                v[x][y] += touches[x][y][i][0] * 5
                v[x][y] += touches[x][y][i][10] * 5
            v[x,y] = v[x][y]/1000 




    '''v[3][5] += touches[x][y][0][5] * 10
    v[3][5] += touches[x][y][0][3] * 10
    v[3][5] += touches[x][y][0][4] * 10
    v[3][5] += touches[x][y][0][7] * 10
    v[3][5] += touches[x][y][0][6] * 10'''

    #print(v[3][5]/100000)

    return v

# FUCKA ÅT båda HÅLLEN: 8.175, 7.935            
# Fucka MER åt båda hållen: 8, 8, 8.165
# Fucka bara åt 10 hållet: 7.88, 8

# 8 OM VI BARA FUCKAR 10 VÄGGEN
# 7.925 ELLER 8,1 OM VI FUCKAR ÅT SIDORNA
# 8.15 ELLER 8

def main():
    touch_map = green(n)
    graph_touches(touch_map,5,5)
    v_map = pot_find(touch_map)
    graph_v_map(v_map)
    print()



#    x_axis_simple = []
#   for j in range(1, 101):
#      x_axis_simple.append(j)
#    print(sols)
#   print(len(sols))
#  print(x_axis)
# print(len(x_axis))
# print(x_axis_simple)
# print(len(x_axis_simple))
# make_other_graph(sols, x_axis, x_axis_simple)


main()
