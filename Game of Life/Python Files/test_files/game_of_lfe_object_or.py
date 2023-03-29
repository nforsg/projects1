import numpy as np
from matplotlib import pyplot as plt

def lotka_voltera(i, alpha, gamma, beta, delta, x, y):
    dx = alpha * x[i] - gamma * y[i]
    dy = - beta * [i] + delta * x[i] * y[i] 

def timestep():
    '''The Euler Method'''

